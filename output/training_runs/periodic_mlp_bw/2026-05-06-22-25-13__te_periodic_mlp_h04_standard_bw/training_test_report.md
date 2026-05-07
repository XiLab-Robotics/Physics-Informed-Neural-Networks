# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_bw\2026-05-06-22-25-13__te_periodic_mlp_h04_standard_bw\checkpoints\periodic_mlp-epoch=049-val_mae=0.00315372.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.029506`
- val_mae: `0.003154`
- val_rmse: `0.003809`

## Test Metrics

- test_loss: `0.031233`
- test_mae: `0.003525`
- test_rmse: `0.004132`

## Interpretation

The held-out val error stayed finite with MAE=0.003154 deg and RMSE=0.003809 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003525 deg and RMSE=0.004132 deg, which indicates a numerically stable baseline run.
