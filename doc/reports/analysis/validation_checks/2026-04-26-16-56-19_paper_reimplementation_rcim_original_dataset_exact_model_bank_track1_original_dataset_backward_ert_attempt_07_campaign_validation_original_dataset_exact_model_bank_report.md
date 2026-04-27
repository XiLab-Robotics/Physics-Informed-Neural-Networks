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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `21.653%`
- winning mean component MAE: `0.050291`
- winning mean component RMSE: `0.141437`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 21.653 | 0.050291 | 0.141437 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 80}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003175 | 0.003885 | 37.307 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000018 | 0.000026 | 0.102 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001774 | 0.002630 | 39.807 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000028 | 0.000041 | 2.874 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.023413 | 0.039189 | 1.742 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000019 | 0.000027 | 4.416 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.214270 | 0.775648 | 7.511 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000042 | 8.405 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.084200 | 0.161900 | 23.434 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000046 | 0.000070 | 5.449 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.048236 | 0.103205 | 15.944 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000008 | 0.000013 | 6.678 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.095789 | 0.140435 | 181.008 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000056 | 0.000119 | 6.250 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.116544 | 0.539545 | 39.016 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000053 | 0.000180 | 6.003 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.059301 | 0.147095 | 3.752 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000057 | 0.000121 | 8.560 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.308520 | 0.773128 | 13.156 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/007_track1_original_dataset_backward_ert_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-53-11__track1_original_dataset_backward_ert_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-53-11__track1_original_dataset_backward_ert_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-53-11__track1_original_dataset_backward_ert_attempt_07_campaign_validation/validation_summary.yaml`
