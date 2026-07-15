# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints`
- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints`
- Run Instance Id: `2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Test MAE: `0.0033426282461732626`
- Test RMSE: `0.004237575456500053`
- Validation MAE: `0.0034984424710273743`
- Output Directory: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints\checkpoints\latent_state_hysteresis_probe-epoch=236-val_mae=0.00349844.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
