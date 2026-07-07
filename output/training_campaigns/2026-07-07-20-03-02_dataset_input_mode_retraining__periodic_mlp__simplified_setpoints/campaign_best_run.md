# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_mlp__simplified_setpoints`
- Run Name: `te_periodic_mlp_global__simplified_setpoints`
- Run Instance Id: `2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints`
- Model Family: `periodic_mlp_global`
- Model Type: `periodic_mlp`
- Test MAE: `0.003345954231917858`
- Test RMSE: `0.004047157242894173`
- Validation MAE: `0.003012983128428459`
- Output Directory: `output\training_runs\periodic_mlp\2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\periodic_mlp\2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_mlp\2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_mlp\2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints\checkpoints\periodic_mlp-epoch=090-val_mae=0.00301298.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

