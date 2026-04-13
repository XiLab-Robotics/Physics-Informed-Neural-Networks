# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h01_long_budget_regularized`;
- run name: `track1_hgbm_h01_long_budget_regularized`;
- output run name: `track1_hgbm_h01_long_budget_regularized_campaign_run`;
- run instance id: `2026-04-13-15-19-19__track1_hgbm_h01_long_budget_regularized_campaign_run`;
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
| Validation | 0.002645 | 0.002887 | 9.659 | 3.588 | 0.000167 |
| Test | 0.002620 | 0.002817 | 8.807 | 2.749 | 0.000154 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `8.807%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002391 | 0.003201 | 0.002368 | 0.000000 |
| `h1` | 0.000026 | 0.000032 | 0.000025 | 0.001615 |
| `h3` | 0.000019 | 0.000024 | 0.000019 | 0.022359 |
| `h39` | 0.000020 | 0.000027 | 0.000022 | 0.026993 |
| `h40` | 0.000031 | 0.000047 | 0.000031 | 0.070799 |
| `h78` | 0.000028 | 0.000033 | 0.000024 | 0.050713 |
| `h81` | 0.000014 | 0.000018 | 0.000013 | 0.079880 |
| `h156` | 0.000056 | 0.000149 | 0.000062 | 0.078554 |
| `h162` | 0.000041 | 0.000111 | 0.000046 | 0.088424 |
| `h240` | 0.000036 | 0.000069 | 0.000038 | 0.076033 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002391` | amplitude MAE `0.002368`
- `h156` | coefficient MAE `0.000056` | amplitude MAE `0.000062`
- `h162` | coefficient MAE `0.000041` | amplitude MAE `0.000046`
- `h240` | coefficient MAE `0.000036` | amplitude MAE `0.000038`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041517 | 0.070601 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033102 | 0.054224 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.909%` | curve MAE `0.004884`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.589%` | curve MAE `0.003136`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `4.036%` | curve MAE `0.002704`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
