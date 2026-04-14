# Track 1 Exact-Paper Open-Cell Repair Campaign Results Report

## Overview

This report closes the exact-paper open-cell repair campaign prepared in:

- `doc/reports/campaign_plans/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md`

The campaign executed `6` exact-paper validation runs through the dedicated
launcher:

- completed runs: `6`
- failed runs: `0`
- execution window: `2026-04-13 22:07:17+02:00` to `2026-04-13 22:09:59+02:00`
- campaign artifact root:
  `output/training_campaigns/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/`

This campaign was designed under the new `Track 1` paradigm:

- the primary objective is exact-paper table closure across Tables `3-6`;
- the campaign winner remains a required bookkeeping artifact;
- however, the winner does not define campaign success by itself.

## Objective And Outcome

The campaign had three concrete goals:

1. refresh the exact-paper baseline under the new cell-closure-first framing;
2. test whether paper-aligned family subsets can close any currently open
   cells in Tables `3-5`;
3. reduce the number of harmonics still marked
   `not_yet_matched_tables_3_6`.

Outcome:

- all `6` runs completed successfully;
- all `6` runs exported ONNX artifacts with `0` failed targets;
- no run closed any new numeric paper-target cell in Tables `3-5`;
- the best campaign runs reduced Table `6` open harmonics from `3` to `2`;
- specifically, harmonic `240` moved from
  `not_yet_matched_tables_3_6` to `partially_matched_tables_3_6`;
- no harmonic became fully closed.

The campaign therefore improved harmonic-family alignment slightly, but it did
not close the real numeric gaps that still keep `Track 1` open.

## Ranking Policy

This campaign cannot be ranked primarily by winner `MAPE`, because all runs
produced the same winning-family aggregate metric. The explicit serialized
campaign policy is therefore:

- primary metric: `harmonic_closed_count_desc`
- first tie breaker: `harmonic_open_count_asc`
- second tie breaker: `met_paper_cell_count_desc`
- third tie breaker: `matched_table6_family_target_count_desc`
- fourth tie breaker: `regression_count_asc`
- fifth tie breaker: `enabled_family_count_desc`
- sixth tie breaker: `run_name`

Interpretation:

- this policy exists only to serialize the required campaign-best artifacts;
- the real `Track 1` interpretation remains the cell-closure matrix below.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Config | Family Scope | Harmonics Open | Harmonics Partial | Met Cells | Regressions |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `1` | `exact_open_cell_paper_family_reference` | `6` paper-selected families | `2` | `8` | `14` | `0` |
| `2` | `exact_open_cell_phase_gap_bridge` | `5` phase-bridge families | `2` | `8` | `14` | `0` |
| `3` | `exact_open_cell_refresh_full_bank` | all `10` families | `3` | `7` | `14` | `0` |
| `4` | `exact_open_cell_tree_control_bank` | `8` tree-heavy families | `3` | `7` | `14` | `0` |
| `5` | `exact_open_cell_low_order_repair` | `5` low-order families | `3` | `7` | `11` | `3` |
| `6` | `exact_open_cell_high_order_tree_repair` | `3` tree families | `4` | `6` | `11` | `3` |

| Config | Winner | Mean Component MAPE [%] | Export Mode | Exported | Failed |
| --- | --- | ---: | --- | ---: | ---: |
| `exact_open_cell_paper_family_reference` | `RF` | `18.369` | `strict` | `120` | `0` |
| `exact_open_cell_phase_gap_bridge` | `RF` | `18.369` | `strict` | `100` | `0` |
| `exact_open_cell_refresh_full_bank` | `RF` | `18.369` | `continue` | `200` | `0` |
| `exact_open_cell_tree_control_bank` | `RF` | `18.369` | `strict` | `160` | `0` |
| `exact_open_cell_low_order_repair` | `RF` | `18.369` | `strict` | `100` | `0` |
| `exact_open_cell_high_order_tree_repair` | `RF` | `18.369` | `strict` | `60` | `0` |

## Campaign Best Run

The explicit bookkeeping winner is:

- `exact_open_cell_paper_family_reference`

It was selected because it achieved:

- the minimum harmonic-open count in the campaign: `2`
- the maximum harmonic-partial count in the campaign: `8`
- zero numeric regressions versus the canonical baseline
- the broadest paper-aligned family coverage among the tied top runs

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** evidence that `Track 1` is solved;
- it is only the cleanest top-ranked run under the paper-closure-first
  ranking policy.

## Cell-Closure Impact

### Tables `3-5`

There was no numeric closure progress in the campaign.

The still-open numeric cells after the best run remain:

| Table | Harmonics Still Open |
| --- | --- |
| Table `3` amplitude RMSE | `0`, `1`, `3`, `81`, `240` |
| Table `4` phase MAE | `1`, `3`, `162`, `240` |
| Table `5` phase RMSE | `1`, `3`, `39`, `162`, `240` |

### Table `6`

The campaign did produce one harmonic-status improvement:

- harmonic `240` moved from `not_yet_matched_tables_3_6` to
  `partially_matched_tables_3_6`

Best achieved harmonic status after the campaign:

- fully closed harmonics: `0`
- partially matched harmonics: `8`
- still-open harmonics: `2` -> `0`, `1`

## Open Numeric Gaps After The Best Run

