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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `18.749%`
- winning mean component MAE: `0.077304`
- winning mean component RMSE: `0.211494`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 18.749 | 0.077304 | 0.211494 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003158 | 0.004527 | 6.387 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000031 | 0.000041 | 0.179 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002358 | 0.003411 | 42.535 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000024 | 0.000034 | 2.880 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.025766 | 0.033190 | 1.414 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000037 | 0.000056 | 3.443 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.022745 | 0.034616 | 1.961 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000034 | 0.000049 | 4.215 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.041196 | 0.066541 | 86.875 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000052 | 0.000081 | 6.869 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.096890 | 0.323099 | 62.304 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000012 | 0.000018 | 3.853 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.060986 | 0.109585 | 7.740 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000101 | 0.000326 | 23.529 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.789585 | 1.858598 | 41.038 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000133 | 0.000370 | 13.878 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.172357 | 0.761335 | 8.166 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000047 | 0.000075 | 17.024 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.253264 | 0.822430 | 21.943 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/006_track1_original_dataset_forward_et_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-33-40__track1_original_dataset_forward_et_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-33-40__track1_original_dataset_forward_et_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-33-40__track1_original_dataset_forward_et_attempt_06_campaign_validation/validation_summary.yaml`
