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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `25.370%`
- winning mean component MAE: `0.070258`
- winning mean component RMSE: `0.153697`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 25.370 | 0.070258 | 0.153697 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.002937 | 0.003642 | 5.975 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000021 | 0.000028 | 0.121 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.001968 | 0.002551 | 48.170 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000019 | 0.000025 | 2.355 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.023620 | 0.032967 | 1.321 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000029 | 0.000037 | 2.657 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.021335 | 0.034413 | 1.768 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000023 | 0.000038 | 2.800 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.033024 | 0.048067 | 49.757 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000041 | 0.000059 | 7.319 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.078245 | 0.197233 | 174.451 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000014 | 3.319 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.063111 | 0.089039 | 6.930 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000066 | 0.000187 | 14.236 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.570000 | 1.139753 | 34.916 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000034 | 0.000076 | 8.372 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.343268 | 0.888697 | 12.735 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000042 | 0.000073 | 12.659 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.197101 | 0.483336 | 92.162 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/015_track1_original_dataset_forward_ert_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-33-19__track1_original_dataset_forward_ert_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-33-19__track1_original_dataset_forward_ert_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-33-19__track1_original_dataset_forward_ert_attempt_15_campaign_validation/validation_summary.yaml`
