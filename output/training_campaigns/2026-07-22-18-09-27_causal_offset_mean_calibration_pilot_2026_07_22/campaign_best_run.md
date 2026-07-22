# Campaign Best Run

## Overview

- Campaign Name: `causal_offset_mean_calibration_pilot_2026_07_22`
- Run Name: `te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints`
- Run Instance Id: `2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `causal_offset_mean_periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Test MAE: `0.0012772574555128813`
- Test RMSE: `0.0017385343089699745`
- Validation MAE: `0.0014689491363242269`
- Output Directory: `output\training_runs\causal_offset_mean_calibration\2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\causal_offset_mean_calibration\2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\causal_offset_mean_calibration\2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\causal_offset_mean_calibration\2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints\checkpoints\periodic_mlp-epoch=020-val_mae=0.00146895.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

