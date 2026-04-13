# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h162240_engineered_heavy`;
- run name: `track1_hgbm_h162240_engineered_heavy`;
- output run name: `track1_hgbm_h162240_engineered_heavy_campaign_run`;
- run instance id: `2026-04-13-15-46-41__track1_hgbm_h162240_engineered_heavy_campaign_run`;
- comparison scope: `offline_only`;
- `Target A` status: **not_yet_met**

## Harmonic Configuration

- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
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
| Validation | 0.002732 | 0.002977 | 9.600 | 3.588 | 0.000179 |
| Test | 0.002696 | 0.002900 | 9.644 | 2.749 | 0.000163 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.644%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002474 | 0.003223 | 0.002441 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000025 | 0.001597 |
| `h3` | 0.000021 | 0.000027 | 0.000019 | 0.026029 |
| `h39` | 0.000021 | 0.000028 | 0.000022 | 0.029716 |
| `h40` | 0.000031 | 0.000047 | 0.000033 | 0.069127 |
| `h78` | 0.000032 | 0.000041 | 0.000029 | 0.059696 |
| `h81` | 0.000014 | 0.000019 | 0.000013 | 0.082918 |
| `h156` | 0.000083 | 0.000296 | 0.000092 | 0.114962 |
| `h162` | 0.000040 | 0.000105 | 0.000045 | 0.090371 |
| `h240` | 0.000043 | 0.000082 | 0.000044 | 0.088137 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002474` | amplitude MAE `0.002441`
- `h156` | coefficient MAE `0.000083` | amplitude MAE `0.000092`
- `h240` | coefficient MAE `0.000043` | amplitude MAE `0.000044`
- `h162` | coefficient MAE `0.000040` | amplitude MAE `0.000045`
- `h78` | coefficient MAE `0.000032` | amplitude MAE `0.000029`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040556 | 0.071074 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033544 | 0.059438 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `5.437%` | curve MAE `0.003358`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `11.177%` | curve MAE `0.003655`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `0.990%` | curve MAE `0.000663`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
