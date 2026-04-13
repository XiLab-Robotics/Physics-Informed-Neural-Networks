# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h013_engineered_recheck`;
- run name: `track1_hgbm_h013_engineered_recheck`;
- output run name: `track1_hgbm_h013_engineered_recheck_campaign_run`;
- run instance id: `2026-04-13-01-58-06__track1_hgbm_h013_engineered_recheck_campaign_run`;
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
| Validation | 0.002687 | 0.002933 | 9.496 | 3.588 | 0.000177 |
| Test | 0.002650 | 0.002852 | 9.501 | 2.749 | 0.000160 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.501%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002416 | 0.003162 | 0.002388 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000025 | 0.001600 |
| `h3` | 0.000020 | 0.000028 | 0.000018 | 0.025298 |
| `h39` | 0.000021 | 0.000028 | 0.000022 | 0.030591 |
| `h40` | 0.000031 | 0.000046 | 0.000033 | 0.069357 |
| `h78` | 0.000033 | 0.000041 | 0.000030 | 0.060125 |
| `h81` | 0.000014 | 0.000018 | 0.000014 | 0.080430 |
| `h156` | 0.000083 | 0.000285 | 0.000091 | 0.107123 |
| `h162` | 0.000042 | 0.000119 | 0.000043 | 0.094231 |
| `h240` | 0.000046 | 0.000093 | 0.000049 | 0.087330 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002416` | amplitude MAE `0.002388`
- `h156` | coefficient MAE `0.000083` | amplitude MAE `0.000091`
- `h240` | coefficient MAE `0.000046` | amplitude MAE `0.000049`
- `h162` | coefficient MAE `0.000042` | amplitude MAE `0.000043`
- `h78` | coefficient MAE `0.000033` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040177 | 0.070688 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033349 | 0.058389 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `4.324%` | curve MAE `0.002670`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `10.739%` | curve MAE `0.003512`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `0.995%` | curve MAE `0.000667`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
