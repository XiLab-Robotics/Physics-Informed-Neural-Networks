# Campaign Best Run

## Overview

- Campaign Name: `track2g_curve_aware_training_campaign_2026_06_08`
- Run Name: `te_track2g_curve_aware_raw_centered_shape_fw`
- Run Instance Id: `2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0031812870875000954`
- Test RMSE: `0.0035711326636373997`
- Validation MAE: `0.003250579349696636`
- Output Directory: `output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw`
- Metrics Snapshot: `output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw/metrics_summary.yaml`
- Report Path: `output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=036-val_mae=0.00325058.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
