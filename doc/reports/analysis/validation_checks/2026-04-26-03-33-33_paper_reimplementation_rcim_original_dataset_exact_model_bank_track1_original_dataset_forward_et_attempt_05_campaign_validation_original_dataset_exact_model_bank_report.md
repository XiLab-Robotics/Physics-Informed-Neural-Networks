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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `39.080%`
- winning mean component MAE: `0.103956`
- winning mean component RMSE: `0.244857`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 39.080 | 0.103956 | 0.244857 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003690 | 0.005360 | 7.181 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000037 | 0.000048 | 0.216 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002393 | 0.003717 | 32.247 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000020 | 0.000028 | 2.456 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.028842 | 0.038924 | 1.572 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000038 | 0.000053 | 3.316 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.032436 | 0.059675 | 2.628 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000033 | 0.000053 | 3.911 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.053790 | 0.089363 | 143.129 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000071 | 0.000098 | 11.221 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.089106 | 0.234659 | 342.704 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000018 | 0.000027 | 5.642 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.062796 | 0.084696 | 5.913 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000093 | 0.000352 | 15.808 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 1.057842 | 2.086060 | 77.052 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000053 | 0.000168 | 9.126 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.336474 | 1.163877 | 14.966 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000196 | 0.000501 | 47.717 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.307236 | 0.884624 | 15.717 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/005_track1_original_dataset_forward_et_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-32-40__track1_original_dataset_forward_et_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-32-40__track1_original_dataset_forward_et_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-32-40__track1_original_dataset_forward_et_attempt_05_campaign_validation/validation_summary.yaml`
