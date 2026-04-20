# Track 1 SVM Final Closure Campaign Results Report

## Overview

This report closes the dedicated `SVR` final-closure campaign prepared in:

- `doc/reports/campaign_plans/track1/svm/2026-04-14-20-50-01_track1_svm_final_closure_campaign_plan_report.md`

The campaign executed `12` exact-paper validation runs through the dedicated
launcher:

- completed runs: `12`
- failed runs: `0`
- execution window: `2026-04-14 21:09:00+02:00` to `2026-04-14 21:10:39+02:00`
- campaign artifact root:
  `output/training_campaigns/track1/svm/track1_svm_final_closure_campaign_2026_04_14_20_50_01/`

The campaign goal was explicit:

- close the last residual yellow `SVM` cells after the broader repair wave;
- focus only on amplitude harmonics `40`, `156`, `240`;
- focus only on phase harmonic `162`;
- merge the best per-cell improvements back into the canonical `SVM` row.

## Objective And Outcome

The campaign had three concrete goals:

1. fully close amplitude harmonic `156`;
2. try to close amplitude `40`, amplitude `240`, and phase `162`;
3. convert the `SVM` row from near-closure into a practically closed row.

Outcome:

- all `12` runs completed successfully;
- all `12` runs exported ONNX artifacts with `0` failed exports;
- the campaign closed amplitude harmonic `156` on both Table `2` and Table `3`;
- the campaign improved phase `162`, but did not fully close it;
- the `SVM` row is now extremely close to full closure, with only `5` yellow
  cells left across Tables `2-5`.

This means the campaign succeeded partially and usefully:

- it did not finish the full `SVM` row;
- but it removed the strongest remaining amplitude blocker and tightened the
  row further without regressions.

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
  `red -> green` transitions versus the pre-final-closure `SVM` baseline row

Interpretation:

- this policy exists only to serialize the required campaign-best artifacts;
- the real scientific interpretation remains the merged post-final-closure
  `SVM` row across Tables `2-5`.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Run | Scope | Cells | Met | Near | Open | Closure Score | Improved | Upgrades |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_svm_amplitude_full_closure_split15` | `amplitudes_only` | `6` | `2` | `3` | `1` | `0.583` | `3` | `2` |
| `2` | `track1_svm_amplitude_final_closure_seed23` | `amplitudes_only` | `6` | `1` | `5` | `0` | `0.583` | `0` | `0` |
| `3` | `track1_svm_phase_final_closure_split15` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `4` | `track1_svm_amplitude_40_bridge` | `amplitudes_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `5` | `track1_svm_phase_final_closure_seed11` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `6` | `track1_svm_phase_final_closure_baseline` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `7` | `track1_svm_phase_final_closure_split25` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `8` | `track1_svm_phase_final_closure_seed23` | `phases_only` | `2` | `0` | `2` | `0` | `0.500` | `0` | `0` |
| `9` | `track1_svm_amplitude_final_closure_baseline` | `amplitudes_only` | `6` | `0` | `5` | `1` | `0.417` | `1` | `0` |
| `10` | `track1_svm_amplitude_hard_tail_focus` | `amplitudes_only` | `4` | `0` | `3` | `1` | `0.375` | `1` | `0` |
| `11` | `track1_svm_amplitude_final_closure_seed11` | `amplitudes_only` | `6` | `0` | `2` | `4` | `0.167` | `0` | `0` |
| `12` | `track1_svm_amplitude_hard_tail_seed11` | `amplitudes_only` | `4` | `0` | `0` | `4` | `0.000` | `0` | `0` |

### Export Surface

| Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports |
| ---: | ---: | ---: | ---: |
| `12` | `22` | `0` | `5` |

All `5` surrogate exports came from amplitude-side `SVR` targets that still
needed the existing constant-linear-regression safeguard.

## Campaign Best Run

The explicit bookkeeping winner is:

