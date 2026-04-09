# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting`;
- run name: `te_harmonic_wise_h01340_engineered_stage2`;
- output run name: `te_harmonic_wise_h01340_engineered_stage2_campaign_run`;
- run instance id: `2026-04-09-20-44-15__te_harmonic_wise_h01340_engineered_stage2_campaign_run`;
- comparison scope: `offline_only`;
- `Target A` status: **not_yet_met**

## Harmonic Configuration

- selected harmonics: `0, 1, 39, 40`
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
| Validation | 0.003467 | 0.003960 | 11.910 | 7.436 | 0.000365 |
| Test | 0.003213 | 0.003606 | 10.797 | 5.178 | 0.000372 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `10.797%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `5.178%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002447 | 0.003203 | 0.002414 | 0.000000 |
| `h1` | 0.000026 | 0.000032 | 0.000025 | 0.001650 |
| `h39` | 0.000021 | 0.000027 | 0.000021 | 0.029782 |
| `h40` | 0.000032 | 0.000046 | 0.000033 | 0.069840 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002447` | amplitude MAE `0.002414`
- `h40` | coefficient MAE `0.000032` | amplitude MAE `0.000033`
- `h1` | coefficient MAE `0.000026` | amplitude MAE `0.000025`
- `h39` | coefficient MAE `0.000021` | amplitude MAE `0.000021`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040318 | 0.070440 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033648 | 0.057883 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `6.132%` | curve MAE `0.003787`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.885%` | curve MAE `0.003233`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `1.874%` | curve MAE `0.001255`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
