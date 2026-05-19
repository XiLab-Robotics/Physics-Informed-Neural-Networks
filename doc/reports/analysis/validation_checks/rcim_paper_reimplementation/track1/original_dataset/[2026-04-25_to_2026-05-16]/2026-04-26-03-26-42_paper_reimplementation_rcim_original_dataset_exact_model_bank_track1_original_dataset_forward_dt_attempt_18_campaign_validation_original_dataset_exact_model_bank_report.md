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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `107.265%`
- winning mean component MAE: `0.075260`
- winning mean component RMSE: `0.194947`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 107.265 | 0.075260 | 0.194947 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.002977 | 0.003792 | 7.695 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000031 | 0.000048 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002524 | 0.003668 | 1686.182 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000027 | 0.000043 | 3.409 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.036287 | 0.070980 | 1.961 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000035 | 0.000049 | 3.089 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.032880 | 0.058081 | 2.496 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000035 | 0.000052 | 4.448 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.052676 | 0.081727 | 55.309 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000060 | 0.000080 | 14.747 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.103155 | 0.227730 | 115.891 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000014 | 0.000022 | 4.435 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.069673 | 0.124054 | 7.837 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000122 | 0.000402 | 18.243 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.362586 | 0.855373 | 52.303 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000092 | 0.000320 | 12.331 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.338998 | 1.104296 | 15.205 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000041 | 0.000057 | 13.290 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.427719 | 1.173228 | 18.992 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/018_track1_original_dataset_forward_dt_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-25-54__track1_original_dataset_forward_dt_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-25-54__track1_original_dataset_forward_dt_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-25-54__track1_original_dataset_forward_dt_attempt_18_campaign_validation/validation_summary.yaml`
