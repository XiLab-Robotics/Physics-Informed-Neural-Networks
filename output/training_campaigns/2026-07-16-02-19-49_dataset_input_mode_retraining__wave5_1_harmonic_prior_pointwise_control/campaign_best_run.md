# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__polished_actual_values`
- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values`
- Run Instance Id: `2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_bw`
- Model Type: `wave3_harmonic_prior_residual`
- Test MAE: `0.0021902553271502256`
- Test RMSE: `0.003538577351719141`
- Validation MAE: `0.001896379515528679`
- Output Directory: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-16-03-08-07__te_wave5_1_harmonic_prior_pointwise_control_bw__polished_actual_values\checkpoints\wave3_harmonic_prior_residual-epoch=113-val_mae=0.00189638.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
