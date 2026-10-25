# Product Design

Version **0.3.0** contains two independent skills:

- [product-brief](skills/product-brief/SKILL.md) frames the user task, evidence, scope, consequential states, and observable outcomes.
- [design-product](skills/design-product/SKILL.md) designs the selected solution's flows, interactions, recovery, and visual experience. It reuses an adequate brief and established UI patterns.

Use either skill with pasted context or repository files. Neither requires Linear or another skill. Product design saves a concise handoff to `docs/designs/<topic>.md` by default, or updates a relevant existing document. Explicit destinations and text-only requests take precedence. It preserves unrelated sections and stops before production changes. Designing does not stage, commit, publish, or add ignore rules.

An audit identifies supported problems and may already specify an adequate fix. Design develops a selected change when consequential choices remain, or documents it when requested. It is not a mandatory stage after every audit. [Software Design](../software-design/README.md) covers system contracts and code structure independently. See the [design evaluation](../../evals/design-skills.md) and [results](../../evals/results/2026-10-25-design-skills.md).

The brief includes STE-inspired writing guidance for clear English prose. It preserves technical detail without enforcing the full ASD-STE100 dictionary or claiming formal compliance. No personal preset is required. See the [writing evaluation](../../evals/results/2026-10-24-ste-writing.md).

```sh
npx skills@latest add ruohao1/agent-skills --skill product-brief design-product --agent codex claude-code opencode
```

Choose either skill by listing only its name. Add `--global` for use across projects. In Codex invoke `$design-product` or `$product-brief`; in Claude Code use `/design-product` for standalone installation or `/product-design:design-product` for the native plugin. In OpenCode ask to use the skill by name.

From a checkout, the full Product Design category includes the upstream Archify and Prototype skills:

```sh
python3 scripts/setup.py install --category product-design --agent codex --scope global
```

For this custom plugin alone through the native route:

```sh
python3 scripts/setup.py install --plugin product-design --route native --agent codex --scope global
```

See [setup](../../docs/setup.md) for Claude Code scopes and existing-installation handling. A native plugin and a category are different selections: upstream skills are not bundled inside this plugin.

Version 0.2.0 retires `product-diagrams` in favor of upstream `archify`, and `product-wireframes` in favor of upstream `prototype`. It also removes `product-design-review` after its baseline tasks already passed without added guidance. Use an ordinary design-review request. Old installed copies remain until their owner explicitly removes them.
