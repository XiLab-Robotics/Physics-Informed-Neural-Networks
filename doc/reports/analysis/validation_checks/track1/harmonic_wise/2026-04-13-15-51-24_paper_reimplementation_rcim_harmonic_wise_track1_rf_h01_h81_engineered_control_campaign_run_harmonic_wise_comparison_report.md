# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_random_forest_track1_h01_h81_engineered_control`;
- run name: `track1_rf_h01_h81_engineered_control`;
- output run name: `track1_rf_h01_h81_engineered_control_campaign_run`;
- run instance id: `2026-04-13-15-49-55__track1_rf_h01_h81_engineered_control_campaign_run`;
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
| Validation | 0.003081 | 0.003320 | 10.994 | 3.588 | 0.000202 |
| Test | 0.003239 | 0.003431 | 10.982 | 2.749 | 0.000198 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `10.982%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.003069 | 0.003641 | 0.003030 | 0.000000 |
| `h1` | 0.000025 | 0.000030 | 0.000023 | 0.001505 |
| `h3` | 0.000023 | 0.000029 | 0.000022 | 0.027626 |
| `h39` | 0.000023 | 0.000030 | 0.000024 | 0.030998 |
| `h40` | 0.000030 | 0.000043 | 0.000028 | 0.071249 |
| `h78` | 0.000041 | 0.000052 | 0.000037 | 0.061716 |
| `h81` | 0.000013 | 0.000017 | 0.000013 | 0.081149 |
| `h156` | 0.000091 | 0.000280 | 0.000101 | 0.101188 |
| `h162` | 0.000050 | 0.000130 | 0.000050 | 0.088985 |
| `h240` | 0.000051 | 0.000114 | 0.000054 | 0.110658 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.003069` | amplitude MAE `0.003030`
- `h156` | coefficient MAE `0.000091` | amplitude MAE `0.000101`
- `h240` | coefficient MAE `0.000051` | amplitude MAE `0.000054`
- `h162` | coefficient MAE `0.000050` | amplitude MAE `0.000050`
- `h78` | coefficient MAE `0.000041` | amplitude MAE `0.000037`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040250 | 0.069420 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033243 | 0.054521 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `13.158%` | curve MAE `0.008125`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `20.478%` | curve MAE `0.006696`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `8.432%` | curve MAE `0.005650`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
