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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `18.239%`
- winning mean component MAE: `0.043994`
- winning mean component RMSE: `0.116647`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 18.239 | 0.043994 | 0.116647 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002930 | 0.003729 | 67.615 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000023 | 0.000031 | 0.137 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001658 | 0.002314 | 73.159 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000027 | 0.000039 | 2.696 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.025104 | 0.035873 | 1.889 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000019 | 0.000028 | 4.407 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.201503 | 0.790466 | 7.098 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000028 | 0.000041 | 9.781 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.092374 | 0.142135 | 41.729 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000048 | 0.000071 | 6.003 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.050311 | 0.094394 | 17.630 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000018 | 7.987 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.079380 | 0.108187 | 35.600 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000097 | 0.000324 | 7.497 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.142475 | 0.495698 | 15.935 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000071 | 0.000191 | 6.999 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.062963 | 0.134787 | 3.646 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000115 | 0.000311 | 21.348 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.176745 | 0.407656 | 15.388 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/010_track1_original_dataset_backward_ert_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-02-56__track1_original_dataset_backward_ert_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-02-56__track1_original_dataset_backward_ert_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-02-56__track1_original_dataset_backward_ert_attempt_10_campaign_validation/validation_summary.yaml`
