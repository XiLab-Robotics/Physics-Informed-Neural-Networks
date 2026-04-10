# Exact Paper Untracked Artifact Cleanup

## Overview

This document records the cleanup of leftover untracked artifacts produced while
stabilizing the exact-paper RCIM validation workflow.

After the normal commit of the exact-paper workflow, several untracked
validation roots remained under
`output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`.
Those roots correspond either to:

- crash-interrupted runs; or
- intermediate duplicate runs that were intentionally excluded from the commit
  once cleaner later runs became available.

They should not remain in the worktree because they add noise and blur the
canonical artifact surface.

## Technical Approach

The cleanup must remain narrow and explicit:

- remove only untracked exact-paper validation roots that are either incomplete
  or superseded by later committed runs;
- remove the one orphaned untracked validation-report Markdown file tied to a
  crash-era exact-paper run;
- keep all committed exact-paper artifact roots untouched;
- keep all other repository outputs untouched.

## Involved Components

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `doc/reports/analysis/validation_checks/`
- `doc/README.md`

## Implementation Steps

1. Identify untracked exact-paper validation roots remaining after the commit.
2. Confirm whether each root is incomplete or superseded by a later canonical
   run.
3. Remove only those untracked exact-paper directories and the orphaned report
   Markdown file.
4. Verify that `git status` is clean after cleanup.
