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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `29.423%`
- winning mean component MAE: `0.054948`
- winning mean component RMSE: `0.137428`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 29.423 | 0.054948 | 0.137428 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002836 | 0.003715 | 41.565 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000027 | 0.000040 | 0.159 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001940 | 0.002628 | 38.055 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000024 | 0.000039 | 2.531 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.023500 | 0.048650 | 1.769 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000017 | 0.000025 | 3.745 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.169071 | 0.799580 | 6.127 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000041 | 8.779 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.115924 | 0.196066 | 222.887 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000044 | 0.000059 | 7.140 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.087419 | 0.221246 | 33.556 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000008 | 0.000012 | 7.063 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.122055 | 0.197509 | 105.255 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000152 | 0.000677 | 7.469 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.111923 | 0.232314 | 17.403 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000066 | 0.000204 | 6.955 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.116670 | 0.371831 | 6.421 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000080 | 0.000138 | 24.830 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.292235 | 0.536354 | 17.321 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/018_track1_original_dataset_backward_ert_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-28-04__track1_original_dataset_backward_ert_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-28-04__track1_original_dataset_backward_ert_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-28-04__track1_original_dataset_backward_ert_attempt_18_campaign_validation/validation_summary.yaml`
