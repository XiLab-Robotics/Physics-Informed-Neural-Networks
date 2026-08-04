# Wave 5.2A Paired Dataset Diagnostics

> Supersession note, `2026-08-04`: the dirty-to-clean implication below is an
> intra-machine paired-dataset hypothesis. It is not the canonical future
> Cross-Machine Backbone Adaptation workflow, which fine-tunes a
> source-machine checkpoint on a smaller dataset from another target machine.

## Overview

This diagnostic compares matched `simplified_dataset` and `polished_dataset`
directional curves. It is a dataset-alignment and noise-awareness report,
not a training result and not a `TE Curve Verification Pipeline` promotion.

This run covers the full paired matrix.

The externally running full-wave `polished_dataset` retraining campaign
remains out of scope for this artifact.

## Run Configuration

| Field | Value |
| --- | ---: |
| Run ID | `2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix` |
| Available paired directional records | 1938 |
| Selected paired directional records | 1938 |
| Row stride | 1 |
| Maximum rows per file | 20000 |

## Aggregate Signals

| Metric | Mean polished minus simplified delta |
| --- | ---: |
| Curve mean / offset [deg] | 0.000965366 |
| Peak-to-peak [deg] | -0.000000101 |
| Mean absolute adjacent TE delta [deg] | -0.000000003 |
| Maximum harmonic amplitude delta [deg] | 0.001749405 |

| Metric | Mean absolute delta |
| --- | ---: |
| Curve mean / offset [deg] | 0.003216838 |
| Peak-to-peak [deg] | 0.000000134 |
| Mean absolute adjacent TE delta [deg] | 0.000000003 |

## Classification Thresholds

| Class | Trigger |
| --- | --- |
| `sampling_anomaly` | row-count delta above `10` or theta-range delta above `1.000000000 deg` |
| `shape_changed` | peak-to-peak or standard-deviation delta above `0.000250000 deg` |
| `smoothness_changed` | mean adjacent-delta delta above `0.000001000 deg` or max adjacent-delta delta above `0.000500000 deg` |
| `harmonic_changed` | maximum diagnostic harmonic-amplitude delta above `0.000250000 deg` |
| `offset_shifted` | curve mean / offset delta above `0.000500000 deg` after the previous checks pass |
| `nearly_identical` | none of the above thresholds fires |

## Classification Summary

| Class | Pair Count |
| --- | ---: |
| `nearly_identical` | 65 |
| `offset_shifted` | 901 |
| `shape_changed` | 0 |
| `smoothness_changed` | 1 |
| `harmonic_changed` | 944 |
| `sampling_anomaly` | 27 |

## Direction Aggregates

| Direction | Pairs | Mean Abs Offset Delta [deg] | Mean Abs P2P Delta [deg] | Offset-Shifted | Nearly Identical |
| --- | ---: | ---: | ---: | ---: | ---: |
| backward | 969 | 0.003216917 | 0.000000235 | 458 | 35 |
| forward | 969 | 0.003216760 | 0.000000033 | 443 | 30 |

## Global Aggregate Row

| Pairs | Mean Abs Offset Delta [deg] | Mean Abs P2P Delta [deg] | Mean Abs Smoothness Delta [deg] | Mean Abs Max Harmonic Delta [deg] |
| ---: | ---: | ---: | ---: | ---: |
| 1938 | 0.003216838 | 0.000000134 | 0.000000003 | 0.001749405 |

## Paired Preview

| Direction | Speed | Torque | Temperature | Mean Delta [deg] | P2P Delta [deg] | Smoothness Delta [deg] | Class |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| backward | 100.0 | 0.0 | 25.0 | 0.004892870 | 0.000000000 | -0.000000000 | `sampling_anomaly` |
| forward | 100.0 | 0.0 | 25.0 | 0.004892870 | 0.000000000 | 0.000000000 | `harmonic_changed` |
| backward | 100.0 | 0.0 | 30.0 | 0.009049226 | 0.000000148 | 0.000000002 | `sampling_anomaly` |
| forward | 100.0 | 0.0 | 30.0 | 0.009049230 | -0.000000178 | 0.000000000 | `harmonic_changed` |
| backward | 100.0 | 0.0 | 35.0 | 0.008925404 | -0.000000000 | -0.000000000 | `sampling_anomaly` |
| forward | 100.0 | 0.0 | 35.0 | 0.008925404 | -0.000000000 | 0.000000000 | `harmonic_changed` |
| backward | 100.0 | 100.0 | 25.0 | 0.003109183 | -0.000000000 | 0.000000000 | `harmonic_changed` |
| forward | 100.0 | 100.0 | 25.0 | 0.003109183 | -0.000000000 | 0.000000000 | `harmonic_changed` |
| backward | 100.0 | 100.0 | 30.0 | -0.003153272 | -0.000000000 | 0.000000000 | `harmonic_changed` |
| forward | 100.0 | 100.0 | 30.0 | -0.003153272 | 0.000000000 | 0.000000000 | `harmonic_changed` |
| backward | 100.0 | 100.0 | 35.0 | -0.000793096 | 0.000000000 | -0.000000000 | `harmonic_changed` |
| forward | 100.0 | 100.0 | 35.0 | -0.000793096 | 0.000000000 | -0.000000000 | `harmonic_changed` |

## Interpretation

This pass proves that the two dataset surfaces can be paired by
operating condition and direction across the full available matrix
without touching training campaign state. The reported deltas are
diagnostic signals for choosing the next model-design branch; they are
not model-validation metrics.

The full-matrix evidence keeps peak-to-peak and smoothness deltas near
zero while exposing offset and nonzero-harmonic differences. The next
model-design gate should therefore prioritize offset / mean heads,
centered-shape loss, harmonic-consistency diagnostics, and within-machine
dirty-to-clean supervision before a heavy first PINN. Sampling anomalies
remain isolated and should be handled as masks or exclusions, not as the main
modeling target.

## Machine-Readable Artifacts

- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/pair_metrics.csv`
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/harmonic_metrics.csv`
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/aggregate_summary.csv`
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/summary.json`

## Reproduction

```powershell
python -B scripts/reports/analysis/build_wave52a_paired_dataset_diagnostics.py --max-pairs 0
```
