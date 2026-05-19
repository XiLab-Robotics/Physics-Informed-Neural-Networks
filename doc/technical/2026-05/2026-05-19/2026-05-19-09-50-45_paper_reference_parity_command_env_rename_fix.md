# Paper Reference Parity Command Environment Rename Fix

## Overview

This document plans a narrow documentation correction after the Conda
environment rename introduced by commit `a136e760abc5cc5cab0aaa6683b93f9439e98d92`.

Commit `74e9a397964068ac2d3c7ac12fb81cade2036486` added the paper-reference
archive parity report command before the rename was reconciled. One command in
`doc/guide/project_usage_guide.md` still uses the obsolete
`standard_ml_codex_env` environment name.

## Technical Approach

Update only the affected command in `doc/guide/project_usage_guide.md`:

- replace `conda run -n standard_ml_codex_env` with
  `conda run -n pinns_env`;
- preserve the existing command path, suffix, and surrounding documentation.

No code, generated validation artifact, model archive, or campaign state change
is required.

No subagent is planned for this task.

## Involved Components

| Component | Role |
| --- | --- |
| `doc/guide/project_usage_guide.md` | Contains the stale command to fix. |
| `doc/README.md` | Registers this technical document. |
| `scripts/tooling/markdown/markdown_style_check.py` | Repository Markdown warning checker. |
| `scripts/tooling/markdown/run_markdownlint.py` | Repository Markdownlint entry point. |

## Implementation Steps

1. Update the stale Conda environment name in the paper-reference archive parity
   command.
2. Run scoped Markdown QA on the modified Markdown files.
3. Check Git status and staged size before committing.
4. Create a narrow commit containing only this documentation correction and
   this technical document.
