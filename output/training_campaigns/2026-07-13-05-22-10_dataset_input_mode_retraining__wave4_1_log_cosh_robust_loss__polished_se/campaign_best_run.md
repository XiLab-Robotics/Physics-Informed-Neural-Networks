# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
- Run Name: `te_wave4_1_log_cosh_robust_loss_global__polished_setpoints`
- Run Instance Id: `2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002200285205617547`
- Test RMSE: `0.003572094487026334`
- Validation MAE: `0.0019121065270155668`
- Output Directory: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=155-val_mae=0.00191211.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
