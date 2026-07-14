# Wave4 2 Gaussian Nll Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_bw__simplified_setpoints`
- Model Family: `wave4_2_gaussian_nll_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-22-47__te_wave4_2_gaussian_nll_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.10096127.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `17.816240`
- val_mae: `0.100961`
- val_rmse: `0.124886`
- val_pointwise_loss: `17.816240`
- val_centered_curve_shape_loss: `5.156337`
- val_curve_offset_loss: `2.255540`
- val_curve_amplitude_loss: `97.677094`
- val_sparse_harmonic_shape_loss: `0.145617`
- val_interval_coverage: `0.894424`
- val_interval_width: `6.248809`
- val_mean_sigma: `2.437986`
- val_structured_mae: `0.086645`
- val_structured_rmse: `0.109495`
- val_residual_offset_mean_abs: `0.112642`

## Test Metrics

- test_loss: `26.198933`
- test_mae: `0.099431`
- test_rmse: `0.123764`
- test_pointwise_loss: `26.198933`
- test_centered_curve_shape_loss: `4.767944`
- test_curve_offset_loss: `2.404187`
- test_curve_amplitude_loss: `93.929283`
- test_sparse_harmonic_shape_loss: `0.133767`
- test_interval_coverage: `0.901256`
- test_interval_width: `6.332100`
- test_mean_sigma: `2.470482`
- test_structured_mae: `0.085015`
- test_structured_rmse: `0.108365`
- test_residual_offset_mean_abs: `0.113999`

## Interpretation

The held-out val error stayed finite with MAE=0.100961 deg and RMSE=0.124886 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.099431 deg and RMSE=0.123764 deg, which indicates a numerically stable baseline run.
