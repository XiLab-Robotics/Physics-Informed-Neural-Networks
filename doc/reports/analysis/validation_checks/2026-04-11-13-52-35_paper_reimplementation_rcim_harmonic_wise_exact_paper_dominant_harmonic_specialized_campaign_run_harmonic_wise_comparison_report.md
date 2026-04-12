# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_exact_paper_dominant_specialized`;
- run name: `exact_paper_dominant_harmonic_specialized`;
- output run name: `exact_paper_dominant_harmonic_specialized_campaign_run`;
- run instance id: `2026-04-11-13-51-52__exact_paper_dominant_harmonic_specialized_campaign_run`;
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
| Validation | 0.002630 | 0.002870 | 9.564 | 3.588 | 0.000165 |
| Test | 0.002690 | 0.002885 | 9.123 | 2.749 | 0.000158 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.123%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002474 | 0.003264 | 0.002448 | 0.000000 |
| `h1` | 0.000025 | 0.000030 | 0.000024 | 0.001548 |
| `h3` | 0.000019 | 0.000024 | 0.000018 | 0.021080 |
| `h39` | 0.000020 | 0.000026 | 0.000021 | 0.026739 |
| `h40` | 0.000030 | 0.000046 | 0.000030 | 0.068402 |
| `h78` | 0.000028 | 0.000034 | 0.000024 | 0.049689 |
| `h81` | 0.000013 | 0.000017 | 0.000012 | 0.077194 |
| `h156` | 0.000057 | 0.000161 | 0.000060 | 0.082246 |
| `h162` | 0.000040 | 0.000120 | 0.000047 | 0.076587 |
| `h240` | 0.000036 | 0.000069 | 0.000038 | 0.072636 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002474` | amplitude MAE `0.002448`
- `h156` | coefficient MAE `0.000057` | amplitude MAE `0.000060`
- `h162` | coefficient MAE `0.000040` | amplitude MAE `0.000047`
- `h240` | coefficient MAE `0.000036` | amplitude MAE `0.000038`
- `h40` | coefficient MAE `0.000030` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041317 | 0.070714 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032944 | 0.053636 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.582%` | curve MAE `0.004682`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.435%` | curve MAE `0.003085`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.362%` | curve MAE `0.002253`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.

