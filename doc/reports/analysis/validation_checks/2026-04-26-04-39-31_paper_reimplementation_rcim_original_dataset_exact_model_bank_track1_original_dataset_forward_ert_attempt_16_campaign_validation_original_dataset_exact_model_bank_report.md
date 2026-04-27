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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `15.665%`
- winning mean component MAE: `0.075843`
- winning mean component RMSE: `0.162185`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 15.665 | 0.075843 | 0.162185 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003146 | 0.003650 | 5.990 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000031 | 0.142 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.001725 | 0.002502 | 33.476 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000021 | 0.000028 | 2.431 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.023959 | 0.031629 | 1.314 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000029 | 0.000043 | 2.465 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.022642 | 0.031920 | 1.968 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000038 | 3.393 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.042686 | 0.062659 | 47.246 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000044 | 0.000060 | 9.662 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.117431 | 0.336230 | 43.666 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000015 | 3.647 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.051570 | 0.080923 | 4.734 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000039 | 0.000170 | 10.857 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.449547 | 0.785379 | 18.728 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000035 | 0.000083 | 9.701 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.377117 | 0.888628 | 13.896 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000035 | 0.000065 | 8.046 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.350932 | 0.857464 | 76.274 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/016_track1_original_dataset_forward_ert_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-36-25__track1_original_dataset_forward_ert_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-36-25__track1_original_dataset_forward_ert_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-36-25__track1_original_dataset_forward_ert_attempt_16_campaign_validation/validation_summary.yaml`
