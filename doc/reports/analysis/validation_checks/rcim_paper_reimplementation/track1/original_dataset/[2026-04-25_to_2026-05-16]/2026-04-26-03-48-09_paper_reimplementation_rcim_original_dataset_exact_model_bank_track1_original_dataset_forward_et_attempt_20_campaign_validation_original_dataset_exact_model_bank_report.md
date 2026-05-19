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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `25.819%`
- winning mean component MAE: `0.094385`
- winning mean component RMSE: `0.219264`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 25.819 | 0.094385 | 0.219264 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003451 | 0.004251 | 7.502 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000033 | 0.000045 | 0.190 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002741 | 0.003544 | 52.545 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000023 | 0.000030 | 3.020 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.026940 | 0.035953 | 1.506 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000035 | 0.000047 | 3.268 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.024607 | 0.035012 | 2.024 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000033 | 0.000049 | 4.218 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.048051 | 0.077909 | 68.004 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000062 | 0.000087 | 10.531 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.122520 | 0.339337 | 184.572 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000017 | 0.000025 | 5.995 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.071466 | 0.094749 | 5.931 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000117 | 0.000366 | 29.875 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 1.019524 | 2.034442 | 52.426 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000069 | 0.000280 | 12.085 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.199893 | 0.815084 | 8.681 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000110 | 0.000374 | 21.388 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.273615 | 0.724434 | 16.798 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/020_track1_original_dataset_forward_et_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-47-19__track1_original_dataset_forward_et_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-47-19__track1_original_dataset_forward_et_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-47-19__track1_original_dataset_forward_et_attempt_20_campaign_validation/validation_summary.yaml`
