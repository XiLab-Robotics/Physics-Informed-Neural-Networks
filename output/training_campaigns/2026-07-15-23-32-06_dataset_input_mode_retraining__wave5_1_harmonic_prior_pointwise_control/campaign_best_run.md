# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__simplified_setpoints`
- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints`
- Run Instance Id: `2026-07-15-23-51-01__te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Test MAE: `0.0033862905111163855`
- Test RMSE: `0.004122171550989151`
- Validation MAE: `0.003562851110473275`
- Output Directory: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-15-23-51-01__te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-15-23-51-01__te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-15-23-51-01__te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-15-23-51-01__te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints\checkpoints\wave3_harmonic_prior_residual-epoch=223-val_mae=0.00356285.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
