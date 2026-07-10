# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints`
- Run Name: `te_wave3_2_harmonic_residual_offset_global__polished_setpoints`
- Run Instance Id: `2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Test MAE: `0.002219775225967169`
- Test RMSE: `0.003586746985092759`
- Validation MAE: `0.0019052241696044803`
- Output Directory: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints\checkpoints\harmonic_residual_offset_probe-epoch=124-val_mae=0.00190522.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
