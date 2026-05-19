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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `26.290%`
- winning mean component MAE: `0.066851`
- winning mean component RMSE: `0.146005`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 26.290 | 0.066851 | 0.146005 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 8, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002475 | 0.003036 | 35.810 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000026 | 0.000036 | 0.153 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001509 | 0.002162 | 130.591 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000018 | 0.000027 | 1.879 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.019883 | 0.024378 | 1.448 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000015 | 0.000020 | 3.283 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.297366 | 0.737211 | 10.557 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000025 | 0.000040 | 9.190 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.100976 | 0.165974 | 66.467 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000037 | 0.000049 | 7.584 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.074907 | 0.159174 | 20.999 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 8.531 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.076459 | 0.103333 | 87.160 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000304 | 0.000973 | 20.463 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.185960 | 0.549359 | 37.411 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000101 | 0.000293 | 14.279 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.135485 | 0.293881 | 7.261 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000104 | 0.000192 | 19.112 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.374515 | 0.733949 | 17.324 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/015_track1_original_dataset_backward_lgbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-00-17-11__track1_original_dataset_backward_lgbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-00-17-11__track1_original_dataset_backward_lgbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-00-17-11__track1_original_dataset_backward_lgbm_attempt_15_campaign_validation/validation_summary.yaml`
