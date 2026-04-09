# Harmonic-Wise Comparison Pipeline Report

## Overview

This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.

- model family: `paper_reimplementation_rcim_harmonic_wise`;
- model type: `harmonic_wise_hist_gradient_boosting`;
- run name: `te_harmonic_wise_full_rcim_baseline_reference`;
- output run name: `te_harmonic_wise_full_rcim_baseline_reference_campaign_run`;
- run instance id: `2026-04-09-20-41-59__te_harmonic_wise_full_rcim_baseline_reference_campaign_run`;
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
| Validation | 0.002538 | 0.002781 | 9.474 | 3.588 | 0.000167 |
| Test | 0.002726 | 0.002925 | 9.403 | 2.749 | 0.000169 |

## Paper Alignment

- Paper offline threshold for `Target A`: `4.7%` mean percentage error.
- Current repository test result: `9.403%` mean percentage error.
- Current verdict: `not_yet_met`.
- Oracle truncation-only test error with the selected harmonics: `2.749%`.

## Per-Harmonic Error Diagnostics

| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |
| --- | ---: | ---: | ---: | ---: |
| `h0` | 0.002537 | 0.003093 | 0.002508 | 0.000000 |
| `h1` | 0.000027 | 0.000032 | 0.000025 | 0.001707 |
| `h3` | 0.000019 | 0.000024 | 0.000018 | 0.022277 |
| `h39` | 0.000022 | 0.000030 | 0.000024 | 0.031252 |
| `h40` | 0.000031 | 0.000043 | 0.000029 | 0.073988 |
| `h78` | 0.000031 | 0.000041 | 0.000025 | 0.052735 |
| `h81` | 0.000014 | 0.000017 | 0.000013 | 0.078577 |
| `h156` | 0.000084 | 0.000253 | 0.000090 | 0.118946 |
| `h162` | 0.000057 | 0.000144 | 0.000058 | 0.107040 |
| `h240` | 0.000047 | 0.000097 | 0.000051 | 0.091247 |

Top coefficient-error contributors on the test split:

- `h0` | coefficient MAE `0.002537` | amplitude MAE `0.002508`
- `h156` | coefficient MAE `0.000084` | amplitude MAE `0.000090`
- `h162` | coefficient MAE `0.000057` | amplitude MAE `0.000058`
- `h240` | coefficient MAE `0.000047` | amplitude MAE `0.000051`
- `h40` | coefficient MAE `0.000031` | amplitude MAE `0.000029`

## Offline Motion-Profile Playback

These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.

| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `robot` | 180 | 0.040640 | 0.068958 | 288.1 | 598.2 | 31.6 |
| `cycloidal` | 180 | 0.032848 | 0.053702 | 500.0 | 351.5 | 26.7 |

## Test Preview Samples

- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | forward | mean percentage error `7.841%` | curve MAE `0.004842`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1200.0Nm25.0deg.csv` | backward | mean percentage error `8.456%` | curve MAE `0.002765`
- `data/datasets/Test_25degree/1000rpm/1000.0rpm1300.0Nm25.0deg.csv` | forward | mean percentage error `3.440%` | curve MAE `0.002305`

## Interpretation

The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.
