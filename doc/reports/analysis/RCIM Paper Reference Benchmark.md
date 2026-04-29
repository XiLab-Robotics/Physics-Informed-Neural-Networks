# RCIM Paper Reference Benchmark

## Purpose

This report turns the paper
`reference/RCIM_ML-compensation.pdf` into a repository-owned benchmark package.
Its role is to keep the paper findings easy to inspect during planning,
training review, and colleague-facing status updates.

At the current repository state, the comparison is explicitly `offline-only`.
The repository does not yet have the online compensation pipeline needed for a
real Table 9 style comparison.

## Guided Reading

Read the paper in this order:

1. `Sections 2-3`: problem setup, dataset structure, selected harmonics, and
   model evaluation logic.
2. `Section 3.7` plus `Tables 2-6`: harmonic-level model ranking and the
   deployed model choices.
3. `Sections 4-5` plus `Table 9`: TwinCAT/PLC integration and the final online
   compensation benchmark.

The most important paper message is not only that ML can fit the reducer TE,
but that a deployable harmonic-wise prediction stack can be integrated into a
PLC and produce large online reductions in TE during real motion profiles.

## What The Paper Actually Says

### Problem Setup

- The paper models rotational Transmission Error of an RV reducer as a function
  of `input speed`, `applied torque`, and `oil temperature`.
- The paper explicitly treats `forward` and `backward` TE curves as distinct
  phenomena, even though the later notation is generalized with one shared
  directional subscript.
- The TE is reconstructed from selected harmonic components rather than from
  one monolithic end-to-end neural predictor.
- The paper explicitly separates:
  - offline harmonic prediction;
  - PLC integration;
  - online compensation validation.

### Experimental Domain

- Total experimental samples: `1026`
- Speed levels: `100` to `1800 rpm`
- Torque levels: `0` to `1800 Nm`
- Temperature levels: `25`, `30`, `35 C`

### Forward And Backward Interpretation

- Equation `(2)` is direction-generic and must be read as valid for both the
  forward and backward formulations.
- The generalized amplitude and phase symbols therefore stand for two parallel
  branches: forward-side harmonic parameters and backward-side harmonic
  parameters.
- Section `3.1` implies direction-specific training datasets, so the paper
  families should be understood as trained separately on forward and backward
  data.
- The tables published in the paper for the full family comparison surface are
  the forward-side tables.
- The recovered models currently stored in this repository are also the
  forward-side models.

### Harmonic Structure

The paper emphasizes these harmonics as the practical basis for TE modeling and
compensation:

- `0`
- `1`
- `3`
- `39`
- `40`
- `78`
- `81`
- `156`
- `162`
- `240`

The deployed compensation baseline then centers primarily on:

- `0`
- `1`
- `39`

Additional validation variants also include:

- `40`
- `78`

## Model Selection Summary

### Paper-Level Conclusion

The paper does not end with a single universal winner across every harmonic.
Instead, it converges toward a deployable stack dominated by tree and boosting
 models.

### Harmonic-Level Selected Models

| Harmonic | Selected Paper Model(s) |
| --- | --- |
| `0` | `SVM` |
| `1` | `RF / LGBM` |
| `3` | `HGBM` |
| `39` | `HGBM` |
| `40` | `ERT / GBM` |
| `78` | `HGBM / RF` |
| `81` | `RF` |
| `156` | `ERT / RF` |
| `162` | `ERT` |
| `240` | `ERT` |

### Why This Matters Here

- The paper is not arguing for a plain MLP-first deployment path.
- It favors models that are compact, interpretable enough for deployment work,
  and supported by the Beckhoff/TwinCAT stack.
- This is already directionally consistent with the current repository state,
  where the global offline winner is also tree-based.

## Extracted Reference Metrics

### Offline Prediction Validation

For unseen validation scenarios executed in TwinCAT-side prediction tests, the
paper reports mean percentage errors along the TE function of:

- `2.6%`
- `3.1%`
- `4.7%`

This is the most practical offline reference target that the repository can
aim to reproduce before the online compensation loop exists.

### Motion-Profile Test Conditions

| Motion Profile | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: |
| `Robot` | 303 | 759 | 31.6 |
| `Cycloidal` | 500 | 370 | 26.7 |

### Online Compensation Benchmark

| Profile | Case | TE RMS [deg] | TE Max [deg] | Reduction [%] |
| --- | --- | ---: | ---: | --- |
| `Robot` | No compensation | 0.0478 | 0.0681 | `-` |
| `Robot` | Comp `(0,1,39)` | 0.0080 | 0.0325 | `83.3 / 52.4` |
| `Robot` | Comp `(0,1,39,40)` | 0.0078 | 0.0309 | `83.6 / 54.7` |
| `Robot` | Comp `(0,1,39,78)` | 0.0079 | 0.0319 | `83.5 / 53.2` |
| `Cycloidal` | No compensation | 0.0282 | 0.0534 | `-` |
| `Cycloidal` | Comp `(0,1,39)` | 0.0017 | 0.0044 | `94.0 / 91.7` |
| `Cycloidal` | Comp `(0,1,39,40)` | 0.0017 | 0.0062 | `94.0 / 88.3` |
| `Cycloidal` | Comp `(0,1,39,78)` | 0.0027 | 0.0020 | `90.5 / 96.3` |

## Minimum Practical Targets For This Repository

### Target A

Match or beat the paper on a comparable offline prediction benchmark.

Minimum repository target:

- reproduce a paper-comparable TE-curve validation protocol;
- reach `<= 4.7%` mean percentage error on unseen comparable scenarios.

### Target B

Replicate the paper online compensation benchmark.

Minimum repository target:

- at least `83%` robot-profile TE RMS reduction;
- at least `90%` cycloidal-profile TE RMS reduction;
- and a cycloidal-profile TE max reduction in the same practical range as the
  paper benchmark.

## Repository Comparison At The Current State

### What Is Already Aligned

- The repository global offline winner is tree-based:
  - family: `tree`
  - model type: `hist_gradient_boosting`
  - run: `te_hist_gbr_tabular`
- The strongest current neural branch is still behind the tree winner:
  - family: `residual_harmonic_mlp`
- This is directionally consistent with the paper, where the deployable
  harmonic stack is dominated by tree and boosting models.

### Comparison Structure To Preserve

The repository should now keep three explicit offline comparison tracks:

- `Track 1`: exact-paper full family-bank replication
- `Track 1.5`: postponed harmonic-wise support branch
- `Track 2`: repository direct-TE comparable benchmark

The first track answers whether the repository can reproduce the paper-facing
family-bank model inventory across the four canonical full-matrix replication
tables. The postponed `Track 1.5` branch answers later harmonic-wise
reconstruction questions without redefining canonical `Track 1` status. The
second track answers whether the repository's already trained direct-TE
families can match or beat the paper at the level of final offline TE-curve
prediction quality.

These tracks must not be merged in reporting. Future paper-comparison
tables should explicitly label each entry as either:

- `exact-paper full family-bank`
- `harmonic-wise support branch`
- `result-level comparable direct-TE`

### Canonical Track 1 Closure Rule

For `Track 1`, the primary closure criterion is no longer the best campaign
winner under the shared offline evaluator.

The canonical `Track 1` closure rule is now:

- reproduce the paper-facing cells in Tables `2`, `3`, `4`, and `5`;
- interpret the current repository `Track 1` closure target as the
  forward-side exact-paper replication surface;
- keep progress summaries tied to the four full-matrix replication surfaces:
  - `Table 2 - Amplitude MAE Full-Matrix Replication`;
  - `Table 3 - Amplitude RMSE Full-Matrix Replication`;
  - `Table 4 - Phase MAE Full-Matrix Replication`;
  - `Table 5 - Phase RMSE Full-Matrix Replication`;
- treat completion as `19` accepted models for each of the `10` algorithm
  families;
- treat `Table 6` and any harmonic-wise TE-curve evaluator only as supporting
  or historical evidence outside the primary `Track 1` closure gate.

Repository consequence:

- a harmonic-wise campaign winner may still be useful diagnostically;
- however, it does not close `Track 1` by itself;
- `Track 1` closes only when the canonical exact-paper full family-bank
  surface is complete across the four full-matrix tables with `10 x 19`
  accepted models.

### What Is Not Yet Comparable

- The repository now has a repository-owned harmonic-wise offline validation
  protocol, but the first baseline does not yet match the paper threshold.
- The repository does not yet have a harmonic-wise online compensation loop.
- The repository does not yet have TwinCAT-side or equivalent motion-profile
  compensation tests matching the paper's `Robot` and `Cycloidal` profile
  benchmark.
- Therefore, the repository cannot yet claim a real comparison against the
  paper's `Table 9`.

### Primary Track 1 Status: Exact-Paper Table Replication

The primary `Track 1` status must now be read from this canonical benchmark
surface, with the older exact-paper validation report treated as historical
supporting evidence:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/validation_checks/track1/exact_paper/forward/shared/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`

Current exact-paper table-replication status from the canonical benchmark
surface is:

- `Table 2 - Amplitude MAE Full-Matrix Replication` remains partially open;
- `Table 3 - Amplitude RMSE Full-Matrix Replication` is numerically closed;
- `Table 4 - Phase MAE Full-Matrix Replication` is numerically closed;
- `Table 5 - Phase RMSE Full-Matrix Replication` is numerically closed.

The highest-priority still-open harmonics now remain concentrated around:

- `39`
- `156`
- `162`

Important interpretation:

- this exact-paper full-matrix status is the canonical `Track 1` status;
- a harmonic-wise campaign result can inform later analysis, but it does not
  replace the `Track 1` table-level closure rule;
- the `2026-04-19` cellwise remaining-family closeout completed the intended
  `19`-model banks for each non-`SVM` family;
- `Track 1` should therefore be read as a family-bank replication program, not
  as a harmonic-wise family-alignment program.

### 2026-04-18 Partial Refresh Addendum (Historical Snapshot)

This addendum is the canonical benchmark refresh after the interrupted
remaining-family rerun batch:

- completed refreshed families: `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`
- at that intermediate checkpoint, still pending rerun after the remote terminal
  crash: `XGBM`, `LGBM`
- `SVM` continues to read from the accepted repository reference archive
- supporting report:
  `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report.md`

The tables below should be read as the current canonical best-envelope
comparison after the partial refresh. The older detailed dashboard further
below remains useful as historical context, but this addendum is now the
highest-priority comparison surface until the pending reruns are completed.

This historical snapshot is now superseded by the later
`2026-04-18 Final Remaining-Family Closeout Addendum`.

#### 2026-04-18 Table 2 - Amplitude MAE

| Harmonic | Paper Best Family | Paper Target MAE | Repo Best Family | Repo Best MAE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0` | `HGBM` | 0.002400 | `XGBM` | 0.002465 | 6.46e-05 | `🟡` |
| `1` | `RF` | 2.40e-05 | `ERT` | 2.42e-05 | 2.14e-07 | `🟡` |
| `3` | `HGBM` | 1.50e-05 | `HGBM` | 1.83e-05 | 3.32e-06 | `🟡` |
| `39` | `HGBM` | 2.10e-05 | `HGBM` | 2.30e-05 | 2.04e-06 | `🟡` |
| `40` | `ERT` | 2.30e-05 | `RF` | 2.21e-05 | -8.59e-07 | `🟢` |
| `78` | `HGBM` | 2.70e-05 | `LGBM` | 2.46e-05 | -2.41e-06 | `🟢` |
| `81` | `RF` | 1.10e-05 | `ERT` | 1.13e-05 | 2.64e-07 | `🟡` |
| `156` | `ERT` | 1.70e-05 | `ERT` | 5.03e-05 | 3.33e-05 | `🔴` |
| `162` | `ERT` | 2.30e-05 | `ERT` | 5.41e-05 | 3.11e-05 | `🔴` |
| `240` | `ERT` | 2.40e-05 | `GBM` | 3.38e-05 | 9.84e-06 | `🔴` |

