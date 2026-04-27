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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `13.895%`
- winning mean component MAE: `0.045090`
- winning mean component RMSE: `0.119478`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 13.895 | 0.045090 | 0.119478 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003056 | 0.003686 | 31.544 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000023 | 0.000033 | 0.133 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001671 | 0.002379 | 38.270 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000023 | 0.000033 | 2.330 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.020862 | 0.025708 | 1.606 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000018 | 0.000029 | 3.749 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.238590 | 0.788896 | 8.125 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000027 | 0.000041 | 8.272 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.085059 | 0.129569 | 40.007 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000038 | 0.000054 | 5.363 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.051320 | 0.097326 | 26.356 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000008 | 0.000011 | 6.756 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.083733 | 0.122942 | 52.354 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000099 | 0.000288 | 6.418 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.070238 | 0.161691 | 6.415 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000050 | 0.000128 | 4.687 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.059177 | 0.203653 | 2.849 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000084 | 0.000222 | 8.806 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.242638 | 0.733389 | 9.970 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/008_track1_original_dataset_backward_rf_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-15-49__track1_original_dataset_backward_rf_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-15-49__track1_original_dataset_backward_rf_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-15-49__track1_original_dataset_backward_rf_attempt_08_campaign_validation/validation_summary.yaml`
