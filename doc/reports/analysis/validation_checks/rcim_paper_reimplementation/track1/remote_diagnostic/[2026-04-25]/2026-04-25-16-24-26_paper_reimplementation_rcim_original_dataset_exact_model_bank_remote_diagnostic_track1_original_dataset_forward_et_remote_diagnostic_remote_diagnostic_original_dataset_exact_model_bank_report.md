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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `20.818%`
- winning mean component MAE: `0.082981`
- winning mean component RMSE: `0.192891`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 20.818 | 0.082981 | 0.192891 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003323 | 0.004035 | 6.400 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000029 | 0.000037 | 0.170 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002232 | 0.002958 | 48.447 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000026 | 0.000034 | 3.128 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.029417 | 0.038047 | 1.627 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000042 | 0.000065 | 3.525 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.026674 | 0.038848 | 2.291 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000037 | 0.000057 | 4.790 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.044921 | 0.072734 | 83.197 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000064 | 0.000089 | 12.135 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.079773 | 0.179240 | 46.626 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000016 | 0.000022 | 5.099 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.068331 | 0.101651 | 6.808 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000078 | 0.000279 | 18.660 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.494145 | 1.092141 | 25.472 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000055 | 0.000185 | 9.683 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.342556 | 0.975869 | 12.626 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000052 | 0.000096 | 13.178 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.484870 | 1.158546 | 91.671 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_diagnostic/et/2026-04-25_track1_forward_et_remote_diagnostic/001_track1_original_dataset_forward_et_remote_diagnostic.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-23-32__track1_original_dataset_forward_et_remote_diagnostic_remote_diagnostic`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-23-32__track1_original_dataset_forward_et_remote_diagnostic_remote_diagnostic/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-23-32__track1_original_dataset_forward_et_remote_diagnostic_remote_diagnostic/validation_summary.yaml`
