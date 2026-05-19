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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `22.337%`
- winning mean component MAE: `0.065373`
- winning mean component RMSE: `0.196866`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 22.337 | 0.065373 | 0.196866 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003154 | 0.004205 | 62.703 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000038 | 0.000052 | 0.223 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002829 | 0.004795 | 86.874 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000032 | 0.000049 | 3.254 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.029724 | 0.043116 | 2.269 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000029 | 0.000044 | 6.832 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.249743 | 1.092059 | 8.825 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000035 | 0.000055 | 12.369 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.140827 | 0.238811 | 75.714 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000069 | 0.000100 | 8.803 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.063546 | 0.136568 | 30.178 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000022 | 10.136 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.106339 | 0.159008 | 34.073 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000164 | 0.000541 | 7.769 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.191424 | 0.770310 | 12.381 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000080 | 0.000207 | 8.209 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.091849 | 0.227964 | 5.040 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000165 | 0.000532 | 15.415 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.362023 | 1.062022 | 33.330 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/010_track1_original_dataset_backward_et_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-24-40__track1_original_dataset_backward_et_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-24-40__track1_original_dataset_backward_et_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-24-40__track1_original_dataset_backward_et_attempt_10_campaign_validation/validation_summary.yaml`
