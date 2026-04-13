# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h156162240_bridge_1`;
- run name: `track1_hgbm_h156162240_bridge_1`;
- output run name: `track1_hgbm_h156162240_bridge_1_campaign_run`;
- run instance id: `2026-04-13-15-31-55__track1_hgbm_h156162240_bridge_1_campaign_run`;
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
| Validation | 0.002571 | 0.002815 | 9.158 | 3.588 | 0.000162 |
| Test | 0.002632 | 0.002830 | 8.971 | 2.749 | 0.000155 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `8.971%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002412 | 0.003202 | 0.002388 | 0.000000 |
| `h1` | 0.000027 | 0.000032 | 0.000025 | 0.001662 |
| `h3` | 0.000019 | 0.000024 | 0.000018 | 0.021378 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.028185 |
| `h40` | 0.000031 | 0.000047 | 0.000031 | 0.069381 |
| `h78` | 0.000027 | 0.000035 | 0.000023 | 0.052840 |
| `h81` | 0.000013 | 0.000017 | 0.000012 | 0.077278 |
| `h156` | 0.000056 | 0.000182 | 0.000061 | 0.075474 |
| `h162` | 0.000037 | 0.000117 | 0.000043 | 0.074572 |
| `h240` | 0.000035 | 0.000069 | 0.000037 | 0.069693 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002412` | amplitude MAE `0.002388`
- `h156` | coefficient MAE `0.000056` | amplitude MAE `0.000061`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000043`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000037`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041386 | 0.070506 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033003 | 0.054845 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `6.209%` | curve MAE `0.003834`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `8.449%` | curve MAE `0.002763`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `1.625%` | curve MAE `0.001089`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
