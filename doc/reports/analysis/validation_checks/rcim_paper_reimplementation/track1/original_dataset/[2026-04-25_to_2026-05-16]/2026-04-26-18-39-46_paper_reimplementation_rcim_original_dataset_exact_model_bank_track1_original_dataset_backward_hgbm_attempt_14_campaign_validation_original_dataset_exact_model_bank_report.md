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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `23.360%`
- winning mean component MAE: `0.065860`
- winning mean component RMSE: `0.138320`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 23.360 | 0.065860 | 0.138320 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002700 | 0.003700 | 48.252 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000025 | 0.000035 | 0.147 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.002072 | 0.003733 | 139.887 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000022 | 0.000038 | 2.347 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.019467 | 0.030139 | 1.417 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000017 | 0.000025 | 4.166 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.253396 | 0.545603 | 9.299 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000026 | 0.000034 | 9.052 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.091684 | 0.175903 | 31.415 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000036 | 0.000060 | 5.711 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.081109 | 0.152102 | 35.504 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000019 | 8.422 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.113257 | 0.157415 | 55.162 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000236 | 0.000846 | 13.109 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.162884 | 0.305871 | 22.556 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000089 | 0.000246 | 12.257 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.146868 | 0.378780 | 7.316 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000092 | 0.000175 | 18.451 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.377354 | 0.873359 | 19.362 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/014_track1_original_dataset_backward_hgbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-38-21__track1_original_dataset_backward_hgbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-38-21__track1_original_dataset_backward_hgbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-38-21__track1_original_dataset_backward_hgbm_attempt_14_campaign_validation/validation_summary.yaml`
