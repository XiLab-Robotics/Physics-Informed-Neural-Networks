# Campaign Best Run

## Overview

- Campaign Name: `shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21`
- Run Name: `te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints`
- Run Instance Id: `2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Test MAE: `0.0014626294141635299`
- Test RMSE: `0.0018308096332475543`
- Validation MAE: `0.0019827946089208126`
- Output Directory: `output\training_runs\shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence\2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence\2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence\2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence\2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=008-val_mae=0.00198279.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
