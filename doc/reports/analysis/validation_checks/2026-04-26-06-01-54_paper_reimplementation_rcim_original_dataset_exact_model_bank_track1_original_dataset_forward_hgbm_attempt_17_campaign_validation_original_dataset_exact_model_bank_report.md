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

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `27.659%`
- winning mean component MAE: `0.104482`
- winning mean component RMSE: `0.184584`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 27.659 | 0.104482 | 0.184584 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002725 | 0.003918 | 15.108 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000026 | 0.000035 | 0.149 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001986 | 0.002684 | 61.413 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000023 | 2.104 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.021058 | 0.029829 | 1.181 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000039 | 2.114 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.021129 | 0.030856 | 1.702 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000028 | 0.000044 | 3.622 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.041231 | 0.071258 | 134.907 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000052 | 5.631 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.084516 | 0.161941 | 46.667 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000012 | 0.000019 | 3.832 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.057326 | 0.091536 | 7.216 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000131 | 0.000387 | 21.920 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.836912 | 1.413000 | 111.128 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000140 | 0.000453 | 19.582 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.460400 | 0.804603 | 23.098 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000048 | 0.000110 | 36.322 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.457426 | 0.896301 | 27.823 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/017_track1_original_dataset_forward_hgbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-00-26__track1_original_dataset_forward_hgbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-00-26__track1_original_dataset_forward_hgbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-00-26__track1_original_dataset_forward_hgbm_attempt_17_campaign_validation/validation_summary.yaml`
