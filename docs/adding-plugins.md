# Adding custom or upstream tools

Product Design and Engineering describe the task. Custom and upstream describe ownership. Prefer an existing upstream skill when it satisfies the need; do not copy it here merely to list it. Each addition must have a concrete use and remain usable on the advertised agents.

## Custom skills

Put a plugin in `plugins/<plugin-name>/`, with shared skill content in `skills/<unique-skill-name>/SKILL.md`. Keep required references, scripts and assets inside that skill directory. Use lowercase names separated by hyphens; the frontmatter name must match the directory.

```markdown
---
name: example-workflow
description: Use when a specific recurring task needs this workflow.
---

Task-specific instructions and the smallest resources needed to apply them.
```

Before adding instructions, record a realistic prompt and criteria under `evals/`, run a baseline without the candidate, then check the candidate against the same task and a narrower counterexample. Report actual observations. If the baseline already meets the need, omit the candidate instead of manufacturing a failure or padding the catalog.

Copy the structure of [Product Design](../plugins/product-design/) for the paired `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` files. Keep name, version, description and author identical. Both declare `"skills": "./skills/"`. The Codex manifest also supplies its `interface` metadata. Increment both versions together when packaged content changes.

Register the plugin at the same position in both native catalogs. Codex's `.agents/plugins/marketplace.json` uses:

```json
{
  "name": "example-tools",
  "source": {"source": "local", "path": "./plugins/example-tools"},
  "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
  "category": "Productivity"
}
```

Claude's `.claude-plugin/marketplace.json` uses:

```json
{"name": "example-tools", "source": "./plugins/example-tools"}
```

The Skills CLI discovers local skill directories through the Claude catalog. Keep remote entries out of these two catalogs.

Add each custom skill to `catalog.json` with its category, `ownership: "custom"`, `source: "local"`, actual path and description. Add a plugin bundle listing exactly its packaged skill names, with native marketplace `personal` and repository `ruohao1/agent-skills`. The validator requires exact agreement; no unregistered local skill or empty placeholder plugin is allowed.

## Upstream selections

Add a source with its public GitHub `owner/repository` and a full forty-character commit. Add only the chosen skill names and paths using `ownership: "upstream"`. Inspect their license, linked resources, scripts and references to other skills at that revision. Record prerequisites and verify discovery in a disposable installation. A source pin must identify a commit, not a moving branch or tag.

Add a bundle only when a corresponding complete native plugin exists. Its `native` metadata records marketplace, repository and host-specific `setup` instructions for hooks, authentication or activation. Portable installation does not include native features. Native versions follow the host marketplace rather than the portable commit pin.

Do not add a second copy or alias for an existing skill. Check unique names across the whole selection. If a dependency is genuinely required, curate it explicitly; a mention of another skill does not automatically install it.

## Configuration presets

Register each preset's unique `name` and `description` in `catalog.json` under `presets`. Keep one shared instruction source in `configs/<preset>/AGENTS.md`, following [personal](../configs/personal/README.md). Setup installs it under each host's native instruction filename. Each host needs at least one agent definition in `configs/<preset>/<agent>/agents/`: TOML for Codex, Markdown with YAML frontmatter for Claude Code and OpenCode. Use unique reviewer names, matching the filename and any native `name` field. Put descriptions and instructions in each native definition; OpenCode also requires an explicit mode.

Keep credentials, machine-specific paths, provider choices, and copied personal settings out of the preset. Describe any deliberate tool restrictions and permission inheritance accurately. Use host-native fields only when supported by the documented host version. Do not package presets as fake skills or add them to `--all`; users choose them separately.

Run the validator and preservation tests, then check fresh, existing, and repeated application in disposable homes/projects. Verify actual host loading where possible and record what was not checked. Preference files state a user's choices; claims of improved behavior need separate comparative evidence.

## MCP servers

Keep MCP server selections in `catalog.json` under `mcp_servers`, separate from
skills, plugins, and instruction presets. The current installer supports only
`chrome-devtools`, with an exact npm version and a description. Do not package
upstream MCP code or create a placeholder skill for it.

When changing its version or launch options, check the official package and
host documentation. Run preservation tests and a real MCP handshake plus a
browser tool in a disposable profile. Record the package version, host versions,
and runtime limits. Existing configurations are preserved rather than upgraded.

## Verification and maintenance

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_marketplace.py
```

The validator checks paired catalogs/manifests, exact local selection, unique names, frontmatter, referenced resources, escaping symlinks, registered preset directories, and native agent syntax. Unit tests include invalid packages and installer preservation failures. Runtime setup uses Python 3.11+ and its standard library; PyYAML is only a development dependency.

Use disposable homes, agent configuration roots, npm caches and project folders for actual installation tests. Supply them in the test child process's environment. Never redirect an unreviewed install into your normal setup. Inspect copied resources and source metadata, repeat the selection, and verify unrelated files remain unchanged. Test native plugins separately to avoid duplicate instructions.

A successful package install does not establish authenticated agent loading. Start a test host session where available; record any unperformed activation check explicitly. Keep network/native smoke tests separate from deterministic CI.

Updates are explicit maintenance. Review an upstream revision and its dependencies, edit its pin, repeat the relevant checks, then publish the catalog change. Existing installations are preserved by the coordinator; users review and update selected tools through their owning installer as described in [setup](setup.md). Keep implementation plans with the implementation PR, never in a standalone planning PR unless requested.
