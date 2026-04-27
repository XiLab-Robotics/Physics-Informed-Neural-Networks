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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `26.316%`
- winning mean component MAE: `0.089130`
- winning mean component RMSE: `0.175812`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 26.316 | 0.089130 | 0.175812 | `{'estimator__learning_rate': 0.22, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002712 | 0.003592 | 5.809 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000031 | 0.000037 | 0.181 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001942 | 0.002473 | 27.910 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000024 | 2.242 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.019921 | 0.026229 | 1.098 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000023 | 0.000031 | 2.004 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.021856 | 0.033253 | 1.783 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000023 | 0.000035 | 2.936 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.037954 | 0.051432 | 150.516 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000049 | 5.615 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.099173 | 0.194449 | 91.904 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000012 | 0.000016 | 3.982 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.053535 | 0.074912 | 4.866 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000135 | 0.000321 | 21.839 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.691037 | 1.230454 | 63.075 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000164 | 0.000452 | 28.939 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.406879 | 0.803203 | 18.030 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000048 | 0.000087 | 10.011 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.357981 | 0.919372 | 57.266 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/010_track1_original_dataset_forward_hgbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-48-58__track1_original_dataset_forward_hgbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-48-58__track1_original_dataset_forward_hgbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-48-58__track1_original_dataset_forward_hgbm_attempt_10_campaign_validation/validation_summary.yaml`
