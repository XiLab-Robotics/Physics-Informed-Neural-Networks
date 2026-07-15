# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values`
- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values`
- Run Instance Id: `2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Test MAE: `0.0023435212206095457`
- Test RMSE: `0.00343461730517447`
- Validation MAE: `0.002226645825430751`
- Output Directory: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values\checkpoints\latent_state_hysteresis_probe-epoch=078-val_mae=0.00222665.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
