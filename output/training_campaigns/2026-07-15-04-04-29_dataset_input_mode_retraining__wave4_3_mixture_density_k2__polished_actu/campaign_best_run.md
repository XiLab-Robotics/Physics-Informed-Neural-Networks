# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_actual_values`
- Run Name: `te_wave4_3_mixture_density_k2_fw__polished_actual_values`
- Run Instance Id: `2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values`
- Model Family: `wave4_3_mixture_density_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0019355221884325147`
- Test RMSE: `0.0032235831022262573`
- Validation MAE: `0.0017245280323550105`
- Output Directory: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=256-val_mae=0.00172453.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