#### 2026-04-18 Table 3 - Amplitude RMSE

| Harmonic | Paper Best Family | Paper Target RMSE | Repo Best Family | Repo Best RMSE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0` | `SVM` | 0.003300 | `SVM` | 0.00311 | -1.90e-04 | `🟢` |
| `1` | `RF` | 3.50e-05 | `ERT` | 3.44e-05 | -5.54e-07 | `🟢` |
| `3` | `HGBM` | 2.50e-05 | `HGBM` | 2.57e-05 | 7.32e-07 | `🟡` |
| `39` | `HGBM` | 3.20e-05 | `HGBM` | 3.12e-05 | -7.78e-07 | `🟢` |
| `40` | `ERT` | 3.60e-05 | `ERT` | 3.27e-05 | -3.34e-06 | `🟢` |
| `78` | `HGBM` | 4.50e-05 | `LGBM` | 3.57e-05 | -9.30e-06 | `🟢` |
| `81` | `RF` | 1.50e-05 | `RF` | 1.85e-05 | 3.53e-06 | `🟡` |
| `156` | `ERT` | 1.30e-04 | `ERT` | 1.85e-04 | 5.50e-05 | `🔴` |
| `162` | `ERT` | 1.60e-04 | `RF` | 1.65e-04 | 5.18e-06 | `🟡` |
| `240` | `ERT` | 4.20e-05 | `RF` | 5.58e-05 | 1.38e-05 | `🔴` |

#### 2026-04-18 Table 4 - Phase MAE

| Harmonic | Paper Best Family | Paper Target MAE | Repo Best Family | Repo Best MAE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `1` | `LGBM` | 0.001800 | `HGBM` | 0.001832 | 3.22e-05 | `🟡` |
| `3` | `HGBM` | 0.0200 | `GBM` | 0.0237 | 0.003747 | `🟡` |
| `39` | `HGBM` | 0.0210 | `HGBM` | 0.0197 | -0.001326 | `🟢` |
| `40` | `GBM` | 0.0360 | `ERT` | 0.0358 | -2.29e-04 | `🟢` |
| `78` | `RF` | 0.0740 | `RF` | 0.0512 | -0.0228 | `🟢` |
| `81` | `RF` | 0.0530 | `RF` | 0.0471 | -0.005922 | `🟢` |
| `156` | `RF` | 0.5100 | `RF` | 0.4121 | -0.0979 | `🟢` |
| `162` | `DT` | 0.2000 | `RF` | 0.2235 | 0.0235 | `🟡` |
| `240` | `DT` | 0.2300 | `RF` | 0.2665 | 0.0365 | `🟡` |

#### 2026-04-18 Table 5 - Phase RMSE

| Harmonic | Paper Best Family | Paper Target RMSE | Repo Best Family | Repo Best RMSE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `1` | `HGBM` | 0.002500 | `GBM` | 0.002492 | -7.90e-06 | `🟢` |
| `3` | `HGBM` | 0.0290 | `HGBM` | 0.0339 | 0.004872 | `🟡` |
| `39` | `HGBM` | 0.0270 | `HGBM` | 0.0324 | 0.005421 | `🟡` |
| `40` | `RF` | 0.0550 | `RF` | 0.0546 | -4.28e-04 | `🟢` |
| `78` | `RF` | 0.1600 | `RF` | 0.1246 | -0.0354 | `🟢` |
| `81` | `RF` | 0.0820 | `RF` | 0.0659 | -0.0161 | `🟢` |
| `156` | `RF` | 1.200 | `ERT` | 0.9146 | -0.2854 | `🟢` |
| `162` | `ERT` | 0.6400 | `RF` | 0.7389 | 0.0989 | `🟡` |
| `240` | `ERT` | 0.5800 | `ERT` | 0.8217 | 0.2417 | `🔴` |

#### 2026-04-18 Table 6 - Harmonic Closure

| `k` | Paper `A*_k` | Repo Best Ampl Family | Ampl Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status | Overall |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `SVM` | `SVM` | `met_paper_target` | `-` | `ERT` | `ERT` | `not_applicable` | `not_applicable` | `fully_matched_tables_3_6` | `🟢` |
| `1` | `RF` | `ERT` | `met_paper_target` | `LGBM` | `HGBM` | `GBM` | `above_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `3` | `HGBM` | `HGBM` | `above_paper_target` | `HGBM` | `GBM` | `HGBM` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |
| `39` | `HGBM` | `HGBM` | `met_paper_target` | `HGBM` | `HGBM` | `HGBM` | `met_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `40` | `ERT` | `ERT` | `met_paper_target` | `GBM` | `ERT` | `RF` | `met_paper_target` | `met_paper_target` | `fully_matched_tables_3_6` | `🟢` |
| `78` | `HGBM` | `LGBM` | `met_paper_target` | `RF` | `RF` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `81` | `RF` | `RF` | `above_paper_target` | `RF` | `RF` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `156` | `ERT` | `ERT` | `above_paper_target` | `RF` | `RF` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `162` | `ERT` | `RF` | `above_paper_target` | `ERT` | `RF` | `RF` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |
| `240` | `ERT` | `RF` | `above_paper_target` | `ERT` | `RF` | `ERT` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |

### 2026-04-21 Open-Cell Full-Matrix Closure Addendum

This addendum supersedes the earlier residual-wave best-envelope reading
and is now the canonical benchmark refresh after the open-cell
full-matrix closure campaign.

- completed refreshed families: `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`
- completed validation runs now available in canonical local review paths: `756/756`
- locally reconstructed relaunch validation artifacts: `459`
- later recovered first-launch `MLP` validation artifacts: `297`
- promoted targeted family-target pairs: `17/28`
- retained baseline family-target pairs: `11/28`
- supporting report: `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report.md`

The benchmark now reads from the better value between:

- the already accepted canonical baseline present in the repository matrices;
- the new `2026-04-20-23-50-13` open-cell closure retries.

This keeps previously healthy cells stable while allowing the closure
wave to upgrade only the family-target pairs it actually improved.

The later post-closeout `MLP` artifact recovery resolves the original local
wrapper-reconciliation incident without changing the canonical best-envelope
reading:

- the full `297`-run `MLP` first-launch artifact set is now available in the
  canonical local validation roots;
- several family-internal `MLP` cells improved relative to the earlier partial
  local snapshot;
- none of those recovered `MLP` values beats the already accepted
  cross-family benchmark envelope on Tables `2-5`.

#### 2026-04-21 Table 2 - Amplitude MAE

| Harmonic | Paper Best Family | Paper Target | Repo Best Family | Repo Best | Gap Vs Paper | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `0` | `HGBM` | 0.0024 | `HGBM` | 0.00232717 | -7.283e-05 | `🟢` |
| `1` | `RF` | 2.4e-05 | `RF` | 2.36445e-05 | -3.555e-07 | `🟢` |
| `3` | `HGBM` | 1.5e-05 | `HGBM` | 1.43994e-05 | -6.006e-07 | `🟢` |
| `39` | `HGBM` | 2.1e-05 | `HGBM` | 2.13842e-05 | 3.84154e-07 | `🟡` |
| `40` | `ERT` | 2.3e-05 | `ERT` | 2.23281e-05 | -6.719e-07 | `🟢` |
| `78` | `HGBM` | 2.7e-05 | `HGBM` | 2.46364e-05 | -2.3636e-06 | `🟢` |
| `81` | `RF` | 1.1e-05 | `RF` | 1.01903e-05 | -8.097e-07 | `🟢` |
| `156` | `ERT` | 1.7e-05 | `ERT` | 1.86274e-05 | 1.62745e-06 | `🟡` |
| `162` | `ERT` | 2.3e-05 | `ERT` | 2.61501e-05 | 3.15008e-06 | `🟡` |
| `240` | `ERT` | 2.4e-05 | `GBM` | 2.05529e-05 | -3.4471e-06 | `🟢` |

- met paper cells on Table `2`: `7/10`

#### 2026-04-21 Table 3 - Amplitude RMSE

| Harmonic | Paper Best Family | Paper Target | Repo Best Family | Repo Best | Gap Vs Paper | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `0` | `SVM` | 0.0033 | `LGBM` | 0.00297361 | -0.00032639 | `🟢` |
| `1` | `RF` | 3.5e-05 | `RF` | 3.18311e-05 | -3.1689e-06 | `🟢` |
| `3` | `HGBM` | 2.5e-05 | `HGBM` | 1.95199e-05 | -5.4801e-06 | `🟢` |
| `39` | `HGBM` | 3.2e-05 | `HGBM` | 2.88632e-05 | -3.13677e-06 | `🟢` |
| `40` | `ERT` | 3.6e-05 | `ERT` | 3.30992e-05 | -2.9008e-06 | `🟢` |
| `78` | `HGBM` | 4.5e-05 | `HGBM` | 3.6544e-05 | -8.456e-06 | `🟢` |
| `81` | `RF` | 1.5e-05 | `LGBM` | 1.36486e-05 | -1.3514e-06 | `🟢` |
| `156` | `ERT` | 0.00013 | `ERT` | 4.45204e-05 | -8.54796e-05 | `🟢` |
| `162` | `ERT` | 0.00016 | `ERT` | 4.92697e-05 | -0.00011073 | `🟢` |
| `240` | `ERT` | 4.2e-05 | `GBM` | 3.30219e-05 | -8.9781e-06 | `🟢` |

- met paper cells on Table `3`: `10/10`

#### 2026-04-21 Table 4 - Phase MAE

| Harmonic | Paper Best Family | Paper Target | Repo Best Family | Repo Best | Gap Vs Paper | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `1` | `LGBM` | 0.0018 | `LGBM` | 0.0017062 | -9.38e-05 | `🟢` |
| `3` | `HGBM` | 0.02 | `HGBM` | 0.0198844 | -0.000115621 | `🟢` |
| `39` | `HGBM` | 0.021 | `HGBM` | 0.0190255 | -0.0019745 | `🟢` |
| `40` | `GBM` | 0.036 | `GBM` | 0.0326008 | -0.0033992 | `🟢` |
| `78` | `RF` | 0.074 | `RF` | 0.0542333 | -0.0197667 | `🟢` |
| `81` | `RF` | 0.053 | `GBM` | 0.0445389 | -0.0084611 | `🟢` |
| `156` | `RF` | 0.51 | `ERT` | 0.377856 | -0.132144 | `🟢` |
| `162` | `DT` | 0.2 | `DT` | 0.137578 | -0.0624223 | `🟢` |
| `240` | `DT` | 0.23 | `DT` | 0.149592 | -0.080408 | `🟢` |

- met paper cells on Table `4`: `9/9`

#### 2026-04-21 Table 5 - Phase RMSE

| Harmonic | Paper Best Family | Paper Target | Repo Best Family | Repo Best | Gap Vs Paper | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `1` | `HGBM` | 0.0025 | `LGBM` | 0.00242588 | -7.412e-05 | `🟢` |
| `3` | `HGBM` | 0.029 | `HGBM` | 0.0277127 | -0.00128729 | `🟢` |
| `39` | `HGBM` | 0.027 | `LGBM` | 0.0258044 | -0.0011956 | `🟢` |
| `40` | `RF` | 0.055 | `GBM` | 0.0490362 | -0.0059638 | `🟢` |
| `78` | `RF` | 0.16 | `ERT` | 0.119094 | -0.040906 | `🟢` |
| `81` | `RF` | 0.082 | `GBM` | 0.0643284 | -0.0176716 | `🟢` |
| `156` | `RF` | 1.2 | `ERT` | 0.88784 | -0.31216 | `🟢` |
| `162` | `ERT` | 0.64 | `RF` | 0.555209 | -0.0847908 | `🟢` |
| `240` | `ERT` | 0.58 | `RF` | 0.527103 | -0.052897 | `🟢` |

- met paper cells on Table `5`: `9/9`

Current canonical reading:

- total remaining non-green cells across Tables `2-5`: `3`
- open Table `2` harmonics: `39, 156, 162`
- open Table `3` harmonics: `none`
- open Table `4` harmonics: `none`
- open Table `5` harmonics: `none`

Track interpretation:

- `Track 1` is now judged only from Tables `2-5` plus the `10 x 19` accepted family-bank rule.
- Harmonic-wise Table `6` evidence remains historical support and does not gate `Track 1` closure.

### Deprecated Dashboard: Best-Envelope Reading

This dashboard is kept temporarily for historical continuity, but it is **not**
the primary first-reading surface for `Track 1`.

### 2026-04-18 Final Remaining-Family Closeout Addendum

This addendum supersedes the earlier partial refresh and is now the canonical
benchmark reading after the recovered `XGBM` and `LGBM` reruns completed.

- final refreshed families now include: `MLP`, `RF`, `DT`, `ET`, `ERT`,
  `GBM`, `HGBM`, `XGBM`, `LGBM`
- `SVM` still reads from the accepted repository reference archive
- supporting report:
  `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-18-16-34-18_track1_remaining_family_final_closeout_campaign_results_report.md`

The final batch closeout improves the canonical amplitude-side envelope
slightly through the new `LGBM` row, while leaving the harmonic-level closure
reading structurally unchanged.

#### 2026-04-18 Final Table 2 - Amplitude MAE

| Harmonic | Paper Best Family | Paper Target MAE | Repo Best Family | Repo Best MAE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0` | `HGBM` | 0.002400 | `XGBM` | 0.002465 | 6.46e-05 | `🟡` |
| `1` | `RF` | 2.40e-05 | `LGBM` | 2.39e-05 | -9.24e-08 | `🟢` |
| `3` | `HGBM` | 1.50e-05 | `LGBM` | 1.72e-05 | 2.16e-06 | `🟡` |
| `39` | `HGBM` | 2.10e-05 | `LGBM` | 2.27e-05 | 1.74e-06 | `🟡` |
| `40` | `ERT` | 2.30e-05 | `RF` | 2.21e-05 | -8.59e-07 | `🟢` |
| `78` | `HGBM` | 2.70e-05 | `LGBM` | 2.56e-05 | -1.41e-06 | `🟢` |
| `81` | `RF` | 1.10e-05 | `ERT` | 1.13e-05 | 2.64e-07 | `🟡` |
| `156` | `ERT` | 1.70e-05 | `ERT` | 5.03e-05 | 3.33e-05 | `🔴` |
| `162` | `ERT` | 2.30e-05 | `ERT` | 5.41e-05 | 3.11e-05 | `🔴` |
| `240` | `ERT` | 2.40e-05 | `GBM` | 3.38e-05 | 9.84e-06 | `🔴` |

