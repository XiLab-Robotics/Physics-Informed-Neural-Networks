# Periodic Mlp Harmonic Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_global`
- Model Family: `periodic_mlp_harmonic_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_harmonic\2026-06-26-04-20-03__te_periodic_mlp_harmonic_global\checkpoints\periodic_mlp-epoch=138-val_mae=0.00119613.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001872`
- val_mae: `0.001196`
- val_rmse: `0.001551`
- val_pointwise_loss: `0.001872`
- val_centered_curve_shape_loss: `0.002171`
- val_curve_offset_loss: `0.000368`
- val_curve_amplitude_loss: `0.020985`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002924`
- test_mae: `0.001264`
- test_rmse: `0.001737`
- test_pointwise_loss: `0.002924`
- test_centered_curve_shape_loss: `0.003057`
- test_curve_offset_loss: `0.000984`
- test_curve_amplitude_loss: `0.029600`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001196 deg and RMSE=0.001551 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001264 deg and RMSE=0.001737 deg, which indicates a numerically stable baseline run.
