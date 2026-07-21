# Shape Gate Loss V2 Checkpoint Selection Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence\2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=008-val_mae=0.00198279.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.021138`
- val_mae: `0.001983`
- val_rmse: `0.002445`
- val_pointwise_loss: `0.017484`
- val_centered_curve_shape_loss: `0.014076`
- val_curve_offset_loss: `0.003407`
- val_curve_amplitude_loss: `0.048856`
- val_sparse_harmonic_shape_loss: `0.000339`

## Test Metrics

- test_loss: `0.011095`
- test_mae: `0.001463`
- test_rmse: `0.001831`
- test_pointwise_loss: `0.009410`
- test_centered_curve_shape_loss: `0.007082`
- test_curve_offset_loss: `0.002328`
- test_curve_amplitude_loss: `0.019544`
- test_sparse_harmonic_shape_loss: `0.000146`

## Interpretation

The held-out val error stayed finite with MAE=0.001983 deg and RMSE=0.002445 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001463 deg and RMSE=0.001831 deg, which indicates a numerically stable baseline run.
