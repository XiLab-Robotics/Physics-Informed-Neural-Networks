# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h0181_heavy_reference`;
- run name: `track1_hgbm_h0181_heavy_reference`;
- output run name: `track1_hgbm_h0181_heavy_reference_campaign_run`;
- run instance id: `2026-04-13-15-26-40__track1_hgbm_h0181_heavy_reference_campaign_run`;
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
| Validation | 0.002667 | 0.002907 | 9.643 | 3.588 | 0.000167 |
| Test | 0.002735 | 0.002929 | 9.131 | 2.749 | 0.000160 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.131%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002517 | 0.003290 | 0.002484 | 0.000000 |
| `h1` | 0.000027 | 0.000033 | 0.000025 | 0.001647 |
| `h3` | 0.000019 | 0.000024 | 0.000019 | 0.021214 |
| `h39` | 0.000020 | 0.000027 | 0.000021 | 0.027171 |
| `h40` | 0.000031 | 0.000048 | 0.000031 | 0.071667 |
| `h78` | 0.000026 | 0.000033 | 0.000022 | 0.046520 |
| `h81` | 0.000013 | 0.000018 | 0.000012 | 0.078429 |
| `h156` | 0.000057 | 0.000165 | 0.000060 | 0.085838 |
| `h162` | 0.000039 | 0.000117 | 0.000046 | 0.076367 |
| `h240` | 0.000033 | 0.000065 | 0.000035 | 0.068390 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002517` | amplitude MAE `0.002484`
- `h156` | coefficient MAE `0.000057` | amplitude MAE `0.000060`
- `h162` | coefficient MAE `0.000039` | amplitude MAE `0.000046`
- `h240` | coefficient MAE `0.000033` | amplitude MAE `0.000035`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000031`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041587 | 0.071077 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033006 | 0.054129 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `8.562%` | curve MAE `0.005287`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.336%` | curve MAE `0.003053`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `4.337%` | curve MAE `0.002906`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
