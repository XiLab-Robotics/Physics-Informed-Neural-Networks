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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `18.996%`
- winning mean component MAE: `0.048112`
- winning mean component RMSE: `0.120877`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 18.996 | 0.048112 | 0.120877 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002885 | 0.003507 | 72.291 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000025 | 0.000036 | 0.144 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.002027 | 0.003271 | 106.646 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000026 | 0.000045 | 2.472 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.023669 | 0.032223 | 1.791 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000017 | 0.000025 | 3.857 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.316977 | 0.983216 | 10.765 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000028 | 0.000041 | 9.111 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.084199 | 0.117981 | 23.588 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000045 | 0.000066 | 4.755 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.058780 | 0.108580 | 13.834 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000010 | 0.000015 | 8.215 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.094841 | 0.126592 | 49.455 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000145 | 0.000604 | 9.982 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.095107 | 0.248134 | 17.618 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000049 | 0.000140 | 5.247 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.080448 | 0.202390 | 4.554 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000057 | 0.000114 | 9.158 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.154798 | 0.469688 | 7.446 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/019_track1_original_dataset_backward_rf_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-51-52__track1_original_dataset_backward_rf_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-51-52__track1_original_dataset_backward_rf_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-51-52__track1_original_dataset_backward_rf_attempt_19_campaign_validation/validation_summary.yaml`
