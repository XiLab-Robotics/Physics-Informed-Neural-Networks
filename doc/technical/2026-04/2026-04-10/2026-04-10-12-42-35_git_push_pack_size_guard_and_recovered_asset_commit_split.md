# Git Push Pack Size Guard And Recovered Asset Commit Split

## Overview

The latest local commit `68c2ec6` cannot be pushed to GitHub because the
generated remote pack exceeds the server-side `2.00 GiB` limit. The failure is
not caused by one file larger than `100 MB`, but by the aggregate size of the
newly introduced recovered RCIM asset set, dominated by the
`reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`
subtree.

This task has two required outcomes:

1. formalize a repository rule that GitHub-bound commits must be checked not
   only for per-file size violations but also for aggregate push/pack size
   risk; and
2. repair the current local history by replacing the oversized commit with a
   smaller sequence that can be pushed successfully.

No subagent is planned for this task. Runtime subagent launch is not expected
and would still require explicit user approval if conditions change.

## Technical Approach

The implementation will proceed in two coordinated parts.

First, the repository rules in `AGENTS.md` will be tightened so the Git
pre-commit workflow explicitly includes an aggregate push-size guard for
GitHub-bound commits. The rule should go beyond the existing `100 MB`
single-file check and require a pre-commit assessment of the total staged data
intended for the next push. The rule should also state that if the staged delta
is large enough to risk the GitHub remote pack ceiling, the work must be split
before commit creation instead of relying on a failed push attempt as the
detection mechanism.

Second, the current local branch will be repaired by removing the oversized
commit from `HEAD` while preserving the file changes in the working tree. The
recovered RCIM asset integration will then be re-committed in smaller logical
batches:

1. one commit for all current changes except
   `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`;
2. three additional commits that add the `instance_archives/` subtree in
   separate batches sized conservatively below the remote pack threshold.

Before each replacement commit is created, the staged scope should be measured
so the split is validated by size rather than guessed from file counts alone.

## Involved Components

- `AGENTS.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-10/2026-04-10-12-42-35_git_push_pack_size_guard_and_recovered_asset_commit_split.md`
- local Git history on `main`
- `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`

## Implementation Steps

1. Update `AGENTS.md` so GitHub-bound commits require both:
   - the existing single-file size guard; and
   - a new aggregate staged/push-size check that blocks oversized commits from
     being created.
2. Preserve this task plan in `doc/README.md` as a new technical-document
   entry.
3. After user approval, run a non-destructive history repair with
   `git reset --soft HEAD~1`.
4. Restage and recreate the recovered-asset integration as one commit excluding
   `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`.
5. Split the `instance_archives/` subtree into three measured staging batches
   and create three additional commits.
6. Verify each resulting commit scope before any push attempt so the branch can
   be pushed incrementally without crossing the GitHub remote pack limit.
