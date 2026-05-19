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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `46.843%`
- winning mean component MAE: `0.073597`
- winning mean component RMSE: `0.209194`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 46.843 | 0.073597 | 0.209194 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003586 | 0.004936 | 14.385 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000030 | 0.000041 | 0.177 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002322 | 0.003375 | 466.579 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000025 | 0.000040 | 3.106 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.034428 | 0.061296 | 1.937 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000041 | 0.000055 | 3.589 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.030495 | 0.057357 | 2.497 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000037 | 0.000067 | 4.798 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.051826 | 0.081088 | 116.687 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000059 | 0.000083 | 15.677 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.078854 | 0.189663 | 121.430 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000013 | 0.000018 | 4.627 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.071767 | 0.105846 | 6.135 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000088 | 0.000316 | 16.292 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.579567 | 1.460831 | 27.089 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000122 | 0.000435 | 15.458 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.259882 | 1.001301 | 13.121 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000132 | 0.000373 | 42.935 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.285069 | 1.007560 | 13.491 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/009_track1_original_dataset_forward_et_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-36-36__track1_original_dataset_forward_et_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-36-36__track1_original_dataset_forward_et_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-36-36__track1_original_dataset_forward_et_attempt_09_campaign_validation/validation_summary.yaml`
