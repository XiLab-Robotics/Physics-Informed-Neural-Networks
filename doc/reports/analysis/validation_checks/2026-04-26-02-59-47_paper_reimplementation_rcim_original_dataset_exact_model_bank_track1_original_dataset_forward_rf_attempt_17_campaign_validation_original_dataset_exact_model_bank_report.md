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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `19.860%`
- winning mean component MAE: `0.091223`
- winning mean component RMSE: `0.187163`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 19.860 | 0.091223 | 0.187163 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 80}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003571 | 0.004618 | 16.875 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000026 | 0.000035 | 0.151 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001858 | 0.002653 | 62.889 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000018 | 0.000026 | 2.198 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.023810 | 0.035009 | 1.328 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000031 | 0.000048 | 2.728 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.026776 | 0.043904 | 2.127 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000030 | 0.000050 | 3.915 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.039757 | 0.068951 | 74.119 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000044 | 0.000068 | 6.767 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.062685 | 0.158341 | 35.351 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000011 | 0.000019 | 3.315 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.059616 | 0.097517 | 7.837 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000088 | 0.000284 | 13.518 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.716415 | 1.428120 | 71.123 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000174 | 0.000879 | 10.872 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.382032 | 0.762488 | 18.953 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000049 | 0.000134 | 23.847 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.416256 | 0.952959 | 19.422 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/017_track1_original_dataset_forward_rf_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-56-36__track1_original_dataset_forward_rf_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-56-36__track1_original_dataset_forward_rf_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-56-36__track1_original_dataset_forward_rf_attempt_17_campaign_validation/validation_summary.yaml`