#### 2026-04-18 Final Table 3 - Amplitude RMSE

| Harmonic | Paper Best Family | Paper Target RMSE | Repo Best Family | Repo Best RMSE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0` | `SVM` | 0.003300 | `SVM` | 0.00311 | -1.90e-04 | `🟢` |
| `1` | `RF` | 3.50e-05 | `LGBM` | 3.30e-05 | -1.98e-06 | `🟢` |
| `3` | `HGBM` | 2.50e-05 | `LGBM` | 2.43e-05 | -6.51e-07 | `🟢` |
| `39` | `HGBM` | 3.20e-05 | `LGBM` | 3.07e-05 | -1.34e-06 | `🟢` |
| `40` | `ERT` | 3.60e-05 | `ERT` | 3.27e-05 | -3.34e-06 | `🟢` |
| `78` | `HGBM` | 4.50e-05 | `LGBM` | 3.77e-05 | -7.28e-06 | `🟢` |
| `81` | `RF` | 1.50e-05 | `RF` | 1.85e-05 | 3.53e-06 | `🟡` |
| `156` | `ERT` | 1.30e-04 | `ERT` | 1.85e-04 | 5.50e-05 | `🔴` |
| `162` | `ERT` | 1.60e-04 | `RF` | 1.65e-04 | 5.18e-06 | `🟡` |
| `240` | `ERT` | 4.20e-05 | `RF` | 5.58e-05 | 1.38e-05 | `🔴` |

#### 2026-04-18 Final Table 4 - Phase MAE

| Harmonic | Paper Best Family | Paper Target MAE | Repo Best Family | Repo Best MAE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `1` | `LGBM` | 0.001800 | `HGBM` | 0.001832 | 3.22e-05 | `🟡` |
| `3` | `HGBM` | 0.0200 | `GBM` | 0.0237 | 0.003747 | `🟡` |
| `39` | `HGBM` | 0.0210 | `HGBM` | 0.0197 | -0.001326 | `🟢` |
| `40` | `GBM` | 0.0360 | `ERT` | 0.0358 | -2.29e-04 | `🟢` |
| `78` | `RF` | 0.0740 | `RF` | 0.0512 | -0.0228 | `🟢` |
| `81` | `RF` | 0.0530 | `LGBM` | 0.0470 | -0.005986 | `🟢` |
| `156` | `RF` | 0.5100 | `RF` | 0.4121 | -0.0979 | `🟢` |
| `162` | `DT` | 0.2000 | `RF` | 0.2235 | 0.0235 | `🟡` |
| `240` | `DT` | 0.2300 | `RF` | 0.2665 | 0.0365 | `🟡` |

#### 2026-04-18 Final Table 5 - Phase RMSE

| Harmonic | Paper Best Family | Paper Target RMSE | Repo Best Family | Repo Best RMSE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `1` | `HGBM` | 0.002500 | `GBM` | 0.002492 | -7.90e-06 | `🟢` |
| `3` | `HGBM` | 0.0290 | `HGBM` | 0.0339 | 0.004872 | `🟡` |
| `39` | `HGBM` | 0.0270 | `LGBM` | 0.0323 | 0.005272 | `🟡` |
| `40` | `RF` | 0.0550 | `RF` | 0.0546 | -4.28e-04 | `🟢` |
| `78` | `RF` | 0.1600 | `RF` | 0.1246 | -0.0354 | `🟢` |
| `81` | `RF` | 0.0820 | `RF` | 0.0659 | -0.0161 | `🟢` |
| `156` | `RF` | 1.200 | `ERT` | 0.9146 | -0.2854 | `🟢` |
| `162` | `ERT` | 0.6400 | `RF` | 0.7389 | 0.0989 | `🟡` |
| `240` | `ERT` | 0.5800 | `ERT` | 0.8217 | 0.2417 | `🔴` |

#### 2026-04-18 Final Table 6 - Harmonic Closure

| `k` | Paper `A*_k` | Repo Best Ampl Family | Ampl Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status | Overall |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `SVM` | `SVM` | `met_paper_target` | `-` | `ERT` | `ERT` | `not_applicable` | `not_applicable` | `fully_matched_tables_3_6` | `🟢` |
| `1` | `RF` | `LGBM` | `met_paper_target` | `LGBM` | `HGBM` | `GBM` | `above_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `3` | `HGBM` | `LGBM` | `met_paper_target` | `HGBM` | `GBM` | `HGBM` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |
| `39` | `HGBM` | `LGBM` | `met_paper_target` | `HGBM` | `HGBM` | `LGBM` | `met_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `40` | `ERT` | `ERT` | `met_paper_target` | `GBM` | `ERT` | `RF` | `met_paper_target` | `met_paper_target` | `fully_matched_tables_3_6` | `🟢` |
| `78` | `HGBM` | `LGBM` | `met_paper_target` | `RF` | `RF` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `81` | `RF` | `RF` | `above_paper_target` | `RF` | `LGBM` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `156` | `ERT` | `ERT` | `above_paper_target` | `RF` | `RF` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `162` | `ERT` | `RF` | `above_paper_target` | `ERT` | `RF` | `RF` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |
| `240` | `ERT` | `RF` | `above_paper_target` | `ERT` | `RF` | `ERT` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |

Use the full paper-matrix replication dashboard below as the canonical view for
model-by-model and harmonic-by-harmonic replication against the paper tables.

This section is now the canonical always-updated colleague-facing dashboard
for the paper-facing `Track 1` closure effort.

Maintenance rule:

- update this section after every material `Track 1` progress step;
- keep the paper-side tables stable unless a source-reading correction is
  required;
- refresh the repository-side tables from the latest canonical exact-paper
  best run;
- after changing the full-matrix repository values, run
  `scripts/reports/refresh_track1_benchmark_colored_markers.py` so the
  colored `🟢/🟡/🔴` dashboard markers stay synchronized with the numeric cells;
- treat this section as open work until `Track 1` reaches full closure.

Current repository evidence source for the dashboard:

- best current exact-paper run:
  `exact_open_cell_paper_family_reference`
- run instance id:
  `2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run`
- detailed supporting report:
  `doc/reports/analysis/validation_checks/track1/exact_paper/forward/shared/2026-04-13-22-09-00_paper_reimplementation_rcim_exact_model_bank_exact_open_cell_paper_family_reference_campaign_run_exact_paper_model_bank_report.md`

Status legend used below:

- `🟢` target reached or beaten
- `🟡` not reached yet, but the positive gap is within `25%` of the paper
  target and is therefore treated as near-target / acceptable follow-up
- `🔴` not reached and still materially open

Scope note:

- the paper-side tables below are repository-owned reconstructions of paper
  Tables `2-6`;
- the repository-side tables are analogous tracking surfaces built from the
  current exact-paper validation outputs;
- Table `2` is necessarily a repository inference of the paper-facing deployed
  harmonic selection summary, because the repository needs one normalized view
  that can be compared directly against the current `Track 1` best run.

#### Table 2 - Amplitude MAE

Paper-side repository-owned reconstruction:

| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002600 | 5.60e-05 | 1.60e-04 | 1.50e-04 | 7.90e-05 | 2.60e-04 | 9.10e-05 | 4.40e-04 | 6.90e-04 | 2.90e-04 |
| `MLP` | 0.009500 | 0.006500 | 0.006500 | 0.005600 | 0.006900 | 0.007100 | 0.007400 | 0.006800 | 0.008100 | 0.005500 |
| `RF` | 0.003000 | 2.40e-05 | 2.00e-05 | 2.90e-05 | 2.60e-05 | 3.80e-05 | 1.10e-05 | 5.70e-05 | 6.80e-05 | 2.90e-05 |
| `DT` | 0.003400 | 2.90e-05 | 2.20e-05 | 4.00e-05 | 3.20e-05 | 5.90e-05 | 1.30e-05 | 6.30e-05 | 6.20e-05 | 5.10e-05 |
| `ET` | 0.003500 | 3.10e-05 | 2.40e-05 | 3.80e-05 | 3.20e-05 | 5.90e-05 | 1.80e-05 | 5.70e-05 | 8.80e-05 | 7.20e-05 |
| `ERT` | 0.003100 | 2.70e-05 | 2.30e-05 | 2.90e-05 | 2.30e-05 | 3.80e-05 | 1.20e-05 | 1.70e-05 | 2.30e-05 | 2.40e-05 |
| `GBM` | 0.003100 | 2.70e-05 | 2.10e-05 | 2.80e-05 | 2.70e-05 | 3.90e-05 | 1.20e-05 | 6.10e-05 | 7.10e-05 | 3.00e-05 |
| `HGBM` | 0.002400 | 2.70e-05 | 1.50e-05 | 2.10e-05 | 2.60e-05 | 2.70e-05 | 1.20e-05 | 1.00e-04 | 1.70e-04 | 3.50e-05 |
| `XGBM` | 0.002500 | 5.50e-05 | 8.10e-05 | 1.10e-04 | 6.60e-05 | 1.10e-04 | 4.60e-05 | 2.30e-04 | 2.60e-04 | 1.40e-04 |
| `LGBM` | 0.002500 | 2.70e-05 | 1.80e-05 | 2.40e-05 | 2.70e-05 | 3.00e-05 | 1.20e-05 | 9.00e-05 | 1.60e-04 | 3.20e-05 |

Repository-side analogous Track 1 table:

| `k` | Paper `A*_k` | Repo Best Ampl Family | Ampl Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status |
| --- | --- | --- | ---: | --- | --- | --- | ---: | ---: | ---: |
| `0` | `HGBM` | `HGBM` | `above_paper_target` | `-` | `ERT` | `ERT` | `not_applicable` | `not_applicable` | `partially_matched_tables_3_6` |
| `1` | `RF` | `ERT` | `above_paper_target` | `LGBM` | `HGBM` | `LGBM` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` |
| `3` | `HGBM` | `GBM` | `above_paper_target` | `HGBM` | `GBM` | `LGBM` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` |
| `39` | `HGBM` | `GBM` | `above_paper_target` | `HGBM` | `HGBM` | `HGBM` | `met_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` |
| `40` | `ERT` | `ERT` | `met_paper_target` | `GBM` | `ERT` | `RF` | `above_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `78` | `HGBM` | `HGBM` | `met_paper_target` | `RF` | `RF` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `81` | `RF` | `RF` | `above_paper_target` | `RF` | `GBM` | `GBM` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `156` | `ERT` | `ERT` | `above_paper_target` | `RF` | `ERT` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `162` | `ERT` | `ERT` | `above_paper_target` | `DT` | `ERT` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |
| `240` | `ERT` | `GBM` | `above_paper_target` | `DT` | `RF` | `ERT` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` |

Current dashboard reading:

- fully green harmonics: none yet
- partial yellow harmonics: `0`, `1`, `39`, `40`, `78`, `81`, `156`, `162`
- fully red harmonics: `3`, `240`

This means `Track 1` is still structurally open after the cellwise refresh,
blocked by:

- amplitude-side numeric pressure that remains at `0`, `1`, `3`, `39`, `156`, `162`, and `240`;
- phase-side family-alignment drift even where the numeric gaps improved;
- the hard residual at `240`, which still stays red on the phase `RMSE` surface;
- and the fact that no harmonic is yet both numerically closed and family-aligned across Table `6`.

### Canonical Track 1 Dashboard: Full Paper-Matrix Replication

This dashboard is now the canonical first-reading surface for the clarified
first objective of `Track 1`:

- reproduce the paper matrices family by family;
- keep the exact paper model rows intact;
- read campaign progress as row replication, not only as best-envelope closure.

Current repository evidence source for the full matrices:

- latest exact-paper forward last three open cells overnight mega campaign:
  `track1_forward_last_three_open_cells_overnight_mega_campaign_2026-04-29_18_09_41`
- execution window:
  `2026-04-29T18:50:00+02:00` to `2026-04-29T22:44:24+02:00`
- supporting campaign report:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-30-01-25-40_track1_forward_last_three_open_cells_overnight_mega_campaign_results_report.md`

