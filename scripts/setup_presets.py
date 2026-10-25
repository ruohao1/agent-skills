"""Preview and add personal instructions and native agent definitions."""
from __future__ import annotations

from dataclasses import dataclass, replace
import difflib
import hashlib
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import tomllib
from typing import Mapping

try:
    from .setup_inventory import AGENTS, Target, host_roots, parse_json, safe_write_path, scope_root
except ImportError:
    from setup_inventory import AGENTS, Target, host_roots, parse_json, safe_write_path, scope_root


PARTS = ("instructions", "agents")


@dataclass(frozen=True)
class Change:
    path: Path
    before: bytes | None
    after: bytes
    mode: int
    backup: Path | None = None


@dataclass
class PresetPlan:
    name: str
    target: Target
    parts: tuple[str, ...]
    changes: tuple[Change, ...] = ()
    status: str = "missing"
    reason: str = "Add the selected preset files; reload the host afterward"


def load_sources(root: Path, name: str, agent: str, parts: tuple[str, ...]) -> list[tuple[str, Path, bytes]]:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or agent not in AGENTS:
        raise ValueError("Invalid preset or agent")
    if not parts or not set(parts) <= set(PARTS):
        raise ValueError("Choose instructions, agents, or both")
    folder = root / "configs" / name / agent
    sources = []
    if "instructions" in parts:
        sources.append(("instructions", folder.parent / "AGENTS.md"))
    if "agents" in parts:
        agents = folder / "agents"
        suffix = ".toml" if agent == "codex" else ".md"
        roles = sorted(agents.glob("*"))
        if not roles or any(p.suffix != suffix for p in roles):
            raise ValueError(f"Missing or unsupported preset agent definitions: {agents}")
        sources.extend(("agents", path) for path in roles)
    result = []
    for part, path in sources:
        safe_write_path(path)
        content = path.read_bytes()
        if not content.decode("utf-8").strip():
            raise ValueError(f"Empty preset file: {path}")
        result.append((part, path, content))
    return result


def _read(path: Path) -> bytes | None:
    safe_write_path(path)
    return path.read_bytes() if path.exists() else None


def _block(name: str, content: bytes) -> bytes:
    return (f"<!-- agent-skills:{name}:begin -->\n".encode() + content.rstrip() +
            f"\n<!-- agent-skills:{name}:end -->\n".encode())


def _instructions(name: str, before: bytes | None, content: bytes) -> bytes:
    block = _block(name, content)
    if before is None or not before:
        return block
    if before == content:
        return before
    before.decode("utf-8")
    marker = f"<!-- agent-skills:{name}:".encode()
    if marker in before:
        if before.count(marker) == 2 and before.count(block) == 1:
            return before
        raise ValueError("Preset instructions were changed or their markers are incomplete; preserved")
    return before + (b"\n" if before.endswith(b"\n") else b"\n\n") + block


def _project_dirs(target: Target, env: Mapping[str, str]) -> list[Path]:
    if target.scope != "project":
        return []
    project = scope_root(target, env)
    result = []
    for parent in (project, *project.parents):
        result.append(parent)
        if (parent / ".git").exists() or parent == host_roots(env)["home"]:
            break
    return result


def _agent_files(directory: Path, suffix: str):
    if not directory.exists():
        return
    def unreadable(error):
        raise error
    for current, dirs, files in os.walk(directory, onerror=unreadable):
        dirs.sort()
        for name in sorted(dirs + files):
            path = Path(current) / name
            if path.is_symlink():
                raise ValueError(f"Cannot inspect redirected agent path: {path}")
            if name in files and path.suffix == suffix:
                yield path


