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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `19.553%`
- winning mean component MAE: `0.050606`
- winning mean component RMSE: `0.132597`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 19.553 | 0.050606 | 0.132597 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 7}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.002930 | 0.003841 | 72.160 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000027 | 0.000037 | 0.158 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002164 | 0.003800 | 66.396 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000034 | 0.000065 | 3.285 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.027131 | 0.037193 | 2.048 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000023 | 0.000037 | 5.078 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.247440 | 1.092240 | 8.544 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000036 | 0.000049 | 11.979 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.113035 | 0.157620 | 37.678 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000073 | 0.000100 | 7.313 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.067091 | 0.126740 | 18.056 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000011 | 0.000016 | 8.960 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.117219 | 0.153959 | 55.867 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000095 | 0.000246 | 9.085 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.113514 | 0.293289 | 22.846 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000064 | 0.000172 | 7.648 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.088366 | 0.229965 | 6.390 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000084 | 0.000177 | 11.961 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.182185 | 0.419796 | 16.048 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/019_track1_original_dataset_backward_dt_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-14-54__track1_original_dataset_backward_dt_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-14-54__track1_original_dataset_backward_dt_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-14-54__track1_original_dataset_backward_dt_attempt_19_campaign_validation/validation_summary.yaml`
