# Campaign Best Run

## Overview

- Campaign Name: `wave52r_stage4_data_only_residual_capacity_2026_07_28`
- Run Name: `te_stage4_h08_r5_deep__polished_setpoints_fw`
- Run Instance Id: `2026-07-28-10-59-18__te_stage4_h08_r5_deep__polished_setpoints_fw`
- Model Family: `stage4_h08_r5_deep`
- Model Type: `data_only_residual_capacity`
- Test MAE: `0.001454935991205275`
- Test RMSE: `0.001825041719712317`
- Validation MAE: `0.0014897265937179327`
- Output Directory: `output\training_runs\data_only_residual_capacity\2026-07-28-10-59-18__te_stage4_h08_r5_deep__polished_setpoints_fw`
- Metrics Snapshot: `output\training_runs\data_only_residual_capacity\2026-07-28-10-59-18__te_stage4_h08_r5_deep__polished_setpoints_fw/metrics_summary.yaml`
- Report Path: `output\training_runs\data_only_residual_capacity\2026-07-28-10-59-18__te_stage4_h08_r5_deep__polished_setpoints_fw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\data_only_residual_capacity\2026-07-28-10-59-18__te_stage4_h08_r5_deep__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=021-val_mae=0.00148973.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
