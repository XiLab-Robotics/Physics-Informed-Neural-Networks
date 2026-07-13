# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints`
- Run Name: `te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints`
- Run Instance Id: `2026-07-13-08-11-55__te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0022896823938935995`
- Test RMSE: `0.0036451024934649467`
- Validation MAE: `0.001966372597962618`
- Output Directory: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-08-11-55__te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-08-11-55__te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-08-11-55__te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-08-11-55__te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=044-val_mae=0.00196637.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
