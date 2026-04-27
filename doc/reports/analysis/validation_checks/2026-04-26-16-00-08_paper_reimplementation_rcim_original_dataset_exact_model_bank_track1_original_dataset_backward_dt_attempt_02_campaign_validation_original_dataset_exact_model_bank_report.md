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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `19.063%`
- winning mean component MAE: `0.050895`
- winning mean component RMSE: `0.151114`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 19.063 | 0.050895 | 0.151114 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.002786 | 0.003877 | 45.658 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000031 | 0.000040 | 0.183 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002061 | 0.002689 | 67.248 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000031 | 0.000046 | 3.083 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.029233 | 0.040958 | 2.293 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000025 | 0.000033 | 5.368 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.175007 | 0.872161 | 6.403 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000029 | 0.000045 | 9.371 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.114532 | 0.229082 | 71.110 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000075 | 0.000099 | 9.272 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.102639 | 0.239373 | 35.846 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000011 | 0.000019 | 8.358 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.135243 | 0.191717 | 44.756 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000075 | 0.000354 | 9.673 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.081018 | 0.252907 | 7.216 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000073 | 0.000239 | 10.242 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.062111 | 0.135238 | 3.757 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000097 | 0.000228 | 11.074 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.261922 | 0.902056 | 11.284 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/002_track1_original_dataset_backward_dt_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-59-22__track1_original_dataset_backward_dt_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-59-22__track1_original_dataset_backward_dt_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-59-22__track1_original_dataset_backward_dt_attempt_02_campaign_validation/validation_summary.yaml`
