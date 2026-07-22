# Shape First Distilled Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `shape_first_distilled_periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_first_training_rule_distillation\2026-07-22-14-38-51__te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints\checkpoints\periodic_gru_sequence-epoch=007-val_mae=0.00200434.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020768`
- val_mae: `0.002004`
- val_rmse: `0.002466`
- val_pointwise_loss: `0.017261`
- val_centered_curve_shape_loss: `0.014137`
- val_curve_offset_loss: `0.003124`
- val_curve_amplitude_loss: `0.046970`
- val_sparse_harmonic_shape_loss: `0.000339`

## Test Metrics

- test_loss: `0.011573`
- test_mae: `0.001523`
- test_rmse: `0.001920`
- test_pointwise_loss: `0.009925`
- test_centered_curve_shape_loss: `0.007235`
- test_curve_offset_loss: `0.002689`
- test_curve_amplitude_loss: `0.018799`
- test_sparse_harmonic_shape_loss: `0.000150`

## Interpretation

The held-out val error stayed finite with MAE=0.002004 deg and RMSE=0.002466 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001523 deg and RMSE=0.001920 deg, which indicates a numerically stable baseline run.
