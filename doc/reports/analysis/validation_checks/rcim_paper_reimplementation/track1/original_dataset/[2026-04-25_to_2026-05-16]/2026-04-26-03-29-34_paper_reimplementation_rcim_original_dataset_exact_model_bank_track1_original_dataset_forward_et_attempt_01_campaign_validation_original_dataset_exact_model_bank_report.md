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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `25.272%`
- winning mean component MAE: `0.090368`
- winning mean component RMSE: `0.214121`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 25.272 | 0.090368 | 0.214121 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003429 | 0.004207 | 6.802 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000032 | 0.000044 | 0.187 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002253 | 0.003559 | 81.288 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000025 | 0.000035 | 3.055 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.034983 | 0.048942 | 1.914 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000046 | 0.000058 | 4.036 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.039331 | 0.073719 | 3.223 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000030 | 0.000043 | 3.767 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.049024 | 0.080903 | 65.132 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000073 | 0.000096 | 12.284 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.108720 | 0.318537 | 124.194 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000016 | 0.000022 | 5.496 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.056568 | 0.072620 | 4.501 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000101 | 0.000301 | 20.951 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.874854 | 1.754148 | 74.168 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000088 | 0.000269 | 12.621 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.183074 | 0.798109 | 7.533 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000187 | 0.000528 | 28.877 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.364159 | 0.912162 | 20.139 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/001_track1_original_dataset_forward_et_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-28-40__track1_original_dataset_forward_et_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-28-40__track1_original_dataset_forward_et_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-28-40__track1_original_dataset_forward_et_attempt_01_campaign_validation/validation_summary.yaml`
