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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `28.076%`
- winning mean component MAE: `0.071593`
- winning mean component RMSE: `0.189393`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 28.076 | 0.071593 | 0.189393 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003597 | 0.005730 | 22.201 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000030 | 0.000042 | 0.172 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002249 | 0.003239 | 65.842 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000023 | 0.000033 | 2.747 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.024916 | 0.034342 | 1.359 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000039 | 0.000058 | 3.411 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.030431 | 0.052326 | 2.497 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000028 | 0.000038 | 3.431 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.046961 | 0.074211 | 78.234 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000057 | 0.000077 | 15.211 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.095680 | 0.182545 | 230.486 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000011 | 0.000016 | 3.659 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.062293 | 0.094051 | 5.188 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000097 | 0.000339 | 18.601 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.573663 | 1.478689 | 26.616 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000088 | 0.000236 | 15.421 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.199572 | 0.616222 | 10.352 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000038 | 0.000054 | 13.944 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.320496 | 1.056220 | 14.074 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/009_track1_original_dataset_forward_dt_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-17-32__track1_original_dataset_forward_dt_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-17-32__track1_original_dataset_forward_dt_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-17-32__track1_original_dataset_forward_dt_attempt_09_campaign_validation/validation_summary.yaml`
