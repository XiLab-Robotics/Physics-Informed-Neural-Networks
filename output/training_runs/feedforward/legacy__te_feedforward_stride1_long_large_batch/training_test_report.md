# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_long_large_batch`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_stride1_long_large_batch\checkpoints\feedforward-epoch=050-val_mae=0.00310382.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007425`
- val_mae: `0.003104`
- val_rmse: `0.003551`

## Test Metrics

- test_loss: `0.007650`
- test_mae: `0.003358`
- test_rmse: `0.003769`

## Interpretation

The held-out val error stayed finite with MAE=0.003104 deg and RMSE=0.003551 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003358 deg and RMSE=0.003769 deg, which indicates a numerically stable baseline run.
