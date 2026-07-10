# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints`
- Run Name: `te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints`
- Run Instance Id: `2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_global`
- Model Type: `sequential_residual_offset_probe`
- Test MAE: `0.002453744877129793`
- Test RMSE: `0.00385081279091537`
- Validation MAE: `0.002173546701669693`
- Output Directory: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_2_clean_sequential_residual_offset\2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints\checkpoints\sequential_residual_offset_probe-epoch=128-val_mae=0.00217355.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
