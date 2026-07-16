# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_setpoints`
- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints`
- Run Instance Id: `2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_global`
- Model Type: `wave3_harmonic_prior_residual`
- Test MAE: `0.002231063088402152`
- Test RMSE: `0.0036034826189279556`
- Validation MAE: `0.001900798873975873`
- Output Directory: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-00-50-35__te_wave5_1_harmonic_prior_pointwise_control_global__polished_setpoints\checkpoints\wave3_harmonic_prior_residual-epoch=131-val_mae=0.00190080.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
