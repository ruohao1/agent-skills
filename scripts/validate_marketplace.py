#!/usr/bin/env python3
"""Check this repository's two catalogs and shared skill plugin layout."""

from __future__ import annotations

from pathlib import Path
import re
import sys
import tomllib

try:
    from .setup import load_catalog, require, identifier, _check_content
    from .setup_inventory import AGENTS, read_json
    from .setup_presets import PARTS, load_sources
except ImportError:
    from setup import load_catalog, require, identifier, _check_content
    from setup_inventory import AGENTS, read_json
    from setup_presets import PARTS, load_sources

try:
    import yaml
except ImportError:
    sys.exit("Install validation dependencies: python3 -m pip install -r requirements-dev.txt")


ROOT = Path(__file__).resolve().parents[1]
VERSION = re.compile(
    r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def catalog(root: Path, path: str, agent: str) -> tuple[str, list[str]]:
    data = read_json(root / path)
    require(identifier(data.get("name")), f"{path}: invalid marketplace name")
    if agent == "codex":
        metadata = data.get("interface")
        require(isinstance(metadata, dict) and nonempty(metadata.get("displayName")),
                f"{path}: interface.displayName is required")
    else:
        metadata = data.get("owner")
        require(isinstance(metadata, dict) and nonempty(metadata.get("name")),
                f"{path}: owner.name is required")

    entries = data.get("plugins")
    require(isinstance(entries, list), f"{path}: plugins must be an array")
    names = []
    for entry in entries:
        require(isinstance(entry, dict), f"{path}: plugin entry must be an object")
        name = entry.get("name")
        require(identifier(name), f"{path}: invalid plugin name {name!r}")
        require(name not in names, f"{path}: duplicate plugin {name}")
        names.append(name)
        expected = f"./plugins/{name}"
        source = entry.get("source")
        if agent == "codex":
            require(isinstance(source, dict) and source.get("source") == "local",
                    f"{path}: {name} must use a local source object")
            source = source.get("path")
            policy = entry.get("policy")
            require(isinstance(policy, dict), f"{path}: {name} requires a policy object")
            require(policy.get("installation") in ("AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"),
                    f"{path}: {name} has an invalid installation policy")
            require(policy.get("authentication") in ("ON_INSTALL", "ON_USE"),
                    f"{path}: {name} has an invalid authentication policy")
            require(nonempty(entry.get("category")), f"{path}: {name} requires a category")
        require(source == expected, f"{path}: {name} source must be {expected}")
        require((root / expected).is_dir(), f"{path}: missing plugin directory {expected}")
    return data["name"], names


def validate_skill(root: Path, path: Path, plugin: Path) -> None:
    label = str(path.relative_to(root))
    require(path.resolve().is_relative_to(plugin.resolve()), f"{label}: skill escapes its plugin")
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)^---[ \t]*\r?\n(.*)\Z", content, re.MULTILINE | re.DOTALL)
    require(match is not None, f"{label}: missing YAML frontmatter or Markdown body")
    metadata = yaml.safe_load(match.group(1))
    require(isinstance(metadata, dict), f"{label}: frontmatter must be a mapping")
    require(identifier(metadata.get("name")) and metadata["name"] == path.parent.name,
            f"{label}: frontmatter name must match the skill directory")
    description = metadata.get("description")
    require(nonempty(description) and len(description) <= 1024,
            f"{label}: description must contain 1–1024 characters")
    require(nonempty(match.group(2)), f"{label}: instructions must not be empty")
    _check_content(path.parent, path.parent.name)


def validate_plugin(root: Path, name: str, known_skills: set[str]) -> int:
    plugin = root / "plugins" / name
    require(plugin.resolve().is_relative_to((root / "plugins").resolve()),
            f"{name}: plugin directory escapes plugins/")
    manifests = []
    for agent in ("codex", "claude"):
        manifest = read_json(plugin / f".{agent}-plugin/plugin.json")
        require(manifest.get("name") == name, f"{name}: {agent} manifest name must match directory")
        version = manifest.get("version")
        match = VERSION.fullmatch(version) if isinstance(version, str) else None
        require(match is not None, f"{name}: {agent} version must be semantic versioning")
        prerelease = match.group(4)
        require(prerelease is None or all(
            not part.isdigit() or part == "0" or not part.startswith("0")
            for part in prerelease.split(".")
        ), f"{name}: numeric prerelease identifiers cannot have leading zeroes")
        require(nonempty(manifest.get("description")), f"{name}: {agent} description is required")
        author = manifest.get("author")
        require(isinstance(author, dict) and nonempty(author.get("name")),
                f"{name}: {agent} author.name is required")
        require(manifest.get("skills") == "./skills/", f"{name}: {agent} skills must be ./skills/")
        manifests.append(manifest)

    for field in ("name", "version", "description", "author"):
        require(manifests[0][field] == manifests[1][field], f"{name}: manifests disagree on {field}")
    interface = manifests[0].get("interface")
    require(isinstance(interface, dict), f"{name}: Codex interface is required")
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        require(nonempty(interface.get(field)), f"{name}: Codex interface.{field} is required")
    capabilities = interface.get("capabilities")
    require(isinstance(capabilities, list) and all(nonempty(item) for item in capabilities),
            f"{name}: Codex interface.capabilities must be an array of strings")
    prompts = interface.get("defaultPrompt")
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3
            and all(nonempty(item) and len(item) <= 128 for item in prompts),
            f"{name}: Codex interface.defaultPrompt must have 1–3 strings of at most 128 characters")

    skills = plugin / "skills"
    require(skills.is_dir(), f"{name}: missing skills/ directory")
    skill_dirs = [path for path in skills.iterdir() if path.is_dir() and not path.name.startswith(".")]
    require(bool(skill_dirs), f"{name}: include at least one skill")
    for directory in skill_dirs:
        require(directory.name not in known_skills,
                f"{name}: duplicate skill name {directory.name!r} would collide in OpenCode")
        known_skills.add(directory.name)
        validate_skill(root, directory / "SKILL.md", plugin)
    return len(skill_dirs)


