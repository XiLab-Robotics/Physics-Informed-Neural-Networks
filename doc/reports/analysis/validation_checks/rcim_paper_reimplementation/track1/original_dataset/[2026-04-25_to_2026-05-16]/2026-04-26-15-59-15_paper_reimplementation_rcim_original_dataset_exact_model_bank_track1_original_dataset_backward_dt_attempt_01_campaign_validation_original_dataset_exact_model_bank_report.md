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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `24.109%`
- winning mean component MAE: `0.043209`
- winning mean component RMSE: `0.134447`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 24.109 | 0.043209 | 0.134447 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003622 | 0.005360 | 170.317 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000027 | 0.000040 | 0.155 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001841 | 0.002541 | 24.609 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000024 | 0.000037 | 2.512 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.024766 | 0.034187 | 1.877 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000020 | 0.000028 | 4.709 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.203102 | 0.824710 | 7.162 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000026 | 0.000037 | 8.423 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.101007 | 0.149163 | 63.001 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000053 | 0.000074 | 5.427 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.052384 | 0.088088 | 62.819 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000011 | 0.000016 | 9.716 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.091221 | 0.135455 | 43.877 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000132 | 0.000462 | 9.702 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.120792 | 0.641618 | 9.127 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000109 | 0.000574 | 6.855 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.053205 | 0.080937 | 2.959 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000120 | 0.000356 | 11.475 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.168514 | 0.590811 | 13.346 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/001_track1_original_dataset_backward_dt_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-58-28__track1_original_dataset_backward_dt_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-58-28__track1_original_dataset_backward_dt_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-58-28__track1_original_dataset_backward_dt_attempt_01_campaign_validation/validation_summary.yaml`
