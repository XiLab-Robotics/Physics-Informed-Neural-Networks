# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values`
- Run Name: `te_periodic_mlp_harmonic_bw__polished_actual_values`
- Run Instance Id: `2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values`
- Model Family: `periodic_mlp_harmonic_bw`
- Model Type: `periodic_mlp`
- Test MAE: `0.0013025462394580245`
- Test RMSE: `0.0022197405342012644`
- Validation MAE: `0.0011714595602825284`
- Output Directory: `output\training_runs\periodic_mlp_harmonic\2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\periodic_mlp_harmonic\2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_mlp_harmonic\2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_mlp_harmonic\2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values\checkpoints\periodic_mlp-epoch=128-val_mae=0.00117146.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

