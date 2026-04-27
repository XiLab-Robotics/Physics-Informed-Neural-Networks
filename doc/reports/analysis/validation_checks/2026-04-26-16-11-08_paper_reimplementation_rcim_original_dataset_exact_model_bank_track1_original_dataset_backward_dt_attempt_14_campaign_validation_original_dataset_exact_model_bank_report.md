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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `19.450%`
- winning mean component MAE: `0.051182`
- winning mean component RMSE: `0.170416`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 19.450 | 0.051182 | 0.170416 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003486 | 0.005194 | 41.032 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000032 | 0.000047 | 0.186 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002135 | 0.003897 | 62.750 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000025 | 0.000046 | 2.789 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.026141 | 0.036022 | 1.964 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000022 | 0.000032 | 5.437 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.241095 | 1.076576 | 8.537 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000026 | 0.000036 | 8.825 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.121665 | 0.229437 | 56.859 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000070 | 0.000094 | 8.755 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.065089 | 0.133073 | 39.279 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000020 | 8.632 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.131450 | 0.207721 | 57.680 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000151 | 0.000558 | 10.012 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.112611 | 0.421821 | 17.557 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000076 | 0.000244 | 8.023 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.122929 | 0.485019 | 5.608 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000073 | 0.000166 | 19.546 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.145374 | 0.637899 | 6.088 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/014_track1_original_dataset_backward_dt_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-10-22__track1_original_dataset_backward_dt_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-10-22__track1_original_dataset_backward_dt_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-10-22__track1_original_dataset_backward_dt_attempt_14_campaign_validation/validation_summary.yaml`
