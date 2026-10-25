"""Read installed skill identities without changing an agent's configuration."""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Mapping


AGENTS = ("codex", "claude-code", "opencode")


@dataclass(frozen=True)
class Target:
    agent: str
    scope: str
    project: Path | None = None


@dataclass
class Installation:
    name: str
    source: str | None
    path: Path | None
    route: str
    enabled: bool | None
    digest: str | None
    plugin: str | None = None
    version: str | None = None
    modified: bool = False
    ref: str | None = None
    skill_path: str | None = None


@dataclass
class Inventory:
    installations: list[Installation] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def parse_json(text: str, location: object, *, comments: bool = False) -> dict:
    if comments:
        # Match strings first so comment markers and commas inside prompts stay literal.
        string = r'"(?:[^"\\]|\\.)*"'
        text = re.sub(string + r'|//[^\r\n]*|/\*[\s\S]*?\*/',
                      lambda m: m[0] if m[0].startswith('"') else " ", text)
        original = text
        text = re.sub(string + r'|,\s*(?=[}\]])',
                      lambda m: m[0] if m[0].startswith('"') or
                      original[:m.start()].rstrip()[-1:] in ("", "{", "[", ",", ":") else "", text)
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"{location}: duplicate key {key!r}")
            result[key] = value
        return result
    data = json.loads(text, object_pairs_hook=unique)
    if not isinstance(data, dict):
        raise ValueError(f"{location}: expected an object")
    return data


def read_json(path: Path, *, comments: bool = False) -> dict:
    return parse_json(path.read_text(encoding="utf-8"), path, comments=comments)


def safe_write_path(path: Path) -> None:
    for part in (path.absolute(), *path.absolute().parents):
        if part.is_symlink():
            raise ValueError(f"Write path is a symlink: {part}")
        if part != path.absolute() and part.exists() and not part.is_dir():
            raise ValueError(f"Parent path is not a directory: {part}")
    if path.exists() and (not path.is_file() or path.stat().st_nlink != 1):
        raise ValueError(f"Write target is not an unshared regular file: {path}")