def validate_presets(root: Path, selection: dict) -> None:
    presets = {p["name"] for p in selection.get("presets", [])}
    directory = root / "configs"
    directories = {p.name for p in directory.iterdir() if p.is_dir() and not p.name.startswith(".")} if directory.exists() else set()
    require(directories == presets, "Every configs/ directory must be registered as a preset")
    for name in sorted(presets):
        for agent in AGENTS:
            for part, source, content in load_sources(root, name, agent, PARTS):
                text = content.decode("utf-8")
                if part == "instructions":
                    require("<!-- agent-skills:" not in text, "Preset source must not include installation markers")
                    continue
                if agent == "codex":
                    data = tomllib.loads(text)
                    require(data.get("name") == source.stem and nonempty(data.get("developer_instructions")),
                            f"{source}: agent name must match filename and instructions are required")
                else:
                    match = re.match(r"\A---\r?\n(.*?)^---[ \t]*\r?\n(.+)", text, re.M | re.S)
                    require(match is not None and bool(match[2].strip()), f"{source}: agent frontmatter/body required")
                    data = yaml.safe_load(match[1])
                    require(isinstance(data, dict), f"{source}: expected frontmatter mapping")
                    if agent == "claude-code":
                        require(data.get("name") == source.stem, f"{source}: agent name must match filename")
                    else:
                        require(data.get("mode") in ("primary", "subagent", "all"), f"{source}: invalid agent mode")
                require(nonempty(data.get("description")), f"{source}: agent description required")


def validate_repository(root: Path) -> tuple[str, int, int]:
    codex_name, codex_plugins = catalog(root, ".agents/plugins/marketplace.json", "codex")
    claude_name, claude_plugins = catalog(root, ".claude-plugin/marketplace.json", "claude")
    require(codex_name == claude_name, "Marketplace names differ between agents")
    require(codex_plugins == claude_plugins, "Plugin names or order differ between catalogs")
    directories = {path.name for path in (root / "plugins").iterdir() if path.is_dir() and not path.name.startswith(".")}
    require(directories == set(codex_plugins), "Every plugins/ directory must be registered in both catalogs")
    known_skills: set[str] = set()
    skill_count = sum(validate_plugin(root, name, known_skills) for name in codex_plugins)
    selection = load_catalog(root)
    validate_presets(root, selection)
    local = [s for s in selection["skills"] if s["ownership"] == "custom"]
    require({s["name"] for s in local} == known_skills, "Setup catalog must exactly match packaged custom skills")
    local_bundles = [p for p in selection["plugins"] if any(s["name"] in p["skills"] for s in local)]
    require([p["name"] for p in local_bundles] == codex_plugins, "Setup bundles must match native plugin names/order")
    for plugin in local_bundles:
        expected = {p.name for p in (root / "plugins" / plugin["name"] / "skills").iterdir() if p.is_dir() and not p.name.startswith(".")}
        require(set(plugin["skills"]) == expected, f'{plugin["name"]}: setup bundle differs from packaged skills')
        require(plugin["native"]["marketplace"] == codex_name, "Setup and native marketplace names differ")
        for skill in (s for s in local if s["name"] in expected):
            require(skill["path"] == f'plugins/{plugin["name"]}/skills/{skill["name"]}', f'{skill["name"]}: incorrect packaged path')
    return codex_name, len(codex_plugins), skill_count


def main() -> int:
    try:
        name, plugins, skills = validate_repository(ROOT)
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    selection = load_catalog(ROOT)
    presets = len(selection.get("presets", []))
    servers = len(selection.get("mcp_servers", []))
    print(f"Validated {name}: 2 catalogs, {plugins} plugins, {skills} skills, {presets} presets, {servers} MCP servers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
