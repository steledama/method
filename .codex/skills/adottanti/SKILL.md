---
name: adottanti
description: Project skill for the periodic runtime-o1 audit of the method's adopter repositories. Use when the user asks for /adottanti, the monthly adopter audit, or the distance-from-telos photograph of the adopters.
---

# adottanti

Use the Claude project skill as the canonical source of instructions:

`../../../.claude/skills/adottanti/SKILL.md`

When this skill triggers, read that file and follow it. Codex has no Skill tool, so reading that file is how this skill is invoked: where the canonical text asks to invoke a skill with the Skill tool (as `cycle` does for `eval` and `exec`), open that skill's wrapper and read its canonical file. This wrapper exists only
so Codex can discover the project-level skill without duplicating the workflow.
