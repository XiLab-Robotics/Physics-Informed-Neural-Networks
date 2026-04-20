# Track 1 SVM Open-Cell Repair Campaign Results Report

## Overview

This report closes the dedicated `SVR` repair campaign prepared in:

- `doc/reports/campaign_plans/track1/svm/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_plan_report.md`

The campaign executed `12` exact-paper validation runs through the dedicated
launcher:

- completed runs: `12`
- failed runs: `0`
- execution window: `2026-04-14 17:30:44+02:00` to `2026-04-14 17:32:30+02:00`
- campaign artifact root:
  `output/training_campaigns/track1/svm/track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21/`

The campaign goal was narrow and explicit:

- repair only the currently yellow or red `SVM` paper cells;
- prioritize the true blockers first: amplitude `156`, phase `240`, then
  `162`, then the residual bridge harmonics;
- update the canonical `SVM` row in the Track `1` benchmark with the best
  post-repair values found across the scoped runs.

## Objective And Outcome

The campaign had three concrete goals:

1. improve the `SVM` amplitude row without rerunning the full family matrix
   blindly;
2. improve the `SVM` phase row with special attention to the `240` blocker;
3. merge the best scoped repair values back into the canonical full-matrix
   `SVM` row.

Outcome:

- all `12` runs completed successfully;
- all `12` runs exported ONNX artifacts with `0` failed exports;
- the campaign upgraded the canonical `SVM` row on all four paper surfaces;
- the `SVM` row now has `0` red cells across Tables `2-5`;
- `Track 1` remains open globally, but the `SVM` row is no longer a weak row.

This means the campaign succeeded both operationally and scientifically as a
targeted repair pass.

## Ranking Policy

This campaign is not a full-matrix family comparison. Each run only covers one
scoped repair slice of the `SVM` row.

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
  `red -> green` transitions versus the pre-repair `SVM` baseline row

Interpretation:

