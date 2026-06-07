---
name: audit-kb
description: Project skill for the metodo repository knowledge-base audit. Use when the user asks for /audit-kb, a KB audit, health checks, catalog (kb.md) coverage, or link/frontmatter validation.
---

# audit-kb

Use the Claude project skill as the canonical source of instructions:

`../../../.claude/skills/audit-kb/SKILL.md`

When this skill triggers, read that file and follow it. This wrapper exists only so Codex can discover the project-level skill without duplicating the workflow.
