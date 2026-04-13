# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h013_h162_h240_joint`;
- run name: `track1_hgbm_h013_h162_h240_joint`;
- output run name: `track1_hgbm_h013_h162_h240_joint_campaign_run`;
- run instance id: `2026-04-13-01-51-49__track1_hgbm_h013_h162_h240_joint_campaign_run`;
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
| Validation | 0.002619 | 0.002860 | 9.535 | 3.588 | 0.000165 |
| Test | 0.002674 | 0.002870 | 9.067 | 2.749 | 0.000158 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.067%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002462 | 0.003220 | 0.002442 | 0.000000 |
| `h1` | 0.000026 | 0.000032 | 0.000025 | 0.001617 |
| `h3` | 0.000019 | 0.000023 | 0.000019 | 0.021642 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.028126 |
| `h40` | 0.000031 | 0.000047 | 0.000030 | 0.071163 |
| `h78` | 0.000028 | 0.000035 | 0.000023 | 0.054038 |
| `h81` | 0.000013 | 0.000017 | 0.000012 | 0.079675 |
| `h156` | 0.000057 | 0.000162 | 0.000058 | 0.086076 |
| `h162` | 0.000037 | 0.000114 | 0.000044 | 0.074808 |
| `h240` | 0.000035 | 0.000069 | 0.000035 | 0.070977 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002462` | amplitude MAE `0.002442`
- `h156` | coefficient MAE `0.000057` | amplitude MAE `0.000058`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000044`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000035`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041090 | 0.070526 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032874 | 0.053191 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `8.157%` | curve MAE `0.005037`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `10.854%` | curve MAE `0.003549`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.753%` | curve MAE `0.002514`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
