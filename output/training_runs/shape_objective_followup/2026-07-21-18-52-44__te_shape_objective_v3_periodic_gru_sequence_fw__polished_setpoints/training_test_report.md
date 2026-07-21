# Shape Objective V3 Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `shape_objective_v3_periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_objective_followup\2026-07-21-18-52-44__te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=028-val_mae=0.00182045.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024374`
- val_mae: `0.001820`
- val_rmse: `0.002247`
- val_pointwise_loss: `0.014633`
- val_centered_curve_shape_loss: `0.013077`
- val_curve_offset_loss: `0.001557`
- val_curve_amplitude_loss: `0.032602`
- val_sparse_harmonic_shape_loss: `0.000307`

## Test Metrics

- test_loss: `0.013327`
- test_mae: `0.001400`
- test_rmse: `0.001756`
- test_pointwise_loss: `0.008323`
- test_centered_curve_shape_loss: `0.006679`
- test_curve_offset_loss: `0.001644`
- test_curve_amplitude_loss: `0.018416`
- test_sparse_harmonic_shape_loss: `0.000132`

## Interpretation

The held-out val error stayed finite with MAE=0.001820 deg and RMSE=0.002247 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001400 deg and RMSE=0.001756 deg, which indicates a numerically stable baseline run.
