# Track 1 SVM Open-Cell Repair Campaign Preparation

## Overview

This technical document prepares the next `Track 1` campaign as a dedicated
`SVR` repair batch for the currently open `SVM` cells in the canonical paper
tables.

The objective is not to rerun the full `SVM` matrix blindly. The objective is
to attack the currently `yellow` and `red` cells in the canonical benchmark
with a broader but still targeted campaign that explores multiple repair
directions in parallel.

The campaign should prioritize the true blockers first:

- amplitude `RMSE` harmonic `156`;
- phase `MAE/RMSE` harmonic `240`;
- second-priority repair at `162`;
- broader pressure on the remaining near-closed `yellow` cells.

## Technical Approach

The exact-paper runner already supports:

- `target_scope.mode` with `amplitudes_only` or `phases_only`;
- `target_scope.harmonic_order_filter`;
- family restriction through `training.enabled_families`.

Therefore, the repair campaign can stay repository-compatible without requiring
new runner code. The campaign should use the existing exact-paper workflow and
prepare multiple explicit runs that differ by:

- target group: amplitudes or phases;
- harmonic subset;
- random seed;
- test split;
- export strictness when appropriate.

The campaign should be broad enough to test more than one route per open
region, but still remain interpretable. The recommended design is one umbrella
campaign with several `SVR` runs, grouped as:

- baseline rechecks for amplitudes and phases;
- blocker-focused repairs for `156` and `240`;
- bridge repairs for `162` and nearby harmonics;
- wider near-closure batches for the remaining `yellow` cells;
- split perturbations through controlled seed/test-split variation.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/campaign_plans/`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

## Implementation Steps

1. Create the campaign planning report that maps the current `SVM` open cells
   and defines the candidate repair run matrix.
2. After approval, generate a new exact-paper campaign package under
   `config/.../campaigns/` with explicit `SVR` repair YAML files.
3. Create the dedicated PowerShell launcher and matching launcher note.
4. Update `doc/running/active_training_campaign.yaml` with the prepared
   campaign state.
5. Provide the exact PowerShell launch command for the operator.
