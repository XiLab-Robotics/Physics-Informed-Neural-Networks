# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_random_forest_track1_h081_focus`;
- run name: `track1_rf_h081_focus`;
- output run name: `track1_rf_h081_focus_campaign_run`;
- run instance id: `2026-04-13-01-55-26__track1_rf_h081_focus_campaign_run`;
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
| Validation | 0.003122 | 0.003351 | 11.328 | 3.588 | 0.000195 |
| Test | 0.003315 | 0.003500 | 11.166 | 2.749 | 0.000198 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `11.166%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.003147 | 0.003719 | 0.003095 | 0.000000 |
| `h1` | 0.000026 | 0.000031 | 0.000024 | 0.001601 |
| `h3` | 0.000022 | 0.000027 | 0.000021 | 0.025709 |
| `h39` | 0.000024 | 0.000030 | 0.000026 | 0.031425 |
| `h40` | 0.000029 | 0.000042 | 0.000028 | 0.069697 |
| `h78` | 0.000038 | 0.000050 | 0.000035 | 0.060548 |
| `h81` | 0.000013 | 0.000016 | 0.000013 | 0.076867 |
| `h156` | 0.000067 | 0.000245 | 0.000078 | 0.095709 |
| `h162` | 0.000048 | 0.000133 | 0.000050 | 0.085388 |
| `h240` | 0.000043 | 0.000106 | 0.000047 | 0.086530 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.003147` | amplitude MAE `0.003095`
- `h156` | coefficient MAE `0.000067` | amplitude MAE `0.000078`
- `h162` | coefficient MAE `0.000048` | amplitude MAE `0.000050`
- `h240` | coefficient MAE `0.000043` | amplitude MAE `0.000047`
- `h78` | coefficient MAE `0.000038` | amplitude MAE `0.000035`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040838 | 0.069043 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033041 | 0.054786 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `14.338%` | curve MAE `0.008854`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `18.813%` | curve MAE `0.006152`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `8.027%` | curve MAE `0.005378`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
