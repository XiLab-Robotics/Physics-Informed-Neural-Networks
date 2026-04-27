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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `14.830%`
- winning mean component MAE: `0.044193`
- winning mean component RMSE: `0.117520`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 14.830 | 0.044193 | 0.117520 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 80}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003304 | 0.004155 | 30.575 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000035 | 0.143 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001746 | 0.002273 | 28.702 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000025 | 0.000036 | 2.577 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.020340 | 0.025695 | 1.544 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000018 | 0.000028 | 3.796 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.233400 | 0.809421 | 8.021 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000028 | 0.000041 | 8.464 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.088611 | 0.137511 | 34.122 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000037 | 0.000051 | 5.396 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.057421 | 0.111026 | 40.607 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000008 | 0.000012 | 7.104 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.085924 | 0.120718 | 71.525 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000053 | 0.000141 | 4.963 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.065374 | 0.225295 | 5.416 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000045 | 0.000113 | 4.478 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.042099 | 0.080978 | 2.420 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000096 | 0.000247 | 11.908 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.241111 | 0.715096 | 10.011 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/008_track1_original_dataset_backward_ert_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-56-26__track1_original_dataset_backward_ert_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-56-26__track1_original_dataset_backward_ert_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-56-26__track1_original_dataset_backward_ert_attempt_08_campaign_validation/validation_summary.yaml`
