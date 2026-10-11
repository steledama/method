---
name: cycle
description: Project skill for the joint cycle in metodo. Use when the user asks for /cycle, a full round eval all → exec all → commit, or when the autonomous cycle unit runs `cycle autonomo` without a custodian.
---

# cycle

Use the Claude project skill as the canonical source of instructions:

`../../../.claude/skills/cycle/SKILL.md`

When this skill triggers, read that file and follow it. This wrapper exists only so Codex can discover the project-level skill without duplicating the workflow.
