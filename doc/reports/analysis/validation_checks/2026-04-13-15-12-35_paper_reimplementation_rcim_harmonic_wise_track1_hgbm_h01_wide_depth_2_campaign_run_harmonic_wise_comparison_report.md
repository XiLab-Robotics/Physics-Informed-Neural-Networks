# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h01_wide_depth_2`;
- run name: `track1_hgbm_h01_wide_depth_2`;
- output run name: `track1_hgbm_h01_wide_depth_2_campaign_run`;
- run instance id: `2026-04-13-15-11-49__track1_hgbm_h01_wide_depth_2_campaign_run`;
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
| Validation | 0.002700 | 0.002938 | 9.830 | 3.588 | 0.000169 |
| Test | 0.002611 | 0.002810 | 8.707 | 2.749 | 0.000154 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `8.707%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002389 | 0.003184 | 0.002365 | 0.000000 |
| `h1` | 0.000027 | 0.000033 | 0.000025 | 0.001678 |
| `h3` | 0.000019 | 0.000024 | 0.000019 | 0.021436 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.027406 |
| `h40` | 0.000031 | 0.000048 | 0.000030 | 0.069951 |
| `h78` | 0.000027 | 0.000034 | 0.000023 | 0.050541 |
| `h81` | 0.000014 | 0.000018 | 0.000013 | 0.082888 |
| `h156` | 0.000058 | 0.000168 | 0.000059 | 0.080038 |
| `h162` | 0.000039 | 0.000120 | 0.000045 | 0.076187 |
| `h240` | 0.000034 | 0.000065 | 0.000035 | 0.070706 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002389` | amplitude MAE `0.002365`
- `h156` | coefficient MAE `0.000058` | amplitude MAE `0.000059`
- `h162` | coefficient MAE `0.000039` | amplitude MAE `0.000045`
- `h240` | coefficient MAE `0.000034` | amplitude MAE `0.000035`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041353 | 0.070452 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032821 | 0.053371 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `6.893%` | curve MAE `0.004256`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `7.632%` | curve MAE `0.002496`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `2.556%` | curve MAE `0.001712`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
