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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `16.152%`
- winning mean component MAE: `0.065481`
- winning mean component RMSE: `0.157430`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 16.152 | 0.065481 | 0.157430 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 7}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003248 | 0.004178 | 6.417 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000031 | 0.000042 | 0.179 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002288 | 0.002944 | 33.610 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000024 | 0.000035 | 2.886 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.028340 | 0.042352 | 1.576 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000044 | 0.000060 | 3.908 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.029586 | 0.041957 | 2.543 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000029 | 0.000039 | 3.675 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.039348 | 0.056261 | 55.353 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000061 | 0.000086 | 12.118 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.056179 | 0.097420 | 56.762 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000013 | 0.000018 | 4.321 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.064260 | 0.089296 | 5.947 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000085 | 0.000289 | 21.830 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.690311 | 1.574139 | 39.997 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000109 | 0.000334 | 10.458 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.143929 | 0.593239 | 6.126 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000045 | 0.000071 | 14.285 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.186214 | 0.488405 | 24.898 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/006_track1_original_dataset_forward_dt_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-14-47__track1_original_dataset_forward_dt_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-14-47__track1_original_dataset_forward_dt_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-14-47__track1_original_dataset_forward_dt_attempt_06_campaign_validation/validation_summary.yaml`
