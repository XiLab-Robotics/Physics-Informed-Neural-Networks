# Markdown Final Blank Line Check Rule

## Overview

The repository already requires Markdown warning checks on repository-owned
Markdown files created or modified by a task.

The user requested one more explicit addition to that rule:

- include the final blank-line state of the file in the Markdown check routine,
  especially for `README.md` and other repository-owned Markdown indexes.

The practical motivation is that some editor-integrated Markdown checkers may
surface a trailing repeated-empty-line condition at the end of the file even
when the repository-owned checker does not report it the same way.

## Technical Approach

The persistent Markdown check rule should be tightened so the final-pass review
of touched Markdown files also confirms:

- no duplicated empty line at the end of the file;
- no accidental trailing repeated blank-line pair left after edits;
- only a normal single final newline remains at end of file.

This should become part of the repository's Markdown workflow guidance, not a
one-off cleanup note.

The rule should remain scoped to repository-owned Markdown files touched by the
task.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `AGENTS.md`
  Repository instruction file that should receive the more explicit Markdown
  final blank-line check rule after approval.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that should describe the same final-pass Markdown
  check after approval.
- `doc/technical/2026-03/2026-03-27/2026-03-27-12-45-14_markdown_warning_final_check_rule_for_created_and_modified_docs.md`
  Existing broader Markdown warning-check rule that this note refines.
- `doc/technical/2026-03/2026-03-27/2026-03-27-12-44-18_readme_md012_final_check_rule.md`
  Existing README-specific note that motivates the broader final blank-line
  clarification.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before modifying persistent repository rules
   or workflow documentation.
3. After approval, update `AGENTS.md` so the Markdown final-pass check includes
   the file-ending blank-line condition for touched Markdown files.
4. Update `doc/guide/project_usage_guide.md` so the same final-pass check is
   visible in the documented Markdown workflow.
5. Keep the rule scoped to touched repository-owned Markdown files rather than a
   repository-wide cleanup requirement.
