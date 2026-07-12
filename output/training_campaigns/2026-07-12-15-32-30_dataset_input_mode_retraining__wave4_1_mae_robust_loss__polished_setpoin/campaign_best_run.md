# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints`
- Run Name: `te_wave4_1_mae_robust_loss_fw__polished_setpoints`
- Run Instance Id: `2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints`
- Model Family: `wave4_1_mae_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0021090346854180098`
- Test RMSE: `0.0035446591209620237`
- Validation MAE: `0.0017919032834470272`
- Output Directory: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_1_mae_robust_loss\2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00179190.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
