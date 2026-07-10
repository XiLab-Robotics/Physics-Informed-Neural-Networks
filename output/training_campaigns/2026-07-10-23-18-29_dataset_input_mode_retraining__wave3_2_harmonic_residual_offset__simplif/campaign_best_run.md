# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints`
- Run Name: `te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints`
- Run Instance Id: `2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Test MAE: `0.003391365986317396`
- Test RMSE: `0.004142212215811014`
- Validation MAE: `0.0036225691437721252`
- Output Directory: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave3_2_harmonic_residual_offset\2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints\checkpoints\harmonic_residual_offset_probe-epoch=121-val_mae=0.00362257.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
