# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_setpoints`
- Run Name: `te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints`
- Run Instance Id: `2026-07-10-10-05-23__te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.002450165804475546`
- Test RMSE: `0.003838052973151207`
- Validation MAE: `0.00216898275539279`
- Output Directory: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-10-05-23__te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-10-05-23__te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-10-05-23__te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-10-05-23__te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints\checkpoints\sequential_residual_offset_probe-epoch=137-val_mae=0.00216898.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