Status legend used in the repository matrices:

- `🟢` repository value reached or beat the paper cell
- `🟡` repository value is still above the paper cell, but the positive gap is
  within `25%` of the paper value
- `🔴` repository value is still materially above the paper cell

Important scope boundary:

- the matrices below use the exact same model-family rows as the paper:
  `SVM`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`
- the repository values come from our repository-owned implementations of
  those model families under the exact-paper validation branch
- Tables `2` and `6` remain useful summary/context surfaces, but the primary
  first `Track 1` replication target is the full matrix structure of Tables
  `3`, `4`, and `5`

### 2026-04-21 MLP Family Full-Matrix Repair Addendum

This addendum records the dedicated post-relaunch `MLP` family repair
wave that ran after the broader open-cell closeout had already been
published.

- campaign name: `track1_mlp_family_full_matrix_repair_campaign_2026_04_21_17_20_12`
- completed validation runs: `324/324`
- promoted targeted family-target pairs: `1/12`
- retained baseline family-target pairs: `11/12`
- supporting report: `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.md`

Canonical reading rule for this addendum:

- the accepted MLP row continues to read from the better value between
  the already accepted benchmark baseline and this dedicated repair
  wave;
- this MLP-only wave improves the accepted numeric value on `A40`, but it
  does not change the global Track 1 cross-family closure counts.

Post-closeout remaining non-green cells in the accepted `MLP` family row:

- `Table 2`: `1, 156, 240`
- `Table 3`: `1, 240`
- `Table 4`: `162`
- `Table 5`: `162`

### 2026-04-22 MLP Residual Cell Final Closure Addendum

This addendum records the dedicated residual-cell `MLP` closure wave
that targeted only the final four distinct accepted `MLP` target pairs
still blocking complete family closure in the canonical Tables `2-5`.

- campaign name: `track1_mlp_residual_cell_final_closure_campaign_2026_04_21_23_32_36`
- completed validation runs: `216/216`
- promoted targeted family-target pairs: `4/4`
- retained baseline family-target pairs: `0/4`
- supporting report: `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report.md`

Canonical reading rule for this addendum:

- the accepted MLP row continues to read from the better value between
  the already accepted benchmark baseline and this dedicated residual
  closure wave;
- this wave is allowed to close previously yellow residual cells but it
  does not alter the Track 1 scope definition itself.

Post-closeout remaining non-green cells in the accepted `MLP` family row:

- `Table 2`: `none`
- `Table 3`: `none`
- `Table 4`: `162`
- `Table 5`: `162`

#### Table 2 - Amplitude MAE Full-Matrix Replication

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002600 | 5.60e-05 | 1.60e-04 | 1.50e-04 | 7.90e-05 | 2.60e-04 | 9.10e-05 | 4.40e-04 | 6.90e-04 | 2.90e-04 |
| `MLP` | 0.009500 | 0.006500 | 0.006500 | 0.005600 | 0.006900 | 0.007100 | 0.007400 | 0.006800 | 0.008100 | 0.005500 |
| `RF` | 0.003000 | 2.40e-05 | 2.00e-05 | 2.90e-05 | 2.60e-05 | 3.80e-05 | 1.10e-05 | 5.70e-05 | 6.80e-05 | 2.90e-05 |
| `DT` | 0.003400 | 2.90e-05 | 2.20e-05 | 4.00e-05 | 3.20e-05 | 5.90e-05 | 1.30e-05 | 6.30e-05 | 6.20e-05 | 5.10e-05 |
| `ET` | 0.003500 | 3.10e-05 | 2.40e-05 | 3.80e-05 | 3.20e-05 | 5.90e-05 | 1.80e-05 | 5.70e-05 | 8.80e-05 | 7.20e-05 |
| `ERT` | 0.003100 | 2.70e-05 | 2.30e-05 | 2.90e-05 | 2.30e-05 | 3.80e-05 | 1.20e-05 | 1.70e-05 | 2.30e-05 | 2.40e-05 |
| `GBM` | 0.003100 | 2.70e-05 | 2.10e-05 | 2.80e-05 | 2.70e-05 | 3.90e-05 | 1.20e-05 | 6.10e-05 | 7.10e-05 | 3.00e-05 |
| `HGBM` | 0.002400 | 2.70e-05 | 1.50e-05 | 2.10e-05 | 2.60e-05 | 2.70e-05 | 1.20e-05 | 1.00e-04 | 1.70e-04 | 3.50e-05 |
| `XGBM` | 0.002500 | 5.50e-05 | 8.10e-05 | 1.10e-04 | 6.60e-05 | 1.10e-04 | 4.60e-05 | 2.30e-04 | 2.60e-04 | 1.40e-04 |
| `LGBM` | 0.002500 | 2.70e-05 | 1.80e-05 | 2.40e-05 | 2.70e-05 | 3.00e-05 | 1.20e-05 | 9.00e-05 | 1.60e-04 | 3.20e-05 |
<!-- markdownlint-enable MD013 -->

Forward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00240236` | `🟢 4.74467e-05` | `🟢 0.000135655` | `🟢 6.97981e-05` | `🟢 7.8059e-05` | `🟢 0.00015192` | `🟢 6.98458e-05` | `🟢 0.000316539` | `🟢 0.000371459` | `🟢 0.000242439` |
| `MLP` | `🟢 0.00345704` | `🟢 0.00171012` | `🟢 0.00210367` | `🟢 0.00194599` | `🟢 0.00215552` | `🟢 0.00206027` | `🟢 0.00179699` | `🟢 0.00246043` | `🟢 0.00211723` | `🟢 0.00255737` |
| `RF` | `🟢 0.0027414` | `🟢 2.16036e-05` | `🟢 1.75022e-05` | `🟢 2.48662e-05` | `🟢 2.09579e-05` | `🟢 3.65863e-05` | `🟢 9.25868e-06` | `🟢 3.65455e-05` | `🟢 3.84016e-05` | `🟢 2.86232e-05` |
| `DT` | `🟢 0.00297738` | `🟢 2.65389e-05` | `🟢 1.96269e-05` | `🟢 3.50183e-05` | `🟢 2.75625e-05` | `🟢 4.74183e-05` | `🟢 1.07044e-05` | `🟢 4.25289e-05` | `🟢 4.42742e-05` | `🟢 3.60934e-05` |
| `ET` | `🟢 0.00289541` | `🟢 2.72356e-05` | `🟢 1.97413e-05` | `🟢 3.35054e-05` | `🟢 2.66845e-05` | `🟢 4.82001e-05` | `🟢 1.16915e-05` | `🟢 4.21641e-05` | `🟢 4.20594e-05` | `🟢 4.49836e-05` |
| `ERT` | `🟢 0.0026374` | `🟢 2.07938e-05` | `🟢 1.88926e-05` | `🟢 2.58271e-05` | `🟢 2.06984e-05` | `🟢 2.93542e-05` | `🟢 8.76095e-06` | `🟡 1.84366e-05` | `🟢 2.20824e-05` | `🟡 2.8738e-05` |
| `GBM` | `🟢 0.00306606` | `🟢 2.24145e-05` | `🟢 1.62835e-05` | `🟢 2.39433e-05` | `🟢 2.38098e-05` | `🟢 2.65514e-05` | `🟢 1.08931e-05` | `🟢 5.3573e-05` | `🟡 8.20687e-05` | `🟢 2.06143e-05` |
| `HGBM` | `🟢 0.00229533` | `🟢 2.15532e-05` | `🟢 1.40313e-05` | `🟢 2.0816e-05` | `🟢 2.16954e-05` | `🟢 2.60491e-05` | `🟢 8.91012e-06` | `🟢 7.95097e-05` | `🟢 5.79553e-05` | `🟢 2.82265e-05` |
| `XGBM` | `🟢 0.00232205` | `🟢 4.56825e-05` | `🟢 7.00635e-05` | `🟢 8.81748e-05` | `🟢 5.75063e-05` | `🟢 0.000100894` | `🟢 4.43722e-05` | `🟢 0.000180962` | `🟢 0.000130144` | `🟢 0.000130039` |
| `LGBM` | `🟢 0.00242855` | `🟢 2.38161e-05` | `🟢 1.38863e-05` | `🟢 2.17697e-05` | `🟢 2.25468e-05` | `🟢 2.64171e-05` | `🟢 9.78776e-06` | `🟢 8.16133e-05` | `🟢 0.000128501` | `🟢 2.75739e-05` |
<!-- markdownlint-enable MD013 -->

