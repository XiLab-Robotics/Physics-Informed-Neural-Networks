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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `47.727%`
- winning mean component MAE: `0.095567`
- winning mean component RMSE: `0.262743`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 47.727 | 0.095567 | 0.262743 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003540 | 0.005177 | 10.914 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000037 | 0.000053 | 0.214 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.003258 | 0.004884 | 530.438 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000026 | 0.000041 | 3.244 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.038747 | 0.073663 | 2.093 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000034 | 0.000050 | 2.964 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.031997 | 0.066472 | 2.339 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000043 | 0.000078 | 6.084 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.060988 | 0.101047 | 64.146 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000060 | 0.000087 | 12.990 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.143344 | 0.493536 | 99.149 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000016 | 0.000026 | 5.175 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.087647 | 0.171916 | 9.499 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000076 | 0.000214 | 15.137 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.597516 | 1.509904 | 68.774 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000078 | 0.000302 | 11.043 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.405579 | 1.296117 | 16.472 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000141 | 0.000491 | 23.666 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.442651 | 1.268061 | 22.468 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/018_track1_original_dataset_forward_et_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-45-22__track1_original_dataset_forward_et_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-45-22__track1_original_dataset_forward_et_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-45-22__track1_original_dataset_forward_et_attempt_18_campaign_validation/validation_summary.yaml`
