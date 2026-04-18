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

The repository should now keep two explicit offline comparison tracks:

- `Track 1`: paper-faithful harmonic-wise benchmark
- `Track 2`: repository direct-TE comparable benchmark

The first track answers whether the repository can reproduce the paper's own
harmonic-wise logic. The second track answers whether the repository's already
trained direct-TE families can match or beat the paper at the level of final
offline TE-curve prediction quality.

These two tracks must not be merged in reporting. Future paper-comparison
tables should explicitly label each entry as either:

- `paper-faithful harmonic-wise`
- `result-level comparable direct-TE`

### Canonical Track 1 Closure Rule

For `Track 1`, the primary closure criterion is no longer the best campaign
winner under the shared offline evaluator.

The canonical `Track 1` closure rule is now:

- reproduce the paper-facing cells in Tables `2`, `3`, `4`, and `5`;
- track status per harmonic target:
  - `A_k` MAE;
  - `A_k` RMSE;
  - `phi_k` MAE;
  - `phi_k` RMSE;
- track harmonic-level closure from Table `6`;
- treat the harmonic-wise TE-curve evaluator only as supporting evidence.

Repository consequence:

- a harmonic-wise campaign winner may still be useful diagnostically;
- however, it does not close `Track 1` by itself;
- `Track 1` closes only when the canonical exact-paper table comparison shows
  the required paper-table cells as matched.

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
- `doc/reports/analysis/validation_checks/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`

Current exact-paper table-replication status from the canonical benchmark
surface is:

- Table `2` amplitude `MAE`: `2/10` harmonics currently meet or beat the paper
  target;
- Table `3` amplitude `RMSE`: `5/10` harmonics currently meet or beat the
  paper target;
- Table `4` phase `MAE`: `5/9` harmonics currently meet or beat the paper
  target;
- Table `5` phase `RMSE`: `5/9` harmonics currently meet or beat the paper
  target;
- harmonic-level Table `6` closure: `2/10` fully matched, `5/10` partially
  matched, `3/10` not yet matched.

The highest-priority still-open harmonics now remain concentrated around:

- `3`
- `81`
- `156`
- `162`
- `240`

Important interpretation:

- this exact-paper table status is the canonical `Track 1` status;
- a harmonic-wise campaign result can inform which open cells to repair next;
- but it does not replace the table-level closure rule.
- the `2026-04-18` partial remaining-family refresh improved several tree and
  boosting rows, but the harmonic-level Table `6` reading still leaves three
  harmonics structurally open.

### 2026-04-18 Partial Refresh Addendum (Historical Snapshot)

This addendum is the canonical benchmark refresh after the interrupted
remaining-family rerun batch:

- completed refreshed families: `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`
- at that intermediate checkpoint, still pending rerun after the remote terminal
  crash: `XGBM`, `LGBM`
- `SVM` continues to read from the accepted repository reference archive
- supporting report:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report.md`

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
  `doc/reports/campaign_results/track1/exact_paper/2026-04-18-16-34-18_track1_remaining_family_final_closeout_campaign_results_report.md`

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
  `doc/reports/analysis/validation_checks/2026-04-13-22-09-00_paper_reimplementation_rcim_exact_model_bank_exact_open_cell_paper_family_reference_campaign_run_exact_paper_model_bank_report.md`

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

| Harmonic | Paper Best Family | Paper Target MAE | Repo Best Family | Repo Best MAE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0` | `HGBM` | 0.002400 | `XGBM` | 0.002465 | 6.46e-05 | `🟡` |
| `1` | `RF` | 2.40e-05 | `HGBM` | 2.54e-05 | 1.45e-06 | `🟡` |
| `3` | `HGBM` | 1.50e-05 | `HGBM` | 1.82e-05 | 3.21e-06 | `🟡` |
| `39` | `HGBM` | 2.10e-05 | `HGBM` | 2.34e-05 | 2.35e-06 | `🟡` |
| `40` | `ERT` | 2.30e-05 | `RF` | 2.21e-05 | -9.06e-07 | `🟢` |
| `78` | `HGBM` | 2.70e-05 | `LGBM` | 2.46e-05 | -2.41e-06 | `🟢` |
| `81` | `RF` | 1.10e-05 | `ERT` | 1.09e-05 | -1.26e-07 | `🟢` |
| `156` | `ERT` | 1.70e-05 | `ERT` | 3.47e-05 | 1.77e-05 | `🔴` |
| `162` | `ERT` | 2.30e-05 | `ERT` | 4.49e-05 | 2.19e-05 | `🔴` |
| `240` | `ERT` | 2.40e-05 | `GBM` | 3.38e-05 | 9.84e-06 | `🔴` |

