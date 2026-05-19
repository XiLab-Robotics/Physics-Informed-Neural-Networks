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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `19.518%`
- winning mean component MAE: `0.054280`
- winning mean component RMSE: `0.160724`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 19.518 | 0.054280 | 0.160724 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003467 | 0.004332 | 6.452 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000028 | 0.000037 | 0.161 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002406 | 0.003262 | 42.911 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000026 | 0.000037 | 3.093 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.027313 | 0.035720 | 1.502 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000042 | 0.000060 | 3.546 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.022719 | 0.030703 | 2.027 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000030 | 0.000040 | 3.655 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.059399 | 0.107417 | 70.010 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000054 | 0.000078 | 12.158 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.086031 | 0.164916 | 135.202 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000015 | 0.000020 | 4.717 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.071407 | 0.125499 | 7.332 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000069 | 0.000189 | 16.016 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.486836 | 1.373936 | 25.778 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000044 | 0.000102 | 8.714 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.129959 | 0.629177 | 5.288 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000059 | 0.000166 | 13.809 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.141427 | 0.578067 | 8.463 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/008_track1_original_dataset_forward_dt_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-16-37__track1_original_dataset_forward_dt_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-16-37__track1_original_dataset_forward_dt_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-16-37__track1_original_dataset_forward_dt_attempt_08_campaign_validation/validation_summary.yaml`
