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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `46.716%`
- winning mean component MAE: `0.100801`
- winning mean component RMSE: `0.189147`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 46.716 | 0.100801 | 0.189147 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003426 | 0.004038 | 7.632 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000026 | 0.000034 | 0.154 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002543 | 0.003777 | 87.748 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000028 | 0.000037 | 3.375 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.025430 | 0.035342 | 1.422 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000049 | 0.000060 | 4.498 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.036042 | 0.052758 | 3.199 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000028 | 0.000037 | 3.577 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.045266 | 0.065461 | 133.325 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000082 | 0.000110 | 18.063 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.102961 | 0.219495 | 66.293 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000018 | 4.028 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.078571 | 0.111097 | 8.611 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000109 | 0.000164 | 98.710 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.651696 | 1.029221 | 44.060 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000119 | 0.000214 | 52.003 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.642451 | 1.312282 | 28.360 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000053 | 0.000091 | 24.834 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.326330 | 0.759556 | 297.705 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/019_track1_original_dataset_forward_gbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-30-18__track1_original_dataset_forward_gbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-30-18__track1_original_dataset_forward_gbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-30-18__track1_original_dataset_forward_gbm_attempt_19_campaign_validation/validation_summary.yaml`
