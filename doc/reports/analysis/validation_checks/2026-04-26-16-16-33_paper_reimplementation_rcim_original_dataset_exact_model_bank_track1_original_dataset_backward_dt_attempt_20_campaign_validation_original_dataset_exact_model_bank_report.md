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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `17.818%`
- winning mean component MAE: `0.040869`
- winning mean component RMSE: `0.112062`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 17.818 | 0.040869 | 0.112062 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003474 | 0.004242 | 44.299 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000029 | 0.000041 | 0.168 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001905 | 0.002850 | 37.529 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000023 | 0.000031 | 2.490 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.023316 | 0.032021 | 1.719 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000020 | 0.000027 | 4.501 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.168640 | 0.801646 | 5.939 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000032 | 0.000052 | 9.867 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.106600 | 0.186088 | 45.083 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000065 | 0.000092 | 8.452 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.063306 | 0.109881 | 69.946 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000019 | 9.586 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.103136 | 0.138831 | 39.676 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000225 | 0.000776 | 14.664 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.095708 | 0.298867 | 6.476 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000074 | 0.000185 | 10.677 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.067443 | 0.129082 | 4.108 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000075 | 0.000170 | 9.990 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.142432 | 0.424271 | 13.366 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/020_track1_original_dataset_backward_dt_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-15-46__track1_original_dataset_backward_dt_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-15-46__track1_original_dataset_backward_dt_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-15-46__track1_original_dataset_backward_dt_attempt_20_campaign_validation/validation_summary.yaml`
