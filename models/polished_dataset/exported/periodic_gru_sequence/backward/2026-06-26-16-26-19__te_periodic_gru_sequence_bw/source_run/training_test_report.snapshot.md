# Periodic Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_bw`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-06-26-16-26-19__te_periodic_gru_sequence_bw\checkpoints\periodic_gru_sequence-epoch=258-val_mae=0.00108795.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001112`
- val_mae: `0.001088`
- val_rmse: `0.001338`
- val_pointwise_loss: `0.001112`
- val_centered_curve_shape_loss: `0.000754`
- val_curve_offset_loss: `0.000358`
- val_curve_amplitude_loss: `0.002975`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001284`
- test_mae: `0.001084`
- test_rmse: `0.001393`
- test_pointwise_loss: `0.001284`
- test_centered_curve_shape_loss: `0.001001`
- test_curve_offset_loss: `0.000282`
- test_curve_amplitude_loss: `0.003125`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001088 deg and RMSE=0.001338 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001084 deg and RMSE=0.001393 deg, which indicates a numerically stable baseline run.
