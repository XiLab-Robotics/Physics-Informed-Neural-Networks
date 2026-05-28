# Residual Harmonic Gru Sequence Fw Dense240 Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_remote_Fw_dense240`
- Model Family: `residual_harmonic_gru_sequence_fw_dense240`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_fw_dense240\2026-05-27-19-32-17__te_residual_harmonic_gru_sequence_remote_fw_dense240\checkpoints\residual_harmonic_gru_sequence-epoch=023-val_mae=0.00326993.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.031981`
- val_mae: `0.003270`
- val_rmse: `0.003785`
- val_structured_mae: `0.017333`
- val_structured_rmse: `0.018927`

## Test Metrics

- test_loss: `0.027109`
- test_mae: `0.003219`
- test_rmse: `0.003653`
- test_structured_mae: `0.017609`
- test_structured_rmse: `0.019483`

## Interpretation

The held-out val error stayed finite with MAE=0.003270 deg and RMSE=0.003785 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003219 deg and RMSE=0.003653 deg, which indicates a numerically stable baseline run.
