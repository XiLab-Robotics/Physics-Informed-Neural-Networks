# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints`
- Run Name: `te_wave4_2_gaussian_nll_global__polished_setpoints`
- Run Instance Id: `2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints`
- Model Family: `wave4_2_gaussian_nll_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0022098668850958347`
- Test RMSE: `0.003605362493544817`
- Validation MAE: `0.0018816946540027857`
- Output Directory: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00188169.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
