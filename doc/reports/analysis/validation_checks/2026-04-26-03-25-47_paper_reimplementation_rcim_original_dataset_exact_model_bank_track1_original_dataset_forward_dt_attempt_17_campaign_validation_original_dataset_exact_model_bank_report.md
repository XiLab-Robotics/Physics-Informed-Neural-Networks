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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `26.200%`
- winning mean component MAE: `0.108183`
- winning mean component RMSE: `0.229282`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 26.200 | 0.108183 | 0.229282 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 8}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003850 | 0.005035 | 18.159 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000030 | 0.000041 | 0.173 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002147 | 0.003042 | 59.470 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000020 | 0.000030 | 2.438 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.029785 | 0.040228 | 1.677 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000038 | 0.000055 | 3.323 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.036450 | 0.058828 | 2.842 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000039 | 0.000062 | 5.064 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.050841 | 0.083269 | 157.292 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000060 | 0.000083 | 8.889 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.095387 | 0.261907 | 47.837 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000014 | 0.000022 | 4.260 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.067024 | 0.116448 | 8.783 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000112 | 0.000351 | 19.162 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.972817 | 1.946724 | 83.466 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000182 | 0.000960 | 11.885 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.400204 | 0.941934 | 18.187 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000050 | 0.000075 | 17.130 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.396418 | 0.897270 | 27.760 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/017_track1_original_dataset_forward_dt_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-25-00__track1_original_dataset_forward_dt_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-25-00__track1_original_dataset_forward_dt_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-25-00__track1_original_dataset_forward_dt_attempt_17_campaign_validation/validation_summary.yaml`
