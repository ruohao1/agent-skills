# Software Design

Version **0.1.0** provides two independent skills:

| Skill | Decisions |
| --- | --- |
| [design-architecture](skills/design-architecture/SKILL.md) | System responsibilities, data ownership, runtime interactions, recovery, and deployment constraints. A single application can need architecture design. |
| [design-code](skills/design-code/SKILL.md) | Module responsibilities, interfaces, dependencies, file and folder organization, and caller migration. |

Use either for a selected change or an existing design. Each reads relevant implementation and callers, preserves settled decisions, and leaves routine implementation choices open. The existing structure can be sufficient. An audit discovers and prioritizes problems; design resolves remaining consequential choices or records an explicitly requested design. An adequate fix can proceed directly to requested implementation.

Designs are saved to `docs/designs/<topic>.md` by default. A relevant existing document, explicit destination, or text-only request takes precedence. A coherent change can share one document across product, architecture, and code scopes. Focused updates preserve unrelated sections. Keep designs with related implementation unless instructed otherwise; designing alone does not stage, commit, publish, change ignore rules, or implement production code.

Neither skill requires a companion or personal preset. `codebase-design`, `domain-modeling`, and `archify` remain optional upstream aids. Product experience decisions belong to [Product Design](../product-design/README.md); no fixed sequence is required.

Install either skill by listing only its name, or select both:

```sh
npx skills@latest add ruohao1/agent-skills --skill design-architecture design-code --agent codex claude-code opencode
```

Add `--global` for use across projects. From a checkout, install this bundle with the setup coordinator:

```sh
python3 scripts/setup.py install --plugin software-design --agent codex --scope global
```

For the native plugin on Codex or Claude Code, add `--route native`. Choose one installation route to avoid duplicate skills. See [setup](../../docs/setup.md), the [evaluation protocol](../../evals/design-skills.md), and [recorded results](../../evals/results/2026-10-25-design-skills.md).
