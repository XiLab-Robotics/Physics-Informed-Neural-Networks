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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `27.772%`
- winning mean component MAE: `0.086319`
- winning mean component RMSE: `0.204614`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 27.772 | 0.086319 | 0.204614 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 8}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003227 | 0.005308 | 21.684 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000031 | 0.000039 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002588 | 0.003443 | 55.172 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000026 | 0.000035 | 3.107 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.034266 | 0.049674 | 1.889 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000042 | 0.000055 | 3.763 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.031896 | 0.050285 | 2.706 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000035 | 0.000051 | 4.356 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.056063 | 0.087514 | 130.762 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000064 | 0.000091 | 11.441 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.117971 | 0.342954 | 57.576 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000015 | 0.000022 | 4.691 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.074423 | 0.120492 | 9.052 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000054 | 0.000175 | 14.977 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.537137 | 1.217929 | 33.016 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000086 | 0.000433 | 14.029 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.424188 | 1.097715 | 16.881 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000064 | 0.000102 | 14.412 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.357886 | 0.911355 | 127.979 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/002_track1_original_dataset_forward_dt_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-10-58__track1_original_dataset_forward_dt_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-10-58__track1_original_dataset_forward_dt_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-10-58__track1_original_dataset_forward_dt_attempt_02_campaign_validation/validation_summary.yaml`
