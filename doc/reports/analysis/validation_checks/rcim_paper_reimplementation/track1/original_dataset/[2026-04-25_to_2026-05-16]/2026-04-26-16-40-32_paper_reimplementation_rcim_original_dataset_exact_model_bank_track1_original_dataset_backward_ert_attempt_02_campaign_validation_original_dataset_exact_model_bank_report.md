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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `15.426%`
- winning mean component MAE: `0.047559`
- winning mean component RMSE: `0.119935`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 15.426 | 0.047559 | 0.119935 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002809 | 0.003587 | 39.398 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000025 | 0.000034 | 0.147 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001950 | 0.002527 | 52.715 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000023 | 0.000037 | 2.302 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.026207 | 0.035303 | 2.024 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000020 | 0.000029 | 4.321 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.160692 | 0.464321 | 5.726 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000027 | 0.000038 | 9.346 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.100273 | 0.208451 | 48.215 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000043 | 0.000062 | 5.217 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.077630 | 0.197975 | 23.850 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000015 | 7.604 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.093145 | 0.128149 | 31.472 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000073 | 0.000337 | 9.515 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.128500 | 0.477361 | 17.232 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000053 | 0.000176 | 8.116 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.066343 | 0.151324 | 3.638 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000069 | 0.000155 | 11.146 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.245736 | 0.608876 | 11.109 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/002_track1_original_dataset_backward_ert_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-37-32__track1_original_dataset_backward_ert_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-37-32__track1_original_dataset_backward_ert_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-37-32__track1_original_dataset_backward_ert_attempt_02_campaign_validation/validation_summary.yaml`
