# Track 1 Forward Maxi Last Non-Green Cells Campaign

## Overview

This technical document prepares the next exact-paper `Track 1` forward-only
repair wave after the completed `forward_last_non_green_cells` closeout.

The canonical forward paper-facing surface still has `9` non-green cells across
Tables `2-5`, all confined to amplitude replication:

- `Table 2 - Amplitude MAE Full-Matrix Replication`: `5` yellow, `2` red
- `Table 3 - Amplitude RMSE Full-Matrix Replication`: `1` yellow, `1` red
- `Table 4 - Phase MAE Full-Matrix Replication`: fully green
- `Table 5 - Phase RMSE Full-Matrix Replication`: fully green

These `9` cells collapse into `7` unique forward repair pairs:

- `ERT ampl 156`
- `ERT ampl 162`
- `ERT ampl 240`
- `GBM ampl 162`
- `XGBM ampl 240`
- `LGBM ampl 0`
- `LGBM ampl 162`

The user request is to prepare one materially larger retry wave with a few
hundred runs rather than another narrow residual sweep.

## Technical Approach

Prepare one forward-only original-dataset exact-model-bank maxi campaign that
remains target-level and inspectable, but raises retry depth substantially for
the last stubborn amplitude pairs.

The campaign should keep the previously validated remote exact-paper launcher
stack and should not reopen any already-green forward target. The queue should
follow three severity tiers:

- `yellow_single_surface`: `24` attempts per pair
- `yellow_multi_surface`: `36` attempts per pair
- `red_multi_surface`: `63` attempts per pair

Applied to the current residual inventory, the planned queue is:

- `3 x 24 = 72` runs for single-surface yellow pairs
- `2 x 36 = 72` runs for multi-surface yellow pairs
- `2 x 63 = 126` runs for red multi-surface pairs

Planned total queue size: `270` training runs.

The intended post-approval implementation remains the standard repository
workflow:

- generate one dedicated campaign config bundle under the Track 1 exact-paper
  original-dataset tree;
- generate one dedicated PowerShell launcher;
- generate one matching launcher note;
- update `doc/running/active_training_campaign.yaml` to the new prepared state;
- hand off the exact remote launch command.

Because `doc/running/active_training_campaign.yaml` is listed in the protected
campaign state, the implementation step must treat that update as an explicit
protected-file action.

No subagent use is planned for this task. If that changes later, explicit user
approval will be requested first.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `output/training_campaigns/track1/exact_paper/`
- `output/validation_checks/`

## Implementation Steps

1. Create the campaign planning report that freezes the `7` residual target
   pairs and the `270`-run tiered retry budget.
2. Wait for explicit user approval of this technical document before creating
   any implementation artifact.
3. After approval, generate the dedicated campaign YAML package for the new
   forward maxi wave.
4. Create the dedicated launcher and the matching launcher note.
5. Update `doc/running/active_training_campaign.yaml` to the new prepared
   campaign state.
6. Provide the exact remote launch command for the approved campaign package.
