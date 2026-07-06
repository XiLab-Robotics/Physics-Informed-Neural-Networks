# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_bw`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-06-26-02-41-02__te_periodic_mlp_bw\checkpoints\periodic_mlp-epoch=128-val_mae=0.00161062.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002723`
- val_mae: `0.001611`
- val_rmse: `0.002076`
- val_pointwise_loss: `0.002723`
- val_centered_curve_shape_loss: `0.003089`
- val_curve_offset_loss: `0.000358`
- val_curve_amplitude_loss: `0.045923`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004028`
- test_mae: `0.001758`
- test_rmse: `0.002334`
- test_pointwise_loss: `0.004028`
- test_centered_curve_shape_loss: `0.004107`
- test_curve_offset_loss: `0.001006`
- test_curve_amplitude_loss: `0.059819`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001611 deg and RMSE=0.002076 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001758 deg and RMSE=0.002334 deg, which indicates a numerically stable baseline run.
