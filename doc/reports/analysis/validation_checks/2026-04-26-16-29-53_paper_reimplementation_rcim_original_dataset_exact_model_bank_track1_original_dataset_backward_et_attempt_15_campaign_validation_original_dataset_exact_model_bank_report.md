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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `39.275%`
- winning mean component MAE: `0.054409`
- winning mean component RMSE: `0.169946`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 39.275 | 0.054409 | 0.169946 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003148 | 0.004243 | 30.808 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000030 | 0.000039 | 0.174 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002187 | 0.003429 | 69.328 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000030 | 0.000047 | 3.247 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.024494 | 0.033920 | 1.820 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000025 | 0.000035 | 5.569 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.113296 | 0.633153 | 4.336 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000030 | 0.000045 | 10.317 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.121331 | 0.217237 | 110.366 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000058 | 0.000074 | 9.201 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.099690 | 0.327539 | 26.361 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000023 | 10.776 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.122103 | 0.181876 | 397.129 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000195 | 0.000618 | 8.887 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.130253 | 0.641112 | 15.218 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000056 | 0.000131 | 10.203 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.071337 | 0.121307 | 4.044 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000083 | 0.000175 | 12.045 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.345408 | 1.063977 | 16.388 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/015_track1_original_dataset_backward_et_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-29-07__track1_original_dataset_backward_et_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-29-07__track1_original_dataset_backward_et_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-29-07__track1_original_dataset_backward_et_attempt_15_campaign_validation/validation_summary.yaml`
