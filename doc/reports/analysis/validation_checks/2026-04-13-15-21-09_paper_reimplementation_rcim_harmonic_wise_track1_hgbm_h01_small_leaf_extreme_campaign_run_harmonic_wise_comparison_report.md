# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h01_small_leaf_extreme`;
- run name: `track1_hgbm_h01_small_leaf_extreme`;
- output run name: `track1_hgbm_h01_small_leaf_extreme_campaign_run`;
- run instance id: `2026-04-13-15-20-17__track1_hgbm_h01_small_leaf_extreme_campaign_run`;
- comparison scope: `offline_only`;
- `Target A` status: **not_yet_met**

## Harmonic Configuration

- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- decomposition point stride: `20`
- percentage-error denominator: `mean_abs_truth`
- feature terms: `base_only`

## Split Coverage

| Split | Directional Curves | Files |
| --- | ---: | ---: |
| Train | 1356 | 678 |
| Validation | 388 | 194 |
| Test | 194 | 97 |

## Offline Curve Reconstruction Metrics

| Split | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | Oracle Mean Percentage Error [%] | Harmonic Target MAE |
| --- | ---: | ---: | ---: | ---: | ---: |
| Validation | 0.002664 | 0.002904 | 9.674 | 3.588 | 0.000167 |
| Test | 0.002700 | 0.002894 | 9.125 | 2.749 | 0.000158 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.125%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002480 | 0.003296 | 0.002453 | 0.000000 |
| `h1` | 0.000027 | 0.000033 | 0.000026 | 0.001636 |
| `h3` | 0.000019 | 0.000024 | 0.000019 | 0.021339 |
| `h39` | 0.000020 | 0.000026 | 0.000021 | 0.026687 |
| `h40` | 0.000030 | 0.000046 | 0.000031 | 0.069966 |
| `h78` | 0.000029 | 0.000038 | 0.000025 | 0.051458 |
| `h81` | 0.000013 | 0.000017 | 0.000012 | 0.075754 |
| `h156` | 0.000055 | 0.000183 | 0.000063 | 0.078217 |
| `h162` | 0.000037 | 0.000115 | 0.000044 | 0.075551 |
| `h240` | 0.000035 | 0.000070 | 0.000036 | 0.073405 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002480` | amplitude MAE `0.002453`
- `h156` | coefficient MAE `0.000055` | amplitude MAE `0.000063`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000044`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000036`
- `h40` | coefficient MAE `0.000030` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041448 | 0.070759 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032850 | 0.053735 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.530%` | curve MAE `0.004650`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.489%` | curve MAE `0.003103`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.367%` | curve MAE `0.002256`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
