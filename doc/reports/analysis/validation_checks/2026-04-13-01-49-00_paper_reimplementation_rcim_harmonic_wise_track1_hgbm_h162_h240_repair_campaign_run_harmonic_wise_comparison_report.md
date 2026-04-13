# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h162_h240_repair`;
- run name: `track1_hgbm_h162_h240_repair`;
- output run name: `track1_hgbm_h162_h240_repair_campaign_run`;
- run instance id: `2026-04-13-01-48-16__track1_hgbm_h162_h240_repair_campaign_run`;
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
| Validation | 0.002595 | 0.002837 | 9.448 | 3.588 | 0.000163 |
| Test | 0.002578 | 0.002776 | 8.795 | 2.749 | 0.000152 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `8.795%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002350 | 0.003092 | 0.002331 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000024 | 0.001601 |
| `h3` | 0.000019 | 0.000024 | 0.000018 | 0.021060 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.027438 |
| `h40` | 0.000031 | 0.000047 | 0.000031 | 0.070809 |
| `h78` | 0.000028 | 0.000036 | 0.000024 | 0.050291 |
| `h81` | 0.000013 | 0.000018 | 0.000013 | 0.078348 |
| `h156` | 0.000055 | 0.000159 | 0.000057 | 0.078934 |
| `h162` | 0.000037 | 0.000112 | 0.000043 | 0.073360 |
| `h240` | 0.000035 | 0.000069 | 0.000036 | 0.071646 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002350` | amplitude MAE `0.002331`
- `h156` | coefficient MAE `0.000055` | amplitude MAE `0.000057`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000043`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000036`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041070 | 0.069849 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032828 | 0.054309 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `8.338%` | curve MAE `0.005149`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `11.275%` | curve MAE `0.003687`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.700%` | curve MAE `0.002479`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
