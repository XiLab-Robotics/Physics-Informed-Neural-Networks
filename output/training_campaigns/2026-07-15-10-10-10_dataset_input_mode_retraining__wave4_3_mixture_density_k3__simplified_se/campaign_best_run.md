# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k3__simplified_setpoints`
- Run Name: `te_wave4_3_mixture_density_k3_fw__simplified_setpoints`
- Run Instance Id: `2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k3_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.0033332209568470716`
- Test RMSE: `0.004102963954210281`
- Validation MAE: `0.003573987167328596`
- Output Directory: `output\training_runs\wave4_3_mixture_density_k3\2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_3_mixture_density_k3\2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_3_mixture_density_k3\2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_3_mixture_density_k3\2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=077-val_mae=0.00357399.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
