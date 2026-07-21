# Campaign Best Run

## Overview

- Campaign Name: `parallel_shape_objective_followup_2026_07_21`
- Run Name: `te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints`
- Run Instance Id: `2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `shape_objective_periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Test MAE: `0.0012364950962364674`
- Test RMSE: `0.00167159887496382`
- Validation MAE: `0.0014288033125922084`
- Output Directory: `output\training_runs\shape_objective_followup\2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\shape_objective_followup\2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\shape_objective_followup\2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\shape_objective_followup\2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints\checkpoints\periodic_mlp-epoch=025-val_mae=0.00142880.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
