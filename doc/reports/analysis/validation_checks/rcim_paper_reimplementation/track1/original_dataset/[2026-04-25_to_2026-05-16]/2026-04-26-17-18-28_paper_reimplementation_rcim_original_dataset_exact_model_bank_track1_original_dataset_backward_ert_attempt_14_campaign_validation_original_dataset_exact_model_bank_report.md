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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `20.207%`
- winning mean component MAE: `0.045275`
- winning mean component RMSE: `0.115140`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 20.207 | 0.045275 | 0.115140 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003474 | 0.004510 | 46.228 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000035 | 0.139 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001893 | 0.003394 | 108.466 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000027 | 0.000047 | 2.795 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.023159 | 0.033553 | 1.690 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000017 | 0.000024 | 4.297 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.155179 | 0.528873 | 5.594 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000024 | 0.000032 | 8.552 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.088014 | 0.177866 | 32.441 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000045 | 0.000067 | 5.533 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.082230 | 0.182142 | 32.035 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000019 | 7.950 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.101887 | 0.157445 | 60.134 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000062 | 0.000173 | 7.214 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.108092 | 0.245658 | 19.992 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000051 | 0.000165 | 5.918 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.094291 | 0.221979 | 4.548 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000067 | 0.000102 | 20.452 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.201677 | 0.631569 | 9.964 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/014_track1_original_dataset_backward_ert_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-15-28__track1_original_dataset_backward_ert_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-15-28__track1_original_dataset_backward_ert_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-15-28__track1_original_dataset_backward_ert_attempt_14_campaign_validation/validation_summary.yaml`
