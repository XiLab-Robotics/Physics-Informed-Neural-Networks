# Track 1 SVR Reference Grid Search Repair Campaign Preparation

## Overview

This document prepares the next `Track 1` `SVR` repair campaign after the
exact-paper workflow was aligned with the recovered paper-reference
`GridSearchCV` path.

The goal is no longer to probe repository-invented `random_seed` and
`test_size` variations. The goal is to re-run the still-open `SVR` cells under
the recovered paper-faithful training rule so the remaining `SVM` gaps are
tested with the same tuning paradigm used by the reference code.

The current residual `SVR` yellow cells are:

- `Table 2` amplitude `A_k` `MAE`: harmonic `40`
- `Table 3` amplitude `A_k` `RMSE`: harmonics `40`, `240`
- `Table 4` phase `phi_k` `MAE`: harmonic `162`
- `Table 5` phase `phi_k` `RMSE`: harmonic `162`

## Technical Approach

The campaign will stay deterministic and paper-faithful.

The key rule is:

- keep the exact-paper split settings unchanged;
- keep the exact recovered input schema unchanged;
- keep the exact recovered `SVR` base estimator unchanged;
- use the repository exact-paper `paper_reference_grid_search` mode;
- vary only the target scope so the paper-faithful grid search can optimize
  the relevant target subset rather than a larger family surface.

The campaign should therefore use narrow scope decomposition:

- one amplitude repair run on `40` and `240` together;
- one amplitude repair run on `40` only;
- one amplitude repair run on `240` only;
- one phase repair run on `162` only.

This is intentionally much narrower than the earlier seed/split campaigns.
Because `GridSearchCV` is now deterministic under the fixed split, repeating the
same scope multiple times would not add information.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
  Exact-paper support logic now responsible for the paper-reference
  `GridSearchCV` path.
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
  Exact-paper validation runner that serializes the chosen search strategy.
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
  Canonical exact-paper configuration surface now exposing
  `training.hyperparameter_search.mode`.
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
  Canonical benchmark that will absorb any `SVR` upgrades produced by the new
  paper-faithful repair run.

## Implementation Steps

1. Create a campaign planning report that explains the deterministic
   `GridSearchCV`-based repair strategy and the candidate run table.
2. Prepare one campaign package with four `SVR`-only runs using the exact-paper
   `paper_reference_grid_search` mode.
3. Add the aligned PowerShell launcher and launcher note.
4. Register the prepared campaign in `doc/running/active_training_campaign.yaml`
   only after the user approves the campaign package.
5. After execution, compare the resulting exact-paper `SVR` row against the
   current canonical `Track 1` benchmark and close the campaign through the
   normal campaign-results workflow.
