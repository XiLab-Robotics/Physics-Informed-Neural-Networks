# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values`
- Run Name: `te_wave3_2_harmonic_residual_offset_global__polished_actual_values`
- Run Instance Id: `2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values`
- Model Family: `wave3_2_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Test MAE: `0.001957989763468504`
- Test RMSE: `0.0030097453854978085`
- Validation MAE: `0.0018363535637035966`
- Output Directory: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values\checkpoints\harmonic_residual_offset_probe-epoch=201-val_mae=0.00183635.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

