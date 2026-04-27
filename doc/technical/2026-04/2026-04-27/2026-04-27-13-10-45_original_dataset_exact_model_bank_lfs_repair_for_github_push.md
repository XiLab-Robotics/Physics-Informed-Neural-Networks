# Original-Dataset Exact-Model-Bank LFS Repair For GitHub Push

## Overview

The current GitHub push is blocked because one exact-model-bank validation
artifact was committed as a normal Git blob instead of a Git LFS pointer:

- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-56-26__track1_original_dataset_backward_ert_attempt_08_campaign_validation/paper_family_model_bank.pkl`

GitHub reports this file as `139.63 MB`, which exceeds the `100 MB` hard file
limit.

The offending blob entered local history in commit:

- `ddb9828a` `Archive Track 1 original-dataset mega raw artifacts`

## Technical Approach

The repair must update both repository policy and the unpushed local history.

The planned fix is:

1. add a narrow `.gitattributes` rule that routes the original-dataset
   exact-model-bank `paper_family_model_bank.pkl` bundles through Git LFS;
2. verify the specific failing path resolves to `filter=lfs`;
3. rewrite the unpushed local commit range so the oversized blob is replaced by
   an LFS pointer;
4. preserve the logical split of the existing local commits as much as
   practical;
5. re-check file-size and push readiness before the next GitHub push attempt.

Because the offending blob is already inside local commits, this is a local
history repair, not just a working-tree file edit.

## Involved Components

- `.gitattributes`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/**/paper_family_model_bank.pkl`
- local commits:
  - `ddb9828a`
  - `7d9c5e49`
  - `e7ea2670`
- current uncommitted forward open-cell repair campaign preparation work

## Implementation Steps

1. Add the narrow Git LFS tracking rule for the original-dataset validation
   `paper_family_model_bank.pkl` bundles.
2. Confirm `git check-attr filter -- <path>` returns `lfs` for the failing
   file.
3. Rebuild the local unpushed commit range so the large bundle is recommitted
   as an LFS pointer instead of a normal Git blob.
4. Re-run commit-size checks on the repaired history.
5. Report the corrected push-ready commit state.
