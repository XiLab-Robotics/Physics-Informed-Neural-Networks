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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `13.890%`
- winning mean component MAE: `0.053248`
- winning mean component RMSE: `0.133627`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 13.890 | 0.053248 | 0.133627 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002596 | 0.003338 | 42.052 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000025 | 0.000033 | 0.143 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001520 | 0.002190 | 37.035 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000028 | 1.975 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.022196 | 0.031450 | 1.704 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000018 | 0.000025 | 3.952 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.173350 | 0.622383 | 5.990 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000028 | 0.000042 | 9.077 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.077761 | 0.109388 | 25.822 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000044 | 0.000064 | 5.189 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.058760 | 0.121923 | 19.350 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000015 | 7.211 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.087172 | 0.120865 | 46.220 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000081 | 0.000241 | 8.669 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.134467 | 0.407713 | 9.821 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000054 | 0.000141 | 6.087 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.064671 | 0.153908 | 3.230 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000107 | 0.000342 | 14.190 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.388825 | 0.964818 | 16.191 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/006_track1_original_dataset_backward_ert_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-50-03__track1_original_dataset_backward_ert_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-50-03__track1_original_dataset_backward_ert_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-50-03__track1_original_dataset_backward_ert_attempt_06_campaign_validation/validation_summary.yaml`
