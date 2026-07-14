# Wave4 2 Gaussian Nll Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_fw__polished_actual_values`
- Model Family: `wave4_2_gaussian_nll_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-42-59__te_wave4_2_gaussian_nll_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=258-val_mae=0.00181578.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.729108`
- val_mae: `0.001816`
- val_rmse: `0.002595`
- val_pointwise_loss: `-1.729108`
- val_centered_curve_shape_loss: `0.004557`
- val_curve_offset_loss: `0.000376`
- val_curve_amplitude_loss: `0.036228`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_interval_coverage: `0.881336`
- val_interval_width: `0.007549`
- val_mean_sigma: `0.002945`
- val_structured_mae: `0.050872`
- val_structured_rmse: `0.068043`
- val_residual_offset_mean_abs: `0.066528`

## Test Metrics

- test_loss: `-1.656796`
- test_mae: `0.002113`
- test_rmse: `0.003566`
- test_pointwise_loss: `-1.656796`
- test_centered_curve_shape_loss: `0.005901`
- test_curve_offset_loss: `0.003412`
- test_curve_amplitude_loss: `0.043133`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_interval_coverage: `0.875913`
- test_interval_width: `0.007892`
- test_mean_sigma: `0.003079`
- test_structured_mae: `0.049441`
- test_structured_rmse: `0.066314`
- test_residual_offset_mean_abs: `0.063929`

## Interpretation

The held-out val error stayed finite with MAE=0.001816 deg and RMSE=0.002595 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002113 deg and RMSE=0.003566 deg, which indicates a numerically stable baseline run.
