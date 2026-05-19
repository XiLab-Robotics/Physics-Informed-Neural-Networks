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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `30.477%`
- winning mean component MAE: `0.073579`
- winning mean component RMSE: `0.175066`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 30.477 | 0.073579 | 0.175066 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003270 | 0.003882 | 6.742 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000027 | 0.000035 | 0.157 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002433 | 0.003672 | 59.554 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000026 | 2.350 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.022647 | 0.028836 | 1.248 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000029 | 0.000040 | 2.471 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.027327 | 0.049630 | 2.316 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000024 | 0.000036 | 3.029 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.039364 | 0.061126 | 87.696 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000037 | 0.000056 | 5.965 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.096507 | 0.235588 | 85.215 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000014 | 3.304 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.056290 | 0.088304 | 5.079 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000026 | 0.000059 | 16.257 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.451572 | 0.991462 | 39.139 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000039 | 0.000126 | 7.257 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.443906 | 1.182362 | 18.759 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000033 | 0.000058 | 9.797 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.254438 | 0.680941 | 222.734 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/019_track1_original_dataset_forward_ert_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-46-06__track1_original_dataset_forward_ert_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-46-06__track1_original_dataset_forward_ert_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-46-06__track1_original_dataset_forward_ert_attempt_19_campaign_validation/validation_summary.yaml`
