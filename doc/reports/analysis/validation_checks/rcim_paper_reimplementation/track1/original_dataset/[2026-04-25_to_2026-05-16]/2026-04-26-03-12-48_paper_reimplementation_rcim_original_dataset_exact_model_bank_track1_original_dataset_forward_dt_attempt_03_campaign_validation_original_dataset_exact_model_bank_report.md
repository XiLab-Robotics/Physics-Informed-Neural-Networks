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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `18.414%`
- winning mean component MAE: `0.061262`
- winning mean component RMSE: `0.174704`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 18.414 | 0.061262 | 0.174704 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003710 | 0.004486 | 7.070 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000032 | 0.000042 | 0.184 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002604 | 0.003785 | 30.042 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000026 | 0.000036 | 3.161 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.029590 | 0.037269 | 1.638 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000041 | 0.000056 | 3.524 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.030271 | 0.055341 | 2.539 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000031 | 0.000047 | 3.766 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.047898 | 0.079645 | 64.164 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000059 | 0.000087 | 10.483 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.081573 | 0.179150 | 99.307 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000015 | 0.000020 | 5.167 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.082535 | 0.140943 | 9.960 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000087 | 0.000356 | 22.304 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.453319 | 1.184631 | 43.024 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000061 | 0.000166 | 8.592 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.232709 | 0.942779 | 8.971 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000054 | 0.000136 | 11.548 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.199363 | 0.690396 | 14.428 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/003_track1_original_dataset_forward_dt_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-11-55__track1_original_dataset_forward_dt_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-11-55__track1_original_dataset_forward_dt_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-11-55__track1_original_dataset_forward_dt_attempt_03_campaign_validation/validation_summary.yaml`
