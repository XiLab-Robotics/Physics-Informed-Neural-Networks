# Campaign Best Run

## Overview

- Campaign Name: `shape_first_training_rule_distillation_pilot_2026_07_22`
- Run Name: `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints`
- Run Instance Id: `2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `shape_first_distilled_periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Test MAE: `0.0014201176818460226`
- Test RMSE: `0.0018664648523554206`
- Validation MAE: `0.001573292538523674`
- Output Directory: `output\training_runs\shape_first_training_rule_distillation\2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\shape_first_training_rule_distillation\2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\shape_first_training_rule_distillation\2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\shape_first_training_rule_distillation\2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints\checkpoints\periodic_mlp-epoch=011-val_mae=0.00157329.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
