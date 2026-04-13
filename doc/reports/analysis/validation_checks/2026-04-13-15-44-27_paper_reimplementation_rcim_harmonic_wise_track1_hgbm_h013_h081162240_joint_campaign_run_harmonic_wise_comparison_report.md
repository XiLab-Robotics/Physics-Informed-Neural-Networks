# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h013_h081162240_joint`;
- run name: `track1_hgbm_h013_h081162240_joint`;
- output run name: `track1_hgbm_h013_h081162240_joint_campaign_run`;
- run instance id: `2026-04-13-15-43-34__track1_hgbm_h013_h081162240_joint_campaign_run`;
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
| Validation | 0.002663 | 0.002904 | 9.634 | 3.588 | 0.000166 |
| Test | 0.002734 | 0.002927 | 9.129 | 2.749 | 0.000160 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.129%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002513 | 0.003286 | 0.002480 | 0.000000 |
| `h1` | 0.000027 | 0.000033 | 0.000025 | 0.001644 |
| `h3` | 0.000018 | 0.000023 | 0.000018 | 0.021025 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.027111 |
| `h40` | 0.000031 | 0.000048 | 0.000031 | 0.071658 |
| `h78` | 0.000026 | 0.000033 | 0.000022 | 0.046549 |
| `h81` | 0.000013 | 0.000018 | 0.000012 | 0.078269 |
| `h156` | 0.000057 | 0.000165 | 0.000060 | 0.085791 |
| `h162` | 0.000037 | 0.000114 | 0.000043 | 0.074255 |
| `h240` | 0.000035 | 0.000069 | 0.000036 | 0.070106 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002513` | amplitude MAE `0.002480`
- `h156` | coefficient MAE `0.000057` | amplitude MAE `0.000060`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000043`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000036`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041563 | 0.071062 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033032 | 0.054111 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `8.530%` | curve MAE `0.005267`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.295%` | curve MAE `0.003039`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `4.308%` | curve MAE `0.002886`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
