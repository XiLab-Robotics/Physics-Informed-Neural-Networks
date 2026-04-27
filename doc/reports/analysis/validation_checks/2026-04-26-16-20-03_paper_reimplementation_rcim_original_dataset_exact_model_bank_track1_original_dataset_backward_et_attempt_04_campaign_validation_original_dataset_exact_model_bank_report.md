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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `24.971%`
- winning mean component MAE: `0.055097`
- winning mean component RMSE: `0.156761`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 24.971 | 0.055097 | 0.156761 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003165 | 0.003976 | 54.367 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000033 | 0.000043 | 0.191 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.001899 | 0.002395 | 31.062 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000032 | 0.000051 | 3.400 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.027329 | 0.037995 | 2.096 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000023 | 0.000031 | 4.926 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.264037 | 1.130451 | 8.959 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000029 | 0.000045 | 9.736 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.117983 | 0.202442 | 30.815 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000064 | 0.000085 | 11.680 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.113624 | 0.308986 | 22.842 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000012 | 0.000019 | 9.262 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.111428 | 0.154080 | 219.860 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000230 | 0.000676 | 10.467 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.072498 | 0.119724 | 7.959 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000080 | 0.000193 | 11.422 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.053491 | 0.071256 | 3.114 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000216 | 0.000668 | 19.093 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.280670 | 0.945347 | 13.204 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/004_track1_original_dataset_backward_et_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-19-18__track1_original_dataset_backward_et_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-19-18__track1_original_dataset_backward_et_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-19-18__track1_original_dataset_backward_et_attempt_04_campaign_validation/validation_summary.yaml`
