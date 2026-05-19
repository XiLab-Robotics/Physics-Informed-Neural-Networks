# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `29.135%`
- winning mean component MAE: `0.086166`
- winning mean component RMSE: `0.199910`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 29.135 | 0.086166 | 0.199910 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.002898 | 0.003632 | 6.068 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000029 | 0.000039 | 0.170 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002208 | 0.003068 | 39.101 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000022 | 0.000031 | 2.698 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.029315 | 0.041647 | 1.620 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000042 | 0.000054 | 3.591 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.032888 | 0.055182 | 2.566 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000027 | 0.000040 | 3.417 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.049673 | 0.075338 | 157.907 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000064 | 0.000087 | 14.018 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.115083 | 0.246875 | 102.270 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000015 | 0.000021 | 4.813 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.087324 | 0.133199 | 9.766 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000144 | 0.000497 | 25.445 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.682543 | 1.487788 | 61.492 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000067 | 0.000161 | 11.445 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.259772 | 0.706191 | 10.669 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000124 | 0.000404 | 14.125 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.374918 | 1.044038 | 82.394 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/010_track1_original_dataset_forward_et_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-37-36__track1_original_dataset_forward_et_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-37-36__track1_original_dataset_forward_et_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-37-36__track1_original_dataset_forward_et_attempt_10_campaign_validation/validation_summary.yaml`
