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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `35.570%`
- winning mean component MAE: `0.055221`
- winning mean component RMSE: `0.158468`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 35.570 | 0.055221 | 0.158468 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003516 | 0.004636 | 51.526 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000034 | 0.000046 | 0.196 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002436 | 0.004124 | 173.968 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000030 | 0.000048 | 2.999 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.030896 | 0.057070 | 2.291 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000025 | 0.000038 | 5.521 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.233201 | 0.999435 | 8.045 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000037 | 0.000057 | 11.865 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.105886 | 0.153379 | 180.794 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000066 | 0.000094 | 6.916 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.097938 | 0.308441 | 37.330 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000022 | 10.219 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.128474 | 0.189288 | 105.212 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000154 | 0.000545 | 8.586 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.091750 | 0.229405 | 7.649 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000082 | 0.000294 | 8.390 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.101867 | 0.272580 | 7.119 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000117 | 0.000274 | 19.458 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.252676 | 0.791106 | 27.755 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/005_track1_original_dataset_backward_et_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-20-10__track1_original_dataset_backward_et_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-20-10__track1_original_dataset_backward_et_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-20-10__track1_original_dataset_backward_et_attempt_05_campaign_validation/validation_summary.yaml`
