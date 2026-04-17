# Track 1 Full-Matrix Family Reproduction Campaign Results Report

## Overview

This report closes the full-matrix family-reproduction campaign prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md`

The campaign executed `20` exact-paper validation runs through the dedicated
launcher:

- completed runs: `20`
- failed runs: `0`
- execution window: `2026-04-14 14:12:14+02:00` to `2026-04-14 14:15:18+02:00`
- campaign artifact root:
  `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/`

This campaign was designed for the clarified first objective of `Track 1`:

- reproduce the paper matrices row by row with repository-owned model
  implementations;
- execute one amplitude run and one phase run for each paper family;
- materialize the real repository-side counterparts of paper Tables `3`, `4`,
  and `5`.

## Objective And Outcome

The campaign had three concrete goals:

1. prepare one exact-paper row-reproduction run for each paper family on the
   amplitude side;
2. prepare one exact-paper row-reproduction run for each paper family on the
   phase side;
3. replace the old best-envelope reading with a real full-matrix
   repository-owned replication surface.

Outcome:

- all `20` runs completed successfully;
- all `20` runs exported ONNX artifacts with `0` failed targets;
- the campaign produced the first complete repository-owned row-by-row
  replication surface for Tables `3`, `4`, and `5`;
- `Track 1` remains open because no table is fully green and several rows still
  contain materially red cells;
- the strongest row-level reproductions are now explicit and inspectable rather
  than hidden inside one all-family winner run.

This means the campaign succeeded operationally and scientifically as a
matrix-reproduction pass, even though it did not close `Track 1`.

## Ranking Policy

This campaign cannot be ranked by one global `MAPE` winner, because each run
only reproduces one paper family row on one target side.

The serialized campaign policy is therefore:

- primary metric: `row_closure_score_desc`
- first tie breaker: `met_paper_cell_count_desc`
- second tie breaker: `open_paper_cell_count_asc`
- third tie breaker: `mean_normalized_gap_ratio_asc`
- fourth tie breaker: `max_normalized_gap_ratio_asc`
- fifth tie breaker: `matched_table6_family_target_count_desc`
- sixth tie breaker: `run_name`

Where:

- `row_closure_score = (met + 0.5 * near) / target_count`
- `met` means the repository row cell reached or beat the paper cell
- `near` means the positive gap stayed within `25%` of the paper cell

Interpretation:

- this policy exists only to serialize the required campaign-best artifacts;
- the real scientific interpretation remains full matrix replication, not one
  global best run.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Run | Family | Scope | Targets | Met | Near | Open | Closure Score |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `1` | `track1_rf_phase_full_matrix` | `RF` | `phases_only` | `9` | `3` | `4` | `2` | `0.556` |
| `2` | `track1_ert_amplitude_full_matrix` | `ERT` | `amplitudes_only` | `10` | `3` | `4` | `3` | `0.500` |
| `3` | `track1_gbm_phase_full_matrix` | `GBM` | `phases_only` | `9` | `3` | `3` | `3` | `0.500` |
| `4` | `track1_hgbm_amplitude_full_matrix` | `HGBM` | `amplitudes_only` | `10` | `3` | `4` | `3` | `0.500` |
| `5` | `track1_hgbm_phase_full_matrix` | `HGBM` | `phases_only` | `9` | `2` | `5` | `2` | `0.500` |
| `6` | `track1_rf_amplitude_full_matrix` | `RF` | `amplitudes_only` | `10` | `2` | `5` | `3` | `0.450` |
| `7` | `track1_ert_phase_full_matrix` | `ERT` | `phases_only` | `9` | `3` | `2` | `4` | `0.444` |
| `8` | `track1_lgbm_amplitude_full_matrix` | `LGBM` | `amplitudes_only` | `10` | `2` | `4` | `4` | `0.400` |
| `9` | `track1_lgbm_phase_full_matrix` | `LGBM` | `phases_only` | `9` | `1` | `5` | `3` | `0.389` |
| `10` | `track1_gbm_amplitude_full_matrix` | `GBM` | `amplitudes_only` | `10` | `1` | `4` | `5` | `0.300` |
| `11` | `track1_dt_phase_full_matrix` | `DT` | `phases_only` | `9` | `0` | `4` | `5` | `0.222` |
| `12` | `track1_dt_amplitude_full_matrix` | `DT` | `amplitudes_only` | `10` | `0` | `2` | `8` | `0.100` |
| `13` | `track1_et_amplitude_full_matrix` | `ET` | `amplitudes_only` | `10` | `0` | `2` | `8` | `0.100` |
| `14` | `track1_et_phase_full_matrix` | `ET` | `phases_only` | `9` | `0` | `1` | `8` | `0.056` |
| `15` | `track1_xgbm_amplitude_full_matrix` | `XGBM` | `amplitudes_only` | `10` | `0` | `1` | `9` | `0.050` |
| `16` | `track1_svm_amplitude_full_matrix` | `SVR` | `amplitudes_only` | `10` | `0` | `1` | `9` | `0.050` |
| `17` | `track1_xgbm_phase_full_matrix` | `XGBM` | `phases_only` | `9` | `0` | `0` | `9` | `0.000` |
| `18` | `track1_svm_phase_full_matrix` | `SVR` | `phases_only` | `9` | `0` | `0` | `9` | `0.000` |
| `19` | `track1_mlp_phase_full_matrix` | `MLP` | `phases_only` | `9` | `0` | `0` | `9` | `0.000` |
| `20` | `track1_mlp_amplitude_full_matrix` | `MLP` | `amplitudes_only` | `10` | `0` | `0` | `10` | `0.000` |

### Export Surface

| Completed Runs | Exported ONNX Files | Failed Exports | Surrogate Exports |
| ---: | ---: | ---: | ---: |
| `20` | `190` | `0` | `4` |

The `4` surrogate exports all came from the `SVR` amplitude row, where a few
targets still needed the existing constant-linear-regression safeguard.

## Campaign Best Run

The explicit bookkeeping winner is:

- `track1_rf_phase_full_matrix`

It was selected because it achieved:

- the highest campaign row-closure score: `0.556`
- `3` met cells and `4` near cells out of `9`
- only `2` materially open cells in the `RF` phase row

Important interpretation:

- this run is the campaign bookkeeping winner;
- it is **not** the global solution for `Track 1`;
- it only means the `RF` phase row is currently the cleanest single row in the
  full-matrix campaign.

## Matrix-Reproduction Impact

### Campaign-Wide Cell Totals

| Surface | Green | Yellow | Red |
| --- | ---: | ---: | ---: |
| Table `3` amplitude `RMSE` | `11` | `27` | `62` |
| Table `4` phase `MAE` | `16` | `28` | `46` |
| Table `5` phase `RMSE` | `16` | `22` | `52` |

### Strongest Current Rows

- strongest amplitude-side row: `ERT` with `3` green, `4` yellow, `3` red
- strongest phase-side combined row: `RF` with `3` met, `4` near, `2` open
- strongest phase `MAE` row by direct visual usefulness: `RF`
- strongest phase `RMSE` rows: `RF` and `HGBM`

### Weakest Current Rows

- weakest amplitude row: `MLP` with `0` green, `0` yellow, `10` red
- weakest phase rows: `SVM`, `XGBM`, and `MLP`, all still fully open under the
  paired row-closure reading

## Interpretation By Table

### Table 3 - Amplitude RMSE

The amplitude side is not uniformly hard.

The campaign shows three distinct bands:

- strongest rows: `ERT`, `HGBM`, `RF`
- usable but incomplete rows: `LGBM`, `GBM`
- clearly off-paper rows: `SVM`, `DT`, `ET`, `XGBM`, `MLP`

Important reading:

- the amplitude side is now clearly tree and boosting dominated;
- `ERT` and `HGBM` are the most paper-faithful amplitude families overall;
- `MLP` is not remotely competitive on this exact-paper branch.

### Table 4 - Phase MAE

Phase `MAE` is the healthiest matrix of the three.

The best rows are:

- `RF`
- `ERT`
- `GBM`
- `HGBM`

Important reading:

- several families are already green on the mid-order harmonics;
- the persistent blockers are still concentrated at `162` and `240`;
- `RF` is the cleanest phase-side row under the current exact-paper split.

### Table 5 - Phase RMSE

Phase `RMSE` is materially harder than phase `MAE`.

The best rows are:

- `RF`
- `HGBM`
- `GBM`
- `ERT`

Important reading:

- `78`, `81`, and `156` are already strong across several rows;
- the dominant unresolved columns are `162` and `240`;
- no family currently gives a paper-faithful fully green phase-`RMSE` row.

## Main Conclusions

The campaign supports six conclusions.

### 1. The Full-Matrix Objective Is Now Operationally Real

This is the first repository-owned campaign that truly reproduces the paper
matrix structure family by family.

That removes the ambiguity of the previous best-envelope reading.

### 2. Track 1 Is Still Open

No table is fully green and no family row is fully replicated.

So the first true `Track 1` objective is not yet closed.

### 3. Tree And Boosting Families Dominate The Exact-Paper Surface

The strongest rows come from:

- `RF`
- `ERT`
- `GBM`
- `HGBM`
- `LGBM` on selected rows

This is directionally consistent with the paper.

### 4. The Phase Side Is Closer Than The Amplitude Side

The campaign-wide totals show:

- amplitude still has `62` red cells
- phase `MAE` has `46` red cells
- phase `RMSE` has `52` red cells

So the amplitude matrix remains the larger closure burden.

### 5. MLP Is The Clearest Non-Starter On This Branch

Both `MLP` rows remain scientifically weak.

That does not just mean “not best”; it means materially off the paper matrix.

### 6. The Next Iteration Should Be Row-Aware And Harmonic-Aware

This campaign was the correct first packaging step.

But the next one should be more surgical:

- keep the stronger families for the rows they already serve well;
- focus targeted repair work on the remaining red harmonics within those rows;
- avoid spending equal effort on rows that are structurally far from the paper.

## Recommended Next Actions

The next technically justified steps are:

1. keep `track1_rf_phase_full_matrix` as the bookkeeping winner for this
   campaign only;
2. keep the real `Track 1` reading anchored to the full family-row matrices in
   the benchmark report;
3. prioritize row-aware repair work around:
   `ERT` amplitude, `HGBM` amplitude, `RF` phase, `GBM` phase, and `HGBM`
   phase;
4. deprioritize `MLP` and likely also `SVM`/`XGBM` for immediate closure work
   unless there is a strong paper-specific reason to keep them active;
5. use the new matrix dashboard to choose the next repair campaign by red-cell
   density rather than by generic family subset intuition.

## Artifact References

- Campaign root:
  `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/`
- Campaign leaderboard:
  `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/campaign_leaderboard.yaml`
- Campaign best run YAML:
  `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/campaign_best_run.yaml`
- Campaign best run note:
  `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/campaign_best_run.md`
- Campaign logs:
  `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/logs/`
- Canonical benchmark dashboard:
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
