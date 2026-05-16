# 2026-05-16-20-04-43 Git Lfs Exact Model Bank Threshold Cleanup

## Overview

This technical document plans the cleanup of Git LFS tracking for the exact
paper model-bank validation artifacts under
`output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/`.
The current `.gitattributes` rule tracks every nested
`paper_family_model_bank.pkl` through Git LFS, including many files that are
well below the repository's practical `100 MB` threshold.

The requested target state is that `.gitattributes` lists only the exact
`paper_family_model_bank.pkl` paths that actually need LFS because their local
file size is greater than `100,000,000` bytes.

## Technical Approach

Use the live repository artifact sizes as the source of truth. The inspection
found `433` matching `paper_family_model_bank.pkl` files. Of those, `2` are
greater than `100,000,000` bytes and therefore should remain LFS-tracked under
the requested threshold:

- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-00-03__track1_original_dataset_forward_rf_attempt_18_campaign_validation/paper_family_model_bank.pkl`
  at `100,703,408` bytes.
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-56-26__track1_original_dataset_backward_ert_attempt_08_campaign_validation/paper_family_model_bank.pkl`
  at `146,414,849` bytes.

The broad wildcard rule in `.gitattributes` will be replaced by those exact
paths. The cleanup intentionally does not rewrite history. It prevents future
small `paper_family_model_bank.pkl` artifacts from being added as new LFS
objects, while already-pushed historical LFS objects remain part of repository
history unless a separate history-rewrite operation is explicitly planned.

For the second workstation, the failed `git pull --rebase` was blocked first by
Git LFS smudge after the repository exceeded its LFS budget, then by unstaged
local generated campaign changes. The recovery path should avoid LFS smudging
during the pull and preserve local generated work before rebasing.

No Codex subagent is planned for this implementation.

## Involved Components

- `.gitattributes`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/**/paper_family_model_bank.pkl`
- Git LFS smudge behavior during `git pull --rebase`
- The second workstation's uncommitted Wave 1 campaign output state

## Implementation Steps

1. Replace the broad exact-model-bank LFS wildcard in `.gitattributes` with the
   two exact paths above.
2. Verify attributes with `git check-attr filter -- <path>` for one retained
   large file and one small file that should no longer be LFS-tracked.
3. Run Markdown checks for this technical document and `doc/README.md`.
4. Provide the second-workstation recovery commands:
   preserve local generated work with a stash or WIP commit, disable LFS smudge
   for the pull, run `git pull --rebase`, then reapply the local work.
5. Stop before creating any commit and wait for explicit approval.
