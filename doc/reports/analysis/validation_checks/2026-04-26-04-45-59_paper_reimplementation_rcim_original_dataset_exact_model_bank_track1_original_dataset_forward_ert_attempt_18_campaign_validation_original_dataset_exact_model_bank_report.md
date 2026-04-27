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

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `45.079%`
- winning mean component MAE: `0.072385`
- winning mean component RMSE: `0.175899`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 45.079 | 0.072385 | 0.175899 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.002986 | 0.003795 | 8.239 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000026 | 0.000042 | 0.154 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002472 | 0.003631 | 545.922 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000025 | 0.000039 | 3.195 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.029487 | 0.063956 | 1.592 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000030 | 0.000042 | 2.610 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.030784 | 0.057908 | 2.343 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000033 | 0.000058 | 4.449 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.044550 | 0.072854 | 74.772 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000038 | 0.000053 | 9.162 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.110108 | 0.268039 | 81.097 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000012 | 0.000019 | 3.819 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.056889 | 0.099859 | 6.400 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000061 | 0.000189 | 12.499 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.453713 | 0.960270 | 52.994 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000049 | 0.000119 | 8.588 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.296050 | 0.875543 | 12.710 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000030 | 0.000058 | 8.962 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.347981 | 0.935608 | 16.987 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/018_track1_original_dataset_forward_ert_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-42-53__track1_original_dataset_forward_ert_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-42-53__track1_original_dataset_forward_ert_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-42-53__track1_original_dataset_forward_ert_attempt_18_campaign_validation/validation_summary.yaml`
