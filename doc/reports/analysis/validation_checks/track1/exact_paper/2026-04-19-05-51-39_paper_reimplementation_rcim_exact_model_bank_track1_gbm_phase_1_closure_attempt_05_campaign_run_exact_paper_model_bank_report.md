# Exact RCIM Paper Model-Bank Validation Report

## Overview

This report summarizes one repository-owned validation run of the
exact paper-faithful RCIM family bank reconstructed from the recovered
paper assets.

- model family: `paper_reimplementation_rcim_exact_model_bank`;
- model type: `exact_paper_family_bank`;
- run name: `track1_gbm_phase_1_closure_attempt_05`;
- output run name: `track1_gbm_phase_1_closure_attempt_05_campaign_run`;
- run instance id: `2026-04-19-05-51-26__track1_gbm_phase_1_closure_attempt_05_campaign_run`;
- source dataframe: `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`;
- enabled families: `GBM`;
- target scope mode: `phases_only`;

## Dataset Scope

- filtered row count: `969`;
- feature schema: `rpm, deg, tor`;
- target count: `1`;
- target schema kind: `phase_exact_paper`;
- included phase `0`: `False`;
- train rows: `823`;
- test rows: `146`;
- maximum `deg` filter: `35.0`;

## Winner Summary

- winning family: `GBM`;
- winning estimator: `GradientBoostingRegressor`;
- winning search mode: `paper_reference_grid_search`;
- winning best params: `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 68}`;
- winning mean component MAPE: `21.930%`;
- winning mean component MAE: `0.001878`;
- winning mean component RMSE: `0.002480`;

## Training Strategy

- hyperparameter search mode: `paper_reference_grid_search`;
- grid-search `n_jobs`: `24`;
- grid-search `pre_dispatch`: `24`;

### Family Search Summary

| Family | Search Mode | CV Folds | Best Score | Best Params |
| --- | --- | ---: | ---: | --- |
| `GBM` | `paper_reference_grid_search` | 5 | 0.734996 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 68}` |

## Family Ranking

| Rank | Family | Estimator | Search Mode | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `GBM` | `GradientBoostingRegressor` | `paper_reference_grid_search` | 21.930 | 0.001878 | 0.002480 |

## Target-Winner Registry

| Target | Winning Family | Estimator | MAPE [%] | MAE | RMSE |
| --- | --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_phase_1` | `GBM` | `GradientBoostingRegressor` | 21.930 | 0.001878 | 0.002480 |

## Paper-Target Comparison

This section serializes the current `paper vs repository` comparison
for each exact-paper target at the family-direction level. The stricter
numeric table replication is reported in the canonical table sections
below.

| Target | Paper Expected Family | Repository Winner | Repo MAPE [%] | Family Direction Status |
| --- | --- | --- | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `RF / LGBM` | `GBM` | 21.930 | `not_matched_expected_family_direction` |

## Paper-Harmonic Comparison

This section collapses the amplitude and phase target evidence into one
harmonic-facing status so `Track 1` closure can later be tied to a
single inspectable harmonic table.

| Harmonic | Paper Expected Family | Ampl Winner | Phase Winner | Matching Targets | Harmonic Status |
| ---: | --- | --- | --- | ---: | --- |
| `1` | `RF / LGBM` | `-` | `GBM` | 0/1 | `no_family_direction_match` |

## Canonical Table 3 Comparison

This table mirrors paper Table 3 for amplitude RMSE and adds the
repository best-achieved RMSE per harmonic together with the remaining
numeric gap against the paper target.

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
| `Repo Best Family` | - | - | - | - | - | - | - | - | - | - |
| `Repo Best RMSE` | - | - | - | - | - | - | - | - | - | - |
| `Paper Best Family` | - | - | - | - | - | - | - | - | - | - |
| `Paper Target RMSE` | - | - | - | - | - | - | - | - | - | - |
| `Gap Vs Paper` | - | - | - | - | - | - | - | - | - | - |
| `Status` | - | - | - | - | - | - | - | - | - | - |

## Canonical Table 4 Comparison

This table mirrors paper Table 4 for phase MAE and adds the repository
best-achieved MAE per harmonic together with the remaining numeric gap
against the paper target.

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
| `Repo Best Family` | `GBM` | - | - | - | - | - | - | - | - |
| `Repo Best MAE` | 0.001878 | - | - | - | - | - | - | - | - |
| `Paper Best Family` | `LGBM` | - | - | - | - | - | - | - | - |
| `Paper Target MAE` | 0.001800 | - | - | - | - | - | - | - | - |
| `Gap Vs Paper` | 7.76e-05 | - | - | - | - | - | - | - | - |
| `Status` | `above_paper_target` | - | - | - | - | - | - | - | - |

## Canonical Table 5 Comparison

This table mirrors paper Table 5 for phase RMSE and adds the repository
best-achieved RMSE per harmonic together with the remaining numeric gap
against the paper target.

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
| `Repo Best Family` | `GBM` | - | - | - | - | - | - | - | - |
| `Repo Best RMSE` | 0.002480 | - | - | - | - | - | - | - | - |
| `Paper Best Family` | `HGBM` | - | - | - | - | - | - | - | - |
| `Paper Target RMSE` | 0.002500 | - | - | - | - | - | - | - | - |
| `Gap Vs Paper` | -1.98e-05 | - | - | - | - | - | - | - | - |
| `Status` | `met_paper_target` | - | - | - | - | - | - | - | - |

## Canonical Table 6 Comparison

This table compares the paper-selected top-performing models from Table 6
against the repository best families measured on the current exact-paper
validation split.

| `k` | Paper `A*_k` | Repo Best Ampl RMSE Family | Ampl RMSE Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `-` | `-` | `-` | `LGBM` | `GBM` | `GBM` | `above_paper_target` | `met_paper_target` | `partially_matched_tables_3_6` |

## ONNX Export Surface

- export enabled: `True`;
- export root: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-19-05-51-26__track1_gbm_phase_1_closure_attempt_05_campaign_run/onnx_export`;
- exported file count: `0`;
- export failure mode: `continue`;
- recovered reference file count: `201`;
- matched relative paths: `0`;
- missing against recovered reference: `201`;
- extra exported relative paths: `0`;
- failed exports: `1`;
- surrogate exports: `0`;

## Runtime Dependencies

| Dependency | Version |
| --- | --- |
| `numpy` | `2.4.3` |
| `pandas` | `2.3.3` |
| `scikit-learn` | `1.8.0` |
| `skl2onnx` | `not_installed` |
| `onnxmltools` | `not_installed` |
| `xgboost` | `3.2.0` |
| `lightgbm` | `4.6.0` |

## Interpretation

This validation run is the strict paper-faithful branch of `Track 1`.
Its role is to reproduce the original RCIM family bank with the exact
recovered input schema, target schema, and export surface before any
repository-specific simplification or target-wise winner assembly.

At the current repository state, the workflow now serializes the numeric
targets from paper Tables 3, 4, 5, and the selected-model targets from
Table 6. The training path can also reproduce the recovered paper-side
`GridSearchCV` strategy instead of only fitting the recovered base
estimators directly. The repository can therefore show both the paper thresholds and
the current exact-paper results side by side. `Track 1` still remains
open until those gaps are actually closed on the repository side.
