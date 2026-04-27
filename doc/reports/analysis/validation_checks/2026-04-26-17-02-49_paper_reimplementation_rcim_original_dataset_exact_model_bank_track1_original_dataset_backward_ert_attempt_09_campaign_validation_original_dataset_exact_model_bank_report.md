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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `15.569%`
- winning mean component MAE: `0.050251`
- winning mean component RMSE: `0.122626`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 15.569 | 0.050251 | 0.122626 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002890 | 0.003729 | 39.316 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000021 | 0.000031 | 0.121 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001626 | 0.002421 | 33.444 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000021 | 0.000031 | 2.137 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.020701 | 0.029842 | 1.572 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000017 | 0.000027 | 3.861 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.321178 | 0.931182 | 10.873 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000023 | 0.000033 | 7.727 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.076289 | 0.139567 | 22.473 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000041 | 0.000058 | 5.900 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.045909 | 0.086196 | 36.471 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000008 | 0.000012 | 6.621 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.092176 | 0.132304 | 64.217 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000097 | 0.000320 | 7.331 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.113358 | 0.391600 | 14.079 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000055 | 0.000137 | 7.103 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.078174 | 0.230687 | 4.477 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000061 | 0.000088 | 13.391 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.202129 | 0.381626 | 14.702 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/009_track1_original_dataset_backward_ert_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-59-47__track1_original_dataset_backward_ert_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-59-47__track1_original_dataset_backward_ert_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-59-47__track1_original_dataset_backward_ert_attempt_09_campaign_validation/validation_summary.yaml`
