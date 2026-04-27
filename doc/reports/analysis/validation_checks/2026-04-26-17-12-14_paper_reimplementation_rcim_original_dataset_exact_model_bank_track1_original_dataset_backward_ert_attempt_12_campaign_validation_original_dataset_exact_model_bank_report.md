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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `11.918%`
- winning mean component MAE: `0.038425`
- winning mean component RMSE: `0.092927`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 11.918 | 0.038425 | 0.092927 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002939 | 0.003707 | 34.251 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000025 | 0.000037 | 0.145 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001798 | 0.002489 | 29.353 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000027 | 0.000041 | 2.640 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.026571 | 0.033761 | 2.032 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000019 | 0.000027 | 4.247 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.162896 | 0.607783 | 5.682 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000027 | 0.000039 | 9.708 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.081638 | 0.145694 | 38.941 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000039 | 0.000051 | 4.798 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.044776 | 0.087455 | 18.170 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000008 | 0.000012 | 6.638 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.080612 | 0.104960 | 24.333 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000158 | 0.000676 | 4.575 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.046164 | 0.095660 | 4.510 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000033 | 0.000067 | 4.785 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.062093 | 0.131168 | 3.440 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000070 | 0.000131 | 11.996 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.220186 | 0.551851 | 16.194 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/012_track1_original_dataset_backward_ert_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-09-10__track1_original_dataset_backward_ert_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-09-10__track1_original_dataset_backward_ert_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-09-10__track1_original_dataset_backward_ert_attempt_12_campaign_validation/validation_summary.yaml`
