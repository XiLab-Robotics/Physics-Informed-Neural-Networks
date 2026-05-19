# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `16.751%`
- winning mean component MAE: `0.059655`
- winning mean component RMSE: `0.128202`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 16.751 | 0.059655 | 0.128202 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003049 | 0.003570 | 5.794 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000023 | 0.000032 | 0.133 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002108 | 0.002724 | 38.643 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000022 | 0.000032 | 2.710 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.021530 | 0.028534 | 1.185 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000029 | 0.000038 | 2.507 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.023110 | 0.037532 | 2.039 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000022 | 0.000029 | 2.698 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.041642 | 0.062944 | 79.877 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000043 | 0.000061 | 10.889 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.063292 | 0.119049 | 88.355 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000014 | 3.457 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.059024 | 0.079601 | 5.271 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000048 | 0.000134 | 11.996 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.532336 | 1.049598 | 25.894 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000057 | 0.000142 | 7.812 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.169876 | 0.483585 | 6.994 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000050 | 0.000084 | 11.014 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.217181 | 0.568138 | 10.997 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/008_track1_original_dataset_forward_ert_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-10-53__track1_original_dataset_forward_ert_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-10-53__track1_original_dataset_forward_ert_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-10-53__track1_original_dataset_forward_ert_attempt_08_campaign_validation/validation_summary.yaml`
