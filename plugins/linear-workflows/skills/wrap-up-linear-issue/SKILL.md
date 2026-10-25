---
name: wrap-up-linear-issue
description: Use when preparing to move a Linear issue to Done or another completed state, or when asked to wrap up completed work or update its final TL;DR.
---

# Wrap up Linear issue

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Before moving a Linear issue to Done or its team's equivalent completed state, save and verify one short TL;DR at the top of its description. This is part of closing an issue; do not wait for a separate wrap-up request. A summary-only request does not authorize closing the issue. Honor explicit draft-only, comment-only, and narrow-edit requests. Finishing an unrelated local task does not trigger Linear updates.

## Establish the outcome

Read the current issue, original scope and acceptance criteria, relevant discussion across pages, and supporting artifacts. Use the connected tools' actual schemas. Distinguish implementation, tests, merge, deployment, source research, and live validation.

Check whether required work is complete. A Done status alone is not proof. If required work remains, explain the gap; do not publish a final wrap-up or move the issue to Done. Keep separate follow-up work separate: source research can be complete while its recommended live experiment remains unperformed. Do not expand the task into an audit or manufacture completion evidence.

## Write the TL;DR

Use a short paragraph or a few compact bullets covering the outcome, its important verification limit or remaining uncertainty, and one useful next action supported by existing context. Omit a next action when none adds value.

Link to decisive existing comments or artifacts, keeping detailed findings and chronology there. Use verified URLs and retain essential context inline when a link is unavailable. Do not invent links, results, decisions, or discovery order. Repository code references need verified immutable links to the published revision and supporting lines. If essential requested code evidence is unpublished or unverifiable, return an unsaved draft and identify the gap. This does not authorize committing or publishing code.

## Preserve and save

Reuse an equivalent current summary without rewriting it. Otherwise prepend a `## TL;DR` section or replace only the existing summary section. Preserve the original description beneath it, including requirements, acceptance criteria, and user notes. Leave comments, title, labels, assignee, priority, project, dates, and relations unchanged. No duplicate completion comment or new follow-up issue is needed.

Read the current description before saving; carry everything outside the summary forward unchanged when the API replaces the full body. Save without another approval round and verify the result. After an ambiguous timeout, read the issue before retrying. If access, evidence, or the save is unavailable or unconfirmed, report the gap and leave status unchanged.

Only after the summary is confirmed saved or already current, make the authorized transition to the team's actual completed state. Verify that result too. Return the confirmed issue link and a brief outcome, or an explicitly unsaved draft when saving was impossible.
