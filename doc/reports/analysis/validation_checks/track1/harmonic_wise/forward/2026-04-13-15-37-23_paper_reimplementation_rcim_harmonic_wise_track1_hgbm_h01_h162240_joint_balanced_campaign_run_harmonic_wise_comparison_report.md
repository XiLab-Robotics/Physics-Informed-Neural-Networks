# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h01_h162240_joint_balanced`;
- run name: `track1_hgbm_h01_h162240_joint_balanced`;
- output run name: `track1_hgbm_h01_h162240_joint_balanced_campaign_run`;
- run instance id: `2026-04-13-15-36-34__track1_hgbm_h01_h162240_joint_balanced_campaign_run`;
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
| Validation | 0.002760 | 0.002998 | 10.067 | 3.588 | 0.000172 |
| Test | 0.002605 | 0.002802 | 8.720 | 2.749 | 0.000153 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `8.720%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002379 | 0.003192 | 0.002350 | 0.000000 |
| `h1` | 0.000027 | 0.000033 | 0.000025 | 0.001624 |
| `h3` | 0.000019 | 0.000024 | 0.000019 | 0.021391 |
| `h39` | 0.000020 | 0.000028 | 0.000021 | 0.029000 |
| `h40` | 0.000031 | 0.000048 | 0.000031 | 0.070045 |
| `h78` | 0.000028 | 0.000038 | 0.000024 | 0.050510 |
| `h81` | 0.000014 | 0.000018 | 0.000013 | 0.080824 |
| `h156` | 0.000058 | 0.000164 | 0.000059 | 0.080094 |
| `h162` | 0.000037 | 0.000116 | 0.000043 | 0.077290 |
| `h240` | 0.000035 | 0.000069 | 0.000037 | 0.071431 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002379` | amplitude MAE `0.002350`
- `h156` | coefficient MAE `0.000058` | amplitude MAE `0.000059`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000043`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000037`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041396 | 0.070472 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032873 | 0.053908 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `8.451%` | curve MAE `0.005218`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `10.540%` | curve MAE `0.003446`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `4.353%` | curve MAE `0.002917`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
