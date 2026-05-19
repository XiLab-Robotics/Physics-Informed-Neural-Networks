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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `29.726%`
- winning mean component MAE: `0.105818`
- winning mean component RMSE: `0.254275`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 29.726 | 0.105818 | 0.254275 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003274 | 0.004910 | 18.704 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000027 | 0.000039 | 0.159 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.003142 | 0.004371 | 67.884 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000028 | 0.000042 | 3.371 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.038302 | 0.052413 | 2.084 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000050 | 0.000067 | 4.387 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.029709 | 0.050444 | 2.516 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000040 | 0.000059 | 4.963 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.067416 | 0.097823 | 175.914 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000076 | 0.000102 | 12.519 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.110567 | 0.227969 | 97.045 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000015 | 0.000020 | 4.570 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.103410 | 0.177250 | 10.869 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000042 | 0.000099 | 16.134 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.887195 | 1.838032 | 44.748 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000067 | 0.000223 | 13.650 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.353429 | 1.146641 | 13.614 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000135 | 0.000389 | 24.849 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.413626 | 1.230329 | 46.818 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/002_track1_original_dataset_forward_et_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-29-41__track1_original_dataset_forward_et_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-29-41__track1_original_dataset_forward_et_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-29-41__track1_original_dataset_forward_et_attempt_02_campaign_validation/validation_summary.yaml`
