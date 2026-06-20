# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/simplified_dataset`.

- direction label: `forward`
- dataset root: `data/simplified_dataset`
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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.
- workflow stage: `search`
- best-parameter source: `grid_search`
- historical wrapper `cross_validate(...)` replay: `True`

## Winner Summary

- winning family: `ELM`
- winning estimator: `ELMRegressor`
- winning mean component MAPE: `99.718%`
- winning mean component MAE: `0.206277`
- winning mean component RMSE: `0.277969`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ELM` | `ELMRegressor` | 99.718 | 0.206277 | 0.277969 | `{'estimator__alpha': 0.001, 'estimator__n_neurons': 100, 'estimator__ufunc': 'tanh'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ELM` | 0.006367 | 0.008485 | 12.077 |
| `fft_y_Fw_filtered_ampl_1` | `ELM` | 0.000034 | 0.000043 | 0.200 |
| `fft_y_Fw_filtered_phase_1` | `ELM` | 0.002693 | 0.003566 | 87.246 |
| `fft_y_Fw_filtered_ampl_3` | `ELM` | 0.000071 | 0.000092 | 8.879 |
| `fft_y_Fw_filtered_phase_3` | `ELM` | 0.066281 | 0.083062 | 3.641 |
| `fft_y_Fw_filtered_ampl_39` | `ELM` | 0.000106 | 0.000150 | 8.733 |
| `fft_y_Fw_filtered_phase_39` | `ELM` | 0.072284 | 0.097109 | 6.240 |
| `fft_y_Fw_filtered_ampl_40` | `ELM` | 0.000044 | 0.000064 | 5.959 |
| `fft_y_Fw_filtered_phase_40` | `ELM` | 0.065352 | 0.092202 | 77.685 |
| `fft_y_Fw_filtered_ampl_78` | `ELM` | 0.000254 | 0.000341 | 100.466 |
| `fft_y_Fw_filtered_phase_78` | `ELM` | 0.147244 | 0.201695 | 764.877 |
| `fft_y_Fw_filtered_ampl_81` | `ELM` | 0.000033 | 0.000042 | 11.464 |
| `fft_y_Fw_filtered_phase_81` | `ELM` | 0.154270 | 0.199579 | 14.340 |
| `fft_y_Fw_filtered_ampl_156` | `ELM` | 0.000661 | 0.001048 | 266.218 |
| `fft_y_Fw_filtered_phase_156` | `ELM` | 1.741823 | 2.081671 | 118.389 |
| `fft_y_Fw_filtered_ampl_162` | `ELM` | 0.000951 | 0.002286 | 239.732 |
| `fft_y_Fw_filtered_phase_162` | `ELM` | 1.026764 | 1.532469 | 49.414 |
| `fft_y_Fw_filtered_ampl_240` | `ELM` | 0.000314 | 0.000596 | 82.536 |
| `fft_y_Fw_filtered_phase_240` | `ELM` | 0.633718 | 0.976902 | 36.540 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/forward/elm/2026-05-04_track1_forward_elm_paper_faithful_grid_search_campaign/001_track1_paper_faithful_grid_search_forward_elm.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation/paper_family_model_bank.pkl`
- python export root: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation/python_export`
- ONNX export root: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation/onnx_export`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation/validation_summary.yaml`
- best-parameter summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation/best_parameter_summary.yaml`
