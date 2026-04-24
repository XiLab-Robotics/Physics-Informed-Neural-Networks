# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_random_forest`;
- run name: `te_harmonic_wise_h013_random_forest_diagnostic`;
- output run name: `te_harmonic_wise_h013_random_forest_diagnostic_campaign_run`;
- run instance id: `2026-04-09-20-43-42__te_harmonic_wise_h013_random_forest_diagnostic_campaign_run`;
- comparison scope: `offline_only`;
- `Target A` status: **not_yet_met**

## Harmonic Configuration

- selected harmonics: `0, 1, 39`
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
| Validation | 0.003820 | 0.004316 | 13.292 | 7.563 | 0.000570 |
| Test | 0.003702 | 0.004107 | 12.084 | 5.310 | 0.000633 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `12.084%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `5.310%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.003069 | 0.003640 | 0.003033 | 0.000000 |
| `h1` | 0.000024 | 0.000030 | 0.000023 | 0.001492 |
| `h39` | 0.000023 | 0.000030 | 0.000025 | 0.031110 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.003069` | amplitude MAE `0.003033`
- `h1` | coefficient MAE `0.000024` | amplitude MAE `0.000023`
- `h39` | coefficient MAE `0.000023` | amplitude MAE `0.000025`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040301 | 0.068765 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033146 | 0.053992 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `13.142%` | curve MAE `0.008115`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `20.004%` | curve MAE `0.006541`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `8.568%` | curve MAE `0.005741`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
