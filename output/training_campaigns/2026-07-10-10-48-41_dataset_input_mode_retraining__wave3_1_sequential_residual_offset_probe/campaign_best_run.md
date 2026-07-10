# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values`
- Run Name: `te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values`
- Run Instance Id: `2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values`
- Model Family: `wave3_1_sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.0022624481935054064`
- Test RMSE: `0.0033262663055211306`
- Validation MAE: `0.002153824083507061`
- Output Directory: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values\checkpoints\sequential_residual_offset_probe-epoch=197-val_mae=0.00215382.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
