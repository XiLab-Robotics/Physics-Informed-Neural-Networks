# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h81156162240_cluster`;
- run name: `track1_hgbm_h81156162240_cluster`;
- output run name: `track1_hgbm_h81156162240_cluster_campaign_run`;
- run instance id: `2026-04-13-15-35-39__track1_hgbm_h81156162240_cluster_campaign_run`;
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
| Validation | 0.002606 | 0.002848 | 9.486 | 3.588 | 0.000164 |
| Test | 0.002594 | 0.002790 | 8.778 | 2.749 | 0.000152 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `8.778%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002369 | 0.003137 | 0.002352 | 0.000000 |
| `h1` | 0.000027 | 0.000032 | 0.000025 | 0.001653 |
| `h3` | 0.000019 | 0.000024 | 0.000018 | 0.021876 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.028198 |
| `h40` | 0.000031 | 0.000047 | 0.000031 | 0.071209 |
| `h78` | 0.000027 | 0.000035 | 0.000022 | 0.055866 |
| `h81` | 0.000013 | 0.000018 | 0.000012 | 0.077958 |
| `h156` | 0.000055 | 0.000186 | 0.000061 | 0.075298 |
| `h162` | 0.000037 | 0.000114 | 0.000044 | 0.074048 |
| `h240` | 0.000034 | 0.000067 | 0.000035 | 0.067133 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002369` | amplitude MAE `0.002352`
- `h156` | coefficient MAE `0.000055` | amplitude MAE `0.000061`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000044`
- `h240` | coefficient MAE `0.000034` | amplitude MAE `0.000035`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041434 | 0.070544 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032878 | 0.053646 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.606%` | curve MAE `0.004697`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.924%` | curve MAE `0.003245`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `2.870%` | curve MAE `0.001923`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
