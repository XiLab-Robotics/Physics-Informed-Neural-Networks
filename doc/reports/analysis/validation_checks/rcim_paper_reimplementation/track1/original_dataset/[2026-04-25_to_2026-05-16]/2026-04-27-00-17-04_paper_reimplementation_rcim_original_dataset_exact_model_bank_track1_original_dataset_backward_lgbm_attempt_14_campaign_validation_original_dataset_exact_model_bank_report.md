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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `57.786%`
- winning mean component MAE: `0.156665`
- winning mean component RMSE: `0.239249`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 57.786 | 0.156665 | 0.239249 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.006048 | 0.007154 | 130.117 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000041 | 0.000073 | 0.241 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002283 | 0.004131 | 158.383 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000049 | 0.000072 | 5.267 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.084412 | 0.100275 | 6.097 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000039 | 0.000049 | 9.684 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 1.015597 | 1.309495 | 38.661 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000033 | 0.000043 | 12.000 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.166307 | 0.260388 | 53.224 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000254 | 0.000306 | 61.489 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.166014 | 0.302814 | 47.983 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000018 | 0.000026 | 13.715 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.191389 | 0.243141 | 145.423 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000484 | 0.000612 | 113.296 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.282749 | 0.524860 | 29.304 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000494 | 0.001180 | 158.631 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.480200 | 0.804970 | 23.671 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000198 | 0.000303 | 60.444 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.580026 | 0.985832 | 30.300 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/014_track1_original_dataset_backward_lgbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-55-03__track1_original_dataset_backward_lgbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-55-03__track1_original_dataset_backward_lgbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-55-03__track1_original_dataset_backward_lgbm_attempt_14_campaign_validation/validation_summary.yaml`
