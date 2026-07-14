# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_2_gaussian_nll__simplified_setpoints`
- Run Name: `te_wave4_2_gaussian_nll_fw__simplified_setpoints`
- Run Instance Id: `2026-07-14-18-14-13__te_wave4_2_gaussian_nll_fw__simplified_setpoints`
- Model Family: `wave4_2_gaussian_nll_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.09219042211771011`
- Test RMSE: `0.11572623252868652`
- Validation MAE: `0.09172054380178452`
- Output Directory: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-14-13__te_wave4_2_gaussian_nll_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-14-13__te_wave4_2_gaussian_nll_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-14-13__te_wave4_2_gaussian_nll_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_2_gaussian_nll\2026-07-14-18-14-13__te_wave4_2_gaussian_nll_fw__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.09172054.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
