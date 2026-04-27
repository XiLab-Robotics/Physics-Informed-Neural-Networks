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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `28.544%`
- winning mean component MAE: `0.086856`
- winning mean component RMSE: `0.219445`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 28.544 | 0.086856 | 0.219445 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003751 | 0.005208 | 16.034 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000034 | 0.000045 | 0.201 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002320 | 0.003103 | 28.479 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000027 | 0.000053 | 3.375 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.036605 | 0.053801 | 2.043 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000039 | 0.000061 | 3.621 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.032928 | 0.053126 | 2.641 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000033 | 0.000058 | 4.204 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.039745 | 0.064309 | 132.534 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000056 | 0.000075 | 10.918 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.116959 | 0.283484 | 132.827 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000014 | 0.000020 | 4.649 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.053744 | 0.080503 | 5.171 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000103 | 0.000291 | 17.924 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.665638 | 1.487501 | 45.929 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000059 | 0.000183 | 9.846 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.430775 | 1.310668 | 16.159 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000082 | 0.000309 | 93.103 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.267340 | 0.826657 | 12.674 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/013_track1_original_dataset_forward_dt_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-21-12__track1_original_dataset_forward_dt_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-21-12__track1_original_dataset_forward_dt_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-21-12__track1_original_dataset_forward_dt_attempt_13_campaign_validation/validation_summary.yaml`