def _agent_destination(target: Target, path: Path, content: bytes, env: Mapping[str, str]) -> Path:
    roots = host_roots(env)
    projects = _project_dirs(target, env)
    folder = {"codex": ".codex", "claude-code": ".claude", "opencode": ".opencode"}[target.agent]
    directories = [roots[target.agent], *(p / folder for p in projects)]
    configs = []
    if target.agent == "codex":
        configs = [d / "config.toml" for d in directories]
    elif target.agent == "opencode":
        directories.append(roots["home"] / ".opencode")
        if env.get("OPENCODE_CONFIG_DIR"):
            directories.append(Path(env["OPENCODE_CONFIG_DIR"]))
        configs = [d / filename for d in (*directories, *projects)
                   for filename in ("opencode.json", "opencode.jsonc")]
        if env.get("OPENCODE_CONFIG"):
            configs.append(Path(env["OPENCODE_CONFIG"]))
    name = path.stem

    def check_config(data: dict, location: object) -> None:
        if not isinstance(data, dict):
            raise ValueError(f"Cannot inspect configuration in {location}")
        key = "agents" if target.agent == "codex" else "agent"
        agents = data.get(key, {})
        if not isinstance(agents, dict):
            raise ValueError(f"Cannot inspect agent definitions in {location}")
        if name in agents:
            raise ValueError(f"Existing agent {name} is configured in {location}; preserved")

    for config in dict.fromkeys(configs):
        if not config.is_absolute():
            raise ValueError(f"Configuration paths must be absolute: {config}")
        raw = _read(config)
        if raw is not None:
            data = (tomllib.loads(raw.decode("utf-8")) if target.agent == "codex" else
                    parse_json(raw.decode("utf-8"), config, comments=True))
            check_config(data, config)
            if target.agent == "codex":
                profiles = data.get("profiles", {})
                if not isinstance(profiles, dict):
                    raise ValueError(f"Cannot inspect profiles in {config}")
                for profile in profiles.values():
                    check_config(profile, config)
    if target.agent == "opencode" and env.get("OPENCODE_CONFIG_CONTENT"):
        check_config(parse_json(env["OPENCODE_CONFIG_CONTENT"], "OPENCODE_CONFIG_CONTENT", comments=True),
                     "OPENCODE_CONFIG_CONTENT")

    matches = []
    for directory in dict.fromkeys(directories):
        for subdir in (("agents", "agent") if target.agent == "opencode" else ("agents",)):
            agents = directory / subdir
            safe_write_path(agents / path.name)
            for existing in _agent_files(agents, path.suffix):
                raw = _read(existing)
                if target.agent == "codex":
                    role = tomllib.loads(raw.decode("utf-8")).get("name")
                    if not isinstance(role, str):
                        raise ValueError(f"Cannot determine agent name: {existing}")
                elif target.agent == "claude-code":
                    header = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", raw.decode("utf-8"), re.S)
                    # shortcut: accept ordinary YAML name scalars; unusual metadata requires manual reconciliation.
                    names = re.findall(r'''^(?:name|"name"|'name'):\s*([a-z0-9-]+|"[a-z0-9-]+"|'[a-z0-9-]+')\s*(?:#.*)?$''',
                                       header[1] if header else "", re.M)
                    keys = re.findall(r'''^(?:name|"name"|'name'):''', header[1] if header else "", re.M)
                    if len(names) != 1 or len(keys) != 1:
                        raise ValueError(f"Cannot determine agent name: {existing}")
                    role = names[0].strip("\"'")
                else:
                    role = existing.relative_to(agents).with_suffix("").as_posix()
                if role == name:
                    if raw != content:
                        raise ValueError(f"Existing agent differs from the preset; preserved: {existing}")
                    matches.append(existing)
    return matches[0] if matches else path


def _destination(target: Target, part: str, source: Path, content: bytes, name: str,
                 env: Mapping[str, str]) -> Path:
    roots = host_roots(env)
    base = roots[target.agent] if target.scope == "global" else scope_root(target, env)
    if not base.is_absolute():
        raise ValueError("Configuration roots must be absolute paths")
    if part == "agents":
        if target.scope == "project":
            base /= {"codex": ".codex", "claude-code": ".claude", "opencode": ".opencode"}[target.agent]
        return _agent_destination(target, base / "agents" / source.name, content, env)
    path = base / ("CLAUDE.md" if target.agent == "claude-code" else "AGENTS.md")
    if target.agent == "codex":
        override = base / "AGENTS.override.md"
        if _read(override):
            return override
    shared_project = target.scope == "project" and path.name == "AGENTS.md"
    if (target.agent == "opencode" or shared_project) and _read(path) is None:
        compatible = env.get("OPENCODE_DISABLE_CLAUDE_CODE") not in ("1", "true")
        if target.scope == "global" and env.get("OPENCODE_DISABLE_CLAUDE_CODE_PROMPT") in ("1", "true"):
            compatible = False
        fallbacks = [roots["home"] / ".claude/CLAUDE.md"] if compatible and not shared_project else []
        if shared_project:
            projects = _project_dirs(target, env)
            fallbacks = [p / "AGENTS.md" for p in projects[1:]]
            if compatible:
                fallbacks.extend(p / "CLAUDE.md" for p in projects)
        for fallback in fallbacks:
            existing = _read(fallback)
            if existing and existing not in (content, _block(name, content)):
                raise ValueError(f"Creating {path} may shadow OpenCode instructions in {fallback}; reconcile them first")
    return path


