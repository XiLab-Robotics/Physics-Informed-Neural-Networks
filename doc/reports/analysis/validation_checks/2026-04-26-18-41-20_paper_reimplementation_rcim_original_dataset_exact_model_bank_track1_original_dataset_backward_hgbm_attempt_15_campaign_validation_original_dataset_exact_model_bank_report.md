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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `25.740%`
- winning mean component MAE: `0.057000`
- winning mean component RMSE: `0.135573`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 25.740 | 0.057000 | 0.135573 | `{'estimator__learning_rate': 0.22, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002543 | 0.003352 | 33.448 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000026 | 0.000035 | 0.152 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001461 | 0.001985 | 123.456 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000018 | 0.000027 | 1.867 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.019445 | 0.024724 | 1.434 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000015 | 0.000021 | 3.251 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.247857 | 0.724098 | 8.708 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000024 | 0.000040 | 8.852 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.094781 | 0.165636 | 52.746 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000037 | 0.000047 | 5.959 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.075044 | 0.162838 | 20.527 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000008 | 0.000012 | 7.357 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.078516 | 0.107151 | 138.343 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000281 | 0.000952 | 12.734 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.142155 | 0.519510 | 21.996 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000103 | 0.000289 | 11.030 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.099277 | 0.247986 | 5.119 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000098 | 0.000193 | 17.401 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.321316 | 0.616985 | 14.685 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/015_track1_original_dataset_backward_hgbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-39-54__track1_original_dataset_backward_hgbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-39-54__track1_original_dataset_backward_hgbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-39-54__track1_original_dataset_backward_hgbm_attempt_15_campaign_validation/validation_summary.yaml`
