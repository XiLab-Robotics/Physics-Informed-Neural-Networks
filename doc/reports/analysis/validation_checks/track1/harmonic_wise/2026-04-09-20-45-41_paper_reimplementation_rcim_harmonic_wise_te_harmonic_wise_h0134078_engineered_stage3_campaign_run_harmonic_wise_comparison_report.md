# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting`;
- run name: `te_harmonic_wise_h0134078_engineered_stage3`;
- output run name: `te_harmonic_wise_h0134078_engineered_stage3_campaign_run`;
- run instance id: `2026-04-09-20-44-59__te_harmonic_wise_h0134078_engineered_stage3_campaign_run`;
- comparison scope: `offline_only`;
- `Target A` status: **not_yet_met**

## Harmonic Configuration

- selected harmonics: `0, 1, 39, 40, 78`
- decomposition point stride: `20`
- percentage-error denominator: `mean_abs_truth`
- feature terms: `speed_torque_product, speed_temperature_product, torque_temperature_product, speed_squared, torque_squared`

## Split Coverage

| Split | Directional Curves | Files |
| --- | ---: | ---: |
| Train | 1356 | 678 |
| Validation | 388 | 194 |
| Test | 194 | 97 |

## Offline Curve Reconstruction Metrics

| Split | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | Oracle Mean Percentage Error [%] | Harmonic Target MAE |
| --- | ---: | ---: | ---: | ---: | ---: |
| Validation | 0.003409 | 0.003846 | 11.750 | 6.996 | 0.000294 |
| Test | 0.003114 | 0.003443 | 10.625 | 4.676 | 0.000298 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `10.625%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `4.676%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002456 | 0.003202 | 0.002424 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000024 | 0.001610 |
| `h39` | 0.000021 | 0.000028 | 0.000022 | 0.029037 |
| `h40` | 0.000032 | 0.000047 | 0.000034 | 0.070087 |
| `h78` | 0.000032 | 0.000041 | 0.000030 | 0.058255 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002456` | amplitude MAE `0.002424`
- `h40` | coefficient MAE `0.000032` | amplitude MAE `0.000034`
- `h78` | coefficient MAE `0.000032` | amplitude MAE `0.000030`
- `h1` | coefficient MAE `0.000026` | amplitude MAE `0.000024`
- `h39` | coefficient MAE `0.000021` | amplitude MAE `0.000022`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040464 | 0.070923 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033387 | 0.057965 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `5.555%` | curve MAE `0.003430`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `10.123%` | curve MAE `0.003310`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `1.902%` | curve MAE `0.001274`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
