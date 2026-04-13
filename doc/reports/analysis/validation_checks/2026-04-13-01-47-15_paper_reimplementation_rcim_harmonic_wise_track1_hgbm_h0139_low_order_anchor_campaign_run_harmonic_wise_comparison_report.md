# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting_track1_h0139_anchor`;
- run name: `track1_hgbm_h0139_low_order_anchor`;
- output run name: `track1_hgbm_h0139_low_order_anchor_campaign_run`;
- run instance id: `2026-04-13-01-46-28__track1_hgbm_h0139_low_order_anchor_campaign_run`;
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
| Validation | 0.002634 | 0.002876 | 9.570 | 3.588 | 0.000166 |
| Test | 0.002738 | 0.002932 | 9.288 | 2.749 | 0.000160 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.288%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002518 | 0.003319 | 0.002488 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000025 | 0.001581 |
| `h3` | 0.000019 | 0.000023 | 0.000019 | 0.020805 |
| `h39` | 0.000020 | 0.000027 | 0.000022 | 0.028149 |
| `h40` | 0.000031 | 0.000047 | 0.000030 | 0.069185 |
| `h78` | 0.000027 | 0.000033 | 0.000022 | 0.048214 |
| `h81` | 0.000013 | 0.000017 | 0.000012 | 0.077287 |
| `h156` | 0.000058 | 0.000162 | 0.000059 | 0.087325 |
| `h162` | 0.000038 | 0.000118 | 0.000044 | 0.076286 |
| `h240` | 0.000034 | 0.000066 | 0.000037 | 0.067586 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002518` | amplitude MAE `0.002488`
- `h156` | coefficient MAE `0.000058` | amplitude MAE `0.000059`
- `h162` | coefficient MAE `0.000038` | amplitude MAE `0.000044`
- `h240` | coefficient MAE `0.000034` | amplitude MAE `0.000037`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000030`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.041336 | 0.070642 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033069 | 0.053632 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.443%` | curve MAE `0.004596`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `9.240%` | curve MAE `0.003021`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `4.096%` | curve MAE `0.002744`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
