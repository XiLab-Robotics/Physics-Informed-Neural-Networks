# Track 1 Forward Last Non-Green Cells Campaign

## Overview

This document prepares the next exact-paper `Track 1` forward-only repair wave
after the completed `forward_final_open_cells` closeout.

The canonical benchmark now shows only `10` forward non-green cells, all
concentrated on the amplitude surfaces:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`

No forward `phase` cells remain open in:

- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The residual forward inventory collapses to `7` unique amplitude target pairs:

- `ERT ampl 156`
- `ERT ampl 162`
- `ERT ampl 240`
- `GBM ampl 162`
- `XGBM ampl 240`
- `LGBM ampl 0`
- `LGBM ampl 162`

## Technical Approach

Prepare one narrow remote exact-paper campaign that attacks only the `7`
remaining forward amplitude target pairs still carrying yellow or red benchmark
status.

The queue should stay inspectable and priority-driven:

- one shared high base retry budget across all `7` residual pairs;
- one stronger extra escalation budget only for the still-red pairs on `h162`;
- no `phase` retry surface;
- no full-family re-run for already-green targets.

The intended retry budget is deliberately more aggressive than the previous
residual wave:

- `12` base attempts for every residual pair;
- `8` extra attempts for each still-red `h162` pair;
- total planned queue target: `108` runs.

The intended post-approval implementation remains the standard repository
workflow:

- campaign config bundle under the Track 1 exact-paper original-dataset tree;
- one dedicated PowerShell launcher;
- one matching launcher note;
- one prepared update to `doc/running/active_training_campaign.yaml`.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`

## Implementation Steps

1. Materialize the planning report for the residual forward amplitude wave and
   freeze the exact residual pair inventory.
1. After approval, generate the dedicated campaign config directory with one
   queue entry per retry attempt.
1. Create the launcher and launcher note for the new remote campaign.
1. Update `doc/running/active_training_campaign.yaml` to the new prepared wave.
1. Hand off the exact remote launch command.
