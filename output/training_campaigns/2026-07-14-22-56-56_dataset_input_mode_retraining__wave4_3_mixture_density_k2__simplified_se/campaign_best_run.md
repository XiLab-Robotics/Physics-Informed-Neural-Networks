# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints`
- Run Name: `te_wave4_3_mixture_density_k2_global__simplified_setpoints`
- Run Instance Id: `2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints`
- Model Family: `wave4_3_mixture_density_k2_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.003256091382354498`
- Test RMSE: `0.0040346900932490826`
- Validation MAE: `0.0034678978845477104`
- Output Directory: `output\training_runs\wave4_3_mixture_density_k2\2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_3_mixture_density_k2\2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_3_mixture_density_k2\2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_3_mixture_density_k2\2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=237-val_mae=0.00346790.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
