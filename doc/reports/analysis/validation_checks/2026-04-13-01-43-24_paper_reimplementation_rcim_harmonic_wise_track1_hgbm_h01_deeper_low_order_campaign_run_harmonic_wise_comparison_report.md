# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h01_deeper`;
- run name: `track1_hgbm_h01_deeper_low_order`;
- output run name: `track1_hgbm_h01_deeper_low_order_campaign_run`;
- run instance id: `2026-04-13-01-42-34__track1_hgbm_h01_deeper_low_order_campaign_run`;
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
| Validation | 0.002631 | 0.002871 | 9.590 | 3.588 | 0.000165 |
| Test | 0.002697 | 0.002890 | 9.199 | 2.749 | 0.000158 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.199%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002464 | 0.003249 | 0.002433 | 0.000000 |
| `h1` | 0.000027 | 0.000032 | 0.000025 | 0.001629 |
| `h3` | 0.000019 | 0.000023 | 0.000019 | 0.020580 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.026775 |
| `h40` | 0.000030 | 0.000046 | 0.000030 | 0.068347 |
| `h78` | 0.000028 | 0.000034 | 0.000024 | 0.049689 |
| `h81` | 0.000013 | 0.000017 | 0.000012 | 0.076032 |
| `h156` | 0.000056 | 0.000159 | 0.000057 | 0.080090 |
| `h162` | 0.000039 | 0.000122 | 0.000045 | 0.076046 |
| `h240` | 0.000035 | 0.000067 | 0.000036 | 0.072655 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002464` | amplitude MAE `0.002433`
- `h156` | coefficient MAE `0.000056` | amplitude MAE `0.000057`
- `h162` | coefficient MAE `0.000039` | amplitude MAE `0.000045`
- `h240` | coefficient MAE `0.000035` | amplitude MAE `0.000036`
- `h40` | coefficient MAE `0.000030` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041280 | 0.070702 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032889 | 0.053569 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `8.220%` | curve MAE `0.005076`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.738%` | curve MAE `0.003184`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.581%` | curve MAE `0.002399`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.

