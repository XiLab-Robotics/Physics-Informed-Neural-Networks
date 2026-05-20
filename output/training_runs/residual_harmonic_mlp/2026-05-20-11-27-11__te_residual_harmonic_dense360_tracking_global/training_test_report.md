# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_dense360_tracking_global`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-20-11-27-11__te_residual_harmonic_dense360_tracking_global\checkpoints\residual_harmonic_mlp-epoch=047-val_mae=0.00294320.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007274`
- val_mae: `0.002943`
- val_rmse: `0.003455`
- val_structured_mae: `0.040648`
- val_structured_rmse: `0.042578`

## Test Metrics

- test_loss: `0.008229`
- test_mae: `0.003434`
- test_rmse: `0.003957`
- test_structured_mae: `0.039462`
- test_structured_rmse: `0.042928`

## Interpretation

The held-out val error stayed finite with MAE=0.002943 deg and RMSE=0.003455 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003434 deg and RMSE=0.003957 deg, which indicates a numerically stable baseline run.
