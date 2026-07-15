# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_setpoints`
- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints`
- Run Instance Id: `2026-07-15-21-27-08__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Test MAE: `0.0025129825808107853`
- Test RMSE: `0.003854199079796672`
- Validation MAE: `0.0022147318813949823`
- Output Directory: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-21-27-08__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-21-27-08__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-21-27-08__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-21-27-08__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints\checkpoints\latent_state_hysteresis_probe-epoch=107-val_mae=0.00221473.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
