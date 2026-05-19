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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `23.120%`
- winning mean component MAE: `0.056597`
- winning mean component RMSE: `0.104357`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 23.120 | 0.056597 | 0.104357 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003082 | 0.003653 | 50.092 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000028 | 0.000041 | 0.163 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001801 | 0.002787 | 38.862 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000021 | 0.000028 | 2.300 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.029730 | 0.036742 | 2.158 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000020 | 0.000026 | 4.341 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.344885 | 0.734780 | 13.099 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000029 | 0.000048 | 8.627 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.106948 | 0.187071 | 52.092 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000084 | 0.000106 | 15.922 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.061816 | 0.101827 | 57.552 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000016 | 8.910 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.084631 | 0.113678 | 48.573 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000328 | 0.001254 | 39.093 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.102615 | 0.202684 | 7.510 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000151 | 0.000264 | 55.041 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.153818 | 0.209902 | 8.345 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000076 | 0.000149 | 12.690 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.185277 | 0.387719 | 13.909 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/020_track1_original_dataset_backward_gbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-15-58__track1_original_dataset_backward_gbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-15-58__track1_original_dataset_backward_gbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-15-58__track1_original_dataset_backward_gbm_attempt_20_campaign_validation/validation_summary.yaml`
