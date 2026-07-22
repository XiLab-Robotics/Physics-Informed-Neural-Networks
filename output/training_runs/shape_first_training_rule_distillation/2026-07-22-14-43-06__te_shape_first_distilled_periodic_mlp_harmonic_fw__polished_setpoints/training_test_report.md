# Shape First Distilled Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `shape_first_distilled_periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_first_training_rule_distillation\2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints\checkpoints\periodic_mlp-epoch=011-val_mae=0.00157329.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.015708`
- val_mae: `0.001573`
- val_rmse: `0.002010`
- val_pointwise_loss: `0.009553`
- val_centered_curve_shape_loss: `0.007614`
- val_curve_offset_loss: `0.003152`
- val_curve_amplitude_loss: `0.102087`
- val_sparse_harmonic_shape_loss: `0.000131`

## Test Metrics

- test_loss: `0.011639`
- test_mae: `0.001420`
- test_rmse: `0.001866`
- test_pointwise_loss: `0.007084`
- test_centered_curve_shape_loss: `0.005375`
- test_curve_offset_loss: `0.003210`
- test_curve_amplitude_loss: `0.075478`
- test_sparse_harmonic_shape_loss: `9.024077e-05`

## Interpretation

The held-out val error stayed finite with MAE=0.001573 deg and RMSE=0.002010 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001420 deg and RMSE=0.001866 deg, which indicates a numerically stable baseline run.
