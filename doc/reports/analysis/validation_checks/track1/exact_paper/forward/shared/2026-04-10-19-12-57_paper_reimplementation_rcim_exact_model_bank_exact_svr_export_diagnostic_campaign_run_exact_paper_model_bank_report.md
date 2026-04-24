# Exact RCIM Paper Model-Bank Validation Report

## Overview

This report summarizes one repository-owned validation run of the
exact paper-faithful RCIM family bank reconstructed from the recovered
paper assets.

- model family: `paper_reimplementation_rcim_exact_model_bank`;
- model type: `exact_paper_family_bank`;
- run name: `exact_svr_export_diagnostic`;
- output run name: `exact_svr_export_diagnostic_campaign_run`;
- run instance id: `2026-04-10-19-12-57__exact_svr_export_diagnostic_campaign_run`;
- source dataframe: `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`;
- enabled families: `SVR`;

## Dataset Scope

- filtered row count: `969`;
- feature schema: `rpm, deg, tor`;
- target count: `20`;
- train rows: `775`;
- test rows: `194`;
- maximum `deg` filter: `35.0`;

## Winner Summary

- winning family: `SVR`;
- winning estimator: `SVR`;
- winning mean component MAPE: `103.265%`;
- winning mean component MAE: `0.138346`;
- winning mean component RMSE: `0.248620`;

## Family Ranking

| Rank | Family | Estimator | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `SVR` | `SVR` | 103.265 | 0.138346 | 0.248620 |

## Target-Winner Registry

| Target | Winning Family | Estimator | MAPE [%] | MAE | RMSE |
| --- | --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | `SVR` | 11.855 | 0.002659 | 0.003918 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | `SVR` | 0.310 | 0.000053 | 0.000070 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | `SVR` | 21.840 | 0.000157 | 0.000179 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | `SVR` | 15.075 | 0.000149 | 0.000178 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | `SVR` | 10.097 | 0.000082 | 0.000096 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | `SVR` | 37.240 | 0.000252 | 0.000315 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | `SVR` | 34.124 | 0.000094 | 0.000104 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | `SVR` | 225.194 | 0.000495 | 0.001107 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | `SVR` | 125.798 | 0.000682 | 0.002181 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | `SVR` | 68.068 | 0.000305 | 0.000572 |
| `fft_y_Fw_filtered_phase_0` | `SVR` | `SVR` | 0.000 | 0.000000 | 0.000000 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | `SVR` | 30.371 | 0.002481 | 0.003851 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | `SVR` | 1.792 | 0.032275 | 0.041559 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | `SVR` | 2.180 | 0.026820 | 0.051155 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | `SVR` | 71.008 | 0.057269 | 0.093671 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | `SVR` | 1180.277 | 0.189246 | 0.313926 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | `SVR` | 14.280 | 0.123017 | 0.194313 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | `SVR` | 122.219 | 1.088104 | 1.636588 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | `SVR` | 27.256 | 0.542212 | 1.217816 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | `SVR` | 66.312 | 0.700564 | 1.410798 |

## ONNX Export Surface

- export enabled: `True`;
- export root: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/baseline_reproduction/shared/2026-04-10-19-12-57__exact_svr_export_diagnostic_campaign_run/onnx_export`;
- exported file count: `20`;
- export failure mode: `continue`;
- recovered reference file count: `201`;
- matched relative paths: `0`;
- missing against recovered reference: `201`;
- extra exported relative paths: `20`;
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
