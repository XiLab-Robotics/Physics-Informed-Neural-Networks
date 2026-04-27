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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `30.081%`
- winning mean component MAE: `0.084145`
- winning mean component RMSE: `0.172444`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 30.081 | 0.084145 | 0.172444 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.002876 | 0.004179 | 16.204 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000033 | 0.142 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002405 | 0.003326 | 29.818 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000026 | 0.000039 | 3.157 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.029087 | 0.040672 | 1.603 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000032 | 0.000044 | 2.845 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.029083 | 0.049114 | 2.459 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000031 | 0.000048 | 3.854 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.045000 | 0.070716 | 123.709 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000050 | 0.000071 | 6.918 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.086549 | 0.173732 | 69.038 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000012 | 0.000017 | 3.791 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.058689 | 0.094518 | 6.212 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000029 | 0.000069 | 9.660 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.599310 | 1.046135 | 34.861 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000061 | 0.000230 | 12.552 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.394425 | 0.901072 | 15.454 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000051 | 0.000078 | 11.399 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.351014 | 0.892347 | 217.861 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/002_track1_original_dataset_forward_ert_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-51-27__track1_original_dataset_forward_ert_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-51-27__track1_original_dataset_forward_ert_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-51-27__track1_original_dataset_forward_ert_attempt_02_campaign_validation/validation_summary.yaml`
