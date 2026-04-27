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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `50.178%`
- winning mean component MAE: `0.092811`
- winning mean component RMSE: `0.222925`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 50.178 | 0.092811 | 0.222925 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.002895 | 0.003730 | 5.759 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000028 | 0.000039 | 0.163 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002584 | 0.003478 | 71.430 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000022 | 0.000034 | 2.605 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.028529 | 0.038333 | 1.560 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000049 | 0.000076 | 4.094 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.033325 | 0.064559 | 2.830 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000037 | 0.000059 | 4.573 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.060887 | 0.096555 | 139.241 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000070 | 0.000094 | 10.385 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.128438 | 0.357538 | 99.800 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000019 | 0.000028 | 5.992 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.084323 | 0.130605 | 7.765 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000059 | 0.000123 | 25.485 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.685118 | 1.401024 | 54.978 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000090 | 0.000385 | 11.482 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.479468 | 1.434083 | 21.300 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000055 | 0.000139 | 14.245 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.257419 | 0.704693 | 469.698 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/019_track1_original_dataset_forward_et_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-46-21__track1_original_dataset_forward_et_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-46-21__track1_original_dataset_forward_et_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-46-21__track1_original_dataset_forward_et_attempt_19_campaign_validation/validation_summary.yaml`
