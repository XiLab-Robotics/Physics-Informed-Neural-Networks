# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__simplified_setpoints`
- Run Name: `te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints`
- Run Instance Id: `2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints`
- Model Family: `wave5_1_harmonic_prior_smooth_l1_structured_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Test MAE: `0.003436887403950095`
- Test RMSE: `0.004167952109128237`
- Validation MAE: `0.0036475416272878647`
- Output Directory: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-17-30__te_wave5_1_harmonic_prior_smooth_l1_structured_fw__simplified_setpoints\checkpoints\wave3_harmonic_prior_residual-epoch=070-val_mae=0.00364754.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
