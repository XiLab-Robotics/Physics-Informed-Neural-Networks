# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward_bw\2026-05-06-20-41-50__te_feedforward_stride1_high_compute_long_remote_bw\checkpoints\feedforward-epoch=093-val_mae=0.00304864.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027714`
- val_mae: `0.003049`
- val_rmse: `0.003545`

## Test Metrics

- test_loss: `0.027001`
- test_mae: `0.003262`
- test_rmse: `0.003749`

## Interpretation

The held-out val error stayed finite with MAE=0.003049 deg and RMSE=0.003545 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003262 deg and RMSE=0.003749 deg, which indicates a numerically stable baseline run.
