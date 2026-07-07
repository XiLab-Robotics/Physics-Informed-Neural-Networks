# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints`
- Run Name: `te_periodic_mlp_harmonic_fw__simplified_setpoints`
- Run Instance Id: `2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints`
- Model Family: `periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Test MAE: `0.003064638003706932`
- Test RMSE: `0.003709434298798442`
- Validation MAE: `0.0028028017841279507`
- Output Directory: `output\training_runs\periodic_mlp_harmonic\2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\periodic_mlp_harmonic\2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_mlp_harmonic\2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_mlp_harmonic\2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints\checkpoints\periodic_mlp-epoch=055-val_mae=0.00280280.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

