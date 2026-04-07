# GitHub Quality Workflow Naming And Markdownlint Memory Fix

## Overview

The new repository-quality workflow is currently named too generically as `CI`,
and its `markdownlint` step fails on GitHub-hosted runners with a JavaScript
heap-out-of-memory error when linting the full Markdown scope in one invocation.

This task fixes both issues:

- rename the workflow to a clearer repository-facing name;
- change the Markdownlint execution strategy to a chunked run pattern that the
  repository already documents for large Markdown scopes.

## Technical Approach

The fix will remain repository-owned inside `.github/workflows/ci.yml`.

The workflow rename should make the required status check easier to understand
inside GitHub branch rules. A clearer name such as `Repository Quality Checks`
is better than the generic `CI` label in this repository context.

The Markdownlint failure will be fixed by using a chunked file list instead of a
single huge invocation over `README.md`, `AGENTS.md`, `doc`, and `site`. This
matches the already documented repository practice for large Markdown linting
scopes and avoids the Node.js heap blow-up shown by the failed GitHub run.

## Involved Components

- `.github/workflows/ci.yml`
- `doc/README.md`

## Implementation Steps

1. Rename the workflow to a clearer GitHub-facing name.
2. Replace the single-shot `markdownlint` call with a chunked invocation over
   the repository-owned Markdown set relevant to the workflow.
3. Keep the rest of the quality workflow unchanged.
4. Run repository checks needed to confirm the YAML remains valid and the
   touched Markdown scope stays warning-free.
