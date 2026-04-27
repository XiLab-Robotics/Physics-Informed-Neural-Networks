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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `23.036%`
- winning mean component MAE: `0.045031`
- winning mean component RMSE: `0.118001`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 23.036 | 0.045031 | 0.118001 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003013 | 0.003651 | 33.729 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000033 | 0.139 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001491 | 0.001984 | 87.664 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000022 | 0.000035 | 2.332 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.021922 | 0.027325 | 1.618 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000016 | 0.000022 | 3.499 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.137891 | 0.486999 | 4.959 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000025 | 0.000038 | 8.889 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.084906 | 0.157708 | 64.711 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000046 | 0.000068 | 6.401 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.066799 | 0.176817 | 20.115 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000014 | 7.418 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.082556 | 0.107263 | 140.948 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000147 | 0.000605 | 6.851 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.088122 | 0.353333 | 11.039 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000040 | 0.000080 | 6.503 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.076239 | 0.256975 | 3.755 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000095 | 0.000226 | 14.064 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.292231 | 0.668849 | 13.052 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/015_track1_original_dataset_backward_ert_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-18-35__track1_original_dataset_backward_ert_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-18-35__track1_original_dataset_backward_ert_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-18-35__track1_original_dataset_backward_ert_attempt_15_campaign_validation/validation_summary.yaml`
