# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints`
- Run Name: `te_wave4_3_mixture_density_k2_fw__polished_setpoints`
- Run Instance Id: `2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints`
- Model Family: `wave4_3_mixture_density_k2_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Test MAE: `0.002155335620045662`
- Test RMSE: `0.0035515420604497194`
- Validation MAE: `0.001849626307375729`
- Output Directory: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\wave4_3_mixture_density_k2\2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00184963.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
