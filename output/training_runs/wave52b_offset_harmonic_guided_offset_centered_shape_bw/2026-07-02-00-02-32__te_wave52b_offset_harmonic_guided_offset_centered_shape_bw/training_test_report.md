# Wave52B Offset Harmonic Guided Offset Centered Shape Bw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw`
- Model Family: `wave52b_offset_harmonic_guided_offset_centered_shape_bw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_bw\2026-07-02-00-02-32__te_wave52b_offset_harmonic_guided_offset_centered_shape_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=122-val_mae=0.00260437.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.059352`
- val_mae: `0.002604`
- val_rmse: `0.003222`
- val_pointwise_loss: `0.037238`
- val_centered_curve_shape_loss: `0.036250`
- val_curve_offset_loss: `0.000988`
- val_curve_amplitude_loss: `0.294318`
- val_sparse_harmonic_shape_loss: `0.000894`
- val_structured_mae: `0.019549`
- val_structured_rmse: `0.023002`
- val_base_mae: `0.011105`
- val_base_rmse: `0.012784`
- val_residual_offset_mean_abs: `0.010560`

## Test Metrics

- test_loss: `0.030590`
- test_mae: `0.002012`
- test_rmse: `0.002626`
- test_pointwise_loss: `0.019978`
- test_centered_curve_shape_loss: `0.019011`
- test_curve_offset_loss: `0.000967`
- test_curve_amplitude_loss: `0.133304`
- test_sparse_harmonic_shape_loss: `0.000447`
- test_structured_mae: `0.020345`
- test_structured_rmse: `0.023741`
- test_base_mae: `0.011287`
- test_base_rmse: `0.012898`
- test_residual_offset_mean_abs: `0.010795`

## Interpretation

The held-out val error stayed finite with MAE=0.002604 deg and RMSE=0.003222 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002012 deg and RMSE=0.002626 deg, which indicates a numerically stable baseline run.
