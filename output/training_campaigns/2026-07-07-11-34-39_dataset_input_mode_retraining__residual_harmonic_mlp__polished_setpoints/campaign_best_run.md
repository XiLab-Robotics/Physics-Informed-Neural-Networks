# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints`
- Run Name: `te_residual_harmonic_mlp_bw__polished_setpoints`
- Run Instance Id: `2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Test MAE: `0.0017251045210286975`
- Test RMSE: `0.002305245492607355`
- Validation MAE: `0.0016264503356069326`
- Output Directory: `output\training_runs\residual_harmonic_mlp\2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_mlp\2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_mlp\2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_mlp\2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints\checkpoints\residual_harmonic_mlp-epoch=093-val_mae=0.00162645.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
