# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order06_static_recovery`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-03-20-16-11-22__te_harmonic_order06_static_recovery\checkpoints\harmonic_regression-epoch=005-val_mae=0.04052873.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.945974`
- val_mae: `0.040529`
- val_rmse: `0.042572`

## Test Metrics

- test_loss: `0.970904`
- test_mae: `0.039406`
- test_rmse: `0.042796`

## Interpretation

The held-out val error stayed finite with MAE=0.040529 deg and RMSE=0.042572 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.039406 deg and RMSE=0.042796 deg, which indicates a numerically stable baseline run.