Quick read for Table `2`:

- amplitude `MAE` is strongest on `40`, `78`, and `81`;
- the near-closure amplitude `MAE` columns are `0`, `1`, `3`, and `39`;
- the dominant unresolved amplitude `MAE` columns are `156`, `162`, and `240`.

#### Table 3 - Amplitude RMSE

Paper-side repository-owned reconstruction:

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

Repository-side analogous Track 1 table:

| Harmonic | Paper Best Family | Paper Target RMSE | Repo Best Family | Repo Best RMSE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `0` | `SVM` | 0.003300 | `SVM` | 0.003110 | -1.90e-04 | `🟢` |
| `1` | `RF` | 3.50e-05 | `HGBM` | 3.52e-05 | 1.76e-07 | `🟢` |
| `3` | `HGBM` | 2.50e-05 | `HGBM` | 2.57e-05 | 7.42e-07 | `🟡` |
| `39` | `HGBM` | 3.20e-05 | `HGBM` | 3.17e-05 | -3.47e-07 | `🟢` |
| `40` | `ERT` | 3.60e-05 | `RF` | 3.28e-05 | -3.24e-06 | `🟢` |
| `78` | `HGBM` | 4.50e-05 | `LGBM` | 3.57e-05 | -9.30e-06 | `🟢` |
| `81` | `RF` | 1.50e-05 | `RF` | 1.82e-05 | 3.22e-06 | `🟡` |
| `156` | `ERT` | 1.30e-04 | `ERT` | 1.05e-04 | -2.46e-05 | `🟢` |
| `162` | `ERT` | 1.60e-04 | `ERT` | 1.44e-04 | -1.64e-05 | `🟢` |
| `240` | `ERT` | 4.20e-05 | `RF` | 5.47e-05 | 1.27e-05 | `🔴` |

#### Table 4 - Phase MAE

Paper-side repository-owned reconstruction:

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

Repository-side analogous Track 1 table:

| Harmonic | Paper Best Family | Paper Target MAE | Repo Best Family | Repo Best MAE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `1` | `LGBM` | 0.001800 | `HGBM` | 0.001846 | 4.64e-05 | `🟡` |
| `3` | `HGBM` | 0.0200 | `GBM` | 0.0238 | 0.003757 | `🟡` |
| `39` | `HGBM` | 0.0210 | `LGBM` | 0.0204 | -6.25e-04 | `🟢` |
| `40` | `GBM` | 0.0360 | `ERT` | 0.0345 | -0.001478 | `🟢` |
| `78` | `GBM` | 0.0740 | `RF` | 0.0516 | -0.0224 | `🟢` |
| `81` | `GBM` | 0.0530 | `LGBM` | 0.0475 | -0.005526 | `🟢` |
| `156` | `RF` | 0.5100 | `ERT` | 0.3967 | -0.1133 | `🟢` |
| `162` | `DT` | 0.2000 | `ERT` | 0.2125 | 0.0125 | `🟡` |
| `240` | `DT` | 0.2300 | `ERT` | 0.2699 | 0.0399 | `🟡` |

#### Table 5 - Phase RMSE

Paper-side repository-owned reconstruction:

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

Repository-side analogous Track 1 table:

| Harmonic | Paper Best Family | Paper Target RMSE | Repo Best Family | Repo Best RMSE | Gap Vs Paper | Status |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| `1` | `HGBM` | 0.002500 | `GBM` | 0.002510 | 1.01e-05 | `🟡` |
| `3` | `HGBM` | 0.0290 | `HGBM` | 0.0343 | 0.005302 | `🟡` |
| `39` | `HGBM` | 0.0270 | `HGBM` | 0.0326 | 0.005648 | `🟡` |
| `40` | `GBM` | 0.0550 | `ERT` | 0.0541 | -8.81e-04 | `🟢` |
| `78` | `RF` | 0.1600 | `RF` | 0.1250 | -0.0350 | `🟢` |
| `81` | `LGBM` | 0.0820 | `RF` | 0.0681 | -0.0139 | `🟢` |
| `156` | `ERT` | 1.200 | `ERT` | 0.9129 | -0.2871 | `🟢` |
| `162` | `ERT` | 0.6400 | `ERT` | 0.7186 | 0.0786 | `🟡` |
| `240` | `ERT` | 0.5800 | `ERT` | 0.7573 | 0.1773 | `🔴` |

