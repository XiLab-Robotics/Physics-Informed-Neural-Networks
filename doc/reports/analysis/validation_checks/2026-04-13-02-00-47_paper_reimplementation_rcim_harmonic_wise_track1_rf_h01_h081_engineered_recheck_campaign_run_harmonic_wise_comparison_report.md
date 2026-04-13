# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_random_forest_track1_h01_h081_engineered_recheck`;
- run name: `track1_rf_h01_h081_engineered_recheck`;
- output run name: `track1_rf_h01_h081_engineered_recheck_campaign_run`;
- run instance id: `2026-04-13-01-59-49__track1_rf_h01_h081_engineered_recheck_campaign_run`;
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
| Validation | 0.003081 | 0.003320 | 11.013 | 3.588 | 0.000202 |
| Test | 0.003234 | 0.003426 | 10.936 | 2.749 | 0.000198 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `10.936%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.003065 | 0.003633 | 0.003030 | 0.000000 |
| `h1` | 0.000025 | 0.000030 | 0.000024 | 0.001511 |
| `h3` | 0.000023 | 0.000029 | 0.000022 | 0.027645 |
| `h39` | 0.000023 | 0.000030 | 0.000024 | 0.030870 |
| `h40` | 0.000030 | 0.000043 | 0.000029 | 0.071212 |
| `h78` | 0.000041 | 0.000052 | 0.000038 | 0.061454 |
| `h81` | 0.000013 | 0.000017 | 0.000013 | 0.081279 |
| `h156` | 0.000092 | 0.000279 | 0.000103 | 0.100013 |
| `h162` | 0.000050 | 0.000128 | 0.000052 | 0.087885 |
| `h240` | 0.000051 | 0.000115 | 0.000054 | 0.111281 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.003065` | amplitude MAE `0.003030`
- `h156` | coefficient MAE `0.000092` | amplitude MAE `0.000103`
- `h240` | coefficient MAE `0.000051` | amplitude MAE `0.000054`
- `h162` | coefficient MAE `0.000050` | amplitude MAE `0.000052`
- `h78` | coefficient MAE `0.000041` | amplitude MAE `0.000038`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040286 | 0.069375 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033271 | 0.054555 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `13.219%` | curve MAE `0.008162`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `20.246%` | curve MAE `0.006620`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `8.471%` | curve MAE `0.005676`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.

