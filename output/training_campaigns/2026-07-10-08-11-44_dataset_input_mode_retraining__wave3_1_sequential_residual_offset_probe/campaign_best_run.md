# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints`
- Run Name: `te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints`
- Run Instance Id: `2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_fw`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.0034721458796411753`
- Test RMSE: `0.004298313986510038`
- Validation MAE: `0.003654662286862731`
- Output Directory: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_1_sequential_residual_offset_probe\2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints\checkpoints\sequential_residual_offset_probe-epoch=138-val_mae=0.00365466.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
