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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `19.560%`
- winning mean component MAE: `0.072919`
- winning mean component RMSE: `0.203507`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 19.560 | 0.072919 | 0.203507 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003060 | 0.004528 | 26.232 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000030 | 0.000040 | 0.174 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002490 | 0.004235 | 52.482 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000033 | 0.000048 | 3.230 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.031162 | 0.049644 | 2.452 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000024 | 0.000033 | 5.196 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.333792 | 1.284876 | 11.600 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000028 | 0.000040 | 9.325 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.103830 | 0.180341 | 38.723 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000072 | 0.000100 | 8.815 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.108634 | 0.294243 | 29.486 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000011 | 0.000016 | 9.499 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.118665 | 0.155889 | 36.800 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000094 | 0.000371 | 12.213 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.121464 | 0.373320 | 72.592 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000069 | 0.000229 | 10.150 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.118773 | 0.280936 | 6.331 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000125 | 0.000252 | 16.417 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.443098 | 1.237491 | 19.918 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/002_track1_original_dataset_backward_et_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-17-33__track1_original_dataset_backward_et_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-17-33__track1_original_dataset_backward_et_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-17-33__track1_original_dataset_backward_et_attempt_02_campaign_validation/validation_summary.yaml`
