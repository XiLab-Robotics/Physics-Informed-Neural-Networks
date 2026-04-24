# Exact RCIM Paper Model-Bank Validation Report

## Overview

This report summarizes one repository-owned validation run of the
exact paper-faithful RCIM family bank reconstructed from the recovered
paper assets.

- model family: `paper_reimplementation_rcim_exact_model_bank`;
- model type: `exact_paper_family_bank`;
- run name: `exact_full_bank_strict_reference`;
- output run name: `exact_full_bank_strict_reference_campaign_run`;
- run instance id: `2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run`;
- source dataframe: `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`;
- enabled families: `SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM`;

## Dataset Scope

- filtered row count: `969`;
- feature schema: `rpm, deg, tor`;
- target count: `20`;
- train rows: `775`;
- test rows: `194`;
- maximum `deg` filter: `35.0`;

## Winner Summary

- winning family: `RF`;
- winning estimator: `RandomForestRegressor`;
- winning mean component MAPE: `18.369%`;
- winning mean component MAE: `0.056284`;
- winning mean component RMSE: `0.144839`;

## Family Ranking

| Rank | Family | Estimator | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `RF` | `RandomForestRegressor` | 18.369 | 0.056284 | 0.144839 |
| 2 | `HGBM` | `HistGradientBoostingRegressor` | 20.586 | 0.079797 | 0.155340 |
| 3 | `ERT` | `ExtraTreesRegressor` | 21.017 | 0.054424 | 0.139747 |
| 4 | `GBM` | `GradientBoostingRegressor` | 24.343 | 0.062593 | 0.152818 |
| 5 | `DT` | `DecisionTreeRegressor` | 27.419 | 0.063643 | 0.170755 |
| 6 | `LGBM` | `LGBMRegressor` | 32.598 | 0.077943 | 0.155869 |
| 7 | `ET` | `ExtraTreeRegressor` | 35.903 | 0.075773 | 0.178675 |
| 8 | `XGBM` | `XGBRegressor` | 52.299 | 0.109229 | 0.182468 |
| 9 | `SVR` | `SVR` | 103.265 | 0.138346 | 0.248620 |
| 10 | `MLP` | `MLPRegressor` | 1699870741337.933 | 0.212142 | 0.299527 |

## Target-Winner Registry

| Target | Winning Family | Estimator | MAPE [%] | MAE | RMSE |
| --- | --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | `HistGradientBoostingRegressor` | 10.804 | 0.002505 | 0.003699 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | `HistGradientBoostingRegressor` | 0.148 | 0.000025 | 0.000035 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | `HistGradientBoostingRegressor` | 2.321 | 0.000018 | 0.000026 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | `HistGradientBoostingRegressor` | 2.124 | 0.000023 | 0.000032 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | `RandomForestRegressor` | 2.778 | 0.000022 | 0.000033 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | `HistGradientBoostingRegressor` | 8.314 | 0.000025 | 0.000038 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | `ExtraTreesRegressor` | 3.430 | 0.000011 | 0.000019 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | `ExtraTreesRegressor` | 12.812 | 0.000035 | 0.000105 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | `ExtraTreesRegressor` | 7.838 | 0.000045 | 0.000144 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | `ExtraTreesRegressor` | 10.537 | 0.000038 | 0.000072 |
| `fft_y_Fw_filtered_phase_0` | `DT` | `DecisionTreeRegressor` | 0.000 | 0.000000 | 0.000000 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | `HistGradientBoostingRegressor` | 21.061 | 0.001846 | 0.002563 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | `GradientBoostingRegressor` | 1.323 | 0.023757 | 0.034316 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | `HistGradientBoostingRegressor` | 1.628 | 0.020390 | 0.032648 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | `ExtraTreesRegressor` | 48.272 | 0.034522 | 0.054119 |
| `fft_y_Fw_filtered_phase_78` | `RF` | `RandomForestRegressor` | 74.433 | 0.051585 | 0.125012 |
| `fft_y_Fw_filtered_phase_81` | `RF` | `RandomForestRegressor` | 4.324 | 0.047979 | 0.068145 |
| `fft_y_Fw_filtered_phase_156` | `DT` | `DecisionTreeRegressor` | 46.772 | 0.490024 | 1.225761 |
| `fft_y_Fw_filtered_phase_162` | `RF` | `RandomForestRegressor` | 10.098 | 0.230457 | 0.747172 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | `ExtraTreesRegressor` | 19.890 | 0.269941 | 0.757287 |

## ONNX Export Surface

- export enabled: `True`;
- export root: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/baseline_reproduction/shared/2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run/onnx_export`;
- exported file count: `200`;
- export failure mode: `strict`;
- recovered reference file count: `201`;
- matched relative paths: `0`;
- missing against recovered reference: `201`;
- extra exported relative paths: `200`;
- failed exports: `0`;
- surrogate exports: `5`;

## Runtime Dependencies

| Dependency | Version |
| --- | --- |
| `numpy` | `2.3.5` |
| `pandas` | `2.3.3` |
| `scikit-learn` | `1.8.0` |
| `skl2onnx` | `1.20.0` |
| `onnxmltools` | `1.16.0` |
| `xgboost` | `3.2.0` |
| `lightgbm` | `4.6.0` |

## Interpretation

This validation run is the strict paper-faithful branch of `Track 1`.
Its role is to reproduce the original RCIM family bank with the exact
recovered input schema, target schema, and export surface before any
repository-specific simplification or target-wise winner assembly.
