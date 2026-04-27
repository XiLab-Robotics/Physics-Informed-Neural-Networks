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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `24.689%`
- winning mean component MAE: `0.108927`
- winning mean component RMSE: `0.268325`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 24.689 | 0.108927 | 0.268325 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.004187 | 0.005656 | 20.412 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000030 | 0.000043 | 0.175 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002782 | 0.004394 | 91.507 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000020 | 0.000027 | 2.499 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.026400 | 0.034846 | 1.462 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000038 | 0.000055 | 3.405 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.039603 | 0.071657 | 3.152 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000043 | 0.000071 | 5.670 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.064078 | 0.098775 | 146.739 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000053 | 0.000079 | 8.084 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.064332 | 0.118259 | 37.904 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000017 | 0.000030 | 5.350 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.076888 | 0.119839 | 9.579 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000046 | 0.000100 | 13.448 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.738329 | 1.699595 | 46.286 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000070 | 0.000261 | 9.737 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.486123 | 1.378811 | 23.020 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000053 | 0.000197 | 14.297 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.566528 | 1.565488 | 26.367 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/017_track1_original_dataset_forward_et_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-44-24__track1_original_dataset_forward_et_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-44-24__track1_original_dataset_forward_et_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-44-24__track1_original_dataset_forward_et_attempt_17_campaign_validation/validation_summary.yaml`
