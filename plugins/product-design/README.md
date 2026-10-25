# Product Design

This custom plugin contains [product-brief](skills/product-brief/SKILL.md), version **0.2.1**. It frames the user task, evidence, consequential states and observable outcomes, and distinguishes decisions that block implementation from research that can proceed in parallel.

Use it independently with pasted context or repository files; it does not require Linear, another skill, or a fixed output location.

The skill includes STE-inspired writing guidance for clear English prose. It preserves technical detail without enforcing the full ASD-STE100 dictionary or claiming formal compliance. No personal preset is required. See the [writing evaluation](../../evals/results/2026-10-24-ste-writing.md).

```sh
npx skills@latest add ruohao1/agent-skills --skill product-brief --agent codex claude-code opencode
```

Add `--global` for use across projects. In Codex invoke `$product-brief`; in Claude Code use `/product-brief` for standalone installation or `/product-design:product-brief` for the native plugin. In OpenCode ask to use `product-brief`.

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
