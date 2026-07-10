# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__simplified_setpoints`
- Run Name: `te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints`
- Run Instance Id: `2026-07-10-13-09-01__te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_bw`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.003486015135422349`
- Test RMSE: `0.004293318837881088`
- Validation MAE: `0.003647998906672001`
- Output Directory: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-09-01__te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-09-01__te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-09-01__te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-09-01__te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints\checkpoints\sequential_residual_offset_probe-epoch=151-val_mae=0.00364800.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