Backward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00244815` | `🔴 0.00012218` | `🟢 0.000122128` | `🟢 9.19617e-05` | `🟢 3.72479e-05` | `🟢 0.000109804` | `🟢 3.67643e-05` | `🟢 0.000386544` | `🟢 0.00042391` | `🟢 0.000217944` |
| `MLP` | `🟢 0.00393679` | `🟢 0.00182461` | `🟢 0.00247029` | `🟢 0.0024777` | `🟢 0.00248698` | `🟢 0.00212886` | `🟢 0.00246561` | `🟢 0.00232499` | `🟢 0.00225488` | `🟢 0.00259757` |
| `RF` | `🟢 0.00248235` | `🟢 1.91284e-05` | `🟢 1.6782e-05` | `🟢 1.50283e-05` | `🟢 2.22018e-05` | `🟢 3.45098e-05` | `🟢 6.83012e-06` | `🔴 7.90409e-05` | `🟢 4.94272e-05` | `🔴 5.05932e-05` |
| `DT` | `🟢 0.00278626` | `🟢 2.56777e-05` | `🟢 2.19025e-05` | `🟢 1.97372e-05` | `🟢 2.57958e-05` | `🟢 5.06834e-05` | `🟢 8.54166e-06` | `🟡 6.61816e-05` | `🟢 4.61088e-05` | `🔴 7.03775e-05` |
| `ET` | `🟢 0.0030276` | `🟢 2.47334e-05` | `🟡 2.49502e-05` | `🟢 2.00874e-05` | `🟢 2.54493e-05` | `🟢 5.48314e-05` | `🟢 9.33761e-06` | `🔴 7.92687e-05` | `🟢 5.12173e-05` | `🟡 7.48752e-05` |
| `ERT` | `🟢 0.00259573` | `🟢 1.75332e-05` | `🟢 1.96649e-05` | `🟢 1.5993e-05` | `🟡 2.31882e-05` | `🟢 3.48878e-05` | `🟢 6.95047e-06` | `🔴 5.3009e-05` | `🔴 3.22538e-05` | `🔴 5.68946e-05` |
| `GBM` | `🟢 0.00306205` | `🟢 2.10163e-05` | `🟢 1.90911e-05` | `🟢 1.8684e-05` | `🟢 2.17104e-05` | `🔴 7.34086e-05` | `🟢 8.54983e-06` | `🔴 0.000178687` | `🔴 0.000135366` | `🔴 6.98378e-05` |
| `HGBM` | `🟢 0.0022091` | `🟢 1.94415e-05` | `🟡 1.60564e-05` | `🟢 1.43313e-05` | `🟢 2.17759e-05` | `🟢 2.43281e-05` | `🟢 8.08478e-06` | `🔴 0.000203439` | `🟢 7.37356e-05` | `🔴 8.15566e-05` |
| `XGBM` | `🟢 0.00229591` | `🟡 5.91334e-05` | `🟢 6.92384e-05` | `🟢 7.69295e-05` | `🟢 3.69048e-05` | `🟢 0.000105099` | `🟢 2.32094e-05` | `🔴 0.000335013` | `🟢 0.000149581` | `🟡 0.000141314` |
| `LGBM` | `🟢 0.00229855` | `🟢 2.25836e-05` | `🟢 1.66943e-05` | `🟢 1.45366e-05` | `🟢 2.39831e-05` | `🟢 2.6598e-05` | `🟢 8.48355e-06` | `🔴 0.000187064` | `🟢 8.70423e-05` | `🔴 7.79646e-05` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `2`:

- paper-side values remain the fixed reconstruction target;
- forward and backward repository-side matrices are intentionally reset to
  `pending`;
- smoke-validation runs are structural checks only and do not populate
  benchmark cells.

#### Table 3 - Amplitude RMSE Full-Matrix Replication

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003300 | 7.40e-05 | 1.80e-04 | 1.80e-04 | 9.50e-05 | 3.30e-04 | 1.00e-04 | 8.80e-04 | 0.002200 | 4.70e-04 |
| `MLP` | 0.0140 | 0.0120 | 0.0120 | 0.0100 | 0.0140 | 0.0130 | 0.0150 | 0.0130 | 0.0160 | 0.0100 |
| `RF` | 0.004100 | 3.50e-05 | 3.00e-05 | 3.80e-05 | 3.70e-05 | 5.60e-05 | 1.50e-05 | 1.70e-04 | 2.20e-04 | 5.40e-05 |
| `DT` | 0.004900 | 4.00e-05 | 3.30e-05 | 5.30e-05 | 4.50e-05 | 8.20e-05 | 1.80e-05 | 2.00e-04 | 1.70e-04 | 1.10e-04 |
| `ET` | 0.004500 | 4.20e-05 | 3.50e-05 | 5.10e-05 | 4.30e-05 | 8.50e-05 | 2.70e-05 | 1.90e-04 | 3.80e-04 | 1.80e-04 |
| `ERT` | 0.004000 | 3.70e-05 | 3.40e-05 | 4.00e-05 | 3.60e-05 | 5.70e-05 | 1.60e-05 | 1.30e-04 | 1.60e-04 | 4.20e-05 |
| `GBM` | 0.004000 | 3.60e-05 | 3.10e-05 | 3.90e-05 | 3.90e-05 | 5.50e-05 | 1.60e-05 | 1.70e-04 | 2.20e-04 | 4.70e-05 |
| `HGBM` | 0.003400 | 3.60e-05 | 2.50e-05 | 3.20e-05 | 3.80e-05 | 4.50e-05 | 1.60e-05 | 2.50e-04 | 5.00e-04 | 7.40e-05 |
| `XGBM` | 0.003500 | 7.10e-05 | 1.00e-04 | 1.30e-04 | 8.70e-05 | 1.50e-04 | 6.00e-05 | 5.40e-04 | 7.50e-04 | 2.10e-04 |
| `LGBM` | 0.003500 | 3.70e-05 | 2.60e-05 | 3.30e-05 | 3.80e-05 | 4.60e-05 | 1.60e-05 | 2.20e-04 | 4.70e-04 | 6.20e-05 |
<!-- markdownlint-enable MD013 -->

Forward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00296139` | `🟢 6.03741e-05` | `🟢 0.000164272` | `🟢 8.96664e-05` | `🟢 9.16899e-05` | `🟢 0.000183971` | `🟢 8.16855e-05` | `🟢 0.00057808` | `🟢 0.0010278` | `🟢 0.000426407` |
| `MLP` | `🟢 0.00441997` | `🟢 0.0021178` | `🟢 0.00274825` | `🟢 0.00246956` | `🟢 0.00294075` | `🟢 0.00269949` | `🟢 0.00216725` | `🟢 0.00306965` | `🟢 0.00276464` | `🟢 0.00311164` |
| `RF` | `🟢 0.00349851` | `🟢 2.87058e-05` | `🟢 2.51533e-05` | `🟢 3.39759e-05` | `🟢 2.92267e-05` | `🟢 5.18908e-05` | `🟢 1.25482e-05` | `🟢 0.000123423` | `🟢 9.18693e-05` | `🟢 4.42349e-05` |
| `DT` | `🟢 0.0037916` | `🟢 3.51154e-05` | `🟢 2.7134e-05` | `🟢 4.87467e-05` | `🟢 3.77766e-05` | `🟢 6.89225e-05` | `🟢 1.63082e-05` | `🟢 0.000132915` | `🟢 0.000102053` | `🟢 6.12138e-05` |
| `ET` | `🟢 0.00372992` | `🟢 3.87746e-05` | `🟢 2.75335e-05` | `🟢 4.96286e-05` | `🟢 4.00261e-05` | `🟢 7.49928e-05` | `🟢 1.83752e-05` | `🟢 9.85037e-05` | `🟢 8.58138e-05` | `🟢 7.24233e-05` |
| `ERT` | `🟢 0.00317175` | `🟢 2.82282e-05` | `🟢 2.50886e-05` | `🟢 3.32522e-05` | `🟢 2.74003e-05` | `🟢 4.15779e-05` | `🟢 1.17256e-05` | `🟢 3.52818e-05` | `🟢 5.12809e-05` | `🟢 4.03803e-05` |
| `GBM` | `🟢 0.0035555` | `🟢 2.91983e-05` | `🟢 2.24733e-05` | `🟢 3.48576e-05` | `🟢 3.18227e-05` | `🟢 3.97891e-05` | `🟢 1.49892e-05` | `🟢 0.000115821` | `🟢 9.66626e-05` | `🟢 3.64241e-05` |
| `HGBM` | `🟢 0.0030112` | `🟢 2.83106e-05` | `🟢 2.11261e-05` | `🟢 2.87325e-05` | `🟢 2.91001e-05` | `🟢 3.783e-05` | `🟢 1.24157e-05` | `🟢 0.000174311` | `🟢 0.000158348` | `🟢 4.40781e-05` |
| `XGBM` | `🟢 0.00289955` | `🟢 5.79546e-05` | `🟢 9.14248e-05` | `🟢 0.000115491` | `🟢 7.78107e-05` | `🟢 0.000140424` | `🟢 5.66951e-05` | `🟢 0.00038103` | `🟢 0.000196509` | `🟢 0.000179581` |
| `LGBM` | `🟢 0.00287085` | `🟢 3.13631e-05` | `🟢 2.21773e-05` | `🟢 2.82859e-05` | `🟢 3.0187e-05` | `🟢 3.77433e-05` | `🟢 1.44219e-05` | `🟢 0.000207545` | `🟢 0.000335258` | `🟢 4.3523e-05` |
<!-- markdownlint-enable MD013 -->

