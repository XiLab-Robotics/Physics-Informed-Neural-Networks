# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave5_1_harmonic_prior_smooth_l1_structured__polished_setpoints`
- Run Name: `te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_setpoints`
- Run Instance Id: `2026-07-16-04-58-25__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_setpoints`
- Model Family: `wave5_1_harmonic_prior_smooth_l1_structured_global`
- Model Type: `wave3_harmonic_prior_residual`
- Test MAE: `0.002236303873360157`
- Test RMSE: `0.00358780799433589`
- Validation MAE: `0.0019102919613942504`
- Output Directory: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-58-25__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-58-25__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-58-25__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-16-04-58-25__te_wave5_1_harmonic_prior_smooth_l1_structured_global__polished_setpoints\checkpoints\wave3_harmonic_prior_residual-epoch=135-val_mae=0.00191029.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
