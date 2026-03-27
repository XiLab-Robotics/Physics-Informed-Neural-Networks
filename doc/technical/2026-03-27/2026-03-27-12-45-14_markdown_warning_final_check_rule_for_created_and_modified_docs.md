# Markdown Warning Final Check Rule For Created And Modified Docs

## Overview

The repository already includes Markdown validation tooling and explicit
documentation for:

- `scripts/tooling/markdown_style_check.py`
- `scripts/tooling/run_markdownlint.py`

The user requested that this become a stronger project rule:

- whenever a Markdown document is created or modified, its Markdown warnings
  should be checked before the task is considered complete.

This rule should apply especially to repository-owned documents such as:

- `README.md`
- files under `doc/`
- script documentation under `doc/scripts/`
- other repository-authored Markdown sources that are edited as part of the
  task.

## Technical Approach

The rule should be added as a persistent project instruction rather than left as
an informal reminder.

The intended workflow is:

1. create or modify the Markdown document;
2. run the repository-owned Markdown warning checks on the touched files or on a
   narrow relevant scope;
3. fix any warnings introduced by the change when the fix is local and
   straightforward;
4. do not close the task while known warning regressions remain in the modified
   Markdown files.

The rule is not intended to force repository-wide Markdown cleanup for every
small change. It is intended to prevent new or preserved warnings in the files
actively touched by the task.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `AGENTS.md`
  Repository instruction file that should receive the persistent rule after
  approval.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that should document the Markdown warning-check
  expectation after approval.
- `doc/scripts/tooling/markdown_style_check.md`
  Existing script documentation for the fast Markdown warning checker.
- `doc/scripts/tooling/run_markdownlint.md`
  Existing script documentation for the broader Markdownlint runner.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before modifying the persistent repository
   rules or workflow documentation.
3. After approval, update `AGENTS.md` so Markdown files created or modified by a
   task must be checked for warnings before closure.
4. Update `doc/guide/project_usage_guide.md` so the same rule is visible in the
   documented repository workflow.
5. Keep the rule scoped to created or modified Markdown files rather than
   requiring a full repository-wide cleanup for every task.
