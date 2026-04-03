# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_high_compute_remote`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-03-21-50-07__te_feedforward_high_compute_remote\checkpoints\feedforward-epoch=048-val_mae=0.00305896.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007267`
- val_mae: `0.003059`
- val_rmse: `0.003625`

## Test Metrics

- test_loss: `0.007402`
- test_mae: `0.003274`
- test_rmse: `0.003873`

## Interpretation

The held-out val error stayed finite with MAE=0.003059 deg and RMSE=0.003625 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003274 deg and RMSE=0.003873 deg, which indicates a numerically stable baseline run.
