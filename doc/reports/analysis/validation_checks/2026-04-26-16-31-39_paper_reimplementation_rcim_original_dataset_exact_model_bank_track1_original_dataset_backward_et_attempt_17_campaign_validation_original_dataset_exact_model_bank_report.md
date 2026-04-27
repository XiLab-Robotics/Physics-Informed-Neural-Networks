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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `26.607%`
- winning mean component MAE: `0.074275`
- winning mean component RMSE: `0.205543`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 26.607 | 0.074275 | 0.205543 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003785 | 0.004725 | 69.583 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000036 | 0.000046 | 0.207 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002235 | 0.003100 | 89.614 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000036 | 0.000062 | 3.521 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.031202 | 0.056700 | 2.317 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000024 | 0.000033 | 5.419 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.368675 | 1.329026 | 12.662 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000037 | 0.000054 | 12.017 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.135597 | 0.228492 | 80.004 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000063 | 0.000093 | 7.442 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.077860 | 0.152991 | 69.476 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000014 | 0.000023 | 10.241 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.117200 | 0.168030 | 46.068 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000163 | 0.000630 | 7.319 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.177000 | 0.579741 | 38.261 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000360 | 0.001564 | 13.495 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.088209 | 0.210245 | 4.572 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000095 | 0.000186 | 13.823 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.408627 | 1.169570 | 19.492 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/017_track1_original_dataset_backward_et_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-30-53__track1_original_dataset_backward_et_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-30-53__track1_original_dataset_backward_et_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-30-53__track1_original_dataset_backward_et_attempt_17_campaign_validation/validation_summary.yaml`
