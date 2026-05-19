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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `75.548%`
- winning mean component MAE: `0.072511`
- winning mean component RMSE: `0.210288`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 75.548 | 0.072511 | 0.210288 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003847 | 0.005285 | 68.075 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000034 | 0.000055 | 0.201 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002488 | 0.003624 | 489.517 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000037 | 0.000055 | 3.957 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.028384 | 0.042331 | 2.142 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000026 | 0.000036 | 6.391 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.239755 | 1.084503 | 8.299 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000027 | 0.000041 | 8.770 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.147655 | 0.269441 | 47.132 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000080 | 0.000109 | 9.819 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.100817 | 0.215106 | 30.650 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000014 | 0.000020 | 10.729 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.117439 | 0.179475 | 639.721 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000309 | 0.001078 | 24.465 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.348935 | 1.123684 | 31.155 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000060 | 0.000150 | 7.973 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.070846 | 0.109588 | 3.810 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000075 | 0.000146 | 15.462 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.316882 | 0.960749 | 27.153 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/013_track1_original_dataset_backward_et_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-27-22__track1_original_dataset_backward_et_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-27-22__track1_original_dataset_backward_et_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-27-22__track1_original_dataset_backward_et_attempt_13_campaign_validation/validation_summary.yaml`
