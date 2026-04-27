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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `25.109%`
- winning mean component MAE: `0.048172`
- winning mean component RMSE: `0.132402`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 25.109 | 0.048172 | 0.132402 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003665 | 0.004905 | 86.938 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000023 | 0.000034 | 0.135 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001574 | 0.002131 | 77.623 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000026 | 0.000045 | 2.721 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.025832 | 0.038430 | 1.882 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000020 | 0.000029 | 4.688 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.191802 | 0.730271 | 6.746 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000024 | 0.000037 | 7.735 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.111785 | 0.228922 | 27.254 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000047 | 0.000070 | 6.454 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.071919 | 0.191331 | 19.105 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000016 | 7.280 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.093414 | 0.151891 | 158.570 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000162 | 0.000588 | 8.026 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.124345 | 0.472493 | 17.278 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000042 | 0.000094 | 6.568 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.064062 | 0.134556 | 3.230 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000058 | 0.000095 | 15.553 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.226453 | 0.559693 | 19.288 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/013_track1_original_dataset_backward_ert_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-12-21__track1_original_dataset_backward_ert_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-12-21__track1_original_dataset_backward_ert_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-12-21__track1_original_dataset_backward_ert_attempt_13_campaign_validation/validation_summary.yaml`
