---
name: method-review
description: Project skill for reviewing drift between a method adopter and the canonical method repository. Use when the user asks for /method-review, method drift, adopter alignment, or propagation of method changes.
---

# method-review

Use the Claude project skill as the canonical source of instructions:

`../../../.claude/skills/method-review/SKILL.md`

When this skill triggers, read that file and follow it. This wrapper exists only
so Codex can discover the project-level skill without duplicating the workflow.
