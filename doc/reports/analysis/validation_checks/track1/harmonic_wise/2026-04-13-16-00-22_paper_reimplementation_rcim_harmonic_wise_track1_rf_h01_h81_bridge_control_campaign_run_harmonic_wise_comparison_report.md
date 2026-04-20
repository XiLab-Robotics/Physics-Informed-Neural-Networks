# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_random_forest_track1_h01_h81_bridge_control`;
- run name: `track1_rf_h01_h81_bridge_control`;
- output run name: `track1_rf_h01_h81_bridge_control_campaign_run`;
- run instance id: `2026-04-13-15-59-15__track1_rf_h01_h81_bridge_control_campaign_run`;
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
| Validation | 0.003126 | 0.003356 | 11.338 | 3.588 | 0.000195 |
| Test | 0.003319 | 0.003504 | 11.236 | 2.749 | 0.000198 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `11.236%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.003151 | 0.003724 | 0.003085 | 0.000000 |
| `h1` | 0.000025 | 0.000031 | 0.000024 | 0.001585 |
| `h3` | 0.000022 | 0.000027 | 0.000021 | 0.025623 |
| `h39` | 0.000024 | 0.000030 | 0.000026 | 0.031268 |
| `h40` | 0.000029 | 0.000042 | 0.000028 | 0.069848 |
| `h78` | 0.000038 | 0.000049 | 0.000035 | 0.060173 |
| `h81` | 0.000013 | 0.000017 | 0.000013 | 0.076884 |
| `h156` | 0.000065 | 0.000239 | 0.000077 | 0.094774 |
| `h162` | 0.000048 | 0.000133 | 0.000049 | 0.085179 |
| `h240` | 0.000043 | 0.000104 | 0.000047 | 0.085816 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.003151` | amplitude MAE `0.003085`
- `h156` | coefficient MAE `0.000065` | amplitude MAE `0.000077`
- `h162` | coefficient MAE `0.000048` | amplitude MAE `0.000049`
- `h240` | coefficient MAE `0.000043` | amplitude MAE `0.000047`
- `h78` | coefficient MAE `0.000038` | amplitude MAE `0.000035`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040790 | 0.068948 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.033016 | 0.054535 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `13.944%` | curve MAE `0.008610`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `19.022%` | curve MAE `0.006220`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `7.953%` | curve MAE `0.005329`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
