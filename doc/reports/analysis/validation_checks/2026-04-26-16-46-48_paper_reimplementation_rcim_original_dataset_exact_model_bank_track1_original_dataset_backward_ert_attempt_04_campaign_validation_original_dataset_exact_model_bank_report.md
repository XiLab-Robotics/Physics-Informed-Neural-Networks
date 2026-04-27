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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `25.372%`
- winning mean component MAE: `0.042495`
- winning mean component RMSE: `0.101449`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 25.372 | 0.042495 | 0.101449 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002762 | 0.003327 | 61.817 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000025 | 0.000035 | 0.144 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001618 | 0.002069 | 28.922 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000029 | 2.117 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.025772 | 0.035657 | 1.956 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000017 | 0.000023 | 3.575 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.224772 | 0.801574 | 7.732 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000023 | 0.000036 | 7.795 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.101610 | 0.178293 | 21.560 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000039 | 0.000053 | 8.095 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.056839 | 0.165402 | 21.961 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000014 | 6.930 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.092452 | 0.125412 | 267.359 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000095 | 0.000279 | 5.522 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.076083 | 0.124629 | 8.089 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000051 | 0.000178 | 6.457 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.046430 | 0.081086 | 3.075 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000080 | 0.000256 | 8.947 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.178705 | 0.409174 | 10.009 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/004_track1_original_dataset_backward_ert_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-43-46__track1_original_dataset_backward_ert_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-43-46__track1_original_dataset_backward_ert_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-43-46__track1_original_dataset_backward_ert_attempt_04_campaign_validation/validation_summary.yaml`
