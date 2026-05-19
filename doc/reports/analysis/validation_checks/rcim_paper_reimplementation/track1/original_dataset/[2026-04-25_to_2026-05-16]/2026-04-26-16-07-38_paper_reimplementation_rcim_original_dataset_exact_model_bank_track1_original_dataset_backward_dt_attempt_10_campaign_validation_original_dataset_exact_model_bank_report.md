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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `19.852%`
- winning mean component MAE: `0.048935`
- winning mean component RMSE: `0.146276`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 19.852 | 0.048935 | 0.146276 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003561 | 0.004519 | 59.716 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000029 | 0.000039 | 0.169 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002131 | 0.003523 | 83.698 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000032 | 0.000049 | 3.287 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.026893 | 0.039358 | 2.001 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000023 | 0.000031 | 5.227 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.308149 | 1.172182 | 10.783 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000033 | 0.000049 | 11.399 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.117345 | 0.161013 | 67.985 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000067 | 0.000091 | 7.956 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.059955 | 0.124965 | 26.925 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000020 | 9.840 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.092483 | 0.129345 | 35.169 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000137 | 0.000410 | 7.421 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.168404 | 0.805010 | 10.213 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000065 | 0.000169 | 6.872 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.061795 | 0.172447 | 3.349 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000135 | 0.000355 | 14.523 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.088510 | 0.165663 | 10.656 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/010_track1_original_dataset_backward_dt_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-06-52__track1_original_dataset_backward_dt_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-06-52__track1_original_dataset_backward_dt_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-06-52__track1_original_dataset_backward_dt_attempt_10_campaign_validation/validation_summary.yaml`
