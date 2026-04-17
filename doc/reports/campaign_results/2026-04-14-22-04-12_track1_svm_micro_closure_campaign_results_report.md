# Track 1 SVM Micro-Closure Campaign Results Report

## Overview

This report closes the dedicated `SVR` micro-closure campaign prepared in:

- `doc/reports/campaign_plans/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_plan_report.md`

The campaign executed `8` exact-paper validation runs through the dedicated
launcher:

- completed runs: `8`
- failed runs: `0`
- execution window: `2026-04-14 21:44:13+02:00` to `2026-04-14 21:52:37+02:00`
- campaign artifact root:
  `output/training_campaigns/track1_svm_micro_closure_campaign_2026_04_14_21_42_47/`

The campaign goal was minimal and explicit:

- test only the last residual `SVM` harmonics `40`, `240`, and `162`;
- avoid reopening any already closed `SVM` surfaces;
- check whether one final narrow pass could finish the row.

## Objective And Outcome

The campaign had three concrete goals:

1. close amplitude `40`;
2. close amplitude `240` on `RMSE`;
3. close phase `162` on both `MAE` and `RMSE`.

Outcome:

- all `8` runs completed successfully;
- all `8` runs exported ONNX artifacts with `0` failed exports;
- no campaign run materially improved the canonical `SVM` row beyond the
  current benchmark values;
- the campaign confirmed that the current `SVM` row is stable, but still not
  fully closed.

This means the campaign succeeded operationally, but scientifically it acted as
a confirmation pass rather than a closure pass.

## Ranking Policy

This campaign is not a full-matrix family comparison. Each run only covers one
scoped residual slice of the `SVM` row.

The serialized campaign policy is therefore:

- primary metric: `cell_closure_score_desc`
- first tie breaker: `met_paper_cell_count_desc`
- second tie breaker: `open_paper_cell_count_asc`
- third tie breaker: `mean_normalized_gap_ratio_asc`
- fourth tie breaker: `max_normalized_gap_ratio_asc`
- fifth tie breaker: `improved_cell_count_desc`
- sixth tie breaker: `status_upgrade_score_desc`
- seventh tie breaker: `run_name`

Where:

- `cell_closure_score = (met + 0.5 * near) / paper_cell_count`
- `met` means the scoped repository cell reached or beat the paper cell
- `near` means the positive gap stayed within `25%` of the paper cell
- `status_upgrade_score` rewards `red -> yellow`, `yellow -> green`, and
  `red -> green` transitions versus the pre-micro-closure `SVM` baseline row

Interpretation:

- this policy exists only to serialize the required campaign-best artifacts;
- the real scientific interpretation remains the merged `SVM` row across
  Tables `2-5`.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Run | Scope | Cells | Met | Near | Open | Closure Score | Improved | Upgrades |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_svm_amplitude_240_only` | `amplitudes_only` | `2` | `1` | `1` | `0` | `0.750` | `0` | `0` |
| `2` | `track1_svm_amplitude_micro_closure_seed23` | `amplitudes_only` | `4` | `1` | `3` | `0` | `0.625` | `0` | `0` |
| `3` | `track1_svm_phase_micro_closure_split15` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `4` | `track1_svm_amplitude_40_only` | `amplitudes_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `5` | `track1_svm_amplitude_micro_closure_baseline` | `amplitudes_only` | `4` | `0` | `4` | `0` | `0.500` | `1` | `0` |
| `6` | `track1_svm_phase_micro_closure_baseline` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `7` | `track1_svm_phase_micro_closure_seed23` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `8` | `track1_svm_amplitude_micro_closure_split15` | `amplitudes_only` | `4` | `0` | `3` | `1` | `0.375` | `1` | `0` |

### Export Surface

| Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports |
| ---: | ---: | ---: | ---: |
| `8` | `11` | `0` | `4` |

## Campaign Best Run

The explicit bookkeeping winner is:

- `track1_svm_amplitude_240_only`

It was selected because it achieved:

- the highest scoped cell-closure score: `0.750`
- `1` met cell and `1` near cell out of `2`
- the cleanest targeted result on the residual amplitude `240` slice

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** a new scientific row winner by itself;
- the canonical `SVM` row does not change as a result of this campaign.

## SVM Row Impact

### Table-Level Before Vs After

| Surface | Before | After |
| --- | --- | --- |
| Table `2` amplitude `MAE` | `9` green, `1` yellow, `0` red | `9` green, `1` yellow, `0` red |
| Table `3` amplitude `RMSE` | `8` green, `2` yellow, `0` red | `8` green, `2` yellow, `0` red |
| Table `4` phase `MAE` | `8` green, `1` yellow, `0` red | `8` green, `1` yellow, `0` red |
| Table `5` phase `RMSE` | `8` green, `1` yellow, `0` red | `8` green, `1` yellow, `0` red |

### Residual SVM Yellow Cells

- Table `2`: `40`
- Table `3`: `40`, `240`
- Table `4`: `162`
- Table `5`: `162`

There are still no remaining red `SVM` cells in Tables `2-5`.

## Canonical Benchmark Impact

This campaign did not change the canonical benchmark totals.

The canonical benchmark therefore remains:

- Table `2` full-matrix totals: `54 / 36 / 10`
- Table `3` full-matrix totals: `53 / 34 / 13`
- Table `4` full-matrix totals: `52 / 37 / 1`
- Table `5` full-matrix totals: `43 / 41 / 6`

The harmonic-level Table `6` reading also remains unchanged.

## Main Conclusions

The campaign supports four conclusions.

### 1. SVM Is At A Real Plateau

The micro-pass reproduced the current residual `SVM` quality but did not
produce a further canonical upgrade.

### 2. The Remaining Gaps Are Very Small But Persistent

The residual cells `40`, `240`, and `162` stay in the yellow band, which means
they are close but not yet fully closed.

### 3. Another Generic SVM Sweep Is Unlikely To Be Efficient

This campaign was already very narrow and still produced no canonical upgrade.

That is a practical sign that `SVM` is no longer the best place for another
generic budget pass.

### 4. The Next SVM Work Should Be Either Surgical Or Stopped

The rational options are now:

- one last highly surgical hand-designed `SVM` attempt on a single residual
  surface; or
- stop spending the main `Track 1` budget on `SVM` and move to another row.

## Produced Campaign Artifacts

The campaign output folder now contains the required serialized winner
artifacts:

- `output/training_campaigns/track1_svm_micro_closure_campaign_2026_04_14_21_42_47/campaign_leaderboard.yaml`
- `output/training_campaigns/track1_svm_micro_closure_campaign_2026_04_14_21_42_47/campaign_best_run.yaml`
- `output/training_campaigns/track1_svm_micro_closure_campaign_2026_04_14_21_42_47/campaign_best_run.md`

The canonical reports updated by this closure are:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
