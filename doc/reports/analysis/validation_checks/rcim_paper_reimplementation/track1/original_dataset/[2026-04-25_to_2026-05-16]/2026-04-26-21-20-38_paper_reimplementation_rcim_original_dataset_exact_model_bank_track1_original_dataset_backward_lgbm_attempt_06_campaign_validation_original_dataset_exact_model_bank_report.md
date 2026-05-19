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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `23.001%`
- winning mean component MAE: `0.084940`
- winning mean component RMSE: `0.171609`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 23.001 | 0.084940 | 0.171609 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 8, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002299 | 0.002878 | 37.332 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000027 | 0.000038 | 0.158 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001717 | 0.002220 | 116.948 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000017 | 0.000026 | 1.680 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.019334 | 0.026084 | 1.424 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000015 | 0.000020 | 3.398 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.341784 | 0.830910 | 11.762 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000028 | 0.000042 | 9.125 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.103113 | 0.147042 | 42.048 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000034 | 0.000047 | 5.817 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.079029 | 0.143363 | 24.861 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000011 | 0.000016 | 8.288 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.091231 | 0.122835 | 49.502 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000255 | 0.000515 | 30.106 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.226555 | 0.554807 | 20.361 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000172 | 0.000406 | 18.906 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.129340 | 0.254421 | 7.192 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000143 | 0.000331 | 21.731 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.618749 | 1.174576 | 26.381 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/006_track1_original_dataset_backward_lgbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-58-49__track1_original_dataset_backward_lgbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-58-49__track1_original_dataset_backward_lgbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-58-49__track1_original_dataset_backward_lgbm_attempt_06_campaign_validation/validation_summary.yaml`
