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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `28.184%`
- winning mean component MAE: `0.063273`
- winning mean component RMSE: `0.168129`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 28.184 | 0.063273 | 0.168129 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.004016 | 0.006592 | 211.931 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000025 | 0.000037 | 0.144 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002040 | 0.003096 | 29.776 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000033 | 0.000049 | 3.369 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.027946 | 0.040407 | 2.124 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000022 | 0.000034 | 5.221 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.275020 | 1.022125 | 9.531 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000027 | 0.000042 | 9.433 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.092854 | 0.123335 | 43.805 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000062 | 0.000088 | 7.521 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.045039 | 0.078066 | 51.361 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000012 | 0.000019 | 10.213 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.104386 | 0.142139 | 53.552 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000217 | 0.000832 | 13.927 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.131521 | 0.388068 | 20.899 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000133 | 0.000594 | 9.856 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.065516 | 0.125095 | 3.954 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000115 | 0.000279 | 15.585 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.453208 | 1.263550 | 33.297 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/001_track1_original_dataset_backward_et_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-16-40__track1_original_dataset_backward_et_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-16-40__track1_original_dataset_backward_et_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-16-40__track1_original_dataset_backward_et_attempt_01_campaign_validation/validation_summary.yaml`
