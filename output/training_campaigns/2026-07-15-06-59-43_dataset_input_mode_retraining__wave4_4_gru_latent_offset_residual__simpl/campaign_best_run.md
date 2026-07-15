# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints`
- Run Name: `te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints`
- Run Instance Id: `2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Test MAE: `0.003510406007990241`
- Test RMSE: `0.00433425372466445`
- Validation MAE: `0.0037724487483501434`
- Output Directory: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints\checkpoints\latent_state_hysteresis_probe-epoch=072-val_mae=0.00377245.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
