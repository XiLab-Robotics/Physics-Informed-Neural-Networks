# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints`
- Run Name: `te_residual_harmonic_mlp_fw__simplified_setpoints`
- Run Instance Id: `2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Test MAE: `0.003217733232304454`
- Test RMSE: `0.0037231810856610537`
- Validation MAE: `0.0030641737394034863`
- Output Directory: `output\training_runs\residual_harmonic_mlp\2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_mlp\2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_mlp\2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_mlp\2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints\checkpoints\residual_harmonic_mlp-epoch=079-val_mae=0.00306417.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
