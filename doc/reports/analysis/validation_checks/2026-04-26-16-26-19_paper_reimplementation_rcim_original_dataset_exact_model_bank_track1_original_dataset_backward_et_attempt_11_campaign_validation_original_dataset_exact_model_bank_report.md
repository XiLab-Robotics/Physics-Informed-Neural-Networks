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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `26.545%`
- winning mean component MAE: `0.052322`
- winning mean component RMSE: `0.146381`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 26.545 | 0.052322 | 0.146381 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003289 | 0.004093 | 85.497 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000029 | 0.000039 | 0.168 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002117 | 0.002869 | 43.203 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000025 | 0.000035 | 2.580 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.028449 | 0.039889 | 2.159 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000025 | 0.000034 | 5.637 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.114874 | 0.454000 | 4.384 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000032 | 0.000047 | 10.619 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.091107 | 0.125636 | 38.618 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000074 | 0.000102 | 8.084 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.099013 | 0.312841 | 28.138 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000014 | 0.000022 | 12.135 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.102989 | 0.139144 | 175.808 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000211 | 0.000806 | 14.499 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.128983 | 0.464622 | 11.774 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000128 | 0.000666 | 8.361 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.110649 | 0.382445 | 6.656 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000132 | 0.000345 | 19.848 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.311971 | 0.853605 | 26.182 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/011_track1_original_dataset_backward_et_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-25-33__track1_original_dataset_backward_et_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-25-33__track1_original_dataset_backward_et_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-25-33__track1_original_dataset_backward_et_attempt_11_campaign_validation/validation_summary.yaml`
