# Sphinx Documentation Regeneration

## Overview

This document defines a focused repository task to regenerate the canonical
Sphinx documentation portal for the current repository state.

The current Sphinx source tree lives under `site/`, and the documented local
build command is:

- `python -m sphinx -W -b html site site/_build/html`

The user requested a regeneration of the repository documentation through that
pipeline. The goal is to rebuild the HTML output so the portal reflects the
latest repository-authored documentation and script docstrings already present
in the canonical tree.

## Technical Approach

The implementation should:

1. verify that the current Python environment can run the canonical Sphinx
   build command;
2. execute the repository build with warnings treated as errors through `-W`;
3. inspect the outcome and confirm whether the generated HTML tree under
   `site/_build/html/` was refreshed successfully;
4. if the build fails, identify the blocking warning or error and repair the
   repository-owned source that caused it;
5. if the build succeeds and tracked build outputs changed, include those
   generated artifacts in the task result only if they belong to the canonical
   repository-owned portal state already tracked in Git.

This task does not require a subagent. The scope is a direct local build plus
targeted repository fixes if the build exposes a canonical documentation
problem.

## Involved Components

- `site/conf.py`
- `site/`
- `site/_build/html/`
- `site/getting_started/local_build.rst`
- `doc/README.md`

## Implementation Steps

1. Keep this technical document as the approval gate for the regeneration task.
2. Run the canonical local Sphinx build command for the repository.
3. If the build fails, inspect the blocking warning or error and patch the
   repository source that prevents a warning-free build.
4. Re-run the build until the canonical Sphinx pipeline succeeds cleanly or a
   clear blocker remains.
5. Review the resulting changed files and summarize whether the generated HTML
   output was updated.
6. Run Markdown warning checks on the touched Markdown scope created or updated
   by this task.
7. Stop after the regeneration and verification pass, report the result, and
   wait for explicit approval before creating any Git commit.
