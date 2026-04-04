# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote\checkpoints\feedforward-epoch=095-val_mae=0.00304393.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007425`
- val_mae: `0.003044`
- val_rmse: `0.003506`

## Test Metrics

- test_loss: `0.007485`
- test_mae: `0.003264`
- test_rmse: `0.003679`

## Interpretation

The held-out val error stayed finite with MAE=0.003044 deg and RMSE=0.003506 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003264 deg and RMSE=0.003679 deg, which indicates a numerically stable baseline run.
