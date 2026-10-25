#!/usr/bin/env python3
"""Select curated tools and delegate installation to their supported installers."""
from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
from typing import Mapping

try:
    from .setup_inventory import (AGENTS, Target, Installation, Inventory, destination, fingerprint,
                                  inspect_target, read_json, receipt_path, scope_root, source_identity, cli_problem, installer_lock, safe_write_path)
    from . import setup_presets, setup_mcp
except ImportError:
    from setup_inventory import (AGENTS, Target, Installation, Inventory, destination, fingerprint,
                                 inspect_target, read_json, receipt_path, scope_root, source_identity, cli_problem, installer_lock, safe_write_path)
    import setup_presets
    import setup_mcp


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
REPOSITORY = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*")
CATEGORIES = ("product-design", "engineering")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def identifier(value: object) -> bool:
    return isinstance(value, str) and len(value) <= 64 and NAME.fullmatch(value) is not None


def load_catalog(root: Path = ROOT) -> dict:
    data = read_json(root / "catalog.json")
    require(data.get("schema_version") == 1, "Unsupported catalog schema")
    version = data.get("installer_version")
    require(isinstance(version, str) and re.fullmatch(r"\d+\.\d+\.\d+", version), "Pin an installer version")
    sources = data.get("sources")
    require(isinstance(sources, dict) and bool(sources), "Sources must be a nonempty object")
    for name, source in sources.items():
        require(identifier(name) and isinstance(source, dict), "Invalid source")
        repo = source.get("repository")
        require(isinstance(repo, str) and REPOSITORY.fullmatch(repo), f"Invalid repository for {name}")
        if "local_path" in source:
            require(source["local_path"] == "." and source.get("ref") is None,
                    "Local source must be the current checkout")
        else:
            ref = source.get("ref")
            require(isinstance(ref, str) and re.fullmatch(r"[0-9a-f]{40}", ref), f"Pin a commit for {name}")
    skills = data.get("skills")
    require(isinstance(skills, list) and bool(skills), "Skills must be a nonempty array")
    known = set()
    for skill in skills:
        require(isinstance(skill, dict), "Invalid skill entry")
        name = skill.get("name")
        require(identifier(name) and name not in known, f"Invalid or duplicate skill {name!r}")
        known.add(name)
        require(skill.get("category") in CATEGORIES, f"Invalid category for {name}")
        source = skill.get("source")
        require(isinstance(source, str) and source in sources, f"Unknown source for {name}")
        expected = "custom" if "local_path" in sources[source] else "upstream"
        require(skill.get("ownership") == expected, f"Incorrect ownership for {name}")
        path = skill.get("path")
        require(isinstance(path, str) and bool(path) and "\\" not in path,
                f"Invalid skill path for {name}")
        parts = PurePosixPath(path)
        require(not parts.is_absolute() and ".." not in parts.parts and parts.name == name,
                f"Skill path escapes source or mismatches {name}")
        require(isinstance(skill.get("description"), str) and bool(skill["description"].strip()),
                f"Description required for {name}")
    plugins = data.get("plugins")
    require(isinstance(plugins, list), "Plugins must be an array")
    plugin_names = set()
    for plugin in plugins:
        require(isinstance(plugin, dict), "Invalid plugin")
        name = plugin.get("name")
        require(identifier(name) and name not in plugin_names, "Invalid or duplicate plugin")
        plugin_names.add(name)
        members = plugin.get("skills")
        require(isinstance(members, list) and bool(members) and all(isinstance(x, str) for x in members),
                f"Invalid members for {name}")
        require(len(set(members)) == len(members) and set(members) <= known, f"Unknown/duplicate members for {name}")
        native = plugin.get("native")
        require(isinstance(native, dict) and identifier(native.get("marketplace")), f"Invalid marketplace for {name}")
        repo = native.get("repository")
        require(isinstance(repo, str) and REPOSITORY.fullmatch(repo), f"Invalid native repository for {name}")
        require(all(sources[s["source"]]["repository"] == repo for s in skills if s["name"] in members),
                f"Native plugin {name} spans different sources")
    presets = data.get("presets", [])
    require(isinstance(presets, list), "Presets must be an array")
    preset_names = set()
    for preset in presets:
        require(isinstance(preset, dict) and identifier(preset.get("name")), "Invalid preset")
        require(preset["name"] not in preset_names, "Duplicate preset")
        preset_names.add(preset["name"])
        require(isinstance(preset.get("description"), str) and bool(preset["description"].strip()),
                "Preset description required")
    servers = data.get("mcp_servers", [])
    require(isinstance(servers, list), "MCP servers must be an array")
    server_names = set()
    for server in servers:
        require(isinstance(server, dict) and server.get("name") == "chrome-devtools", "Unsupported MCP server")
        require(server["name"] not in server_names, "Duplicate MCP server")
        server_names.add(server["name"])
        require(isinstance(server.get("version"), str) and re.fullmatch(r"\d+\.\d+\.\d+", server["version"]),
                "MCP version must be pinned")
        require(isinstance(server.get("description"), str) and bool(server["description"].strip()),
                "MCP description required")
    return data


