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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `28.132%`
- winning mean component MAE: `0.034806`
- winning mean component RMSE: `0.099735`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 28.132 | 0.034806 | 0.099735 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003635 | 0.004496 | 67.666 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000029 | 0.000043 | 0.168 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002205 | 0.003603 | 162.392 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000023 | 0.000034 | 2.292 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.024662 | 0.033192 | 1.892 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000026 | 0.000038 | 5.986 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.111456 | 0.627620 | 4.194 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000038 | 0.000061 | 12.907 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.100728 | 0.144745 | 57.779 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000074 | 0.000100 | 8.720 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.050955 | 0.085827 | 20.313 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000011 | 0.000016 | 9.424 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.115632 | 0.164282 | 124.049 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000139 | 0.000545 | 10.379 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.071371 | 0.197164 | 6.583 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000120 | 0.000665 | 7.772 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.066810 | 0.173353 | 4.864 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000098 | 0.000264 | 11.523 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.113311 | 0.458909 | 15.607 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/011_track1_original_dataset_backward_dt_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-07-45__track1_original_dataset_backward_dt_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-07-45__track1_original_dataset_backward_dt_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-07-45__track1_original_dataset_backward_dt_attempt_11_campaign_validation/validation_summary.yaml`