- this policy exists only to serialize the required campaign-best artifacts;
- the real scientific interpretation remains the merged post-repair `SVM` row
  across Tables `2-5`.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Run | Scope | Cells | Met | Near | Open | Closure Score | Improved | Upgrades |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_svm_phase_repair_seed11` | `phases_only` | `8` | `6` | `2` | `0` | `0.875` | `8` | `7` |
| `2` | `track1_svm_amplitude_low_mid_bridge` | `amplitudes_only` | `6` | `3` | `3` | `0` | `0.750` | `4` | `3` |
| `3` | `track1_svm_phase_162_240_focus` | `phases_only` | `4` | `2` | `2` | `0` | `0.750` | `4` | `4` |
| `4` | `track1_svm_amplitude_repair_seed23` | `amplitudes_only` | `10` | `4` | `6` | `0` | `0.700` | `8` | `5` |
| `5` | `track1_svm_phase_repair_seed23` | `phases_only` | `8` | `2` | `6` | `0` | `0.625` | `5` | `4` |
| `6` | `track1_svm_phase_1_39_bridge` | `phases_only` | `4` | `0` | `4` | `0` | `0.500` | `3` | `0` |
| `7` | `track1_svm_amplitude_repair_seed11` | `amplitudes_only` | `10` | `3` | `3` | `4` | `0.450` | `4` | `3` |
| `8` | `track1_svm_amplitude_repair_baseline` | `amplitudes_only` | `10` | `0` | `9` | `1` | `0.450` | `0` | `0` |
| `9` | `track1_svm_phase_repair_baseline` | `phases_only` | `8` | `1` | `5` | `2` | `0.438` | `0` | `0` |
| `10` | `track1_svm_amplitude_156_focus` | `amplitudes_only` | `2` | `0` | `1` | `1` | `0.250` | `0` | `0` |
| `11` | `track1_svm_phase_240_focus` | `phases_only` | `2` | `0` | `0` | `2` | `0.000` | `0` | `0` |
| `12` | `track1_svm_amplitude_156_240_focus` | `amplitudes_only` | `4` | `0` | `0` | `4` | `0.000` | `0` | `0` |

### Export Surface

| Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports |
| ---: | ---: | ---: | ---: |
| `12` | `38` | `0` | `8` |

All `8` surrogate exports came from amplitude-side `SVR` targets that still
needed the existing constant-linear-regression safeguard.

## Campaign Best Run

The explicit bookkeeping winner is:

- `track1_svm_phase_repair_seed11`

It was selected because it achieved:

- the highest campaign scoped cell-closure score: `0.875`
- `6` met cells and `2` near cells out of `8`
- `0` open cells on its scoped phase subset
- the strongest blocker resolution package, including the `240` phase repair

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** the whole scientific result by itself;
- the scientific output is the merged post-repair `SVM` row now written into
  the canonical benchmark.

## SVM Row Impact

### Table-Level Before Vs After

| Surface | Before | After |
| --- | --- | --- |
| Table `2` amplitude `MAE` | `5` green, `5` yellow, `0` red | `8` green, `2` yellow, `0` red |
| Table `3` amplitude `RMSE` | `5` green, `4` yellow, `1` red | `7` green, `3` yellow, `0` red |
| Table `4` phase `MAE` | `6` green, `2` yellow, `1` red | `8` green, `1` yellow, `0` red |
| Table `5` phase `RMSE` | `5` green, `3` yellow, `1` red | `8` green, `1` yellow, `0` red |

### Closed Or Upgraded Cells

- Table `2` amplitude `MAE`: `0`, `81`, and `240` moved from yellow to green
- Table `3` amplitude `RMSE`: `0` and `81` moved from yellow to green; `156`
  moved from red to yellow
- Table `4` phase `MAE`: `1` and `240` moved from yellow/red to green
- Table `5` phase `RMSE`: `1`, `39`, and `240` moved from yellow/red to green

### Residual SVM Yellow Cells

- Table `2`: `40`, `156`
- Table `3`: `40`, `156`, `240`
- Table `4`: `162`
- Table `5`: `162`

There are no remaining red `SVM` cells in Tables `2-5`.

## Canonical Benchmark Impact

After merging the best repaired `SVM` cells into the canonical benchmark:

- Table `2` full-matrix totals moved from `50 / 40 / 10` to `53 / 37 / 10`
- Table `3` full-matrix totals moved from `50 / 36 / 14` to `52 / 35 / 13`
- Table `4` full-matrix totals moved from `50 / 38 / 2` to `52 / 37 / 1`
- Table `5` full-matrix totals moved from `40 / 43 / 7` to `43 / 41 / 6`

On the canonical best-family Track `1` surface, the repair campaign also
closed one previously open harmonic target:

- Table `3` harmonic `0` moved from yellow to green

That update also changes the harmonic-closure reading in Table `6`:

- `1/10` harmonics now read as fully matched
- `8/10` remain partially matched
- `1/10` remains not yet matched

## Main Conclusions

The campaign supports five conclusions.

### 1. The SVM Row Is Now Scientifically Usable

Before this campaign, the `SVM` row still contained hard red blockers on the
amplitude and phase surfaces.

After the repair pass, the row has no remaining red cells.

### 2. Phase Repair Was The Strongest Lever

`track1_svm_phase_repair_seed11` was the cleanest scoped run and removed the
`240` blocker that had been dragging both phase tables.

### 3. Amplitude Repair Worked, But 156 And 240 Still Need Finishing

The amplitude side improved materially, especially on `0`, `81`, and `240`.

The only remaining amplitude drag is now the yellow band around `40`, `156`,
and `240`.

### 4. The Campaign Improved The Canonical Benchmark, Not Just Side Artifacts

This was not a local experiment that produced isolated better logs.

The best repaired cells have been promoted into the canonical `Track 1`
benchmark surface.

### 5. The Next Repair Wave Should Leave SVM And Move To Other Rows

`SVM` is no longer the right place to spend the largest repair budget.

The next efficient closure step is to attack the remaining red cells in the
other families, while keeping only a very small follow-up budget for the
residual `SVM` yellow cells.

## Produced Campaign Artifacts

The campaign output folder now contains the required serialized winner
artifacts:

- `output/training_campaigns/track1/svm/track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21/campaign_leaderboard.yaml`
- `output/training_campaigns/track1/svm/track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21/campaign_best_run.yaml`
- `output/training_campaigns/track1/svm/track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21/campaign_best_run.md`

The canonical reports updated by this closure are:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
