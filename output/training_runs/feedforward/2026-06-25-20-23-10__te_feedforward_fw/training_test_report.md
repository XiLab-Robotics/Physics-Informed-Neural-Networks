# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_fw`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-06-25-20-23-10__te_feedforward_fw\checkpoints\feedforward-epoch=092-val_mae=0.00162825.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002739`
- val_mae: `0.001628`
- val_rmse: `0.002019`
- val_pointwise_loss: `0.002739`
- val_centered_curve_shape_loss: `0.002454`
- val_curve_offset_loss: `0.000316`
- val_curve_amplitude_loss: `0.039184`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003981`
- test_mae: `0.001726`
- test_rmse: `0.002205`
- test_pointwise_loss: `0.003981`
- test_centered_curve_shape_loss: `0.003580`
- test_curve_offset_loss: `0.000937`
- test_curve_amplitude_loss: `0.054441`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001628 deg and RMSE=0.002019 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001726 deg and RMSE=0.002205 deg, which indicates a numerically stable baseline run.
