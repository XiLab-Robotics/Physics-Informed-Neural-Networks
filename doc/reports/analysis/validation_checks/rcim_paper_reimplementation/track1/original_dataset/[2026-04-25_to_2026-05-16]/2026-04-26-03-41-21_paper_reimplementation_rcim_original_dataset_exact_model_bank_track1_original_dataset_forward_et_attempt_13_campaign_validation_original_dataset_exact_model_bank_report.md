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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `24.963%`
- winning mean component MAE: `0.099020`
- winning mean component RMSE: `0.250759`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 24.963 | 0.099020 | 0.250759 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 2}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.004190 | 0.006524 | 21.710 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000038 | 0.000054 | 0.223 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002522 | 0.003464 | 29.085 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000033 | 0.000065 | 4.081 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.041642 | 0.075282 | 2.327 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000042 | 0.000061 | 4.116 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.029495 | 0.053009 | 2.467 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000037 | 0.000069 | 4.558 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.055358 | 0.095271 | 127.783 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000059 | 0.000084 | 9.306 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.092870 | 0.225668 | 99.819 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000021 | 0.000030 | 6.722 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.072827 | 0.109688 | 7.563 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000099 | 0.000318 | 14.130 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.882478 | 1.909681 | 51.298 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000053 | 0.000166 | 9.213 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.283419 | 1.087382 | 10.664 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000121 | 0.000353 | 46.698 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.416078 | 1.197250 | 22.538 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/013_track1_original_dataset_forward_et_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-40-29__track1_original_dataset_forward_et_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-40-29__track1_original_dataset_forward_et_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-40-29__track1_original_dataset_forward_et_attempt_13_campaign_validation/validation_summary.yaml`
