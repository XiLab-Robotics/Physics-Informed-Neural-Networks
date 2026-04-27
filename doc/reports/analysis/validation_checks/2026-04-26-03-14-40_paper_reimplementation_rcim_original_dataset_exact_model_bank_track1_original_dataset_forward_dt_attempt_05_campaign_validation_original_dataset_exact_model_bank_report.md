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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `18.621%`
- winning mean component MAE: `0.085567`
- winning mean component RMSE: `0.221753`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 18.621 | 0.085567 | 0.221753 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.004015 | 0.005495 | 7.886 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000033 | 0.000043 | 0.193 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002585 | 0.003968 | 32.345 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000020 | 0.000027 | 2.393 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.029137 | 0.040327 | 1.594 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000038 | 0.000052 | 3.352 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.023425 | 0.043798 | 1.944 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000031 | 0.000047 | 3.725 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.046312 | 0.076411 | 51.900 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000048 | 0.000063 | 18.690 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.081095 | 0.292505 | 110.993 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000013 | 0.000020 | 4.283 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.066619 | 0.099193 | 5.952 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000088 | 0.000279 | 13.744 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.813675 | 1.802145 | 50.948 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000056 | 0.000174 | 8.032 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.358895 | 1.088486 | 14.954 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000040 | 0.000070 | 10.322 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.199656 | 0.760201 | 10.542 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/005_track1_original_dataset_forward_dt_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-13-49__track1_original_dataset_forward_dt_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-13-49__track1_original_dataset_forward_dt_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-13-49__track1_original_dataset_forward_dt_attempt_05_campaign_validation/validation_summary.yaml`