#### Table 6 - Harmonic Closure Summary

Paper-side repository-owned reconstruction:

| `k` | Paper `A*_k` | Paper `phi*_k` |
| ---: | --- | --- |
| `0` | `SVM` | `-` |
| `1` | `RF` | `LGBM` |
| `3` | `HGBM` | `HGBM` |
| `39` | `HGBM` | `HGBM` |
| `40` | `ERT` | `GBM` |
| `78` | `HGBM` | `RF` |
| `81` | `RF` | `RF` |
| `156` | `ERT` | `RF` |
| `162` | `ERT` | `ERT` |
| `240` | `ERT` | `ERT` |

Repository-side analogous Track 1 table:

| `k` | Paper `A*_k` | Repo Best Ampl Family | Ampl Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status | Overall Color |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `SVM` | `SVM` | `met_paper_target` | `-` | `ERT` | `ERT` | `not_applicable` | `not_applicable` | `fully_matched_tables_3_6` | `🟢` |
| `1` | `RF` | `HGBM` | `above_paper_target` | `LGBM` | `HGBM` | `GBM` | `above_paper_target` | `above_paper_target` | `not_yet_matched_tables_3_6` | `🔴` |
| `3` | `HGBM` | `HGBM` | `above_paper_target` | `HGBM` | `GBM` | `HGBM` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `39` | `HGBM` | `HGBM` | `met_paper_target` | `HGBM` | `LGBM` | `HGBM` | `met_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `40` | `ERT` | `RF` | `met_paper_target` | `GBM` | `ERT` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `78` | `HGBM` | `LGBM` | `met_paper_target` | `RF` | `RF` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `81` | `RF` | `RF` | `above_paper_target` | `RF` | `LGBM` | `RF` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `156` | `ERT` | `ERT` | `met_paper_target` | `RF` | `ERT` | `ERT` | `met_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `162` | `ERT` | `ERT` | `met_paper_target` | `ERT` | `ERT` | `ERT` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` | `🟡` |
| `240` | `ERT` | `RF` | `above_paper_target` | `ERT` | `ERT` | `ERT` | `above_paper_target` | `above_paper_target` | `partially_matched_tables_3_6` | `🟡` |

Current dashboard reading:

- fully green harmonics: none yet
- partial yellow harmonics: `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240`
- fully red harmonics: `0`, `1`

This means `Track 1` is closer to structural closure than before, but still
blocked by:

- the low-order amplitude and phase pair at `1`;
- the structural amplitude mismatch at `0`;
- the late-phase numeric gaps at `162` and `240`;
- and the still-open phase-side gap at `3`.

### Canonical Track 1 Dashboard: Full Paper-Matrix Replication

This dashboard is now the canonical first-reading surface for the clarified
first objective of `Track 1`:

- reproduce the paper matrices family by family;
- keep the exact paper model rows intact;
- read campaign progress as row replication, not only as best-envelope closure.

Current repository evidence source for the full matrices:

- latest full-matrix row-reproduction campaign:
  `track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51`
- execution window:
  `2026-04-14 14:12:14+02:00` to `2026-04-14 14:15:18+02:00`
- supporting campaign report:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-14-14-35-29_track1_full_matrix_family_reproduction_campaign_results_report.md`

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

