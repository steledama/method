---
name: kb-review
description: Project skill for the metodo repository knowledge-base audit. Use when the user asks for /kb-review, a KB audit, health checks, catalog (kb/kb.md) coverage, or link/frontmatter validation.
---

# kb-review

Use the Claude project skill as the canonical source of instructions:

`../../../.claude/skills/kb-review/SKILL.md`

When this skill triggers, read that file and follow it. This wrapper exists only so Codex can discover the project-level skill without duplicating the workflow.
