---
name: tasks-review
description: Project skill for reviewing open tasks in metodo. Use when the user asks for /tasks-review, task review, o1/plan.md and o2 consistency, priority/dependency review, or suggested next task selection.
---

# tasks-review

Use the Claude project skill as the canonical source of instructions:

`../../../.claude/skills/tasks-review/SKILL.md`

When this skill triggers, read that file and follow it. This wrapper exists only so Codex can discover the project-level skill without duplicating the workflow.
