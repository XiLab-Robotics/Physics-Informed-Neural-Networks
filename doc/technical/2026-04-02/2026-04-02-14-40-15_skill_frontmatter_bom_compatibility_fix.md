# Skill Frontmatter BOM Compatibility Fix

## Overview

The repository-local skill
`.codex/skills/twincat-video-knowledge-pipeline/SKILL.md` was reported by the
skill loader as missing YAML frontmatter even though the file visibly started
with `---`.

The most likely cause is an encoding-level issue rather than a content-level
issue. This document records the compatibility fix so future skill edits do not
reintroduce the same loader failure.

## Technical Approach

The fix is to inspect the raw bytes of the repository-local `SKILL.md` files,
identify whether a UTF-8 byte-order mark is present before the YAML frontmatter,
and re-save only the affected skill file as UTF-8 without BOM.

This keeps the YAML frontmatter unchanged while restoring compatibility with
loaders that require the file to begin directly with `---`.

## Involved Components

- `.codex/skills/twincat-video-knowledge-pipeline/SKILL.md`
- `README.md`

## Implementation Steps

1. Inspect all repository-local `SKILL.md` files for a leading UTF-8 BOM.
2. Re-save the affected skill file without BOM while preserving the content.
3. Re-check the touched Markdown scope so the skill remains well-formed and
   repository-compliant.
4. Record the rule rationale from the README entry point.
