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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `20.651%`
- winning mean component MAE: `0.077763`
- winning mean component RMSE: `0.172462`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 20.651 | 0.077763 | 0.172462 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003011 | 0.003732 | 6.389 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000028 | 0.000037 | 0.165 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002213 | 0.002860 | 42.457 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000019 | 0.000026 | 2.471 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.020941 | 0.029236 | 1.173 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000026 | 0.000036 | 2.362 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.019325 | 0.027945 | 1.576 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000024 | 0.000035 | 3.095 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.029841 | 0.046643 | 47.870 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000041 | 0.000057 | 8.014 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.079030 | 0.218223 | 141.704 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000013 | 3.206 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.053694 | 0.085692 | 5.475 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000074 | 0.000291 | 28.730 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.705922 | 1.353239 | 50.304 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000049 | 0.000160 | 10.184 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.298850 | 0.921309 | 11.242 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000053 | 0.000128 | 12.622 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.264351 | 0.587120 | 13.325 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/020_track1_original_dataset_forward_ert_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-49-19__track1_original_dataset_forward_ert_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-49-19__track1_original_dataset_forward_ert_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-49-19__track1_original_dataset_forward_ert_attempt_20_campaign_validation/validation_summary.yaml`
