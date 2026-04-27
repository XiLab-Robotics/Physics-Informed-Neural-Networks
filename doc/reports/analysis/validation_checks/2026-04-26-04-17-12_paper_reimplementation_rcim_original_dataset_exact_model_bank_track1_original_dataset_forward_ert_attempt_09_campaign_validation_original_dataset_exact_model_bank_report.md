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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `20.638%`
- winning mean component MAE: `0.066602`
- winning mean component RMSE: `0.170473`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 20.638 | 0.066602 | 0.170473 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003049 | 0.004190 | 13.966 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000026 | 0.000038 | 0.151 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.001961 | 0.003214 | 59.600 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000029 | 2.566 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.024432 | 0.042531 | 1.356 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000030 | 0.000041 | 2.614 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.025148 | 0.050237 | 2.032 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000040 | 3.272 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.038051 | 0.059558 | 72.945 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000029 | 0.000042 | 9.511 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.051632 | 0.099959 | 123.409 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000015 | 3.358 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.051091 | 0.082262 | 4.465 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000050 | 0.000186 | 12.032 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.546061 | 1.235541 | 29.970 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000043 | 0.000118 | 8.779 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.263976 | 0.845976 | 12.105 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000033 | 0.000064 | 18.569 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.259774 | 0.814943 | 11.416 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/009_track1_original_dataset_forward_ert_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-14-07__track1_original_dataset_forward_ert_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-14-07__track1_original_dataset_forward_ert_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-14-07__track1_original_dataset_forward_ert_attempt_09_campaign_validation/validation_summary.yaml`
