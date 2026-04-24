# Track 1 Remaining Yellow-Cell Campaign SVM Alias Fix

## Overview

The prepared `Track 1` remaining-yellow-cell overnight bundle failed at the
first `SVM` family config before any real training work started.

The remote exact-paper runner rejected:

- `training.enabled_families: [SVM]`

with:

- `AssertionError: Unsupported exact paper family names requested | SVM`

The failure happened inside
`scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
while resolving the enabled family list for the exact-paper model-bank runner.

## Technical Approach

Apply a narrow compatibility repair that keeps the paper-facing `SVM` wording
in documentation while restoring the canonical exact-runner family identity
`SVR`.

The repair has two parts:

1. update the exact-paper support resolver so configured family names are first
   normalized through the repository alias map, allowing `SVM` to resolve to
   `SVR` instead of failing validation;
2. rewrite the prepared `SVM` campaign YAML files so their
   `training.enabled_families` field uses the canonical runtime name `SVR`,
   reducing the chance of future failures if another caller bypasses alias
   normalization.

The campaign scope, target pairs, retry depth, launcher names, and user-facing
plan language remain unchanged.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/remaining_yellow_cells/svm/2026-04-22_track1_svm_remaining_yellow_cell_campaign/*.yaml`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Patch the exact-paper family resolver to canonicalize configured family
   aliases before unsupported-family validation.
2. Rewrite the prepared `SVM` family YAML bundle so the runner-facing value is
   `SVR`.
3. Confirm the `SVM` launcher still points to the same config directory and run
   names, with no campaign-identity drift.
4. Run YAML parsing, PowerShell parse checks, and Markdown QA on the touched
   documentation scope.
5. Report the relaunch command for the repaired overnight bundle.
