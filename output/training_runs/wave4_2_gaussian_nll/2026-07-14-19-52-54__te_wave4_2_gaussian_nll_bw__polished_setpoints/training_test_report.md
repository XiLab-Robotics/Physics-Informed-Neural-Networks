# Wave4 2 Gaussian Nll Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_bw__polished_setpoints`
- Model Family: `wave4_2_gaussian_nll_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-19-52-54__te_wave4_2_gaussian_nll_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.08419463.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `22.348402`
- val_mae: `0.084195`
- val_rmse: `0.104719`
- val_pointwise_loss: `22.348402`
- val_centered_curve_shape_loss: `4.174016`
- val_curve_offset_loss: `1.015862`
- val_curve_amplitude_loss: `83.583786`
- val_sparse_harmonic_shape_loss: `0.117843`
- val_interval_coverage: `0.903310`
- val_interval_width: `5.604909`
- val_mean_sigma: `2.186767`
- val_structured_mae: `0.082726`
- val_structured_rmse: `0.103482`
- val_residual_offset_mean_abs: `0.086360`

## Test Metrics

- test_loss: `28.651054`
- test_mae: `0.084400`
- test_rmse: `0.105673`
- test_pointwise_loss: `28.651054`
- test_centered_curve_shape_loss: `4.280906`
- test_curve_offset_loss: `0.956501`
- test_curve_amplitude_loss: `84.862976`
- test_sparse_harmonic_shape_loss: `0.120914`
- test_interval_coverage: `0.907351`
- test_interval_width: `5.864646`
- test_mean_sigma: `2.288104`
- test_structured_mae: `0.083121`
- test_structured_rmse: `0.104331`
- test_residual_offset_mean_abs: `0.086919`

## Interpretation

The held-out val error stayed finite with MAE=0.084195 deg and RMSE=0.104719 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.084400 deg and RMSE=0.105673 deg, which indicates a numerically stable baseline run.
