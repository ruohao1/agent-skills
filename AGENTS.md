# graphify

- **graphify** (`~/.Codex/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
- When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else. If the path differs on this machine, locate the installed skill.

# Marketplace conventions

- This repository holds a personal marketplace for Codex, Claude Code, and OpenCode.
- Put each plugin in `plugins/<plugin-name>/`. Keep shared skill content inside that plugin's `skills/` directory.
- Keep `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` consistent: same marketplace name, plugin names, order, and source directories.
- Keep each plugin's Codex and Claude Code manifests consistent for name, version, description, and author.
- Update `CHANGELOG.md` under `Unreleased` alongside changes to skills, plugins, catalogs, setup behavior, or presets. Follow the existing categories and keep entries concise, with user-visible impact and affected plugin versions when relevant.
- The public repository is `ruohao1/agent-skills`. Use the Skills CLI (`npx skills@latest add ruohao1/agent-skills`) as the shared installation route for Codex, Claude Code, and OpenCode; native marketplaces are an additional route for Codex and Claude Code.
- Keep each skill self-contained and use unique skill names across plugins. The Skills CLI discovers their directories through the local entries in `.claude-plugin/marketplace.json`.
- See `docs/adding-plugins.md` for the packaging workflow. Run `python3 scripts/validate_marketplace.py` after changing catalogs, manifests, or skills.

# Curated setup

- `catalog.json` is the custom/upstream selection, with immutable upstream commit pins and a tested Skills CLI version. Do not vendor unchanged upstream tools or use upstream wildcard selections.
- Product Design and Engineering are categories, independent of ownership. Native bundles exist only for real plugins; do not add empty category plugins.
- `scripts/setup.py` coordinates portable or explicit native installs. Preserve existing content; never make `--yes` override a conflict or silently change scope.
- Keep setup runtime dependencies in the Python standard library. Reuse inventory/source/content helpers before adding another parser.
- Register optional configuration presets in `catalog.json`, keep shared instructions in `configs/<preset>/AGENTS.md`, and native agent definitions in `configs/<preset>/<agent>/agents/`. Keep them separate from `--all` skill installation; never bundle credentials or machine-specific settings.
- Preserve existing instructions and named agent definitions, including definitions in host settings and ancestor projects. Preview changes, back up appended instruction files, and report conflicts instead of overwriting.
- Run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate_marketplace.py`. Test real installers only in disposable homes/projects.
- Record behavioral evidence before shipping custom guidance; omit candidates that add no demonstrated value. Keep implementation plans with the implementation PR.
