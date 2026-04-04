# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_high_compute_long_remote`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-04-12-18-37__te_feedforward_high_compute_long_remote\checkpoints\feedforward-epoch=097-val_mae=0.00305764.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008004`
- val_mae: `0.003058`
- val_rmse: `0.003646`

## Test Metrics

- test_loss: `0.009019`
- test_mae: `0.003542`
- test_rmse: `0.004228`

## Interpretation

The held-out val error stayed finite with MAE=0.003058 deg and RMSE=0.003646 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003542 deg and RMSE=0.004228 deg, which indicates a numerically stable baseline run.