def select_skills(catalog: dict, selector: str, values: list[str]) -> list[str]:
    names = [s["name"] for s in catalog["skills"]]
    if selector == "all":
        return names
    if selector == "skill":
        require(bool(values) and all(v in names for v in values), "Unknown or empty skill selection")
        return list(dict.fromkeys(values))
    if selector == "category":
        require(len(values) == 1 and values[0] in CATEGORIES, "Unknown category")
        return [s["name"] for s in catalog["skills"] if s["category"] == values[0]]
    if selector == "plugin":
        plugins = {p["name"]: p for p in catalog["plugins"]}
        require(len(values) == 1 and values[0] in plugins, "Unknown plugin")
        return list(plugins[values[0]]["skills"])
    raise ValueError("Choose all, category, skill, or plugin")


@dataclass
class PlanItem:
    names: tuple[str, ...]
    target: Target
    status: str
    reason: str
    command: tuple[str, ...] | None = None
    location: Path | None = None
    route: str = "skills"
    version: str | None = None


def _existing(skill: dict, catalog: dict, inventory: Inventory) -> tuple[str, str]:
    found = [i for i in inventory.installations if i.name == skill["name"]]
    if not found:
        return "missing", "Not installed"
    source = catalog["sources"][skill["source"]]
    identity = source_identity(source["repository"])
    if any(i.modified for i in found):
        return "conflict", "Locally modified content; preserved"
    if len({i.route for i in found}) > 1:
        return "conflict", "Both native and standalone instructions are installed; choose one route"
    if any(i.enabled is not True for i in found):
        return "needs-setup", "Existing installation is disabled, incomplete, or has unknown activation"
    if any(i.source is not None and i.source != identity for i in found):
        return "conflict", "The installed name belongs to a different source"
    if len({i.digest for i in found if i.digest}) > 1:
        return "conflict", "Different copies of this skill are visible"
    try:
        for installed in found:
            if installed.path:
                _check_content(installed.path, skill["name"])
    except (OSError, ValueError) as error:
        return "needs-setup", f"Existing skill is incomplete: {error}"
    unknown = [i for i in found if i.source is None]
    if unknown:
        local = ROOT / skill["path"]
        if "local_path" not in source or not local.is_dir():
            return "conflict", "Existing content has unknown ownership; preserved"
        expected = fingerprint(local)
        if any(i.digest != expected for i in unknown):
            return "conflict", "Existing content differs from the selected local skill"
    return "present", "Already available; preserved without updating"


