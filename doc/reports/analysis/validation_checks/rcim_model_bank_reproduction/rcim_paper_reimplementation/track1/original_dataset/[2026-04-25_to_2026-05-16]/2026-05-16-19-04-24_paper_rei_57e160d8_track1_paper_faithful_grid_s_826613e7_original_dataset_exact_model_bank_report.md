# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/simplified_dataset`.

- direction label: `backward`
- dataset root: `data\simplified_dataset`
- dataset config: `config\datasets\transmission_error_dataset.yaml`
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
- winning mean component MAPE: `71.027%`
- winning mean component MAE: `0.237422`
- winning mean component RMSE: `0.337425`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ELM` | `ELMRegressor` | 71.027 | 0.237422 | 0.337425 | `{'estimator__alpha': 0.001, 'estimator__n_neurons': 100, 'estimator__ufunc': 'tanh'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ELM` | 0.007392 | 0.009747 | 176.780 |
| `fft_y_Bw_filtered_ampl_1` | `ELM` | 0.000030 | 0.000044 | 0.176 |
| `fft_y_Bw_filtered_phase_1` | `ELM` | 0.002945 | 0.003935 | 46.904 |
| `fft_y_Bw_filtered_ampl_3` | `ELM` | 0.000059 | 0.000078 | 6.275 |
| `fft_y_Bw_filtered_phase_3` | `ELM` | 0.080166 | 0.104573 | 5.970 |
| `fft_y_Bw_filtered_ampl_39` | `ELM` | 0.000055 | 0.000074 | 13.026 |
| `fft_y_Bw_filtered_phase_39` | `ELM` | 1.681690 | 2.195521 | 62.202 |
| `fft_y_Bw_filtered_ampl_40` | `ELM` | 0.000036 | 0.000047 | 12.173 |
| `fft_y_Bw_filtered_phase_40` | `ELM` | 0.176486 | 0.276721 | 111.360 |
| `fft_y_Bw_filtered_ampl_78` | `ELM` | 0.000280 | 0.000373 | 37.881 |
| `fft_y_Bw_filtered_phase_78` | `ELM` | 0.130431 | 0.169502 | 100.209 |
| `fft_y_Bw_filtered_ampl_81` | `ELM` | 0.000021 | 0.000027 | 18.795 |
| `fft_y_Bw_filtered_phase_81` | `ELM` | 0.179679 | 0.236343 | 71.664 |
| `fft_y_Bw_filtered_ampl_156` | `ELM` | 0.001044 | 0.001732 | 209.895 |
| `fft_y_Bw_filtered_phase_156` | `ELM` | 0.623933 | 0.976768 | 80.116 |
| `fft_y_Bw_filtered_ampl_162` | `ELM` | 0.001045 | 0.002398 | 225.391 |
| `fft_y_Bw_filtered_phase_162` | `ELM` | 0.874472 | 1.244618 | 49.127 |
| `fft_y_Bw_filtered_ampl_240` | `ELM` | 0.000440 | 0.001281 | 54.356 |
| `fft_y_Bw_filtered_phase_240` | `ELM` | 0.750818 | 1.187298 | 67.219 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\campaigns\track1\exact_paper\bidirectional_paper_faithful_grid_search\backward\elm\2026-05-04_track1_backward_elm_paper_faithful_grid_search_campaign\001_track1_paper_faithful_grid_search_backward_elm.yaml`
- output directory: `output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank\2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation`
- model bundle: `output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank\2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank\2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank\2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank\2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank\2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation\best_parameter_summary.yaml`
