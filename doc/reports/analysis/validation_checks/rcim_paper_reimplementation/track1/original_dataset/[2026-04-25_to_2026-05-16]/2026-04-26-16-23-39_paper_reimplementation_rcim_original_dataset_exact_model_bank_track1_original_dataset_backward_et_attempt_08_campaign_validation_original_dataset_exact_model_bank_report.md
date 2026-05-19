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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `18.766%`
- winning mean component MAE: `0.070213`
- winning mean component RMSE: `0.194392`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 18.766 | 0.070213 | 0.194392 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003706 | 0.004645 | 35.383 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000028 | 0.000039 | 0.165 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002168 | 0.003132 | 46.785 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000030 | 0.000041 | 3.086 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.025892 | 0.033553 | 2.003 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000022 | 0.000034 | 4.554 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.319905 | 1.280936 | 10.972 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000035 | 0.000053 | 11.088 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.093162 | 0.139058 | 34.413 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000064 | 0.000083 | 8.301 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.075157 | 0.147072 | 43.020 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000009 | 0.000014 | 8.091 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.118690 | 0.185767 | 56.948 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000252 | 0.001228 | 9.542 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.117773 | 0.291169 | 13.521 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000051 | 0.000129 | 5.942 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.082656 | 0.270711 | 4.328 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000370 | 0.000937 | 37.803 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.494072 | 1.334852 | 20.606 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/008_track1_original_dataset_backward_et_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-22-53__track1_original_dataset_backward_et_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-22-53__track1_original_dataset_backward_et_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-22-53__track1_original_dataset_backward_et_attempt_08_campaign_validation/validation_summary.yaml`
