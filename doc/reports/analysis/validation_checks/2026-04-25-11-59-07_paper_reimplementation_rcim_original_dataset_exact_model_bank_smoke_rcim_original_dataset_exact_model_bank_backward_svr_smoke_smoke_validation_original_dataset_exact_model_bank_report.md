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

- train rows / files: `10` / `10`
- validation rows / files: `3` / `3`
- test rows / files: `3` / `3`
- validation split: `0.2`
- test split: `0.1`
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `13.528%`
- winning mean component MAE: `0.113907`
- winning mean component RMSE: `0.145127`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 13.528 | 0.113907 | 0.145127 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.000748 | 0.000843 | 1.719 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000108 | 0.000108 | 0.631 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002279 | 0.002996 | 18.009 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000093 | 0.000114 | 8.527 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.031670 | 0.032610 | 2.805 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000116 | 0.000131 | 22.222 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 1.928868 | 2.509473 | 63.299 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000044 | 0.000056 | 18.255 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.078740 | 0.081437 | 24.836 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000190 | 0.000194 | 10.944 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.009859 | 0.011225 | 3.714 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000007 | 0.000011 | 6.740 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.037682 | 0.038745 | 5.317 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000171 | 0.000174 | 25.384 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.024284 | 0.026653 | 2.271 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000085 | 0.000097 | 21.871 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.031581 | 0.034049 | 2.115 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000267 | 0.000269 | 17.359 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.017442 | 0.018233 | 1.020 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/svr_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-07__rcim_original_dataset_exact_model_bank_backward_svr_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-07__rcim_original_dataset_exact_model_bank_backward_svr_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-07__rcim_original_dataset_exact_model_bank_backward_svr_smoke_smoke_validation/validation_summary.yaml`