def build_plan(root: Path, name: str, targets: list[Target], parts: tuple[str, ...],
               env: Mapping[str, str]) -> list[PresetPlan]:
    result = []
    for target in targets:
        if target.scope not in ("global", "project"):
            raise ValueError("Unknown preset scope")
        sources = load_sources(root, name, target.agent, parts)
        item = PresetPlan(name, target, parts)
        try:
            changes = []
            for part, source, content in sources:
                path = _destination(target, part, source, content, name, env)
                before = _read(path)
                after = _instructions(name, before, content) if part == "instructions" else content
                if part == "agents" and before is not None and before != after:
                    raise ValueError(f"Existing agent differs from the preset; preserved: {path}")
                changes.append(prepare_change(path, before, after))
            item.changes = tuple(changes)
            if all(c.before == c.after for c in changes):
                item.status, item.reason = "present", "Selected preset content already present; preserved"
        except (OSError, ValueError) as error:
            item.status, item.reason = "conflict", str(error)
        result.append(item)
    return result


def prepare_change(path: Path, before: bytes | None, after: bytes) -> Change:
    mode = stat.S_IMODE(path.stat().st_mode) if before is not None else 0o600
    backup = None
    if before is not None and before != after:
        digest = hashlib.sha256(before).hexdigest()[:16]
        backup = path.with_name(path.name + f".agent-skills-{digest}.bak")
        saved = _read(backup)
        if saved is not None and saved != before:
            raise ValueError(f"Existing backup differs; preserved: {backup}")
    return Change(path, before, after, mode, backup)


def _atomic_write(path: Path, before: bytes | None, after: bytes, mode: int) -> None:
    safe_write_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    safe_write_path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".agent-skills-", delete=False) as output:
            temporary = Path(output.name)
            output.write(after)
            output.flush()
            os.fsync(output.fileno())
        temporary.chmod(mode)
        if _read(path) != before:
            raise ValueError(f"File changed after preview; preserved: {path}")
        if before is None:
            os.link(temporary, path)
        else:
            os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def write_change(change: Change, *, private_backup: bool = False) -> None:
    if change.before == change.after:
        return
    if change.backup and _read(change.backup) is None:
        _atomic_write(change.backup, None, change.before, 0o600 if private_backup else change.mode)
    _atomic_write(change.path, change.before, change.after, change.mode)


def apply_plan(items: list[PresetPlan], root: Path, env: Mapping[str, str]) -> list[PresetPlan]:
    results = []
    for item in items:
        if item.status != "missing":
            results.append(item)
            continue
        try:
            fresh = build_plan(root, item.name, [item.target], item.parts, env)[0]
            if fresh.status != "missing":
                results.append(fresh)
                continue
            old = {c.path: c for c in item.changes}
            if set(old) != {c.path for c in fresh.changes} or any(
                    c.after != old[c.path].after or
                    (c.before != old[c.path].before and c.before != old[c.path].after)
                    for c in fresh.changes):
                results.append(replace(item, status="conflict", reason="Preset or destination changed after preview; preserved"))
                continue
            for change in fresh.changes:
                write_change(change)
            verified = build_plan(root, item.name, [item.target], item.parts, env)[0]
            if verified.status != "present":
                raise ValueError("Preset files could not be verified: " + verified.reason)
            results.append(replace(fresh, status="installed", reason="Preset files verified; reload the host session"))
        except (OSError, ValueError) as error:
            results.append(replace(item, status="failed", reason=str(error)))
    return results


def show(items: list[PresetPlan], diff: bool = False) -> None:
    for item in items:
        print(f"{item.status:12} {item.name} [{item.target.agent}, {item.target.scope}]: {item.reason}")
        for change in item.changes:
            print(f"  {change.path}")
            if change.backup:
                print(f"  Backup: {change.backup}")
            if diff and change.before != change.after:
                print("\n".join(difflib.unified_diff(
                    (change.before or b"").decode("utf-8").splitlines(), change.after.decode("utf-8").splitlines(),
                    fromfile=str(change.path), tofile=str(change.path) + " (with preset)", n=0, lineterm="")))


def run(root: Path, name: str, targets: list[Target], parts: tuple[str, ...], action: str,
        yes: bool, env: Mapping[str, str]) -> int:
    items = build_plan(root, name, targets, parts, env)
    print("Configuration preset: " + name + " (" + ", ".join(dict.fromkeys(parts)) + ")")
    show(items, diff=True)
    if action == "plan":
        return int(any(item.status == "conflict" for item in items))
    if not yes and any(item.status == "missing" for item in items):
        if not sys.stdin.isatty():
            raise ValueError("Use --yes after reviewing the preset plan in noninteractive mode")
        if input("Apply the preset changes shown above? [y/N]: ").strip().lower() not in ("y", "yes"):
            return 0
    results = apply_plan(items, root, env)
    show(results)
    unresolved = [item for item in results if item.status not in ("installed", "present")]
    for item in unresolved:
        print(f"Unresolved: {name} for {item.target.agent} at {item.target.scope} scope; resolve the conflict and retry")
    return int(bool(unresolved))