def source_identity(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    value = value.removeprefix("https://github.com/").removesuffix("/").removesuffix(".git")
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
        return value.lower()
    return None


def cli_problem(stderr: str) -> bool:
    # Codex's optional PATH-helper warning does not invalidate plugin inventory.
    relevant = "\n".join(line for line in stderr.splitlines()
                         if not line.startswith("WARNING: proceeding, even though we could not create PATH aliases:"))
    return re.search(r"\b(failed|error|could not|unavailable|unable)\b", relevant, re.I) is not None


def fingerprint(path: Path) -> str:
    root = path.resolve(strict=True)
    digest = hashlib.sha256()
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs.sort()
        for name in sorted(dirs + files):
            child = Path(current) / name
            relative = child.relative_to(root).as_posix().encode()
            digest.update(relative + b"\0")
            if child.is_symlink():
                if not child.resolve().is_relative_to(root) or not child.exists():
                    raise ValueError(f"Unsafe or broken resource link: {child}")
                digest.update(b"link\0" + os.readlink(child).encode())
            elif child.is_file():
                digest.update(b"file\0" + child.read_bytes())
            elif child.is_dir():
                digest.update(b"dir")
            else:
                raise ValueError(f"Not a regular resource: {child}")
            digest.update(b"\0")
    return digest.hexdigest()


def scope_root(target: Target, env: Mapping[str, str]) -> Path:
    if target.scope == "global":
        return Path(env.get("HOME", str(Path.home()))).expanduser().absolute()
    if target.project is None:
        raise ValueError("Project scope needs a project directory")
    return target.project.absolute()


def host_roots(env: Mapping[str, str]) -> dict[str, Path]:
    home = Path(env.get("HOME", str(Path.home())))
    return {"home": home, "codex": Path(env.get("CODEX_HOME") or home / ".codex"),
            "claude-code": Path(env.get("CLAUDE_CONFIG_DIR") or home / ".claude"),
            "opencode": Path(env.get("XDG_CONFIG_HOME") or home / ".config") / "opencode"}


def destination(target: Target, env: Mapping[str, str], name: str) -> Path:
    roots = host_roots(env)
    if target.scope == "project":
        return scope_root(target, env) / (".claude/skills" if target.agent == "claude-code" else ".agents/skills") / name
    base = roots["home"] / ".agents" if target.agent in ("codex", "opencode") else roots[target.agent]
    return base / "skills" / name


def installer_lock(target: Target, env: Mapping[str, str]) -> Path:
    if target.scope == "project":
        return scope_root(target, env) / "skills-lock.json"
    state = env.get("XDG_STATE_HOME")
    return Path(state) / "skills/.skill-lock.json" if state else host_roots(env)["home"] / ".agents/.skill-lock.json"


def receipt_path(target: Target, env: Mapping[str, str]) -> Path:
    return scope_root(target, env) / ".agents/marketplace/personal/state.json"


def skill_roots(target: Target, env: Mapping[str, str]) -> list[tuple[Path, Path]]:
    roots = host_roots(env)
    home = roots["home"]
    global_roots = {
        "codex": [home / ".agents/skills", roots["codex"] / "skills"],
        "claude-code": [roots["claude-code"] / "skills"],
        "opencode": [home / ".agents/skills", roots["opencode"] / "skills", roots["claude-code"] / "skills"],
    }
    result = [(p, home) for p in global_roots[target.agent]]
    if target.scope == "project":
        project = scope_root(target, env)
        for parent in (project, *project.parents):
            folders = {"codex": (".agents", ".codex"), "claude-code": (".claude",),
                       "opencode": (".agents", ".opencode", ".claude")}[target.agent]
            result.extend((parent / folder / "skills", parent) for folder in folders)
            if (parent / ".git").exists():
                break
    return list(dict.fromkeys(result))


def _metadata(root: Path, env: Mapping[str, str]) -> tuple[dict, list[dict]]:
    locks = {}
    paths = [(root / "skills-lock.json", 1)]
    if root == host_roots(env)["home"]:
        paths.insert(0, (installer_lock(Target("codex", "global"), env), 3))
    for path, version in paths:
        if path.exists():
            content = read_json(path)
            if content.get("version") != version:
                raise ValueError(f"Unsupported skill lock version: {path}")
            data = content.get("skills")
            if not isinstance(data, dict) or not all(isinstance(v, dict) for v in data.values()):
                raise ValueError(f"Invalid skill lock: {path}")
            locks.update(data)
    path = root / ".agents/marketplace/personal/state.json"
    records = read_json(path).get("records", {}) if path.exists() else {}
    if not isinstance(records, dict) or not all(isinstance(v, dict) for v in records.values()):
        raise ValueError(f"Invalid setup receipt: {path}")
    return locks, list(records.values())


def _package_skills(package: Path, agent: str) -> list[Path]:
    candidates = (package / "plugin.json", package / (".codex-plugin" if agent == "codex" else ".claude-plugin") / "plugin.json")
    manifest = next((p for p in candidates if p.is_file()), None)
    if manifest is None:
        raise ValueError(f"Cannot inspect installed plugin manifest: {package}")
    locations = read_json(manifest).get("skills", "./skills")
    if isinstance(locations, str):
        locations = [locations]
    if not isinstance(locations, list) or not all(isinstance(p, str) for p in locations):
        raise ValueError(f"Cannot inspect plugin skills: {manifest}")
    result = []
    for location in locations:
        directory = package / location
        if not directory.resolve().is_relative_to(package.resolve()):
            raise ValueError(f"Plugin skill path escapes package: {directory}")
        if (directory / "SKILL.md").is_file():
            result.append(directory)
        elif directory.is_dir():
            result.extend(p.parent for p in directory.glob("*/SKILL.md"))
    return result


def native_inventory(target: Target, env: Mapping[str, str]) -> Inventory:
    result = Inventory()
    if target.agent == "opencode":
        return result
    host = host_roots(env)[target.agent]
    state_exists = (host / "plugins").exists() or (host / ("config.toml" if target.agent == "codex" else "settings.json")).exists()
    if not state_exists:
        return result
    binary = "codex" if target.agent == "codex" else "claude"
    try:
        completed = subprocess.run([binary, "plugin", "list", "--json"], cwd=target.project or None,
                                   env=dict(env), capture_output=True, text=True, timeout=30)
        if completed.returncode or cli_problem(completed.stderr):
            raise ValueError(f"{binary} plugin inventory is incomplete: {completed.stderr.strip()[:300]}")
        data = json.loads(completed.stdout)
        entries = data.get("installed") if target.agent == "codex" and isinstance(data, dict) else data
        if not isinstance(entries, list) or not all(isinstance(e, dict) for e in entries):
            raise ValueError(f"Unrecognized {binary} plugin inventory")
        registry_path = host / "plugins/known_marketplaces.json"
        registry = read_json(registry_path) if target.agent == "claude-code" and registry_path.exists() else {}
        for entry in entries:
            if target.agent == "claude-code":
                scope = entry.get("scope")
                if scope in ("project", "local"):
                    if target.scope == "global":
                        continue
                    project = entry.get("projectPath")
                    if not isinstance(project, str) or not Path(project).is_absolute():
                        raise ValueError("Missing native plugin project scope")
                    if not scope_root(target, env).resolve().is_relative_to(Path(project).resolve()):
                        continue
                elif scope not in ("user", "managed"):
                    raise ValueError("Unrecognized native plugin scope")
            plugin_id = entry.get("pluginId") or entry.get("id")
            if not isinstance(plugin_id, str) or "@" not in plugin_id:
                raise ValueError(f"Missing {binary} plugin identity")
            name, marketplace = plugin_id.split("@", 1)
            if not all(re.fullmatch(r"[A-Za-z0-9_-]+", part) for part in (name, marketplace)):
                raise ValueError("Unrecognized native plugin identifier")
            source = entry.get("marketplaceSource", {}).get("source") or entry.get("source", {}).get("url")
            if not source and marketplace in registry:
                registered = registry[marketplace].get("source", {})
                source = registered.get("repo") or registered.get("url")
            identity = source_identity(source)
            package_path = entry.get("installPath") or entry.get("installedPath")
            package = Path(package_path) if package_path else host / "plugins/cache" / marketplace / name / str(entry.get("version", ""))
            enabled = entry.get("enabled")
            result.installations.append(Installation(plugin_id, identity, package, "native", enabled, None,
                                                     plugin=name, version=entry.get("version")))
            for folder in _package_skills(package, target.agent):
                result.installations.append(Installation(folder.name, identity, folder, "native", enabled,
                                                         fingerprint(folder), plugin=name, version=entry.get("version")))
    except (OSError, ValueError, TypeError, AttributeError, subprocess.SubprocessError) as error:
        result.errors.append(str(error))
    return result


def inspect_target(target: Target, env: Mapping[str, str]) -> Inventory:
    if target.agent not in AGENTS or target.scope not in ("global", "project"):
        raise ValueError("Unsupported agent or scope")
    result = Inventory()
    seen = set()
    metadata = {}
    for root, owner in skill_roots(target, env):
        try:
            if not root.exists() and not root.is_symlink():
                continue
            if owner not in metadata:
                metadata[owner] = _metadata(owner, env)
            locks, receipts = metadata[owner]
            for folder in sorted(root.iterdir()):
                if folder.name.startswith("."):
                    continue
                if folder.is_symlink() and not folder.exists():
                    result.errors.append(f"Broken skill link: {folder}")
                    continue
                if not folder.is_dir():
                    continue
                resolved = folder.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                if not (folder / "SKILL.md").is_file():
                    result.installations.append(Installation(folder.name, None, folder, "skills", None, None))
                    continue
                digest = fingerprint(folder)
                locked = locks.get(folder.name, {})
                source = source_identity(locked.get("source"))
                modified = False
                for receipt in receipts:
                    if receipt.get("name") == folder.name and receipt.get("path") == str(resolved):
                        source = source or source_identity(receipt.get("source"))
                        modified = receipt.get("digest") != digest
                result.installations.append(Installation(folder.name, source, folder, "skills", True, digest,
                                                         modified=modified, ref=locked.get("ref"), skill_path=locked.get("skillPath")))
        except (OSError, ValueError, TypeError) as error:
            result.errors.append(str(error))
    native = native_inventory(target, env)
    for owner in {host_roots(env)["home"], scope_root(target, env)}:
        try:
            _, receipts = _metadata(owner, env)
            for installed in native.installations:
                if installed.path is None or installed.digest is None:
                    continue
                for receipt in receipts:
                    if receipt.get("route") == "native" and receipt.get("name") == installed.name and receipt.get("path") == str(installed.path.resolve()):
                        installed.modified = receipt.get("digest") != installed.digest
                        installed.source = installed.source or source_identity(receipt.get("source"))
        except (OSError, ValueError, TypeError) as error:
            native.errors.append(str(error))
    result.installations.extend(native.installations)
    result.errors.extend(native.errors)
    return result