| Cell | Paper Family | Repository Family | Gap To Paper |
| --- | --- | --- | ---: |
| Table `3` `A_0` RMSE | `SVM` | `HGBM` | `0.000399` |
| Table `3` `A_1` RMSE | `RF` | `HGBM` | `1.76e-07` |
| Table `4` `phi_1` MAE | `LGBM` | `HGBM` | `4.64e-05` |
| Table `5` `phi_1` RMSE | `HGBM` | `GBM` | `1.01e-05` |
| Table `3` `A_3` RMSE | `HGBM` | `HGBM` | `7.42e-07` |
| Table `4` `phi_3` MAE | `HGBM` | `GBM` | `0.003757` |
| Table `5` `phi_3` RMSE | `HGBM` | `HGBM` | `0.005302` |
| Table `5` `phi_39` RMSE | `HGBM` | `HGBM` | `0.005648` |
| Table `3` `A_81` RMSE | `RF` | `RF` | `3.22e-06` |
| Table `4` `phi_162` MAE | `DT` | `ERT` | `0.012507` |
| Table `5` `phi_162` RMSE | `ERT` | `ERT` | `0.078591` |
| Table `3` `A_240` RMSE | `ERT` | `RF` | `1.27e-05` |
| Table `4` `phi_240` MAE | `DT` | `ERT` | `0.039941` |
| Table `5` `phi_240` RMSE | `ERT` | `ERT` | `0.177287` |

The practical reading is blunt:

- low-order gaps at `1` and `3` are now numerically tiny on amplitude, but they
  are still not closed;
- harmonic `0` remains structurally wrong on amplitude because the repository
  best family is still `HGBM` instead of the paper `SVM` branch;
- the major blockers remain phase-side gaps at `3`, `162`, and `240`;
- `240` improved only on harmonic-family alignment, not on numeric closure.

## Interpretation By Run Family

### 1. The Refresh Run Confirmed The Baseline

`exact_open_cell_refresh_full_bank` reproduced the current exact-paper
baseline exactly:

- `5` Table `3` cells met
- `5` Table `4` cells met
- `4` Table `5` cells met
- `0` fully closed harmonics
- `7` partial harmonics
- `3` open harmonics

This means the campaign did not expose hidden regressions in the canonical
full-bank branch.

### 2. The Two Best Runs Improved Only Harmonic Partiality

`exact_open_cell_paper_family_reference` and
`exact_open_cell_phase_gap_bridge` both improved Table `6` status by making
harmonic `240` partial instead of fully open.

But neither run:

- closed a new numeric cell;
- reduced any open numeric gap below paper target;
- produced a first fully closed harmonic.

### 3. Two Repair Subsets Regressed Existing Good Cells

`exact_open_cell_low_order_repair` and
`exact_open_cell_high_order_tree_repair` each regressed `3` previously met
cells versus the canonical baseline.

This matters because it shows that family narrowing by itself is not enough.
The exact-paper branch is sensitive to subset composition, and some supposedly
targeted subsets destroy already-good cells without repairing the intended open
ones.

### 4. Export Stability Is No Longer The Limiting Factor

All `6` runs completed with:

- `0` failed ONNX exports
- `0` matched reference relative paths
- no surrogate-export requirement in this campaign

So the branch is operationally stable. The blocker is no longer exportability.
The blocker is now real paper-target closure.

## Main Conclusions

The campaign supports five conclusions.

### 1. The New Track 1 Framing Worked

The campaign was readable in the correct format:

- which cells stayed open;
- which harmonics stayed open or partial;
- which subsets regressed the baseline.

This is materially better than a winner-only campaign story.

### 2. The Campaign Did Not Solve Any Numeric Paper Gap

No Table `3-5` cell changed from `above_paper_target` to `met_paper_target`.

So, in the strict sense that matters for `Track 1`, the campaign did not close
any table cell.

### 3. Harmonic `240` Improved Only One Level

The best runs moved `240` from fully open to partial. That is real progress,
but still insufficient because all three numeric cells at `240` remain above
target.

### 4. The Main Blockers Are Still Structural

The unresolved branch is now clear:

- `A_0` still wants the `SVM`-side paper behavior;
- `1` and `3` are very close numerically but still open;
- `162` and `240` remain the major phase-side blockers.

### 5. Future Work Must Be More Surgical Than Family Subsets Alone

This campaign shows that family-subset selection alone is too blunt.
If the next iteration is meant to close real cells, it likely needs a more
target-aware exact-paper workflow than the current family-only runner surface.

## Recommended Next Actions

The next technically justified steps are:

1. keep `exact_open_cell_paper_family_reference` as the bookkeeping winner for
   this campaign only;
2. keep the canonical `Track 1` reading anchored to the still-open numeric
   cells listed above;
3. prioritize a next exact-paper iteration that can act more surgically on:
   `A_0`, `phi_3`, `phi_162`, and the full `240` triplet;
4. treat `1` and `3` amplitude as near-threshold cells that may benefit from a
   target-aware refinement instead of another coarse family subset;
5. avoid reusing the low-order-only and high-order-tree-only subsets as-is,
   because both regressed already-good cells.

## Artifact References

- Campaign root:
  `output/training_campaigns/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/`
- Campaign leaderboard:
  `output/training_campaigns/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/campaign_leaderboard.yaml`
- Campaign best run YAML:
  `output/training_campaigns/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/campaign_best_run.yaml`
- Campaign best run note:
  `output/training_campaigns/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/campaign_best_run.md`
- Winning validation summary:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run/validation_summary.yaml`
- Winning model bundle:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run/paper_family_model_bank.pkl`
- Per-run launcher logs:
  `output/training_campaigns/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/logs/`
