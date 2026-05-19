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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `14.372%`
- winning mean component MAE: `0.059587`
- winning mean component RMSE: `0.153470`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 14.372 | 0.059587 | 0.153470 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003135 | 0.003947 | 6.563 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000027 | 0.000036 | 0.156 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002221 | 0.003096 | 26.811 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000024 | 0.000033 | 3.046 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.023643 | 0.031132 | 1.292 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000028 | 0.000039 | 2.470 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.021186 | 0.034664 | 1.789 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000040 | 3.349 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.035364 | 0.065379 | 46.354 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000031 | 0.000041 | 18.425 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.096825 | 0.396400 | 77.002 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000012 | 0.000018 | 3.802 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.047454 | 0.061499 | 6.863 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000041 | 0.000131 | 10.343 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.375921 | 0.824318 | 23.041 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000045 | 0.000145 | 8.044 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.307779 | 0.957125 | 11.536 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000045 | 0.000095 | 11.451 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.218349 | 0.537781 | 10.728 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/004_track1_original_dataset_forward_ert_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-57-56__track1_original_dataset_forward_ert_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-57-56__track1_original_dataset_forward_ert_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-57-56__track1_original_dataset_forward_ert_attempt_04_campaign_validation/validation_summary.yaml`
