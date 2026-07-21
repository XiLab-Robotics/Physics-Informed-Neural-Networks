# Shape Objective Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `shape_objective_periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_objective_followup\2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints\checkpoints\periodic_mlp-epoch=025-val_mae=0.00142880.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.018249`
- val_mae: `0.001429`
- val_rmse: `0.001867`
- val_pointwise_loss: `0.008833`
- val_centered_curve_shape_loss: `0.007328`
- val_curve_offset_loss: `0.002797`
- val_curve_amplitude_loss: `0.099152`
- val_sparse_harmonic_shape_loss: `0.000127`

## Test Metrics

- test_loss: `0.013324`
- test_mae: `0.001236`
- test_rmse: `0.001672`
- test_pointwise_loss: `0.005923`
- test_centered_curve_shape_loss: `0.005083`
- test_curve_offset_loss: `0.002295`
- test_curve_amplitude_loss: `0.079421`
- test_sparse_harmonic_shape_loss: `8.643399e-05`

## Interpretation

The held-out val error stayed finite with MAE=0.001429 deg and RMSE=0.001867 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001236 deg and RMSE=0.001672 deg, which indicates a numerically stable baseline run.
