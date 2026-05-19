# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
- dataset root: `data/datasets`
- dataset config: `config/datasets/transmission_error_dataset.yaml`
- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- decomposition point stride: `1`
- feature schema: `rpm, deg, tor`
- target count: `19`

## Split Summary

- train rows / files: `678` / `678`
- validation rows / files: `194` / `194`
- test rows / files: `97` / `97`
- validation split: `0.2`
- test split: `0.1`
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `14.046%`
- winning mean component MAE: `0.056473`
- winning mean component RMSE: `0.187314`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 14.046 | 0.056473 | 0.187314 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003464 | 0.004362 | 6.611 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000028 | 0.000036 | 0.165 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.001967 | 0.002424 | 48.704 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000026 | 0.000037 | 2.976 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.029205 | 0.037641 | 1.606 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000042 | 0.000066 | 3.437 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.024241 | 0.033453 | 2.120 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000034 | 0.000057 | 4.341 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.056478 | 0.090715 | 59.698 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000067 | 0.000095 | 12.681 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.083981 | 0.255821 | 46.837 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000013 | 0.000018 | 4.091 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.064820 | 0.094113 | 6.006 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000057 | 0.000191 | 13.082 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.327853 | 1.030944 | 13.748 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000064 | 0.000204 | 11.163 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.299880 | 1.175760 | 11.451 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000040 | 0.000059 | 9.454 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.180726 | 0.832976 | 8.694 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_diagnostic/dt/2026-04-25_track1_forward_dt_remote_diagnostic/001_track1_original_dataset_forward_dt_remote_diagnostic.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-22-34__track1_original_dataset_forward_dt_remote_diagnostic_remote_diagnostic`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-22-34__track1_original_dataset_forward_dt_remote_diagnostic_remote_diagnostic/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-22-34__track1_original_dataset_forward_dt_remote_diagnostic_remote_diagnostic/validation_summary.yaml`
