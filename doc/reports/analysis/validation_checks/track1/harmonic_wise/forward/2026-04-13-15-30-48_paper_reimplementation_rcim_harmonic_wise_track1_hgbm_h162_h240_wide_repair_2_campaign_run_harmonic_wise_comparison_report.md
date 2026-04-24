# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h162_h240_wide_repair_2`;
- run name: `track1_hgbm_h162_h240_wide_repair_2`;
- output run name: `track1_hgbm_h162_h240_wide_repair_2_campaign_run`;
- run instance id: `2026-04-13-15-29-58__track1_hgbm_h162_h240_wide_repair_2_campaign_run`;
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
| Validation | 0.002612 | 0.002853 | 9.431 | 3.588 | 0.000164 |
| Test | 0.002633 | 0.002835 | 9.000 | 2.749 | 0.000156 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.000%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002433 | 0.003196 | 0.002405 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000025 | 0.001589 |
| `h3` | 0.000019 | 0.000024 | 0.000019 | 0.020497 |
| `h39` | 0.000020 | 0.000026 | 0.000021 | 0.026797 |
| `h40` | 0.000031 | 0.000047 | 0.000030 | 0.069585 |
| `h78` | 0.000026 | 0.000032 | 0.000023 | 0.047901 |
| `h81` | 0.000013 | 0.000018 | 0.000013 | 0.080085 |
| `h156` | 0.000056 | 0.000159 | 0.000055 | 0.086979 |
| `h162` | 0.000037 | 0.000116 | 0.000042 | 0.074642 |
| `h240` | 0.000035 | 0.000070 | 0.000036 | 0.071205 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002433` | amplitude MAE `0.002405`
- `h156` | coefficient MAE `0.000056` | amplitude MAE `0.000055`
- `h162` | coefficient MAE `0.000037` | amplitude MAE `0.000042`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000036`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041421 | 0.070601 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033027 | 0.054416 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.274%` | curve MAE `0.004492`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `8.433%` | curve MAE `0.002758`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.403%` | curve MAE `0.002280`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
