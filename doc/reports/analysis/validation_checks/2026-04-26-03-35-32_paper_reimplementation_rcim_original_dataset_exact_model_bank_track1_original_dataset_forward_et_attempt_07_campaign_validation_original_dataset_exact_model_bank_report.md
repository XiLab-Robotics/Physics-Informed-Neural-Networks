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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `20.939%`
- winning mean component MAE: `0.096569`
- winning mean component RMSE: `0.262035`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 20.939 | 0.096569 | 0.262035 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003794 | 0.005224 | 9.668 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000036 | 0.000053 | 0.209 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002632 | 0.003991 | 37.162 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000028 | 0.000042 | 3.447 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.031622 | 0.043552 | 1.762 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000035 | 0.000046 | 3.222 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.030441 | 0.054639 | 2.504 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000029 | 0.000043 | 3.783 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.051492 | 0.079156 | 97.738 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000048 | 0.000075 | 21.244 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.157324 | 0.517327 | 66.618 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000013 | 0.000017 | 4.360 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.098393 | 0.179384 | 9.622 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000062 | 0.000164 | 22.004 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.620290 | 1.560634 | 47.993 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000079 | 0.000282 | 9.856 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.484235 | 1.534438 | 23.904 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000048 | 0.000082 | 13.122 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.354205 | 0.999514 | 19.620 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/007_track1_original_dataset_forward_et_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-34-39__track1_original_dataset_forward_et_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-34-39__track1_original_dataset_forward_et_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-34-39__track1_original_dataset_forward_et_attempt_07_campaign_validation/validation_summary.yaml`
