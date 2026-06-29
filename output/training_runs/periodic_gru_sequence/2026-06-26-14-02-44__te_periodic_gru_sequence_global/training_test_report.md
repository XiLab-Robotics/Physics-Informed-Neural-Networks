# Periodic Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_global`
- Model Family: `periodic_gru_sequence_global`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-06-26-14-02-44__te_periodic_gru_sequence_global\checkpoints\periodic_gru_sequence-epoch=157-val_mae=0.00125208.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001601`
- val_mae: `0.001252`
- val_rmse: `0.001553`
- val_pointwise_loss: `0.001601`
- val_centered_curve_shape_loss: `0.001203`
- val_curve_offset_loss: `0.000398`
- val_curve_amplitude_loss: `0.003915`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001721`
- test_mae: `0.001257`
- test_rmse: `0.001613`
- test_pointwise_loss: `0.001721`
- test_centered_curve_shape_loss: `0.001372`
- test_curve_offset_loss: `0.000349`
- test_curve_amplitude_loss: `0.004227`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001252 deg and RMSE=0.001553 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001257 deg and RMSE=0.001613 deg, which indicates a numerically stable baseline run.
