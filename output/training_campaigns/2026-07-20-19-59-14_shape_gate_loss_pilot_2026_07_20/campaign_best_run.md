# Campaign Best Run

## Overview

- Campaign Name: `shape_gate_loss_pilot_2026_07_20`
- Run Name: `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`
- Run Instance Id: `2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `shape_gate_loss_pilot_periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Test MAE: `0.00252225692383945`
- Test RMSE: `0.003132739569991827`
- Validation MAE: `0.002296747174113989`
- Output Directory: `output\training_runs\shape_gate_loss_pilot_periodic_gru_sequence\2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\shape_gate_loss_pilot_periodic_gru_sequence\2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\shape_gate_loss_pilot_periodic_gru_sequence\2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\shape_gate_loss_pilot_periodic_gru_sequence\2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=007-val_mae=0.00229675.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
