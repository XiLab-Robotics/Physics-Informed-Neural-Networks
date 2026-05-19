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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `27.074%`
- winning mean component MAE: `0.073491`
- winning mean component RMSE: `0.211351`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 27.074 | 0.073491 | 0.211351 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003708 | 0.004683 | 7.433 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000035 | 0.000045 | 0.204 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002407 | 0.003772 | 52.299 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000024 | 0.000034 | 2.895 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.027431 | 0.036549 | 1.505 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000042 | 0.000057 | 3.643 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.034489 | 0.065654 | 2.842 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000032 | 0.000048 | 4.119 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.058895 | 0.098907 | 121.639 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000065 | 0.000098 | 8.785 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.114839 | 0.267164 | 154.396 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000015 | 0.000020 | 4.803 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.075677 | 0.122668 | 6.729 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000043 | 0.000133 | 17.680 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.592741 | 1.502326 | 37.698 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000059 | 0.000189 | 10.397 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.246222 | 1.002621 | 10.504 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000042 | 0.000076 | 11.932 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.239556 | 0.910620 | 54.909 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/019_track1_original_dataset_forward_dt_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-26-49__track1_original_dataset_forward_dt_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-26-49__track1_original_dataset_forward_dt_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-26-49__track1_original_dataset_forward_dt_attempt_19_campaign_validation/validation_summary.yaml`
