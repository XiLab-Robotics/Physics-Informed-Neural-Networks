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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `57.614%`
- winning mean component MAE: `0.148595`
- winning mean component RMSE: `0.222596`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 57.614 | 0.148595 | 0.222596 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006526 | 0.008399 | 30.784 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000030 | 0.000040 | 0.173 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002880 | 0.004261 | 49.808 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000050 | 0.000062 | 6.806 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.049277 | 0.062059 | 2.801 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000112 | 0.000128 | 10.896 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.080108 | 0.100980 | 6.624 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000042 | 0.000061 | 5.590 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.077221 | 0.108616 | 163.142 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000187 | 0.000222 | 136.479 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.195332 | 0.382791 | 75.265 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000031 | 7.854 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.167142 | 0.211622 | 31.150 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000370 | 0.000852 | 236.992 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.170487 | 1.457207 | 66.663 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000631 | 0.001745 | 149.406 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.648766 | 0.990595 | 42.901 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000142 | 0.000254 | 50.325 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.423980 | 0.899392 | 21.003 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/007_track1_original_dataset_forward_lgbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-08-39-56__track1_original_dataset_forward_lgbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-08-39-56__track1_original_dataset_forward_lgbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-08-39-56__track1_original_dataset_forward_lgbm_attempt_07_campaign_validation/validation_summary.yaml`