def build_plan(catalog: dict, names: list[str], targets: list[Target], route: str,
               inventories: Mapping[Target, Inventory], env: Mapping[str, str] | None = None) -> list[PlanItem]:
    env = os.environ if env is None else env
    require(route in ("skills", "native"), "Unknown installation route")
    if route == "native":
        plugin = next((p for p in catalog["plugins"] if set(p["skills"]) == set(names)), None)
        require(plugin is not None, "Native installation requires a complete catalog plugin")
        return [_native_plan(catalog, plugin, target, inventories[target]) for target in targets]
    skills = {s["name"]: s for s in catalog["skills"]}
    require(all(name in skills for name in names), "Unknown skill selection")
    result = []
    for target in targets:
        require(target.agent in AGENTS and target.scope in ("global", "project"), "Unsupported agent or scope")
        inventory = inventories[target]
        for name in names:
            skill = skills[name]
            source = catalog["sources"][skill["source"]]
            location = destination(target, env, name).resolve()
            if inventory.errors:
                result.append(PlanItem((name,), target, "needs-setup", "; ".join(inventory.errors), location=location))
                continue
            status, reason = _existing(skill, catalog, inventory)
            command = None
            if status == "missing":
                try:
                    _safe_metadata_path(installer_lock(target, env))
                    _safe_metadata_path(receipt_path(target, env))
                except (OSError, ValueError) as error:
                    result.append(PlanItem((name,), target, "conflict", str(error), location=location))
                    continue
                selected_source = str(ROOT) if "local_path" in source else f'https://github.com/{source["repository"]}/tree/{source["ref"]}/{skill["path"]}'
                command = ("npx", "--yes", f'skills@{catalog["installer_version"]}', "add", selected_source,
                           "--skill", name, "--agent", target.agent, "--copy", "--yes")
                if target.scope == "global":
                    command += ("--global",)
            result.append(PlanItem((name,), target, status, reason, command, location))
    return result


def _native_plan(catalog: dict, plugin: dict, target: Target, inventory: Inventory) -> PlanItem:
    item = PlanItem(tuple(plugin["skills"]), target, "missing", f'Install full {plugin["name"]} plugin', route="native")
    if target.agent == "opencode" or (target.agent == "codex" and target.scope != "global"):
        return replace(item, status="unsupported", reason="This host/scope has no supported native plugin route")
    if inventory.errors:
        return replace(item, status="needs-setup", reason="; ".join(inventory.errors))
    found = [i for i in inventory.installations if i.name in plugin["skills"] or i.plugin == plugin["name"]]
    if any(i.route == "skills" for i in found):
        return replace(item, status="conflict", reason="Standalone skills already overlap this plugin; preserve them and choose one route")
    if found:
        for skill in (s for s in catalog["skills"] if s["name"] in plugin["skills"]):
            status, reason = _existing(skill, catalog, inventory)
            if status != "present":
                return replace(item, status="conflict" if status == "conflict" else "needs-setup", reason=reason)
        step = plugin["native"].get("setup", {}).get(target.agent)
        return replace(item, status="needs-setup" if step else "present", reason=step or "Full plugin already installed; preserved",
                       version=next((i.version for i in found if i.version), None))
    selector = f'{plugin["name"]}@{plugin["native"]["marketplace"]}'
    command = (("codex", "plugin", "add", selector, "--json") if target.agent == "codex" else
               ("claude", "plugin", "install", selector, "--scope", "user" if target.scope == "global" else "project"))
    return replace(item, command=command)


def _check_content(folder: Path, name: str) -> str:
    text = (folder / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)^---[ \t]*\r?\n(.+)", text, re.S | re.M)
    require(match is not None, f"Installed {name} lacks skill frontmatter/body")
    field = re.search(r"^name:\s*['\"]?([a-z0-9-]+)['\"]?\s*$", match[1], re.M)
    require(field is not None and field[1] == name, f"Installed skill name does not match {name}")
    prose = re.sub(r"(`+).*?\1|(?ms:^[ \t]*(~{3,})[^\n]*\n.*?^[ \t]*\2[ \t]*$)", "", text, flags=re.S)
    for link in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", prose):
        if ":" in link or link.startswith("#"):
            continue
        resource = folder / link.split("#")[0]
        require(resource.resolve().is_relative_to(folder.resolve()) and resource.exists(),
                f"Missing or external skill resource: {resource}")
    return fingerprint(folder)


def _safe_metadata_path(path: Path) -> None:
    safe_write_path(path)
    if path.exists():
        if path.name == "skills-lock.json":
            require(set(read_json(path)) <= {"version", "skills"}, f"Installer would discard unknown metadata in {path}")


