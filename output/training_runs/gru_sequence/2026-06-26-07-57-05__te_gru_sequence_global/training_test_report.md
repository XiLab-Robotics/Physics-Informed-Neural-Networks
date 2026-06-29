# Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_global`
- Model Family: `gru_sequence_global`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\gru_sequence\2026-06-26-07-57-05__te_gru_sequence_global\checkpoints\gru_sequence-epoch=182-val_mae=0.00212575.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005707`
- val_mae: `0.002126`
- val_rmse: `0.002653`
- val_pointwise_loss: `0.005707`
- val_centered_curve_shape_loss: `0.005382`
- val_curve_offset_loss: `0.000325`
- val_curve_amplitude_loss: `0.058966`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006481`
- test_mae: `0.002229`
- test_rmse: `0.002872`
- test_pointwise_loss: `0.006481`
- test_centered_curve_shape_loss: `0.006126`
- test_curve_offset_loss: `0.000356`
- test_curve_amplitude_loss: `0.065059`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002126 deg and RMSE=0.002653 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002229 deg and RMSE=0.002872 deg, which indicates a numerically stable baseline run.