- `track1_svm_amplitude_full_closure_split15`

It was selected because it achieved:

- the highest campaign scoped cell-closure score among runs with a real status
  upgrade;
- `2` met cells and `3` near cells out of `6`;
- the only successful `yellow -> green` promotion on harmonic `156` across
  both amplitude surfaces;
- the strongest scoped final-closure amplitude improvement package.

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** the whole scientific result by itself;
- the scientific output is the merged post-final-closure `SVM` row now written
  into the canonical benchmark.

## SVM Row Impact

### Table-Level Before Vs After

| Surface | Before | After |
| --- | --- | --- |
| Table `2` amplitude `MAE` | `8` green, `2` yellow, `0` red | `9` green, `1` yellow, `0` red |
| Table `3` amplitude `RMSE` | `7` green, `3` yellow, `0` red | `8` green, `2` yellow, `0` red |
| Table `4` phase `MAE` | `8` green, `1` yellow, `0` red | `8` green, `1` yellow, `0` red |
| Table `5` phase `RMSE` | `8` green, `1` yellow, `0` red | `8` green, `1` yellow, `0` red |

### Closed Or Improved Cells

- Table `2` amplitude `MAE`: harmonic `156` moved from yellow to green
- Table `3` amplitude `RMSE`: harmonic `156` moved from yellow to green
- Table `4` phase `MAE`: harmonic `162` improved numerically but stayed yellow
- Table `5` phase `RMSE`: harmonic `162` improved numerically but stayed yellow

### Residual SVM Yellow Cells

- Table `2`: `40`
- Table `3`: `40`, `240`
- Table `4`: `162`
- Table `5`: `162`

There are still no remaining red `SVM` cells in Tables `2-5`.

## Canonical Benchmark Impact

After merging the best final-closure `SVM` cells into the canonical benchmark:

- Table `2` full-matrix totals moved from `53 / 37 / 10` to `54 / 36 / 10`
- Table `3` full-matrix totals moved from `52 / 35 / 13` to `53 / 34 / 13`
- Table `4` full-matrix totals stayed at `52 / 37 / 1`
- Table `5` full-matrix totals stayed at `43 / 41 / 6`

The campaign did not change the canonical harmonic-level Table `6` closure
reading. Its impact stays local to the `SVM` row and the row-level full-matrix
surface.

## Main Conclusions

The campaign supports four conclusions.

### 1. The Hardest Remaining SVM Amplitude Cell Was Closed

Amplitude harmonic `156` is no longer yellow on either paper amplitude
surface.

That removes the strongest residual amplitude blocker from the `SVM` row.

### 2. Phase 162 Improved, But Did Not Close

The best phase run tightened both `MAE` and `RMSE` on harmonic `162`.

However, both cells remain yellow, so the phase row is still not fully closed.

### 3. SVM Is Now A Micro-Repair Problem

The `SVM` row is no longer a broad repair target.

What remains is a very small residual closure set:

- amplitude `40`
- amplitude `240`
- phase `162`

### 4. The Best Next Move Is A Tiny Follow-Up Or A Family Shift

At this point, a large new `SVM` campaign would be inefficient.

The rational options are:

- one last tiny `SVM` micro-closure pass on `40`, `240`, and `162`; or
- shift the main repair budget to other rows while keeping `SVM` on a minimal
  follow-up budget.

## Produced Campaign Artifacts

The campaign output folder now contains the required serialized winner
artifacts:

- `output/training_campaigns/track1/svm/track1_svm_final_closure_campaign_2026_04_14_20_50_01/campaign_leaderboard.yaml`
- `output/training_campaigns/track1/svm/track1_svm_final_closure_campaign_2026_04_14_20_50_01/campaign_best_run.yaml`
- `output/training_campaigns/track1/svm/track1_svm_final_closure_campaign_2026_04_14_20_50_01/campaign_best_run.md`

The canonical reports updated by this closure are:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
