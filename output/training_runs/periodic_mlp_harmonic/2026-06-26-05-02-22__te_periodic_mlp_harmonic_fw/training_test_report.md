# Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_fw`
- Model Family: `periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_harmonic\2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw\checkpoints\periodic_mlp-epoch=117-val_mae=0.00114445.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001801`
- val_mae: `0.001144`
- val_rmse: `0.001488`
- val_pointwise_loss: `0.001801`
- val_centered_curve_shape_loss: `0.002105`
- val_curve_offset_loss: `0.000399`
- val_curve_amplitude_loss: `0.018391`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002978`
- test_mae: `0.001326`
- test_rmse: `0.001780`
- test_pointwise_loss: `0.002978`
- test_centered_curve_shape_loss: `0.002963`
- test_curve_offset_loss: `0.001090`
- test_curve_amplitude_loss: `0.027218`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001144 deg and RMSE=0.001488 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001326 deg and RMSE=0.001780 deg, which indicates a numerically stable baseline run.
