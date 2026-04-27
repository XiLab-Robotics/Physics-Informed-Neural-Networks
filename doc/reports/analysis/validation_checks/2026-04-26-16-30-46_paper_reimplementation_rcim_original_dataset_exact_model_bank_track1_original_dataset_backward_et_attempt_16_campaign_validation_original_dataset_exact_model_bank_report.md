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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `28.533%`
- winning mean component MAE: `0.056255`
- winning mean component RMSE: `0.132696`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 28.533 | 0.056255 | 0.132696 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003028 | 0.003736 | 41.392 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000032 | 0.000045 | 0.189 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.001641 | 0.002633 | 40.034 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000034 | 0.000055 | 3.273 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.030606 | 0.045607 | 2.323 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000025 | 0.000034 | 5.312 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.181431 | 0.638956 | 6.417 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000038 | 0.000054 | 12.263 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.125044 | 0.249413 | 128.072 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000063 | 0.000084 | 9.129 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.069617 | 0.118566 | 56.068 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000021 | 11.064 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.122745 | 0.164240 | 147.985 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000142 | 0.000614 | 11.322 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.142561 | 0.326816 | 21.635 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000058 | 0.000161 | 9.065 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.081522 | 0.193823 | 4.099 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000107 | 0.000309 | 13.758 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.310132 | 0.776063 | 18.737 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/016_track1_original_dataset_backward_et_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-30-00__track1_original_dataset_backward_et_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-30-00__track1_original_dataset_backward_et_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-30-00__track1_original_dataset_backward_et_attempt_16_campaign_validation/validation_summary.yaml`
