# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_high_compute`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_high_compute\checkpoints\feedforward-epoch=021-val_mae=0.00319778.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007775`
- val_mae: `0.003198`
- val_rmse: `0.003790`

## Test Metrics

- test_loss: `0.007487`
- test_mae: `0.003319`
- test_rmse: `0.003915`

## Interpretation

The held-out val error stayed finite with MAE=0.003198 deg and RMSE=0.003790 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003319 deg and RMSE=0.003915 deg, which indicates a numerically stable baseline run.
