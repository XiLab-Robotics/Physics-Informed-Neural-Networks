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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `25.652%`
- winning mean component MAE: `0.057406`
- winning mean component RMSE: `0.178572`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 25.652 | 0.057406 | 0.178572 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003425 | 0.005050 | 40.223 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000036 | 0.000057 | 0.207 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002207 | 0.003784 | 48.832 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000027 | 0.000048 | 2.662 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.028921 | 0.059775 | 2.143 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000021 | 0.000028 | 4.770 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.181692 | 0.891360 | 6.594 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000033 | 0.000052 | 11.162 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.108926 | 0.193252 | 110.402 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000060 | 0.000079 | 9.611 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.141191 | 0.455323 | 37.040 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000012 | 0.000017 | 9.745 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.145406 | 0.210510 | 123.921 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000167 | 0.000568 | 8.590 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.106846 | 0.241654 | 11.653 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000074 | 0.000196 | 7.677 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.111110 | 0.497477 | 6.546 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000113 | 0.000253 | 28.995 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.260443 | 0.833387 | 16.619 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/018_track1_original_dataset_backward_et_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-31-46__track1_original_dataset_backward_et_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-31-46__track1_original_dataset_backward_et_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-31-46__track1_original_dataset_backward_et_attempt_18_campaign_validation/validation_summary.yaml`
