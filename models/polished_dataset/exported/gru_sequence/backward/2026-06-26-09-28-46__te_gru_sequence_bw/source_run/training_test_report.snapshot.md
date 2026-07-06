# Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_bw`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\gru_sequence\2026-06-26-09-28-46__te_gru_sequence_bw\checkpoints\gru_sequence-epoch=094-val_mae=0.00214655.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005760`
- val_mae: `0.002147`
- val_rmse: `0.002669`
- val_pointwise_loss: `0.005760`
- val_centered_curve_shape_loss: `0.005401`
- val_curve_offset_loss: `0.000360`
- val_curve_amplitude_loss: `0.055630`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006601`
- test_mae: `0.002271`
- test_rmse: `0.002908`
- test_pointwise_loss: `0.006601`
- test_centered_curve_shape_loss: `0.006176`
- test_curve_offset_loss: `0.000425`
- test_curve_amplitude_loss: `0.061095`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002147 deg and RMSE=0.002669 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002271 deg and RMSE=0.002908 deg, which indicates a numerically stable baseline run.
