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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `12.455%`
- winning mean component MAE: `0.048395`
- winning mean component RMSE: `0.136086`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 12.455 | 0.048395 | 0.136086 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003112 | 0.003973 | 35.846 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000028 | 0.000040 | 0.166 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001479 | 0.001953 | 32.570 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000028 | 0.000043 | 2.823 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.021299 | 0.034539 | 1.560 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000016 | 0.000021 | 3.650 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.356516 | 1.276727 | 12.053 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000029 | 0.000043 | 9.258 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.077605 | 0.116173 | 27.464 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000039 | 0.000054 | 4.625 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.049648 | 0.152124 | 15.225 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000007 | 0.000010 | 5.614 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.071577 | 0.102052 | 32.052 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000131 | 0.000646 | 6.476 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.089102 | 0.257660 | 8.555 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000062 | 0.000181 | 7.186 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.051921 | 0.113078 | 3.054 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000080 | 0.000209 | 11.482 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.196822 | 0.526097 | 16.993 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/003_track1_original_dataset_backward_ert_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-40-39__track1_original_dataset_backward_ert_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-40-39__track1_original_dataset_backward_ert_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-40-39__track1_original_dataset_backward_ert_attempt_03_campaign_validation/validation_summary.yaml`
