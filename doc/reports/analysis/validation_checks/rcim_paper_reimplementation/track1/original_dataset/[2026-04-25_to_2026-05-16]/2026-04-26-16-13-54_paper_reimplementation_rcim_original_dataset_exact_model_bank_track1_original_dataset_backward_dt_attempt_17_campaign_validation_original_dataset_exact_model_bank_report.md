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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `20.471%`
- winning mean component MAE: `0.057279`
- winning mean component RMSE: `0.154982`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 20.471 | 0.057279 | 0.154982 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 8}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003302 | 0.004185 | 44.749 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000032 | 0.000043 | 0.189 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002038 | 0.003006 | 70.251 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000026 | 0.000035 | 2.707 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.024813 | 0.041909 | 1.874 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000023 | 0.000031 | 5.227 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.286974 | 1.099409 | 10.020 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000033 | 0.000053 | 10.269 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.133180 | 0.232428 | 50.804 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000072 | 0.000098 | 8.145 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.060720 | 0.102928 | 51.697 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000021 | 9.142 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.126901 | 0.187605 | 55.835 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000173 | 0.000739 | 9.179 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.197744 | 0.581704 | 24.590 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000191 | 0.000869 | 8.959 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.056811 | 0.080888 | 3.293 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000104 | 0.000301 | 11.059 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.195147 | 0.608416 | 10.960 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/017_track1_original_dataset_backward_dt_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-13-05__track1_original_dataset_backward_dt_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-13-05__track1_original_dataset_backward_dt_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-13-05__track1_original_dataset_backward_dt_attempt_17_campaign_validation/validation_summary.yaml`
