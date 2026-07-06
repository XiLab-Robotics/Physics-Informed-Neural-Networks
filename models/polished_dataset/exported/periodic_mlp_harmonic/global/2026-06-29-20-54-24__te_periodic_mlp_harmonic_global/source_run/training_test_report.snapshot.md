# Periodic Mlp Harmonic Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_global`
- Model Family: `periodic_mlp_harmonic_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_harmonic\2026-06-29-20-54-24__te_periodic_mlp_harmonic_global\checkpoints\periodic_mlp-epoch=061-val_mae=0.00126497.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001988`
- val_mae: `0.001265`
- val_rmse: `0.001644`
- val_pointwise_loss: `0.001988`
- val_centered_curve_shape_loss: `0.002173`
- val_curve_offset_loss: `0.000493`
- val_curve_amplitude_loss: `0.017293`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003083`
- test_mae: `0.001309`
- test_rmse: `0.001794`
- test_pointwise_loss: `0.003083`
- test_centered_curve_shape_loss: `0.002964`
- test_curve_offset_loss: `0.001263`
- test_curve_amplitude_loss: `0.026807`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001265 deg and RMSE=0.001644 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001309 deg and RMSE=0.001794 deg, which indicates a numerically stable baseline run.
