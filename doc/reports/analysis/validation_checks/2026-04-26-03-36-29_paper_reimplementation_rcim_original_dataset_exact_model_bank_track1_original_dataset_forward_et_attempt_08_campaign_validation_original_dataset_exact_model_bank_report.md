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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `17.692%`
- winning mean component MAE: `0.056198`
- winning mean component RMSE: `0.156194`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 17.692 | 0.056198 | 0.156194 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003513 | 0.004334 | 6.738 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000029 | 0.000040 | 0.169 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002483 | 0.003099 | 41.620 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000027 | 0.000041 | 3.272 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.028149 | 0.036579 | 1.522 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000039 | 0.000056 | 3.306 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.027515 | 0.049164 | 2.404 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000029 | 0.000040 | 3.611 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.063294 | 0.113104 | 71.810 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000062 | 0.000092 | 11.992 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.075132 | 0.183319 | 100.190 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000015 | 0.000022 | 4.965 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.076967 | 0.111570 | 6.692 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000086 | 0.000283 | 13.796 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.482571 | 1.360280 | 21.960 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000051 | 0.000141 | 8.298 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.132855 | 0.459432 | 5.392 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000085 | 0.000223 | 18.872 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.174853 | 0.645875 | 9.530 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/008_track1_original_dataset_forward_et_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-35-39__track1_original_dataset_forward_et_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-35-39__track1_original_dataset_forward_et_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-35-39__track1_original_dataset_forward_et_attempt_08_campaign_validation/validation_summary.yaml`
