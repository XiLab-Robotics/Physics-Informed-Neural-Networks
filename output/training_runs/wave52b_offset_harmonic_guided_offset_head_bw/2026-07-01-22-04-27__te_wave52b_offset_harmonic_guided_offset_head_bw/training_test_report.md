# Wave52B Offset Harmonic Guided Offset Head Bw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_head_bw`
- Model Family: `wave52b_offset_harmonic_guided_offset_head_bw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_head_bw\2026-07-01-22-04-27__te_wave52b_offset_harmonic_guided_offset_head_bw\checkpoints\wave52b_offset_harmonic_guided-epoch=098-val_mae=0.00259676.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.037325`
- val_mae: `0.002597`
- val_rmse: `0.003223`
- val_pointwise_loss: `0.037137`
- val_centered_curve_shape_loss: `0.035880`
- val_curve_offset_loss: `0.001256`
- val_curve_amplitude_loss: `0.367015`
- val_sparse_harmonic_shape_loss: `0.000889`
- val_structured_mae: `0.019549`
- val_structured_rmse: `0.023002`
- val_base_mae: `0.011559`
- val_base_rmse: `0.013208`
- val_residual_offset_mean_abs: `0.010983`

## Test Metrics

- test_loss: `0.020172`
- test_mae: `0.002008`
- test_rmse: `0.002632`
- test_pointwise_loss: `0.019987`
- test_centered_curve_shape_loss: `0.018754`
- test_curve_offset_loss: `0.001233`
- test_curve_amplitude_loss: `0.174865`
- test_sparse_harmonic_shape_loss: `0.000445`
- test_structured_mae: `0.020345`
- test_structured_rmse: `0.023741`
- test_base_mae: `0.011377`
- test_base_rmse: `0.012818`
- test_residual_offset_mean_abs: `0.010861`

## Interpretation

The held-out val error stayed finite with MAE=0.002597 deg and RMSE=0.003223 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002008 deg and RMSE=0.002632 deg, which indicates a numerically stable baseline run.
