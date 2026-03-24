# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-03-20-16-31-19__te_harmonic_order12_linear_conditioned_recovery\checkpoints\harmonic_regression-epoch=026-val_mae=0.01700371.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187339`
- val_mae: `0.017004`
- val_rmse: `0.018547`

## Test Metrics

- test_loss: `0.253202`
- test_mae: `0.020782`
- test_rmse: `0.022405`

## Interpretation

The held-out val error stayed finite with MAE=0.017004 deg and RMSE=0.018547 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020782 deg and RMSE=0.022405 deg, which indicates a numerically stable baseline run.
