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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `161.440%`
- winning mean component MAE: `0.155894`
- winning mean component RMSE: `0.234565`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 161.440 | 0.155894 | 0.234565 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.007844 | 0.009362 | 23.833 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000037 | 0.000051 | 0.218 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.003078 | 0.004376 | 2097.439 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000061 | 0.000072 | 7.993 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.058777 | 0.083557 | 3.258 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000114 | 0.000133 | 11.156 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.090735 | 0.120198 | 7.188 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000051 | 0.000074 | 6.907 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.063037 | 0.090223 | 78.560 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000214 | 0.000257 | 76.044 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.182222 | 0.320484 | 162.470 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000028 | 0.000037 | 9.189 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.174722 | 0.229863 | 39.853 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000366 | 0.000766 | 187.129 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.101517 | 1.390392 | 82.944 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000408 | 0.000866 | 142.049 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.733929 | 1.146887 | 34.760 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000142 | 0.000249 | 55.985 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.544710 | 1.058880 | 40.387 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/018_track1_original_dataset_forward_lgbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-12-43-50__track1_original_dataset_forward_lgbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-12-43-50__track1_original_dataset_forward_lgbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-12-43-50__track1_original_dataset_forward_lgbm_attempt_18_campaign_validation/validation_summary.yaml`