Repository-side analogous matrix:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.002503` | `🟢 5.31e-05` | `🟢 1.57e-04` | `🟢 1.49e-04` | `🟡 8.20e-05` | `🟢 2.52e-04` | `🟢 8.23e-05` | `🟢 3.94e-04` | `🟢 6.82e-04` | `🟢 2.52e-04` |
| `MLP` | `🟡 0.010615` | `🔴 0.008904` | `🔴 0.009453` | `🔴 0.007449` | `🟡 0.006993` | `🟢 0.007089` | `🟡 0.00879` | `🟡 0.007806` | `🟢 0.007446` | `🔴 0.008946` |
| `RF` | `🟡 0.003085` | `🟡 2.58e-05` | `🟢 1.90e-05` | `🟢 2.81e-05` | `🟢 2.21e-05` | `🟡 3.91e-05` | `🟡 1.13e-05` | `🟡 6.00e-05` | `🟢 5.67e-05` | `🟡 3.56e-05` |
| `DT` | `🟡 0.00352` | `🟡 3.00e-05` | `🟡 2.33e-05` | `🟢 3.81e-05` | `🟢 2.91e-05` | `🟢 5.74e-05` | `🟡 1.51e-05` | `🔴 8.44e-05` | `🟡 7.33e-05` | `🟢 4.53e-05` |
| `ET` | `🟡 0.003583` | `🟡 3.19e-05` | `🟢 2.31e-05` | `🟢 3.26e-05` | `🟢 2.87e-05` | `🟡 6.23e-05` | `🟢 1.45e-05` | `🔴 8.44e-05` | `🟢 6.95e-05` | `🟢 4.78e-05` |
| `ERT` | `🟡 0.003206` | `🟢 2.42e-05` | `🟢 2.12e-05` | `🟢 2.74e-05` | `🟢 2.23e-05` | `🟡 3.89e-05` | `🟢 1.13e-05` | `🔴 5.03e-05` | `🔴 5.41e-05` | `🔴 3.71e-05` |
| `GBM` | `🟡 0.003237` | `🟡 2.71e-05` | `🟢 1.88e-05` | `🟢 2.68e-05` | `🟢 2.55e-05` | `🟡 3.92e-05` | `🟢 1.15e-05` | `🟡 6.34e-05` | `🟡 7.24e-05` | `🟡 3.38e-05` |
| `HGBM` | `🟡 0.002512` | `🟢 2.57e-05` | `🟡 1.83e-05` | `🟡 2.30e-05` | `🟢 2.41e-05` | `🟢 2.47e-05` | `🟢 1.19e-05` | `🟡 1.01e-04` | `🟢 1.39e-04` | `🟡 4.06e-05` |
| `XGBM` | `🟢 0.002465` | `🟢 5.29e-05` | `🟢 7.21e-05` | `🟢 9.31e-05` | `🟢 6.44e-05` | `🟡 1.17e-04` | `🟡 4.66e-05` | `🟡 2.74e-04` | `🟢 2.21e-04` | `🔴 1.87e-04` |
| `LGBM` | `🟢 0.002490` | `🟢 2.39e-05` | `🟢 1.72e-05` | `🟢 2.27e-05` | `🟢 2.52e-05` | `🟢 2.56e-05` | `🟡 1.21e-05` | `🟡 1.07e-04` | `🟢 1.52e-04` | `🔴 4.71e-05` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `2`:

- amplitude `MAE` is strongest row-wise on `RF`, `HGBM`, `XGBM`, and `LGBM`;
- the hardest amplitude `MAE` columns remain `156`, `162`, and `240`;
- `40`, `78`, and `81` are the healthiest amplitude `MAE` columns.

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

Repository-side analogous matrix:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.003110` | `🟢 7.01e-05` | `🟢 1.79e-04` | `🟢 1.78e-04` | `🟡 9.63e-05` | `🟢 3.15e-04` | `🟢 9.39e-05` | `🟢 8.06e-04` | `🟢 0.002181` | `🟡 4.86e-04` |
| `MLP` | `🟡 0.014081` | `🔴 0.015569` | `🔴 0.015451` | `🔴 0.012642` | `🟢 0.012067` | `🟢 0.012007` | `🟡 0.015045` | `🟢 0.012676` | `🟢 0.012974` | `🔴 0.016513` |
| `RF` | `🟡 0.004143` | `🟡 3.61e-05` | `🟢 2.75e-05` | `🟡 3.84e-05` | `🟢 3.28e-05` | `🟡 5.87e-05` | `🟡 1.85e-05` | `🔴 2.21e-04` | `🟢 1.65e-04` | `🟡 5.58e-05` |
| `DT` | `🟢 0.00488` | `🟡 4.19e-05` | `🟡 3.34e-05` | `🟢 5.24e-05` | `🟢 4.07e-05` | `🟡 8.23e-05` | `🔴 2.34e-05` | `🔴 2.84e-04` | `🟡 2.11e-04` | `🟢 6.86e-05` |
| `ET` | `🟡 0.004656` | `🟡 4.23e-05` | `🟡 3.56e-05` | `🟢 4.39e-05` | `🟢 4.21e-05` | `🟡 9.59e-05` | `🟢 2.30e-05` | `🔴 2.92e-04` | `🟢 2.33e-04` | `🟢 7.39e-05` |
| `ERT` | `🟡 0.004149` | `🟢 3.44e-05` | `🟢 3.17e-05` | `🟢 3.83e-05` | `🟢 3.27e-05` | `🟢 5.57e-05` | `🟡 1.90e-05` | `🔴 1.85e-04` | `🟡 1.74e-04` | `🔴 6.39e-05` |
| `GBM` | `🟡 0.004261` | `🟡 3.79e-05` | `🟢 2.66e-05` | `🟢 3.80e-05` | `🟢 3.58e-05` | `🟢 5.49e-05` | `🟡 1.88e-05` | `🔴 2.23e-04` | `🟢 2.12e-04` | `🟡 5.81e-05` |
| `HGBM` | `🟡 0.003683` | `🟢 3.51e-05` | `🟡 2.57e-05` | `🟢 3.12e-05` | `🟢 3.35e-05` | `🟢 3.72e-05` | `🟡 1.89e-05` | `🟡 3.01e-04` | `🟢 3.23e-04` | `🟡 8.88e-05` |
| `XGBM` | `🟡 0.003714` | `🟢 6.81e-05` | `🟢 9.07e-05` | `🟢 1.24e-04` | `🟢 8.34e-05` | `🟡 1.59e-04` | `🟢 5.98e-05` | `🔴 7.82e-04` | `🟢 6.77e-04` | `🔴 3.14e-04` |
| `LGBM` | `🟡 0.003652` | `🟢 3.30e-05` | `🟢 2.43e-05` | `🟢 3.07e-05` | `🟢 3.53e-05` | `🟢 3.77e-05` | `🟡 1.88e-05` | `🔴 3.00e-04` | `🟢 3.33e-04` | `🔴 9.27e-05` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `3`:

