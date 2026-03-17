# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride5_long_large_batch_big_model`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_stride5_long_large_batch_big_model\checkpoints\feedforward-epoch=104-val_mae=0.00310436.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007794`
- val_mae: `0.003104`
- val_rmse: `0.003666`

## Test Metrics

- test_loss: `0.008567`
- test_mae: `0.003472`
- test_rmse: `0.004004`

## Interpretation

The held-out val error stayed finite with MAE=0.003104 deg and RMSE=0.003666 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003472 deg and RMSE=0.004004 deg, which indicates a numerically stable baseline run.
