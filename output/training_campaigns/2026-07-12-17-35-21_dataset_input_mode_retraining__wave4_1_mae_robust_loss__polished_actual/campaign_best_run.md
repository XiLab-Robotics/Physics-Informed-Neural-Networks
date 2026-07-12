# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_actual_values`
- Run Name: `te_wave4_1_mae_robust_loss_fw__polished_actual_values`
- Run Instance Id: `2026-07-12-18-19-09__te_wave4_1_mae_robust_loss_fw__polished_actual_values`
- Model Family: `wave4_1_mae_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002010481199249625`
- Test RMSE: `0.003415082348510623`
- Validation MAE: `0.0017341992352157831`
- Output Directory: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-18-19-09__te_wave4_1_mae_robust_loss_fw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-18-19-09__te_wave4_1_mae_robust_loss_fw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-18-19-09__te_wave4_1_mae_robust_loss_fw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-18-19-09__te_wave4_1_mae_robust_loss_fw__polished_actual_values\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=202-val_mae=0.00173420.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