- strongest amplitude rows are now clearly `ERT`, `HGBM`, and `RF`;
- the hardest amplitude columns remain `156`, `162`, and `240`;
- `MLP` is fully red on the amplitude side and should not be treated as a
  near-closure branch.

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

Repository-side analogous matrix:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.002177` | `🟢 0.0323` | `🟢 0.0224` | `🟢 0.0573` | `🟢 0.1892` | `🟢 0.1230` | `🟢 1.088` | `🟡 0.5030` | `🟢 0.4320` |
| `MLP` | `🔴 0.009958` | `🟡 0.08016` | `🟡 0.06912` | `🟢 0.078778` | `🟡 0.173426` | `🟡 0.165498` | `🟢 1.561696` | `🟡 0.924807` | `🟡 0.755923` |
| `RF` | `🟢 0.001962` | `🟡 0.024853` | `🟢 0.026966` | `🟢 0.036271` | `🟢 0.051208` | `🟢 0.047078` | `🟢 0.412111` | `🟢 0.2235` | `🟡 0.266524` |
| `DT` | `🟡 0.002239` | `🟢 0.02734` | `🟢 0.032261` | `🟡 0.045456` | `🟢 0.07449` | `🟢 0.06362` | `🟢 0.490408` | `🟡 0.245312` | `🟡 0.287325` |
| `ET` | `🟡 0.002943` | `🟡 0.033978` | `🟢 0.032662` | `🟢 0.045719` | `🟡 0.097698` | `🟢 0.069966` | `🟢 0.495464` | `🟢 0.230945` | `🔴 0.349334` |
| `ERT` | `🟡 0.00236` | `🟡 0.028567` | `🟡 0.028394` | `🟢 0.035771` | `🟢 0.061871` | `🟢 0.052236` | `🟢 0.413796` | `🟡 0.244129` | `🔴 0.293955` |
| `GBM` | `🟢 0.001891` | `🟢 0.023747` | `🟢 0.023351` | `🟡 0.038129` | `🟢 0.060491` | `🟢 0.050932` | `🟢 0.470366` | `🟡 0.279863` | `🟡 0.301835` |
| `HGBM` | `🟢 0.001832` | `🟡 0.024833` | `🟢 0.019674` | `🟢 0.039488` | `🟢 0.070595` | `🟢 0.049391` | `🟢 0.604771` | `🟡 0.387796` | `🟡 0.417077` |
| `XGBM` | `🟡 0.002175` | `🟡 0.0254` | `🟢 0.0278` | `🟢 0.0563` | `🟢 0.1105` | `🟢 0.0828` | `🟢 0.8158` | `🟢 0.5035` | `🟡 0.4319` |
| `LGBM` | `🟡 0.001923` | `🟡 0.0256` | `🟢 0.0205` | `🟢 0.0377` | `🟢 0.0724` | `🟢 0.0470` | `🟢 0.6191` | `🟢 0.3461` | `🟡 0.3806` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `4`:

- phase `MAE` is currently the healthiest matrix of the three;
- strongest rows are `RF`, `ERT`, `GBM`, and `HGBM`;
- the hardest columns remain `162` and especially `240`.

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

Repository-side analogous matrix:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `🟢 0.002908` | `🟢 0.0416` | `🟢 0.0350` | `🟢 0.0937` | `🟢 0.3139` | `🟢 0.1943` | `🟢 1.637` | `🟡 1.187` | `🟢 0.9522` |
| `MLP` | `🟡 0.015508` | `🟡 0.102211` | `🟡 0.089884` | `🟡 0.111899` | `🟡 0.257986` | `🟡 0.229632` | `🟢 1.911885` | `🟡 1.484005` | `🟡 1.251619` |
| `RF` | `🟢 0.002673` | `🟡 0.036058` | `🟡 0.048532` | `🟢 0.054572` | `🟢 0.12464` | `🟢 0.065945` | `🟢 0.94371` | `🟡 0.738917` | `🔴 0.83003` |
| `DT` | `🟡 0.003115` | `🟢 0.039113` | `🟢 0.060054` | `🟡 0.070673` | `🟢 0.151314` | `🟢 0.095694` | `🟢 1.225799` | `🟡 0.891606` | `🔴 0.872011` |
| `ET` | `🔴 0.004534` | `🟡 0.048754` | `🟢 0.061545` | `🟢 0.072549` | `🟡 0.280463` | `🟢 0.121725` | `🟢 1.138228` | `🟢 0.804072` | `🔴 1.052265` |
| `ERT` | `🟡 0.003613` | `🟡 0.040508` | `🟡 0.054928` | `🟢 0.056876` | `🟢 0.152952` | `🟢 0.08056` | `🟢 0.914614` | `🟡 0.746667` | `🔴 0.821654` |
| `GBM` | `🟢 0.002492` | `🟡 0.034311` | `🟢 0.040113` | `🟡 0.057144` | `🟢 0.139595` | `🟢 0.075851` | `🟢 1.021755` | `🟡 0.82481` | `🟡 0.857841` |
| `HGBM` | `🟡 0.002556` | `🟡 0.033872` | `🟡 0.032421` | `🟡 0.06039` | `🟢 0.137252` | `🟢 0.072232` | `🟢 1.03757` | `🟡 0.819126` | `🔴 0.927769` |
| `XGBM` | `🟡 0.003325` | `🟡 0.0356` | `🟡 0.0438` | `🟢 0.0846` | `🟢 0.1805` | `🟢 0.1155` | `🟢 1.240` | `🟡 0.9052` | `🟡 0.9103` |
| `LGBM` | `🟡 0.002649` | `🟡 0.0365` | `🟡 0.0323` | `🟢 0.0580` | `🟢 0.1424` | `🟢 0.0670` | `🟢 1.055` | `🟡 0.7981` | `🟡 0.8872` |
<!-- markdownlint-enable MD013 -->

Quick read for Table `5`:

- phase `RMSE` replication is meaningfully harder than phase `MAE`;
- strongest rows are `RF`, `HGBM`, `GBM`, and `ERT`;
- the dominant unresolved columns remain `240` and `162`.

#### Supporting Summary Reading Rule

For the clarified `Track 1` scope, Tables `2`, `3`, `4`, and `5` are the real
paper-matching evaluation surfaces:

- Table `2`: amplitude `A_k` `MAE`
- Table `3`: amplitude `A_k` `RMSE`
- Table `4`: phase `phi_k` `MAE`
- Table `5`: phase `phi_k` `RMSE`

Table `6` remains a useful harmonic-level support summary, but it must not
replace the four matrix readings above.

Closeout maintenance rule:

- every future `Track 1` campaign closeout that changes any accepted family
  best result must refresh both:
  - the best-envelope/addendum summary surfaces above;
  - the family-by-family colored replication matrices for Tables `2-5`;
- the benchmark is not considered synchronized after closeout until the
  numeric cells and the `🟢/🟡/🔴` markers in those four tables reflect the
  latest accepted post-campaign values.

### Track 1 Family Archive Standard

The repository now treats curated `Track 1` family archives as canonical
benchmark assets rather than optional side notes.

Every family that reaches archive-grade `Track 1` closure should follow the
same package contract under `models/paper_reference/rcim_track1/`:

- `<family>_reference_models/README.md`
- `<family>_reference_models/reference_inventory.yaml`
- `<family>_reference_models/onnx/amplitude/`
- `<family>_reference_models/onnx/phase/`
- `<family>_reference_models/python/amplitude/`
- `<family>_reference_models/python/phase/`
- `<family>_reference_models/data/`
- `<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<family>_reference_models/source_runs/<run_instance_id>/training_config.snapshot.yaml`
- `<family>_reference_models/source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- `<family>_reference_models/source_runs/<run_instance_id>/split_manifest.yaml`

