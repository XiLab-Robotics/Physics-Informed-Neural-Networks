# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_best_training`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_best_training\checkpoints\feedforward-epoch=046-val_mae=0.00303861.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007297`
- val_mae: `0.003039`
- val_rmse: `0.003567`

## Test Metrics

- test_loss: `0.008000`
- test_mae: `0.003409`
- test_rmse: `0.003948`

## Interpretation

The held-out val error stayed finite with MAE=0.003039 deg and RMSE=0.003567 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003409 deg and RMSE=0.003948 deg, which indicates a numerically stable baseline run.
