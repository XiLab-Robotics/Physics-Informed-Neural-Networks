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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `19.826%`
- winning mean component MAE: `0.050767`
- winning mean component RMSE: `0.177656`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 19.826 | 0.050767 | 0.177656 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003501 | 0.004475 | 31.190 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000027 | 0.000036 | 0.156 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002047 | 0.003049 | 77.105 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000029 | 0.000044 | 3.002 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.024720 | 0.031849 | 1.904 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000020 | 0.000031 | 4.310 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.195914 | 0.932633 | 6.824 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000033 | 0.000047 | 10.163 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.109914 | 0.158240 | 45.637 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000063 | 0.000083 | 7.953 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.059337 | 0.127397 | 33.586 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000009 | 0.000014 | 8.481 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.108025 | 0.157245 | 93.989 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000141 | 0.000521 | 7.911 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.125872 | 0.613757 | 9.707 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000098 | 0.000303 | 7.752 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.169555 | 0.689173 | 7.237 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000150 | 0.000390 | 12.919 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.165120 | 0.656176 | 6.875 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/008_track1_original_dataset_backward_dt_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-05-01__track1_original_dataset_backward_dt_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-05-01__track1_original_dataset_backward_dt_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-05-01__track1_original_dataset_backward_dt_attempt_08_campaign_validation/validation_summary.yaml`
