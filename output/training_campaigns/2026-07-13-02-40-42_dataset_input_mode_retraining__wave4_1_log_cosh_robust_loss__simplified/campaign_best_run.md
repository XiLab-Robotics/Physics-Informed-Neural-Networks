# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__simplified_setpoints`
- Run Name: `te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints`
- Run Instance Id: `2026-07-13-02-40-42__te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.003339164424687624`
- Test RMSE: `0.004047723952680826`
- Validation MAE: `0.0035730674862861633`
- Output Directory: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-02-40-42__te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-02-40-42__te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-02-40-42__te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-13-02-40-42__te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=120-val_mae=0.00357307.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