Family-section reporting rule for this benchmark:

- each archived family gets one dedicated benchmark section;
- the section must expose archive root, inventory path, and archive note;
- the section must list the accepted harmonic targets for that family;
- each target row must identify accepted metrics, canonical source run, and
  archived deployment path;
- when the deployment export uses a surrogate estimator surface, the section
  must state that explicitly and distinguish it from the original Python-side
  fitted model identity;
- once available, the section should also point to dataset snapshot and full
  reconstruction provenance.

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

The current `SVM` archive is the first fully populated instance of this
standard and should be used as the template for future `Track 1` family
archives.

### SVM Reference Model Inventory

The accepted repository-owned `SVM` row is now pinned to an explicit curated
set of `19` archived model artifacts:

- archive root:
  `models/paper_reference/rcim_track1/svm_reference_models/`
- machine-readable inventory:
  `models/paper_reference/rcim_track1/svm_reference_models/reference_inventory.yaml`
- dedicated archive note:
  `models/paper_reference/rcim_track1/svm_reference_models/README.md`
- dataset snapshot manifest:
  `models/paper_reference/rcim_track1/svm_reference_models/dataset_snapshot_manifest.yaml`

Full regeneration coverage:

- the archive stores both deployment-facing `ONNX` exports and Python-usable
  fitted estimator pickles for the same `19` accepted targets;
