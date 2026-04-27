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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `38.423%`
- winning mean component MAE: `0.083450`
- winning mean component RMSE: `0.215799`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 38.423 | 0.083450 | 0.215799 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003390 | 0.004250 | 6.808 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000028 | 0.000038 | 0.162 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002282 | 0.003253 | 194.982 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000021 | 0.000029 | 2.550 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.029793 | 0.038118 | 1.664 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000042 | 0.000054 | 3.763 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.023959 | 0.033442 | 2.017 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000033 | 0.000057 | 3.975 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.047072 | 0.067262 | 80.408 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000050 | 0.000080 | 9.828 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.104841 | 0.287963 | 288.102 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000015 | 0.000022 | 5.207 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.076764 | 0.103940 | 6.882 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000093 | 0.000282 | 19.031 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.638243 | 1.525133 | 43.579 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000046 | 0.000107 | 10.394 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.414330 | 1.350640 | 15.315 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000052 | 0.000091 | 17.140 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.244506 | 0.685425 | 18.232 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/015_track1_original_dataset_forward_et_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-42-29__track1_original_dataset_forward_et_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-42-29__track1_original_dataset_forward_et_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-42-29__track1_original_dataset_forward_et_attempt_15_campaign_validation/validation_summary.yaml`
