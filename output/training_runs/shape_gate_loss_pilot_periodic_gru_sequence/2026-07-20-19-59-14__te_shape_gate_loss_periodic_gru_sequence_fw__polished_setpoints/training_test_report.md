# Shape Gate Loss Pilot Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `shape_gate_loss_pilot_periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_gate_loss_pilot_periodic_gru_sequence\2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=007-val_mae=0.00229675.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008242`
- val_mae: `0.002297`
- val_rmse: `0.002750`
- val_pointwise_loss: `0.005697`
- val_centered_curve_shape_loss: `0.004500`
- val_curve_offset_loss: `0.001197`
- val_curve_amplitude_loss: `0.015342`
- val_sparse_harmonic_shape_loss: `0.000108`

## Test Metrics

- test_loss: `0.011919`
- test_mae: `0.002522`
- test_rmse: `0.003133`
- test_pointwise_loss: `0.008580`
- test_centered_curve_shape_loss: `0.005242`
- test_curve_offset_loss: `0.003338`
- test_curve_amplitude_loss: `0.018935`
- test_sparse_harmonic_shape_loss: `0.000113`

## Interpretation

The held-out val error stayed finite with MAE=0.002297 deg and RMSE=0.002750 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002522 deg and RMSE=0.003133 deg, which indicates a numerically stable baseline run.