- each target entry in `reference_inventory.yaml` now records the exact fitted
  estimator parameters, source bundle path, dataset snapshot hash, feature
  list, target list, train/test row counts, split indices, test size, random
  seed, harmonic filter, and target-scope mode;
- source-run config snapshots and run-metadata snapshots are copied under
  `models/paper_reference/rcim_track1/svm_reference_models/source_runs/`,
  making the accepted `SVM` row reconstructible without relying on implicit
  notebook memory or manual campaign folder inspection.

Selection rule:

- when several runs reproduce the same accepted `SVM` target metrics, the
  repository pins the earliest stable canonical source run;
- the strict full-bank reference run
  `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro`
  is preferred whenever later campaigns only reproduce the same accepted
  target;
- later `Track 1` `SVM` repair and closure runs are pinned only for harmonics
  whose accepted benchmark value improved after the strict baseline.

Important implementation note:

- paper family name: `SVM`
- repository implementation family: `SVR`
- some constant-target exports are serialized as `LinearRegression` surrogate
  ONNX models under the `SVR_*` filename surface
- the archived Python pickle for the same target still preserves the fitted
  `SVR` estimator class and parameters, so the surrogate-only ONNX surface does
  not hide the original Python model identity

#### SVM Reference Amplitude Models

<!-- markdownlint-disable MD013 -->
| Target | Harmonic | Accepted MAE | Accepted RMSE | Source Run | Export Estimator | Surrogate | Archived Model |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.002503271` | `0.003110405` | `2026-04-14-17-31-04__track1_svm_amplitude_repair_seed23_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `5.3106e-05` | `7.0056e-05` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `LinearRegression` | `constant_linear_regression` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `0.000157041` | `0.000178649` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `LinearRegression` | `constant_linear_regression` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `0.000148910` | `0.000177738` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `8.2027e-05` | `9.6333e-05` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `LinearRegression` | `constant_linear_regression` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000251534` | `0.000315282` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `8.2292e-05` | `9.3918e-05` | `2026-04-14-17-30-55__track1_svm_amplitude_repair_seed11_campaign_run` | `LinearRegression` | `constant_linear_regression` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl81.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000394296` | `0.000805795` | `2026-04-14-21-09-51__track1_svm_amplitude_full_closure_split15_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000682326` | `0.002181218` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000252053` | `0.000486252` | `2026-04-14-17-31-04__track1_svm_amplitude_repair_seed23_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/amplitude/SVR_ampl240.onnx` |

#### SVM Reference Phase Models

| Target | Harmonic | Accepted MAE | Accepted RMSE | Source Run | Export Estimator | Surrogate | Archived Model |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.002177289` | `0.002908073` | `2026-04-14-17-31-51__track1_svm_phase_repair_seed11_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase1.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.032275186` | `0.041559254` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.022426698` | `0.035037809` | `2026-04-14-17-31-51__track1_svm_phase_repair_seed11_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.057268799` | `0.093671007` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.189245921` | `0.313926178` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.123016520` | `0.194313454` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase81.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.088103571` | `1.636587809` | `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.502968488` | `1.187302541` | `2026-04-14-21-10-28__track1_svm_phase_final_closure_split15_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.432040657` | `0.952225047` | `2026-04-14-17-31-51__track1_svm_phase_repair_seed11_campaign_run` | `SVR` | `none` | `models/paper_reference/rcim_track1/svm_reference_models/onnx/phase/SVR_phase240.onnx` |
<!-- markdownlint-enable MD013 -->

