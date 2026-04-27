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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `35.926%`
- winning mean component MAE: `0.065079`
- winning mean component RMSE: `0.187469`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 35.926 | 0.065079 | 0.187469 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003693 | 0.004606 | 7.290 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000034 | 0.000044 | 0.197 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.003307 | 0.004922 | 37.770 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000028 | 0.000039 | 3.270 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.034048 | 0.046387 | 1.877 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000042 | 0.000056 | 3.413 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.038967 | 0.077813 | 3.333 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000033 | 0.000052 | 4.188 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.050858 | 0.081387 | 113.728 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000054 | 0.000077 | 8.291 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.072162 | 0.178552 | 349.198 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000016 | 0.000025 | 5.238 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.075171 | 0.127527 | 6.525 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000077 | 0.000209 | 19.425 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.580697 | 1.493532 | 48.098 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000042 | 0.000086 | 10.446 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.190899 | 0.855975 | 7.290 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000045 | 0.000072 | 12.118 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.186330 | 0.690548 | 40.896 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/012_track1_original_dataset_forward_et_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-39-29__track1_original_dataset_forward_et_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-39-29__track1_original_dataset_forward_et_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-39-29__track1_original_dataset_forward_et_attempt_12_campaign_validation/validation_summary.yaml`
