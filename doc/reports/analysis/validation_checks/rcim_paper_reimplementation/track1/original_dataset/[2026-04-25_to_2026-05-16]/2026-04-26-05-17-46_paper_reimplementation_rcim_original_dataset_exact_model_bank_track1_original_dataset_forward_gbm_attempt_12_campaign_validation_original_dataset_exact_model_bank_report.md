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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `67.031%`
- winning mean component MAE: `0.085615`
- winning mean component RMSE: `0.158424`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 67.031 | 0.085615 | 0.158424 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 16, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003635 | 0.004307 | 7.383 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000030 | 0.000039 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002084 | 0.002811 | 28.618 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000026 | 0.000035 | 3.247 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.027890 | 0.036515 | 1.529 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000046 | 0.000055 | 3.997 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.035222 | 0.050932 | 3.109 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000032 | 0.000049 | 4.130 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.049035 | 0.070121 | 91.651 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000092 | 0.000111 | 14.709 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.073586 | 0.135789 | 853.725 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000015 | 3.687 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.083037 | 0.110391 | 8.409 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000144 | 0.000299 | 78.268 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.717673 | 1.134674 | 41.484 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000123 | 0.000300 | 40.094 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.378339 | 0.890862 | 18.014 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000060 | 0.000097 | 18.402 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.255619 | 0.572653 | 52.961 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/012_track1_original_dataset_forward_gbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-15-49__track1_original_dataset_forward_gbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-15-49__track1_original_dataset_forward_gbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-15-49__track1_original_dataset_forward_gbm_attempt_12_campaign_validation/validation_summary.yaml`
