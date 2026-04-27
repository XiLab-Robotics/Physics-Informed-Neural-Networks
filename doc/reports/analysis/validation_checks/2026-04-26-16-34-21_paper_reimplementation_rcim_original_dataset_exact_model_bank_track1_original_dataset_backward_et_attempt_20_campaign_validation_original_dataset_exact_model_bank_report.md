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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `21.448%`
- winning mean component MAE: `0.060967`
- winning mean component RMSE: `0.182043`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 21.448 | 0.060967 | 0.182043 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003181 | 0.004166 | 31.847 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000031 | 0.000041 | 0.179 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002080 | 0.003182 | 47.363 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000030 | 0.000046 | 3.192 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.027200 | 0.038236 | 2.016 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000021 | 0.000030 | 4.620 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.165229 | 0.877546 | 5.767 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000036 | 0.000055 | 11.088 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.115794 | 0.208689 | 62.969 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000072 | 0.000098 | 9.671 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.071861 | 0.117117 | 72.182 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000014 | 0.000023 | 11.310 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.107542 | 0.145250 | 49.094 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000336 | 0.001380 | 12.664 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.336766 | 1.045108 | 24.008 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000071 | 0.000165 | 12.176 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.068534 | 0.127880 | 4.218 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000184 | 0.000459 | 24.225 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.259400 | 0.889350 | 18.929 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/020_track1_original_dataset_backward_et_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-33-35__track1_original_dataset_backward_et_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-33-35__track1_original_dataset_backward_et_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-33-35__track1_original_dataset_backward_et_attempt_20_campaign_validation/validation_summary.yaml`
