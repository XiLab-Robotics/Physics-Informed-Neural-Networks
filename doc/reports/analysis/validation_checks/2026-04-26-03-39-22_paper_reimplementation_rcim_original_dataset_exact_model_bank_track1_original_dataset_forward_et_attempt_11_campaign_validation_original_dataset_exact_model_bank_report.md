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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `28.810%`
- winning mean component MAE: `0.089776`
- winning mean component RMSE: `0.215551`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 28.810 | 0.089776 | 0.215551 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003479 | 0.004271 | 6.805 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000034 | 0.000044 | 0.196 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002765 | 0.003743 | 56.750 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000031 | 0.000045 | 3.817 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.025455 | 0.035136 | 1.430 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000044 | 0.000055 | 3.953 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.028701 | 0.045592 | 2.379 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000034 | 0.000048 | 4.478 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.045756 | 0.065626 | 254.029 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000056 | 0.000082 | 10.324 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.117915 | 0.363447 | 72.065 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000015 | 0.000019 | 4.666 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.071002 | 0.121641 | 8.081 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000105 | 0.000366 | 23.445 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.744771 | 1.500561 | 35.840 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000137 | 0.000801 | 12.591 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.482508 | 1.467866 | 19.459 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000047 | 0.000084 | 12.784 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.182881 | 0.486052 | 14.298 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/011_track1_original_dataset_forward_et_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-38-34__track1_original_dataset_forward_et_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-38-34__track1_original_dataset_forward_et_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-38-34__track1_original_dataset_forward_et_attempt_11_campaign_validation/validation_summary.yaml`