Backward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00297317` | `🔴 0.00013583` | `🟢 0.000144553` | `🟢 0.000106955` | `🟢 4.84461e-05` | `🟢 0.000134146` | `🟢 4.11811e-05` | `🟢 0.000849184` | `🟢 0.00148789` | `🟢 0.000308034` |
| `MLP` | `🟢 0.00500305` | `🟢 0.00217587` | `🟢 0.00305953` | `🟢 0.00306248` | `🟢 0.00306197` | `🟢 0.0027425` | `🟢 0.00304781` | `🟢 0.00359669` | `🟢 0.00333342` | `🟢 0.0031084` |
| `RF` | `🟢 0.00334782` | `🟢 2.68348e-05` | `🟢 2.33095e-05` | `🟢 2.09622e-05` | `🟢 3.10832e-05` | `🟢 4.61607e-05` | `🟢 1.01763e-05` | `🔴 0.000269695` | `🟢 0.000139798` | `🔴 8.98524e-05` |
| `DT` | `🟢 0.00387706` | `🟢 3.63799e-05` | `🟡 3.62724e-05` | `🟢 2.74815e-05` | `🟢 3.65537e-05` | `🟢 7.22581e-05` | `🟢 1.26956e-05` | `🟢 0.000130625` | `🟢 0.000113406` | `🟡 0.000127643` |
| `ET` | `🟢 0.0037362` | `🟢 3.68429e-05` | `🟡 3.6898e-05` | `🟢 2.74252e-05` | `🟢 3.9828e-05` | `🟢 7.6e-05` | `🟢 1.43082e-05` | `🟡 0.000197998` | `🟢 0.000128692` | `🟢 0.000145861` |
| `ERT` | `🟢 0.00333832` | `🟢 2.5813e-05` | `🟢 2.84382e-05` | `🟢 2.25142e-05` | `🟢 3.34479e-05` | `🟢 4.72119e-05` | `🟢 1.02593e-05` | `🟡 0.000141236` | `🟢 8.91091e-05` | `🔴 0.00012125` |
| `GBM` | `🟡 0.00417315` | `🟢 3.01611e-05` | `🟢 2.74886e-05` | `🟢 2.70105e-05` | `🟢 2.90895e-05` | `🔴 9.02598e-05` | `🟢 1.22017e-05` | `🔴 0.000414926` | `🟢 0.000172889` | `🔴 9.90601e-05` |
| `HGBM` | `🟢 0.002885` | `🟢 2.82635e-05` | `🟢 2.28014e-05` | `🟢 2.09007e-05` | `🟢 3.10076e-05` | `🟢 3.28317e-05` | `🟢 1.12506e-05` | `🔴 0.000691378` | `🟢 0.000174312` | `🔴 0.000128594` |
| `XGBM` | `🟢 0.00272319` | `🔴 0.000106882` | `🟢 9.0386e-05` | `🟢 9.52484e-05` | `🟢 4.83494e-05` | `🟢 0.000139793` | `🟢 2.96543e-05` | `🔴 0.000773105` | `🟢 0.000234227` | `🟢 0.000200511` |
| `LGBM` | `🟢 0.00287786` | `🟢 3.28906e-05` | `🟢 2.59054e-05` | `🟢 2.13157e-05` | `🟢 3.58482e-05` | `🟢 3.59238e-05` | `🟢 1.36578e-05` | `🔴 0.000459123` | `🟢 0.000194276` | `🔴 0.000154784` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `3`:

- paper-side values remain the fixed reconstruction target;
- forward and backward repository-side matrices are intentionally reset to
  `pending`;
- smoke-validation runs are structural checks only and do not populate
  benchmark cells.

#### Table 4 - Phase MAE Full-Matrix Replication

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002200 | 0.0330 | 0.0270 | 0.0610 | 0.1900 | 0.1300 | 1.200 | 0.4900 | 0.4900 |
| `MLP` | 0.007200 | 0.0650 | 0.0620 | 0.0800 | 0.1600 | 0.1500 | 1.900 | 0.7800 | 0.7000 |
| `RF` | 0.002000 | 0.0240 | 0.0280 | 0.0370 | 0.0740 | 0.0530 | 0.5100 | 0.2300 | 0.2500 |
| `DT` | 0.002100 | 0.0300 | 0.0360 | 0.0430 | 0.0900 | 0.0660 | 0.5200 | 0.2000 | 0.2300 |
| `ET` | 0.002400 | 0.0310 | 0.0350 | 0.0510 | 0.0940 | 0.0870 | 0.7100 | 0.2800 | 0.2600 |
| `ERT` | 0.002200 | 0.0270 | 0.0280 | 0.0400 | 0.0760 | 0.0560 | 0.5300 | 0.2000 | 0.2300 |
| `GBM` | 0.002000 | 0.0240 | 0.0300 | 0.0360 | 0.0740 | 0.0530 | 0.5400 | 0.2500 | 0.2900 |
| `HGBM` | 0.001900 | 0.0200 | 0.0210 | 0.0400 | 0.0910 | 0.0570 | 0.7400 | 0.3500 | 0.3600 |
| `XGBM` | 0.001900 | 0.0240 | 0.0320 | 0.0610 | 0.1400 | 0.0910 | 0.9600 | 0.5400 | 0.3900 |
| `LGBM` | 0.001800 | 0.0210 | 0.0210 | 0.0400 | 0.0950 | 0.0550 | 0.7400 | 0.3500 | 0.3400 |
<!-- markdownlint-enable MD013 -->

Forward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00206264` | `🟢 0.0272462` | `🟢 0.0199` | `🟢 0.0475367` | `🟢 0.132166` | `🟢 0.0971196` | `🟢 1.08053` | `🟢 0.387766` | `🟢 0.322142` |
| `MLP` | `🟢 0.00317452` | `🟢 0.0233929` | `🟢 0.0216331` | `🟢 0.0376109` | `🟢 0.0743748` | `🟢 0.0516697` | `🟢 0.658122` | `🟢 0.35434` | `🟢 0.463599` |
| `RF` | `🟢 0.00158251` | `🟢 0.0181623` | `🟢 0.0194139` | `🟢 0.0299737` | `🟢 0.0465618` | `🟢 0.0463556` | `🟢 0.333473` | `🟢 0.131089` | `🟢 0.14954` |
| `DT` | `🟢 0.00196674` | `🟢 0.0231842` | `🟢 0.0227185` | `🟢 0.0365718` | `🟢 0.0525289` | `🟢 0.0537444` | `🟢 0.327853` | `🟢 0.129959` | `🟢 0.141427` |
| `ET` | `🟢 0.00220789` | `🟢 0.0254555` | `🟢 0.0227454` | `🟢 0.0411961` | `🟢 0.064332` | `🟢 0.0565684` | `🟢 0.482571` | `🟢 0.132855` | `🟢 0.174853` |
| `ERT` | `🟢 0.00172458` | `🟢 0.020385` | `🟢 0.0193248` | `🟢 0.0298409` | `🟢 0.0467775` | `🟢 0.0456165` | `🟢 0.375921` | `🟢 0.13894` | `🟢 0.139049` |
| `GBM` | `🟢 0.00167712` | `🟢 0.0227536` | `🟢 0.029536` | `🟢 0.0346363` | `🟢 0.0636816` | `🟢 0.0454351` | `🟢 0.490354` | `🟢 0.236174` | `🟢 0.219106` |
| `HGBM` | `🟢 0.00147875` | `🟢 0.0186126` | `🟢 0.0167981` | `🟢 0.0339588` | `🟢 0.0590081` | `🟢 0.043818` | `🟢 0.47611` | `🟢 0.271985` | `🟢 0.234177` |
| `XGBM` | `🟢 0.00173949` | `🟢 0.0199928` | `🟢 0.022019` | `🟢 0.0471478` | `🟢 0.0931998` | `🟢 0.0688463` | `🟢 0.681762` | `🟢 0.411338` | `🟢 0.305486` |
| `LGBM` | `🟢 0.0016893` | `🟢 0.0190467` | `🟢 0.0183102` | `🟢 0.0379708` | `🟢 0.0756552` | `🟢 0.0537763` | `🟢 0.556185` | `🟢 0.295841` | `🟢 0.298069` |
<!-- markdownlint-enable MD013 -->

Backward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00195786` | `🟢 0.0260747` | `🔴 0.56393` | `🔴 0.119861` | `🟢 0.106436` | `🟢 0.11743` | `🟢 0.34775` | `🟢 0.329799` | `🟡 0.539813` |
| `MLP` | `🟢 0.00318003` | `🟢 0.0200177` | `🔴 0.281941` | `🟡 0.086572` | `🟢 0.0553362` | `🟢 0.0770297` | `🟢 0.157558` | `🟢 0.0767902` | `🟢 0.299699` |
| `RF` | `🟢 0.00148515` | `🟢 0.0202588` | `🔴 0.153195` | `🔴 0.0753753` | `🟢 0.0348443` | `🔴 0.0725617` | `🟢 0.0597704` | `🟢 0.0486596` | `🟢 0.0918517` |
| `DT` | `🟢 0.00174665` | `🟢 0.0223217` | `🔴 0.10863` | `🔴 0.0945902` | `🟢 0.0458503` | `🟡 0.0816804` | `🟢 0.0492645` | `🟢 0.0512655` | `🟢 0.0885101` |
| `ET` | `🟢 0.00164147` | `🟢 0.024494` | `🔴 0.113296` | `🔴 0.0911072` | `🟢 0.045039` | `🟡 0.0961469` | `🟢 0.0653404` | `🟢 0.0534907` | `🟢 0.229348` |
| `ERT` | `🟢 0.00147949` | `🟢 0.0203398` | `🔴 0.136584` | `🔴 0.0743557` | `🟢 0.0386345` | `🔴 0.0715767` | `🟢 0.0461639` | `🟢 0.0420995` | `🟢 0.14226` |
| `GBM` | `🟢 0.00153303` | `🟡 0.0288352` | `🔴 0.344885` | `🔴 0.0870806` | `🟢 0.0501809` | `🔴 0.0846315` | `🟢 0.102615` | `🟢 0.129266` | `🟢 0.185277` |
| `HGBM` | `🟢 0.00146077` | `🟢 0.0176262` | `🔴 0.239677` | `🔴 0.0810616` | `🟢 0.0501669` | `🔴 0.0785164` | `🟢 0.126681` | `🟢 0.0800121` | `🟢 0.266872` |
| `XGBM` | `🟢 0.00179753` | `🟢 0.0166029` | `🔴 0.303307` | `🔴 0.137977` | `🟢 0.0623943` | `🟢 0.0861429` | `🟢 0.157072` | `🟢 0.151022` | `🟢 0.356205` |
| `LGBM` | `🟢 0.00150908` | `🟢 0.0180053` | `🔴 0.268393` | `🔴 0.090958` | `🟢 0.0469313` | `🔴 0.0764587` | `🟢 0.129653` | `🟢 0.0621016` | `🟢 0.243286` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `4`:

- paper-side values remain the fixed reconstruction target;
- forward and backward repository-side matrices are intentionally reset to
  `pending`;
- smoke-validation runs are structural checks only and do not populate
  benchmark cells.

#### Table 5 - Phase RMSE Full-Matrix Replication

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003100 | 0.0420 | 0.0440 | 0.0970 | 0.3200 | 0.2000 | 1.800 | 1.100 | 1.100 |
| `MLP` | 0.0130 | 0.0840 | 0.0770 | 0.1100 | 0.2400 | 0.2200 | 2.200 | 1.200 | 1.100 |
| `RF` | 0.002800 | 0.0330 | 0.0430 | 0.0550 | 0.1600 | 0.0820 | 1.200 | 0.6800 | 0.6300 |
| `DT` | 0.002800 | 0.0420 | 0.0610 | 0.0610 | 0.2000 | 0.1000 | 1.300 | 0.7300 | 0.6700 |
| `ET` | 0.003300 | 0.0460 | 0.0620 | 0.0740 | 0.2300 | 0.1500 | 1.500 | 0.9300 | 0.6800 |
| `ERT` | 0.003600 | 0.0400 | 0.0440 | 0.0600 | 0.1800 | 0.1100 | 1.200 | 0.6400 | 0.5800 |
| `GBM` | 0.002600 | 0.0340 | 0.0450 | 0.0550 | 0.1800 | 0.0840 | 1.300 | 0.7100 | 0.7100 |
| `HGBM` | 0.002500 | 0.0290 | 0.0270 | 0.0600 | 0.1900 | 0.0850 | 1.300 | 0.7000 | 0.7400 |
| `XGBM` | 0.002800 | 0.0330 | 0.0430 | 0.0890 | 0.2300 | 0.1300 | 1.400 | 0.8100 | 0.7600 |
| `LGBM` | 0.002500 | 0.0300 | 0.0280 | 0.0600 | 0.1900 | 0.0820 | 1.300 | 0.7000 | 0.7100 |
<!-- markdownlint-enable MD013 -->

Forward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00288537` | `🟢 0.0362175` | `🟢 0.0307171` | `🟢 0.0686588` | `🟢 0.18991` | `🟢 0.157212` | `🟢 1.56247` | `🟢 0.913507` | `🟢 0.504478` |
| `MLP` | `🟢 0.00387037` | `🟢 0.0320967` | `🟢 0.0313669` | `🟢 0.0548608` | `🟢 0.106545` | `🟢 0.0748398` | `🟢 1.00843` | `🟢 0.687019` | `🟢 0.739707` |
| `RF` | `🟢 0.00211702` | `🟢 0.0248681` | `🟢 0.0286565` | `🟢 0.0482205` | `🟢 0.0864449` | `🟢 0.060343` | `🟢 0.676607` | `🟢 0.438288` | `🟢 0.425903` |
| `DT` | `🟢 0.00242446` | `🟢 0.030571` | `🟢 0.0307026` | `🟢 0.0532294` | `🟢 0.0890493` | `🟢 0.0805034` | `🟢 1.03094` | `🟢 0.629177` | `🟢 0.578067` |
| `ET` | `🟢 0.00306814` | `🟢 0.035136` | `🟢 0.0346159` | `🟢 0.0665412` | `🟢 0.118259` | `🟢 0.0726197` | `🟢 1.36028` | `🟢 0.459432` | `🟢 0.645875` |
| `ERT` | `🟢 0.00250188` | `🟢 0.0275896` | `🟢 0.0279451` | `🟢 0.0466426` | `🟢 0.0964938` | `🟢 0.0622622` | `🟢 0.824318` | `🟢 0.413294` | `🟢 0.349334` |
| `GBM` | `🟢 0.00243444` | `🟢 0.0303319` | `🟢 0.037133` | `🟢 0.04588` | `🟢 0.0988506` | `🟢 0.0594284` | `🟢 0.850627` | `🟢 0.485444` | `🟢 0.440246` |
| `HGBM` | `🟢 0.00211531` | `🟢 0.0246378` | `🟢 0.0219907` | `🟢 0.0551468` | `🟢 0.0950965` | `🟢 0.0618701` | `🟢 0.748709` | `🟢 0.560556` | `🟢 0.499349` |
| `XGBM` | `🟢 0.00233203` | `🟢 0.0308796` | `🟢 0.0330328` | `🟢 0.0632661` | `🟢 0.135906` | `🟢 0.100681` | `🟢 1.09919` | `🟢 0.727396` | `🟢 0.57162` |
| `LGBM` | `🟢 0.00235914` | `🟢 0.0273235` | `🟢 0.0273769` | `🟢 0.0598769` | `🟢 0.133014` | `🟢 0.0819492` | `🟢 1.03984` | `🟢 0.547315` | `🟢 0.469953` |
<!-- markdownlint-enable MD013 -->