Reconstruction references:

- baseline strict full-bank config:
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-10_exact_paper_model_bank_campaign/02_exact_full_bank_strict_reference.yaml`
- repair campaign configs:
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_svm_open_cell_repair_campaign/02_track1_svm_amplitude_repair_seed11.yaml`
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_svm_open_cell_repair_campaign/03_track1_svm_amplitude_repair_seed23.yaml`
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_svm_open_cell_repair_campaign/08_track1_svm_phase_repair_seed11.yaml`
- final-closure configs:
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_svm_final_closure_campaign/07_track1_svm_amplitude_full_closure_split15.yaml`
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_svm_final_closure_campaign/11_track1_svm_phase_final_closure_split15.yaml`

### Supporting Harmonic-Wise Offline Result

The latest completed repository-owned harmonic-wise campaign is:

- `track1_extended_overnight_campaign_2026_04_13_13_31_57`

Winning validation summary:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run/validation_summary.yaml`

Winning companion report:

- `doc/reports/analysis/validation_checks/2026-04-13-15-12-35_paper_reimplementation_rcim_harmonic_wise_track1_hgbm_h01_wide_depth_2_campaign_run_harmonic_wise_comparison_report.md`

Campaign results report:

- `doc/reports/campaign_results/track1/harmonic_wise/2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report.md`

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
  `scripts/campaigns/run_exact_paper_model_bank_campaign.ps1`
- campaign results report:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-10-19-54-02_exact_paper_model_bank_campaign_results_report.md`
- open-cell repair campaign results report:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md`
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
| Track 1 table replication | Tables `2-5` now serialized canonically; Table `6` remains the harmonic closure summary; `1/10` harmonics fully closed and `8/10` partially closed | comparable_but_not_yet_matching |
| Supporting harmonic-wise TE metric | Held-out mean percentage error now available at `8.707%`, still above the paper threshold `4.7%` | supporting_only_not_yet_matching |
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

- harmonic-wise prediction of `A_k` and `phi_k`
- TE reconstruction from the predicted harmonic terms
- offline motion-profile playback for `Robot` and `Cycloidal` style profiles
- paper-comparable offline validation protocol to close `Target A`
- repository-owned shared offline evaluator for direct-TE model families under
  the same final TE-curve percentage-error protocol
- evaluation of current best direct-TE families under that shared evaluator
- dual-track reporting that keeps paper-faithful and direct-TE result-level
  comparisons separate

These four items belong to the immediate repository branch because they create
the stable offline baseline that the online branch will later depend on.

This immediate branch should now be read as an explicit intermediate stage
between completed `Wave 1` and the later `Wave 2` temporal-model work.

### Implement Later

- online compensation loop execution in the future TestRig / online branch
- uncompensated vs compensated `TE RMS` and `TE max` measurement
- final `Table 9` style benchmark report to close `Target B`

These items should be treated as the follow-up online branch, not as the first
implementation step, because they only become trustworthy once the offline
harmonic prediction and reconstruction stack is already stable.

The future `Wave 2` temporal-model branch also stays in the roadmap, but it is
no longer the immediate next branch. It should open only after the
harmonic-wise comparison framework is implemented and reviewed.

## Sources

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `output/registries/program/current_best_solution.yaml`
