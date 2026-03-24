# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_static_recovery`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-03-20-16-20-27__te_harmonic_order12_static_recovery\checkpoints\harmonic_regression-epoch=017-val_mae=0.04052421.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.946381`
- val_mae: `0.040524`
- val_rmse: `0.042584`

## Test Metrics

- test_loss: `0.971019`
- test_mae: `0.039404`
- test_rmse: `0.042797`

## Interpretation

The held-out val error stayed finite with MAE=0.040524 deg and RMSE=0.042584 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.039404 deg and RMSE=0.042797 deg, which indicates a numerically stable baseline run.
