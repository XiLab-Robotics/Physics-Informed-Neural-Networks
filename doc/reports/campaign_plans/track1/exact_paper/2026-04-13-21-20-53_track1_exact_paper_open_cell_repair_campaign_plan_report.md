# Track 1 Exact-Paper Open-Cell Repair Campaign Plan Report

## Overview

This report prepares the next `Track 1` campaign under the canonical
paper-table replication objective.

The campaign is not a winner search across harmonic-wise configurations.
Its purpose is to close currently open cells in the exact-paper comparison for
Tables `3`, `4`, `5`, and `6`.

The campaign must answer one program-level question:

1. which currently open paper-table cells can be closed now by targeted
   exact-paper family-subset runs on the canonical exact-paper workflow.

## Current Canonical Status

The current exact-paper comparison shows:

- Table `3` amplitude RMSE still open at harmonics `0`, `1`, `3`, `81`, `240`;
- Table `4` phase MAE still open at harmonics `1`, `3`, `162`, `240`;
- Table `5` phase RMSE still open at harmonics `1`, `3`, `39`, `162`, `240`;
- Table `6` harmonic closure still open for every harmonic, with:
  - `0`, `1`, `240` not yet matched;
  - `3`, `39`, `40`, `78`, `81`, `156`, `162` partially matched.

The highest-priority repair queue remains:

- `0`
- `1`
- `3`
- `81`
- `162`
- `240`

## Campaign Principle

The exact-paper runner currently supports:

- family-subset selection;
- exact-paper dataset reuse;
- stable validation-summary serialization;
- ONNX export comparison against the recovered paper bank.

The runner does not yet support per-harmonic target filtering.
For that reason, this campaign is designed around family subsets whose paper
roles align with the still-open cells.

Campaign success must be read through:

1. exact-paper cell status changes in Tables `3-5`;
2. harmonic status changes in Table `6`;
3. family-direction alignment for the repaired harmonics.

The campaign should not be summarized primarily through a single winner model.

## Open-Cell Repair Targets

| Harmonic | Open Cells | Paper-Expected Family Direction |
| --- | --- | --- |
| `0` | Table `3` amplitude RMSE | `SVR` |
| `1` | Table `3` amplitude RMSE; Table `4` phase MAE; Table `5` phase RMSE | `RF` for amplitude, `LGBM` for phase |
| `3` | Table `3` amplitude RMSE; Table `4` phase MAE; Table `5` phase RMSE | `HGBM` |
| `39` | Table `5` phase RMSE | `HGBM` |
| `81` | Table `3` amplitude RMSE | `RF` |
| `162` | Table `4` phase MAE; Table `5` phase RMSE | `ERT` |
| `240` | Table `3` amplitude RMSE; Table `4` phase MAE; Table `5` phase RMSE | `ERT` |

## Candidate Run Matrix

| Config ID | Role | Planned Name | Enabled Families | Export Mode | Primary Repair Goal |
| --- | --- | --- | --- | --- | --- |
| 1 | Canonical refresh baseline | `exact_open_cell_refresh_full_bank` | `SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM` | `continue` | Refresh the exact-paper baseline under the new campaign framing and serialize a direct before/after comparison for all currently open cells. |
| 2 | Low-order repair subset | `exact_open_cell_low_order_repair` | `SVR, RF, GBM, HGBM, LGBM` | `strict` | Attack harmonics `0`, `1`, `3`, and `39`, where the paper-selected low-order families still define the open-cell direction. |
| 3 | High-order tree repair subset | `exact_open_cell_high_order_tree_repair` | `RF, ET, ERT` | `strict` | Attack harmonics `81`, `156`, `162`, and `240`, especially the remaining `ERT`-driven phase and amplitude gaps. |
| 4 | Paper-selected family reference | `exact_open_cell_paper_family_reference` | `SVR, RF, ERT, GBM, HGBM, LGBM` | `strict` | Evaluate only the families actually selected by the paper in Table `6` and measure whether the reduced paper-faithful family bank closes more exact-paper cells. |
| 5 | Phase-gap bridge subset | `exact_open_cell_phase_gap_bridge` | `RF, ERT, GBM, HGBM, LGBM` | `strict` | Re-check the remaining phase-side open cells at `1`, `3`, `39`, `162`, and `240` without the unrelated families. |
| 6 | Tree-control comparator | `exact_open_cell_tree_control_bank` | `RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM` | `strict` | Keep a non-`SVR`, tree-heavy control surface to verify whether `SVR` isolation is actually helping `k=0` or whether it should remain a dedicated single-family branch. |

## Why This Matrix Is Narrow Enough

This is not a combinatorial sweep.

The matrix stays narrow because:

- every run is tied to open cells already known in the canonical comparison;
- the family subsets are interpretable from the paper's own Table `6`
  selections;
- each run can be judged by repaired or still-open cells, not by vague winner
  movement.

## Parameter Notes

### Enabled Families

The primary campaign lever is `training.enabled_families`.

This is currently the only stable and already-implemented way to redirect the
exact-paper branch toward specific paper-table repair regions without changing
the runner code.

### Export Mode

The campaign uses:

- one `continue` refresh baseline so the full bank always serializes a fresh
  comparison artifact even if a family export regresses;
- five `strict` repair/reference runs so the paper-facing reference subsets are
  forced to stay operational.

### Dataset Split

The campaign should keep the exact-paper split unchanged:

- `test_size: 0.20`
- `random_seed: 0`
- `deterministic: true`

This is required so cell-level comparisons remain directly comparable with the
existing canonical exact-paper report.

## Evaluation Rules

Each completed run must be interpreted through:

1. Table `3` open-cell delta;
2. Table `4` open-cell delta;
3. Table `5` open-cell delta;
4. Table `6` harmonic-state delta;
5. family-direction alignment for each repaired harmonic.

The campaign summary should explicitly report:

- which cells changed from `above_paper_target` to `met_paper_target`;
- which harmonics moved from `not_yet_matched_tables_3_6` to
  `partially_matched_tables_3_6`;
- whether any harmonic became fully closed for the first time.

## Operator Deliverables

After approval, the preparation phase must generate:

1. a new exact-paper campaign config package;
2. a dedicated PowerShell launcher under `scripts/campaigns/`;
3. a matching launcher note under `doc/scripts/campaigns/`;
4. updated `doc/running/active_training_campaign.yaml`;
5. the exact terminal launch command.

## Execution Gate

Before this campaign is launched:

1. the technical document must be approved;
2. this planning report must be approved;
3. the config package must exist;
4. the launcher and launcher note must exist;
5. the active campaign state must be updated to the new prepared campaign.

## Next Step

After approval of this planning package, generate the exact-paper open-cell
repair campaign configs, launcher, launcher note, and prepared active-campaign
state.
