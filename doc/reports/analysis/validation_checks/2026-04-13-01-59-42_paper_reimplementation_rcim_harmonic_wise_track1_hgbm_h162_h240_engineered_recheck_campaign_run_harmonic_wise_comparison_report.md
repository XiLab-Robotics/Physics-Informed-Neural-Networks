# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h162_h240_engineered_recheck`;
- run name: `track1_hgbm_h162_h240_engineered_recheck`;
- output run name: `track1_hgbm_h162_h240_engineered_recheck_campaign_run`;
- run instance id: `2026-04-13-01-58-57__track1_hgbm_h162_h240_engineered_recheck_campaign_run`;
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
| Validation | 0.002699 | 0.002944 | 9.507 | 3.588 | 0.000177 |
| Test | 0.002655 | 0.002857 | 9.408 | 2.749 | 0.000160 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.408%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002420 | 0.003144 | 0.002387 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000024 | 0.001593 |
| `h3` | 0.000020 | 0.000028 | 0.000018 | 0.026179 |
| `h39` | 0.000021 | 0.000028 | 0.000022 | 0.030516 |
| `h40` | 0.000031 | 0.000046 | 0.000033 | 0.067338 |
| `h78` | 0.000033 | 0.000042 | 0.000030 | 0.065556 |
| `h81` | 0.000014 | 0.000018 | 0.000014 | 0.082652 |
| `h156` | 0.000084 | 0.000289 | 0.000094 | 0.110037 |
| `h162` | 0.000039 | 0.000107 | 0.000043 | 0.088779 |
| `h240` | 0.000045 | 0.000096 | 0.000047 | 0.087423 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002420` | amplitude MAE `0.002387`
- `h156` | coefficient MAE `0.000084` | amplitude MAE `0.000094`
- `h240` | coefficient MAE `0.000045` | amplitude MAE `0.000047`
- `h162` | coefficient MAE `0.000039` | amplitude MAE `0.000043`
- `h78` | coefficient MAE `0.000033` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040060 | 0.070749 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033525 | 0.059225 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `6.874%` | curve MAE `0.004245`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `12.869%` | curve MAE `0.004208`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `1.313%` | curve MAE `0.000880`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.