Backward repository-owned restart matrix:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.00302093` | `🟢 0.0367106` | `🔴 0.995695` | `🔴 0.173432` | `🟢 0.152783` | `🟢 0.158214` | `🟢 0.662342` | `🟢 0.618167` | `🟡 1.27925` |
| `MLP` | `🟢 0.00394886` | `🟢 0.0251177` | `🔴 0.752583` | `🟡 0.117351` | `🟢 0.0848492` | `🟢 0.106173` | `🟢 0.368369` | `🟢 0.152055` | `🟢 0.473102` |
| `RF` | `🟢 0.00219941` | `🟢 0.029553` | `🔴 0.596752` | `🔴 0.11356` | `🟢 0.0595121` | `🟡 0.097616` | `🟢 0.216907` | `🟢 0.0824429` | `🟢 0.195657` |
| `DT` | `🟢 0.00234214` | `🟢 0.0311835` | `🔴 0.621849` | `🔴 0.142264` | `🟢 0.0785874` | `🟡 0.111159` | `🟢 0.0925728` | `🟢 0.0801539` | `🟢 0.165663` |
| `ET` | `🟢 0.00263308` | `🟢 0.0339203` | `🔴 0.633153` | `🔴 0.125636` | `🟢 0.0780663` | `🟢 0.13548` | `🟢 0.124204` | `🟢 0.0712563` | `🟢 0.510765` |
| `ERT` | `🟢 0.00195305` | `🟢 0.0256952` | `🔴 0.617764` | `🔴 0.105595` | `🟢 0.080009` | `🟢 0.102052` | `🟢 0.0956603` | `🟢 0.0809778` | `🟢 0.497061` |
| `GBM` | `🟢 0.00232457` | `🟡 0.034693` | `🔴 0.73478` | `🔴 0.134991` | `🟢 0.0903153` | `🔴 0.113678` | `🟢 0.202684` | `🟢 0.191873` | `🟢 0.387719` |
| `HGBM` | `🟢 0.00198454` | `🟢 0.0255339` | `🔴 0.707389` | `🔴 0.145841` | `🟢 0.0758641` | `🔴 0.107151` | `🟢 0.201806` | `🟢 0.134257` | `🟢 0.564205` |
| `XGBM` | `🟢 0.00267142` | `🟢 0.0223981` | `🔴 0.61998` | `🔴 0.200606` | `🟢 0.0891048` | `🟢 0.108707` | `🟢 0.236763` | `🟢 0.275683` | `🟢 0.692858` |
| `LGBM` | `🟢 0.00216154` | `🟢 0.0228194` | `🔴 0.654804` | `🔴 0.140965` | `🟢 0.0716468` | `🔴 0.103333` | `🟢 0.257105` | `🟢 0.0882539` | `🟢 0.466785` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `5`:

- paper-side values remain the fixed reconstruction target;
- forward and backward repository-side matrices are intentionally reset to
  `pending`;
- smoke-validation runs are structural checks only and do not populate
  benchmark cells.

#### Supporting Summary Reading Rule

For the clarified bidirectional `Track 1` scope, Tables `2`, `3`, `4`, and `5`
now each carry three aligned surfaces:

- the fixed paper-side reconstruction target;
- the repository-owned `forward` replication matrix;
- the repository-owned `backward` replication matrix.

Canonical reading rule:

- paper-side values remain the immutable benchmark target;
- repository `forward` and `backward` values must be trained, reviewed,
  and accepted independently;
- no smoke-validation artifact may be copied into the canonical
  benchmark matrices;
- a cell becomes non-pending only after the corresponding accepted
  family-target result is available in the repository.

Table `6` remains a useful harmonic-level support summary, but it must not
replace the four matrix readings above.

Closeout maintenance rule:

- every future `Track 1` campaign closeout that changes any accepted
  family best result must refresh all four canonical tables;
- each refresh must update both repository-side direction matrices
  independently;
- the benchmark is not considered synchronized after closeout until the
  paper, `forward`, and `backward` surfaces all reflect the latest
  accepted post-campaign state.

### Track 1 Family Archive Standard

The repository now treats curated `Track 1` family archives as canonical
benchmark assets rather than optional side notes.

Every family that reaches archive-grade `Track 1` closure now follows the
same bidirectional package contract under `models/paper_reference/rcim_track1/`:

- `<direction>/<family>_reference_models/README.md`
- `<direction>/<family>_reference_models/reference_inventory.yaml`
- `<direction>/<family>_reference_models/onnx/amplitude/`
- `<direction>/<family>_reference_models/onnx/phase/`
- `<direction>/<family>_reference_models/python/amplitude/`
- `<direction>/<family>_reference_models/python/phase/`
- `<direction>/<family>_reference_models/data/`
- `<direction>/<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/training_config.snapshot.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/split_manifest.yaml`

Closeout governance rule:

- every future accepted `Track 1` closeout must compare the newly accepted
  target winner against the archived target entry already stored under
  `models/paper_reference/rcim_track1/`;
- when the new closeout improves the accepted target winner, the archive
  entry must be replaced together with its provenance snapshots, dataset
  snapshot manifest, and benchmark references;
- when the accepted target winner does not improve, the existing archive
  entry must be retained unchanged to avoid unnecessary canonical churn.

Planned family rollout under this standard:

- `SVM`
- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The bidirectional original-dataset restart wave is the first closeout that
materializes both `forward` and `backward` archive branches under this
standard.

### SVM Reference Model Inventory

The accepted repository-owned `SVM` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/svm_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/svm_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/svm_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/svm_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/svm_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/svm_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `SVM`
- repository implementation family: `SVR`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `11` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/003_track1_original_dataset_forward_svr_attempt_03.yaml` |
| `backward` | `14` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/010_track1_original_dataset_backward_svr_attempt_10.yaml` |
<!-- markdownlint-enable MD013 -->

### MLP Reference Model Inventory

The accepted repository-owned `MLP` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/mlp_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/mlp_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/mlp_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/mlp_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/mlp_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/mlp_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `MLP`
- repository implementation family: `MLP`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `13` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/006_track1_original_dataset_forward_mlp_attempt_06.yaml` |
| `backward` | `10` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/008_track1_original_dataset_backward_mlp_attempt_08.yaml` |
<!-- markdownlint-enable MD013 -->

### RF Reference Model Inventory

The accepted repository-owned `RF` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/rf_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/rf_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/rf_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/rf_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/rf_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/rf_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `RF`
- repository implementation family: `RF`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `12` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/006_track1_original_dataset_forward_rf_attempt_06.yaml` |
| `backward` | `12` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/002_track1_original_dataset_backward_rf_attempt_02.yaml` |
<!-- markdownlint-enable MD013 -->

### DT Reference Model Inventory

The accepted repository-owned `DT` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/dt_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/dt_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/dt_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/dt_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/dt_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/dt_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `DT`
- repository implementation family: `DT`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `12` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/018_track1_original_dataset_forward_dt_attempt_18.yaml` |
| `backward` | `9` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/002_track1_original_dataset_backward_dt_attempt_02.yaml` |
<!-- markdownlint-enable MD013 -->

### ET Reference Model Inventory

The accepted repository-owned `ET` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/et_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/et_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/et_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/et_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/et_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/et_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `ET`
- repository implementation family: `ET`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `12` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/019_track1_original_dataset_forward_et_attempt_19.yaml` |
| `backward` | `12` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/016_track1_original_dataset_backward_et_attempt_16.yaml` |
<!-- markdownlint-enable MD013 -->

### ERT Reference Model Inventory

The accepted repository-owned `ERT` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/ert_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/ert_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/ert_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/ert_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/ert_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/ert_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `ERT`
- repository implementation family: `ERT`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `10` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/006_track1_original_dataset_forward_ert_attempt_06.yaml` |
| `backward` | `9` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/006_track1_original_dataset_backward_ert_attempt_06.yaml` |
<!-- markdownlint-enable MD013 -->

### GBM Reference Model Inventory

The accepted repository-owned `GBM` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/gbm_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/gbm_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/gbm_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/gbm_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/gbm_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/gbm_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `GBM`
- repository implementation family: `GBM`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `8` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_gbm_attempt_04.yaml` |
| `backward` | `9` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/002_track1_original_dataset_backward_gbm_attempt_02.yaml` |
<!-- markdownlint-enable MD013 -->

### HGBM Reference Model Inventory

The accepted repository-owned `HGBM` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/hgbm_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/hgbm_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/hgbm_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/hgbm_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/hgbm_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/hgbm_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `HGBM`
- repository implementation family: `HGBM`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `11` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/002_track1_original_dataset_forward_hgbm_attempt_02.yaml` |
| `backward` | `10` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/012_track1_original_dataset_backward_hgbm_attempt_12.yaml` |
<!-- markdownlint-enable MD013 -->

### XGBM Reference Model Inventory

The accepted repository-owned `XGBM` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/xgbm_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/xgbm_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/xgbm_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/xgbm_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/xgbm_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/xgbm_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `XGBM`
- repository implementation family: `XGBM`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `11` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_xgbm_attempt_04.yaml` |
| `backward` | `12` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/008_track1_original_dataset_backward_xgbm_attempt_08.yaml` |
<!-- markdownlint-enable MD013 -->

### LGBM Reference Model Inventory

The accepted repository-owned `LGBM` row is now pinned to explicit curated
directional archives rebuilt from the completed original-dataset exact-paper mega
campaign.

<!-- markdownlint-disable MD013 -->
- forward archive root: `models/paper_reference/rcim_track1/forward/lgbm_reference_models`
- backward archive root: `models/paper_reference/rcim_track1/backward/lgbm_reference_models`
- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/reference_inventory.yaml`
- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/lgbm_reference_models/reference_inventory.yaml`
- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/dataset_snapshot_manifest.yaml`
- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/lgbm_reference_models/dataset_snapshot_manifest.yaml`

Selection rule:

- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;
- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;
- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.

Important implementation note:

- paper family name: `LGBM`
- repository implementation family: `LGBM`
- workflow scope: `original_dataset_directional_exact_model_bank`
- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.

Accepted directional target coverage:

| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |
| --- | ---: | --- | --- |
| `forward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |
| `backward` | `19` | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | `1, 3, 39, 40, 78, 81, 156, 162, 240` |

