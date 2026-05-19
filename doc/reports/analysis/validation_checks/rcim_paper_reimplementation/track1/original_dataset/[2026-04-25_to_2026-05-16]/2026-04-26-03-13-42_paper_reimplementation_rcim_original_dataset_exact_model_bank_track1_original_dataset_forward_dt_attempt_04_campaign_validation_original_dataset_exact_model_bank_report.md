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

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `16.332%`
- winning mean component MAE: `0.073535`
- winning mean component RMSE: `0.209522`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 16.332 | 0.073535 | 0.209522 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003571 | 0.004502 | 7.408 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000033 | 0.000049 | 0.190 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002282 | 0.003081 | 34.885 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000025 | 0.000034 | 3.080 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.024957 | 0.033964 | 1.372 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000039 | 0.000052 | 3.502 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.027932 | 0.046835 | 2.240 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000033 | 0.000058 | 4.274 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.043203 | 0.073727 | 52.767 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000050 | 0.000068 | 23.841 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.158648 | 0.478956 | 67.809 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000016 | 0.000027 | 5.386 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.062969 | 0.080985 | 8.703 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000064 | 0.000204 | 19.534 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.486134 | 1.256832 | 29.823 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000092 | 0.000378 | 10.556 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.337633 | 1.168291 | 12.738 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000046 | 0.000091 | 9.853 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.249438 | 0.832790 | 12.356 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/004_track1_original_dataset_forward_dt_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-12-55__track1_original_dataset_forward_dt_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-12-55__track1_original_dataset_forward_dt_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-12-55__track1_original_dataset_forward_dt_attempt_04_campaign_validation/validation_summary.yaml`
