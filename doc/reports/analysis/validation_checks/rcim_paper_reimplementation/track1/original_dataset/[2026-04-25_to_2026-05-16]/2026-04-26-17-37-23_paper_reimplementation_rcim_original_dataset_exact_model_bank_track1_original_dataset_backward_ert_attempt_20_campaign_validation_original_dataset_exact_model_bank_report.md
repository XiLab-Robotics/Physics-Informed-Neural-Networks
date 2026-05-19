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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `14.811%`
- winning mean component MAE: `0.033975`
- winning mean component RMSE: `0.087169`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 14.811 | 0.033975 | 0.087169 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002979 | 0.003762 | 38.933 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000026 | 0.000039 | 0.151 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001673 | 0.002377 | 34.343 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000025 | 0.000039 | 2.606 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.022966 | 0.030693 | 1.695 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000016 | 0.000023 | 3.481 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.147260 | 0.715420 | 5.199 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000029 | 0.000049 | 8.683 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.082561 | 0.132408 | 30.222 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000044 | 0.000059 | 5.195 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.038634 | 0.080009 | 58.908 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000014 | 7.295 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.084280 | 0.115475 | 37.181 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000142 | 0.000479 | 10.546 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.057696 | 0.109144 | 4.433 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000041 | 0.000112 | 8.041 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.053675 | 0.109817 | 3.209 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000082 | 0.000196 | 11.456 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.153388 | 0.356096 | 9.836 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/020_track1_original_dataset_backward_ert_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-34-18__track1_original_dataset_backward_ert_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-34-18__track1_original_dataset_backward_ert_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-34-18__track1_original_dataset_backward_ert_attempt_20_campaign_validation/validation_summary.yaml`
