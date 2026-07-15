# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints`
- Run Name: `te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints`
- Run Instance Id: `2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Test MAE: `0.0024881933350116014`
- Test RMSE: `0.0038259983994066715`
- Validation MAE: `0.002218214562162757`
- Output Directory: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints\checkpoints\latent_state_hysteresis_probe-epoch=164-val_mae=0.00221821.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
