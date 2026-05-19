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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `22.203%`
- winning mean component MAE: `0.067994`
- winning mean component RMSE: `0.199015`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 22.203 | 0.067994 | 0.199015 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003161 | 0.004600 | 53.819 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000031 | 0.000041 | 0.181 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002017 | 0.002930 | 117.929 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000025 | 0.000037 | 2.541 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.024887 | 0.036080 | 1.872 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000024 | 0.000033 | 5.158 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.176818 | 0.884643 | 6.297 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000038 | 0.000057 | 12.293 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.106697 | 0.161268 | 48.178 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000055 | 0.000076 | 6.800 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.070877 | 0.137623 | 23.513 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000021 | 10.335 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.112881 | 0.167598 | 52.858 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000175 | 0.000554 | 14.323 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.166314 | 0.675994 | 11.621 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000113 | 0.000298 | 10.052 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.071891 | 0.170481 | 3.775 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000125 | 0.000405 | 16.680 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.555751 | 1.538546 | 23.629 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/006_track1_original_dataset_backward_et_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-21-05__track1_original_dataset_backward_et_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-21-05__track1_original_dataset_backward_et_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-21-05__track1_original_dataset_backward_et_attempt_06_campaign_validation/validation_summary.yaml`
