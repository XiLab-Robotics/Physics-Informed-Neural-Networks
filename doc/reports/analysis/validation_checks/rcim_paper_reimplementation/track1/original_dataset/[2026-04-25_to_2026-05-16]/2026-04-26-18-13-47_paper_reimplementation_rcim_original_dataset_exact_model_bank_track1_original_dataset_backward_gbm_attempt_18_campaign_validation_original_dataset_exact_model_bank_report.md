# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `backward`
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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `36.836%`
- winning mean component MAE: `0.079935`
- winning mean component RMSE: `0.161646`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 36.836 | 0.079935 | 0.161646 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003096 | 0.003953 | 68.132 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000033 | 0.000048 | 0.190 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.002314 | 0.003458 | 45.939 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000041 | 2.673 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.034820 | 0.059098 | 2.662 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000022 | 0.000030 | 4.810 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.363853 | 0.784172 | 13.860 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000028 | 0.000043 | 9.458 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.115517 | 0.173214 | 192.164 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000097 | 0.000116 | 26.473 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.094775 | 0.202417 | 35.807 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000010 | 0.000013 | 8.085 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.122696 | 0.197129 | 127.189 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000394 | 0.001145 | 34.268 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.153637 | 0.258530 | 21.674 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000161 | 0.000275 | 47.589 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.249023 | 0.639537 | 13.611 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000090 | 0.000155 | 25.895 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.378176 | 0.747896 | 19.410 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/018_track1_original_dataset_backward_gbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-11-52__track1_original_dataset_backward_gbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-11-52__track1_original_dataset_backward_gbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-11-52__track1_original_dataset_backward_gbm_attempt_18_campaign_validation/validation_summary.yaml`
