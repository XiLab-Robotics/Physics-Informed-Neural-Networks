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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `18.271%`
- winning mean component MAE: `0.064441`
- winning mean component RMSE: `0.151992`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 18.271 | 0.064441 | 0.151992 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003298 | 0.004025 | 6.524 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000030 | 0.000040 | 0.175 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002140 | 0.003079 | 66.420 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000019 | 0.000025 | 2.423 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.021109 | 0.028988 | 1.163 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000026 | 0.000033 | 2.297 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.027113 | 0.052237 | 2.149 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000021 | 0.000027 | 2.632 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.032738 | 0.050797 | 51.417 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000034 | 0.000049 | 11.176 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.066497 | 0.207215 | 104.996 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000016 | 3.735 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.045616 | 0.062262 | 4.165 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000054 | 0.000227 | 15.099 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.505565 | 0.924908 | 32.639 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000080 | 0.000326 | 7.222 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.208390 | 0.708327 | 8.642 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000040 | 0.000080 | 9.511 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.311603 | 0.845185 | 14.759 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/001_track1_original_dataset_forward_ert_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-48-16__track1_original_dataset_forward_ert_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-48-16__track1_original_dataset_forward_ert_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-48-16__track1_original_dataset_forward_ert_attempt_01_campaign_validation/validation_summary.yaml`
