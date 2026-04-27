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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `18.829%`
- winning mean component MAE: `0.059235`
- winning mean component RMSE: `0.174025`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 18.829 | 0.059235 | 0.174025 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003433 | 0.004966 | 58.203 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000035 | 0.000052 | 0.205 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002109 | 0.003119 | 71.890 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000035 | 0.000055 | 3.518 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.029367 | 0.061517 | 2.142 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000020 | 0.000027 | 4.467 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.333283 | 1.295840 | 11.192 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000035 | 0.000050 | 11.375 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.093434 | 0.138920 | 30.534 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000075 | 0.000098 | 8.715 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.083477 | 0.208083 | 21.348 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000012 | 0.000020 | 9.646 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.096147 | 0.135480 | 34.840 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000460 | 0.003118 | 12.142 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.100681 | 0.320318 | 7.685 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000062 | 0.000158 | 8.941 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.079890 | 0.173212 | 4.790 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000275 | 0.000905 | 36.268 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.302631 | 0.960530 | 19.860 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/003_track1_original_dataset_backward_et_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-18-26__track1_original_dataset_backward_et_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-18-26__track1_original_dataset_backward_et_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-18-26__track1_original_dataset_backward_et_attempt_03_campaign_validation/validation_summary.yaml`