def _write_receipt(item: PlanItem, catalog: dict, env: Mapping[str, str], digest: str) -> None:
    path = receipt_path(item.target, env)
    _safe_metadata_path(path)
    data = read_json(path) if path.exists() else {"schema_version": 1, "records": {}}
    require(data.get("schema_version") == 1 and isinstance(data.get("records"), dict), "Unknown setup receipt format")
    name = item.names[0]
    skill = next(s for s in catalog["skills"] if s["name"] == name)
    source = catalog["sources"][skill["source"]]
    data["records"][f"{item.target.agent}:{name}"] = {
        "name": name, "source": source["repository"], "ref": source["ref"] if item.route == "skills" else None,
        "agent": item.target.agent, "route": item.route, "version": item.version,
        "path": str(item.location), "digest": digest,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=".state-", delete=False) as out:
            temporary = Path(out.name)
            json.dump(data, out, indent=2)
            out.write("\n")
            out.flush()
            os.fsync(out.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def _apply_native(item: PlanItem, catalog: dict, env: Mapping[str, str]) -> PlanItem:
    plugin = next(p for p in catalog["plugins"] if set(p["skills"]) == set(item.names))
    native = plugin["native"]
    binary = "codex" if item.target.agent == "codex" else "claude"
    def run(command):
        result = subprocess.run(tuple(command), cwd=item.target.project or ROOT, env=dict(env),
                                capture_output=True, text=True, timeout=180)
        require(result.returncode == 0, f'{binary} failed: {(result.stderr or result.stdout)[-600:]}')
        require(not cli_problem(result.stderr), f'{binary} returned incomplete information: {result.stderr[-600:]}')
        return result
    def registered():
        listing = json.loads(run([binary, "plugin", "marketplace", "list", "--json"]).stdout)
        marketplaces = listing.get("marketplaces") if isinstance(listing, dict) else listing
        require(isinstance(marketplaces, list) and all(isinstance(m, dict) for m in marketplaces), "Unrecognized marketplace inventory")
        matches = [m for m in marketplaces if m.get("name") == native["marketplace"]]
        require(len(matches) <= 1, "Ambiguous marketplace registration")
        return matches[0] if matches else None
    match = registered()
    local = any("local_path" in catalog["sources"][s["source"]] for s in catalog["skills"] if s["name"] in item.names)
    if not match:
        command = [binary, "plugin", "marketplace", "add", str(ROOT) if local else native["repository"]]
        if binary == "codex":
            command.append("--json")
        run(command)
        match = registered()
        require(match is not None, "Marketplace registration could not be verified")
    source = match.get("marketplaceSource", {}).get("source") or match.get("source")
    if source == "directory":
        source = match.get("path")
    elif source == "github":
        source = match.get("repo")
    if isinstance(source, dict):
        source = source.get("url") or source.get("repo") or source.get("path")
    same_local = local and isinstance(source, str) and Path(source).is_absolute() and Path(source).resolve() == ROOT.resolve()
    if not same_local and source_identity(source) != source_identity(native["repository"]):
        return replace(item, status="conflict", reason="Marketplace name is already registered to another or unknown source", command=None)
    run(item.command)
    post = inspect_target(item.target, env)
    checked = _native_plan(catalog, plugin, item.target, post)
    if checked.status not in ("present", "needs-setup") or post.errors:
        return replace(item, status="failed", reason="Native installation could not be verified: " + checked.reason, command=None)
    for name in item.names:
        record = next((i for i in post.installations if i.name == name and i.route == "native" and i.path), None)
        require(record is not None, f"Native install is missing {name}")
        digest = _check_content(record.path, name)
        _write_receipt(replace(item, names=(name,), location=record.path.resolve(), version=record.version), catalog, env, digest)
    return replace(checked, status="installed" if checked.status == "present" else "needs-setup",
                   reason=("Full plugin installed; reload the host session" if checked.status == "present" else checked.reason), command=None)


def apply_plan(items: list[PlanItem], catalog: dict, env: Mapping[str, str]) -> list[PlanItem]:
    results = []
    for item in items:
        if item.status != "missing":
            results.append(item)
            continue
        try:
            inventory = inspect_target(item.target, env)
            fresh = build_plan(catalog, list(item.names), [item.target], item.route, {item.target: inventory}, env)[0]
            if fresh.location != item.location:
                results.append(replace(item, status="conflict", reason="Destination changed after preview", command=None))
                continue
            if fresh.status != "missing":
                results.append(fresh)
                continue
            if item.route == "native":
                results.append(_apply_native(fresh, catalog, env))
                continue
            folder = destination(item.target, env, item.names[0])
            if folder.exists() or folder.is_symlink():
                results.append(replace(item, status="conflict", reason="Destination appeared after preview; preserved", command=None))
                continue
            completed = subprocess.run(fresh.command, cwd=item.target.project or ROOT, env=dict(env),
                                       capture_output=True, text=True, timeout=180)
            if completed.returncode:
                raise ValueError(f"Installer exited {completed.returncode}: {(completed.stderr or completed.stdout)[-600:].strip()}")
            digest = _check_content(folder, item.names[0])
            skill = next(s for s in catalog["skills"] if s["name"] == item.names[0])
            source = catalog["sources"][skill["source"]]
            if "local_path" in source:
                require(digest == fingerprint(ROOT / skill["path"]), "Installed files differ from the selected local source")
            else:
                post = inspect_target(item.target, env)
                require(not post.errors and any(i.name == item.names[0] and i.source == source_identity(source["repository"])
                            and i.ref == source["ref"] and i.skill_path == skill["path"] + "/SKILL.md"
                            and i.path and i.path.resolve() == folder.resolve() for i in post.installations),
                        "Installer did not record the selected upstream source, commit, and skill path")
            _write_receipt(item, catalog, env, digest)
            results.append(replace(item, status="installed", reason="Files and source checked; start a new agent session", command=None))
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            results.append(replace(item, status="failed", reason=str(error), command=None))
    return results


def _wizard(catalog: dict) -> list[str]:
    print("Select: 1 all skills, 2 category, 3 individual skills, 4 plugin bundle, 5 configuration preset, 6 MCP server")
    choice = input("Selection [1]: ").strip() or "1"
    if choice == "1":
        selection = ["--all"]
    elif choice == "2":
        selection = ["--category", input("Category (product-design / engineering): ").strip()]
    elif choice == "3":
        for skill in catalog["skills"]:
            print(f'  {skill["name"]}: {skill["description"]}')
        selection = ["--skill", *input("Skill names, separated by spaces: ").split()]
    elif choice == "4":
        print("Bundles: " + ", ".join(p["name"] for p in catalog["plugins"]))
        selection = ["--plugin", input("Plugin name: ").strip()]
        route = input("Route (skills / native) [skills]: ").strip() or "skills"
        selection += ["--route", route]
    elif choice == "5":
        for preset in catalog.get("presets", []):
            print(f'  {preset["name"]}: {preset["description"]}')
        selection = ["--preset", input("Preset name: ").strip()]
        parts = input("Parts (instructions agents) [both]: ").split()
        if parts:
            selection += ["--preset-part", *parts]
    elif choice == "6":
        for server in catalog.get("mcp_servers", []):
            print(f'  {server["name"]}: {server["description"]} (global scope only)')
        selection = ["--mcp", input("MCP server name: ").strip()]
    else:
        raise ValueError("Unknown selection")
    agents = input("Agents (codex claude-code opencode), separated by spaces: ").split()
    scope = input("Scope (global / project): ").strip()
    return ["install", *selection, "--agent", *agents, "--scope", scope]


def _show(items: list[PlanItem]) -> None:
    for item in items:
        version = f" v{item.version}" if item.version else ""
        print(f'{item.status:12} {", ".join(item.names)}{version} [{item.target.agent}, {item.target.scope}]: {item.reason}')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", nargs="?", choices=("list", "plan", "install"))
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true")
    group.add_argument("--category", choices=CATEGORIES)
    group.add_argument("--skill", nargs="+")
    group.add_argument("--plugin")
    group.add_argument("--preset", help="Apply a configuration preset separately from skills/plugins")
    group.add_argument("--mcp", help="Configure a selected MCP server separately from skills/plugins")
    parser.add_argument("--preset-part", nargs="+", choices=setup_presets.PARTS,
                        help="Choose instructions, agents, or both (default)")
    parser.add_argument("--agent", nargs="+", choices=AGENTS)
    parser.add_argument("--scope", choices=("global", "project"))
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--route", choices=("skills", "native"), default="skills")
    parser.add_argument("--yes", action="store_true", help="Confirm the displayed selection; never overrides conflicts")
    try:
        catalog = load_catalog(ROOT)
        args = parser.parse_args(argv)
        if args.action is None:
            require(sys.stdin.isatty(), "Choose list, plan, or install with explicit selection, agents, and scope")
            args = parser.parse_args(_wizard(catalog))
        if args.action == "list":
            servers = catalog.get("mcp_servers", [])
            if args.mcp:
                servers = [s for s in servers if s["name"] == args.mcp]
                require(bool(servers), "Unknown MCP server")
            if not args.preset:
                for server in servers:
                    print(f'{server["name"]:26} MCP server v{server["version"]} (global)\n  {server["description"]}')
            if args.mcp:
                return 0
            if args.preset:
                presets = [p for p in catalog.get("presets", []) if p["name"] == args.preset]
                require(bool(presets), "Unknown preset")
            else:
                presets = catalog.get("presets", [])
            for skill in catalog["skills"]:
                if args.preset:
                    break
                source = catalog["sources"][skill["source"]]
                print(f'{skill["name"]:26} {skill["category"]:14} {skill["ownership"]:8} {source["repository"]}\n  {skill["description"]}')
            for preset in presets:
                print(f'{preset["name"]:26} configuration preset\n  {preset["description"]}')
            return 0
        require(bool(args.agent) and bool(args.scope), "Select --agent and --scope before installation")
        require(args.project.is_dir(), f"Project directory does not exist: {args.project}")
        targets = [Target(agent, args.scope, args.project.absolute()) for agent in dict.fromkeys(args.agent)]
        require(not args.preset_part or bool(args.preset), "--preset-part requires --preset")
        if args.mcp:
            require(args.route == "skills", "--route native is for plugins, not MCP servers")
            servers = [s for s in catalog.get("mcp_servers", []) if s["name"] == args.mcp]
            require(bool(servers), "Unknown MCP server")
            return setup_mcp.run(servers[0], targets, args.action, args.yes, os.environ)
        if args.preset:
            require(args.route == "skills", "--route native is for plugins, not configuration presets")
            require(any(p["name"] == args.preset for p in catalog.get("presets", [])), "Unknown preset")
            return setup_presets.run(ROOT, args.preset, targets, tuple(args.preset_part or setup_presets.PARTS),
                                     args.action, args.yes, os.environ)
        selector, values = next(((key, value if isinstance(value, list) else [value]) for key, value in
                                 (("all", args.all), ("category", args.category), ("skill", args.skill), ("plugin", args.plugin)) if value), ("", []))
        names = select_skills(catalog, selector, values)
        require(args.route != "native" or bool(args.plugin), "The native route requires a complete --plugin")
        inventories = {target: inspect_target(target, os.environ) for target in targets}
        items = build_plan(catalog, names, targets, args.route, inventories)
        print(f"Route: {args.route}" + (" (skills only; no native hooks or servers)" if args.route == "skills" else ""))
        for name in names:
            skill = next(s for s in catalog["skills"] if s["name"] == name)
            print(f'  {name}: {skill["ownership"]}, {catalog["sources"][skill["source"]]["repository"]}')
        _show(items)
        if args.action == "plan":
            return 0 if all(i.status in ("missing", "present") for i in items) else 1
        if not args.yes and any(i.status == "missing" for i in items):
            require(sys.stdin.isatty(), "Use --yes after reviewing the plan in noninteractive mode")
            if input("Install the missing items shown above? [y/N]: ").strip().lower() not in ("y", "yes"):
                return 0
        results = apply_plan(items, catalog, os.environ)
        _show(results)
        unresolved = [i for i in results if i.status not in ("installed", "present")]
        if unresolved:
            print("Unresolved selections (resolve the reported issue, then retry these only):")
            for item in unresolved:
                print(f'  {" ".join(item.names)} for {item.target.agent} at {item.target.scope} scope')
        return 1 if unresolved else 0
    except (OSError, ValueError, EOFError) as error:
        print(f"Setup: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
