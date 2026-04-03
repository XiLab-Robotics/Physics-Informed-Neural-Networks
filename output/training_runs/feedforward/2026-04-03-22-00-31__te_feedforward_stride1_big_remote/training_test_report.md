# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_big_remote`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-04-03-22-00-31__te_feedforward_stride1_big_remote\checkpoints\feedforward-epoch=136-val_mae=0.00301873.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007308`
- val_mae: `0.003019`
- val_rmse: `0.003474`

## Test Metrics

- test_loss: `0.007349`
- test_mae: `0.003278`
- test_rmse: `0.003671`

## Interpretation

The held-out val error stayed finite with MAE=0.003019 deg and RMSE=0.003474 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003278 deg and RMSE=0.003671 deg, which indicates a numerically stable baseline run.