Directional archive snapshot:

| Direction | Unique Source Runs | Representative Source Config |
| --- | ---: | --- |
| `forward` | `13` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_lgbm_attempt_04.yaml` |
| `backward` | `9` | `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/006_track1_original_dataset_backward_lgbm_attempt_06.yaml` |
<!-- markdownlint-enable MD013 -->

### Supporting Harmonic-Wise Offline Result

The latest completed repository-owned harmonic-wise campaign is:

- `track1_extended_overnight_campaign_2026_04_13_13_31_57`

Winning validation summary:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/family_exploration/hgbm/2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run/validation_summary.yaml`

Winning companion report:

- `doc/reports/analysis/validation_checks/track1/harmonic_wise/forward/2026-04-13-15-12-35_paper_reimplementation_rcim_harmonic_wise_track1_hgbm_h01_wide_depth_2_campaign_run_harmonic_wise_comparison_report.md`

Campaign results report:

- `doc/reports/campaign_results/track1/harmonic_wise/forward/2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report.md`

Current best paper-faithful offline result:

- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- feature set: `base_only`
- validation mean percentage error: `9.830%`
- test mean percentage error: `8.707%`
- oracle test mean percentage error: `2.749%`
- current `Target A` status: `not_yet_met`

The repository now also includes a stricter exact-paper validation branch:

- script: `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- config: `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
- scope: recovered `rpm`, `deg`, `tor` inputs; exact `ampl_k` / `phase_k`
  targets; exact family bank; per-target ONNX export
- prepared campaign plan:
  `doc/reports/campaign_plans/track1/exact_paper/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md`
- prepared launcher:
  `scripts/campaigns/track1/exact_paper/run_exact_paper_model_bank_campaign.ps1`
- campaign results report:
  `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md`
- open-cell repair campaign results report:
  `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md`
- `SVM` row final-closure campaign results report:
  `doc/reports/campaign_results/track1/svm/2026-04-14-21-32-55_track1_svm_final_closure_campaign_results_report.md`
- `SVM` row micro-closure campaign results report:
  `doc/reports/campaign_results/track1/svm/2026-04-14-22-04-12_track1_svm_micro_closure_campaign_results_report.md`
- remote `SVR` reference-grid repair campaign results report:
  `doc/reports/campaign_results/track1/svm/2026-04-17-11-00-54_track1_svr_reference_grid_search_repair_campaign_results_report.md`
- exact-faithful `SVM` final-attempt campaign results report:
  `doc/reports/campaign_results/track1/svm/2026-04-17-18-33-39_track1_svm_exact_faithful_final_attempt_campaign_results_report.md`

This exact branch is now implemented, executed, and operationally stabilized.
Its latest paper-closure-first campaign result confirms:

- best campaign bookkeeping run:
  `exact_open_cell_paper_family_reference`
- harmonic-level status improved from `7` partial / `3` open to
  `8` partial / `2` open
- no new numeric paper-target cells were closed

The latest exact-faithful `SVR` follow-up confirms:

- the remote exact-paper launcher is now operational end to end on the LAN node;
- the recovered paper-faithful `SVR` grid still does not close scoped targets
  `40`, `240`, or `162`;
- the final exact-faithful reruns reproduce the already known exact-paper
  `SVR` values instead of improving them;
- scoped `SVR` ONNX export remains open under the current stack.

Repository decision after the final exact-faithful closeout:

- the `SVM` model line is now considered closed for repository purposes;
- the remaining differences against the paper on `40`, `240`, and `162` are
  accepted as small residual mismatches rather than an active `SVM`
  implementation blocker;
- `Track 1` canonical paper replication remains a broader benchmark topic and
  should not be read as a still-open request to rerun the same exact-faithful
  `SVM` path again.

Its promoted full-bank structural reference run is:

- `exact_full_bank_strict_reference`

with:

- winning family `RF`
- winner mean component MAPE `18.369%`
- `200` exported ONNX files
- `0` failed exports

Important scope boundary:

- this exact branch validates recovered-family fitting and per-target ONNX
  export stability;
- it is the canonical closure source for `Track 1` table replication;
- the harmonic-wise TE-curve benchmark remains a supporting diagnostic branch
  for `Target A`, not the primary `Track 1` completion gate.

What the second iteration established:

- the full RCIM set still outperforms all reduced harmonic subsets;
- the engineered operating-condition features did not improve the full-RCIM
  branch in this campaign;
- the reduced subsets `0,1,39` and `0,1,39,40` are weak final targets because
  even their truncation-only oracle stays above `4.7%`;
- the main remaining gap is now better localized to predictor design,
  especially the dominant `h0` term and a smaller late-harmonic cluster.

What the extended overnight campaign added:

- the shared offline evaluator now has a new promoted winner:
  `track1_hgbm_h01_wide_depth_2`;
- the best harmonic-wise result improved from `8.774%` to `8.707%`;
- the strongest companion direction in the same batch is
  `track1_hgbm_h01_h162240_joint_balanced` at `8.720%`;
- the strongest isolated late-repair direction is
  `track1_hgbm_h81156162240_cluster` at `8.778%`;
- the heavy low-order escalation did not beat the lighter wide winner;
- `RandomForest` and engineered-feature retries still did not justify
  promotion over the best no-engineering `HGBM` variants.

Immediate next repository step:

- keep the full RCIM harmonic set as the mainline `Track 1` target;
- use the exact-paper report to define the open-cell repair queue first;
- use the harmonic-wise branch only to support that repair queue, especially
  around:
  - `track1_hgbm_h01_wide_depth_2`;
  - `track1_hgbm_h01_h162240_joint_balanced`;
  - `track1_hgbm_h81156162240_cluster`;
- the final exact-faithful rerun has now confirmed plateau on the residual
  `SVM` cells, so the next research step should move to a new
  target-parameterization implementation rather than another winner-centric
  tuning cycle.

Important interpretation:

- the repository now has both a completed extended harmonic-wise `Track 1`
  campaign and a completed exact-paper family-bank stabilization campaign;
- the best harmonic-wise result improved from `9.403%` to `8.707%`, so the
  branch is moving in the right direction;
- the paper threshold of `4.7%` remains substantially unmet, so the repository
  is still only partially aligned with the paper offline.

### Current Comparison Verdict

<!-- markdownlint-disable MD013 -->
| Comparison Axis | Current Repository Status | Verdict |
| --- | --- | --- |
| Offline winner family direction | Supporting-only harmonic direction evidence remains available, but it is not the canonical `Track 1` closure surface | supporting_only |
| Track 1 table replication | Canonical `Track 1` status is now read only through the four full-matrix replication tables and the `10 x 19` family-bank completion rule; the full surface is still not fully green | comparable_but_not_yet_matching |
| Track 1.5 harmonic-wise support branch | Held-out mean percentage error is available at `8.707%`, still above the paper threshold `4.7%`, but this no longer defines canonical `Track 1` status | supporting_only_not_yet_matching |
| Online compensation benchmark | missing | not yet comparable |
| End-to-end paper replication | missing | not yet comparable |
<!-- markdownlint-enable MD013 -->

## Online Compensation Tracking

This section is intentionally prepared now and must be updated as soon as the
repository implements online compensation tests.

### Repository Online Results

- Status: `not yet available`
- Required future fields:
  - robot profile uncompensated TE RMS and TE max;
  - robot profile compensated TE RMS and TE max;
  - robot profile reduction percentages;
  - cycloidal profile uncompensated TE RMS and TE max;
  - cycloidal profile compensated TE RMS and TE max;
  - cycloidal profile reduction percentages;
  - exact harmonic set used in each online test;
  - execution path used for the test.

### Online Comparison Rule

Once repository-owned online compensation tests exist, update both:

- this report;
- `doc/reports/analysis/Training Results Master Summary.md`

At that point the project can present a real `paper vs repository` end-to-end
comparison instead of the current offline-only comparison.

## Missing Pipeline For A Real Table 9 Comparison

The exact missing pipeline is:

1. a repository-owned harmonic-wise prediction workflow that outputs the same
   practical quantities used in the paper, namely amplitude and phase terms for
   selected harmonics across operating conditions;
2. a TE reconstruction workflow from those predicted harmonic components;
3. a motion-profile playback workflow for the `Robot` and `Cycloidal` style
   profiles used as the final benchmark;
4. an online compensation loop that applies the reconstructed TE correction
   during motion execution rather than only offline evaluation;
5. a measurement and reporting path that records uncompensated versus
   compensated TE RMS and TE max in a Table 9 style format;
6. a repository-owned final comparison report that states whether `Target A`
   and `Target B` were met.

Until those six pieces exist, the repository results remain strong offline
training results, but not yet a true reproduction of the paper benchmark.

## Implementation Priority

### Implement Now

- complete the remaining open cells in the four `Track 1` full-matrix
  replication tables
- preserve and audit the `10 x 19` exact-paper family-bank inventory
- keep the canonical benchmark and family archives synchronized with accepted
  family-bank results
- repository-owned shared offline evaluator for direct-TE model families under
  the same final TE-curve percentage-error protocol
- evaluation of current best direct-TE families under that shared evaluator
- reporting that keeps exact-paper family-bank and direct-TE result-level
  comparisons separate

These items belong to the immediate repository branch because they define the
canonical exact-paper replication surface before the later support and online
branches.

The postponed harmonic-wise work should now be read as `Track 1.5`, not as the
canonical `Track 1` implementation branch.

### Implement Later

- online compensation loop execution in the future TestRig / online branch
- uncompensated vs compensated `TE RMS` and `TE max` measurement
- final `Table 9` style benchmark report to close `Target B`

These items should be treated as the follow-up online branch, not as the first
implementation step, because they only become trustworthy once the offline
harmonic prediction and reconstruction stack is already stable.

The future `Wave 2` temporal-model branch also stays in the roadmap, but it is
no longer blocked by harmonic-wise work being treated as canonical `Track 1`.
`Track 1.5` can proceed later as a separate support branch.

## Sources

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `output/registries/program/current_best_solution.yaml`
