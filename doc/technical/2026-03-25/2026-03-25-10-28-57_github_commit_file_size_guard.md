# GitHub Commit File Size Guard

## Overview

This document proposes a repository workflow update so that every GitHub commit preparation step includes an explicit file-size validation before any push-oriented commit flow proceeds.

The objective is to prevent accidental inclusion of files larger than GitHub's `100 MB` hard limit, stop the workflow before a non-pushable commit is finalized, and notify the user about the blocking files.

## Technical Approach

The repository operating rules will be extended with a mandatory pre-commit GitHub size check.

The updated workflow should require that:

- every GitHub commit preparation includes a scan of the files that are about to be committed;
- the scan checks for any file whose size exceeds `100 MB`;
- if at least one oversized file is detected, the commit workflow must stop immediately;
- the user must be explicitly warned that those files cannot be pushed to GitHub as regular repository objects;
- the warning should identify the blocking file or files clearly enough for corrective action.

This is a procedural rule update. It does not change model logic, training behavior, or runtime code paths.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/technical/2026-03-25/2026-03-25-10-28-57_github_commit_file_size_guard.md`

## Implementation Steps

1. Create this technical document under the day-based technical documentation folder.
2. Reference the new document from `README.md`.
3. After explicit user approval, update `AGENTS.md` to require a `100 MB` file-size guard before GitHub commit creation.
4. After explicit user approval, update `README.md` so the main repository rules reflect the same GitHub file-size guard.
5. Verify that the new rule text is consistent across the documentation.
6. Report completion and wait for explicit approval before creating any Git commit.
