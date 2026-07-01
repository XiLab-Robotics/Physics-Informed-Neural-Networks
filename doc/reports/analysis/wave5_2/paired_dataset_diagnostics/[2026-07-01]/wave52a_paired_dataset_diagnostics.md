# Wave 5.2A Paired Dataset Diagnostics

## Overview

This diagnostic compares matched `simplified_dataset` and `polished_dataset`
directional curves. It is a dataset-alignment and noise-awareness report,
not a training result and not a `TE Curve Verification Pipeline` promotion.

The externally running full-wave `polished_dataset` retraining campaign
remains out of scope for this artifact.

## Run Configuration

| Field | Value |
| --- | ---: |
| Run ID | `2026-07-01-14-10-57__wave52a_paired_dataset_diagnostics` |
| Available paired directional records | 1938 |
| Selected paired directional records | 24 |
| Row stride | 1 |
| Maximum rows per file | 20000 |

## Aggregate Signals

| Metric | Mean polished minus simplified delta |
| --- | ---: |
| Curve mean / offset [deg] | 0.000199185 |
| Peak-to-peak [deg] | 0.000000000 |
| Mean absolute adjacent TE delta [deg] | 0.000000000 |

## Paired Preview

| Direction | Speed | Torque | Temperature | Mean Delta [deg] | P2P Delta [deg] | Smoothness Delta [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| backward | 100.0 | 0.0 | 25.0 | 0.004892870 | 0.000000000 | -0.000000000 |
| backward | 100.0 | 1400.0 | 25.0 | -0.000174930 | 0.000000000 | -0.000000000 |
| backward | 200.0 | 900.0 | 25.0 | 0.003032321 | 0.000000000 | -0.000000000 |
| forward | 300.0 | 400.0 | 25.0 | -0.003640093 | -0.000000000 | 0.000000000 |
| forward | 300.0 | 1800.0 | 25.0 | -0.002686232 | 0.000000000 | -0.000000000 |
| forward | 400.0 | 1300.0 | 25.0 | -0.003068028 | -0.000000000 | -0.000000000 |
| forward | 500.0 | 800.0 | 25.0 | -0.003131144 | -0.000000000 | 0.000000000 |
| backward | 600.0 | 300.0 | 30.0 | -0.001768498 | -0.000000000 | -0.000000000 |
| backward | 600.0 | 1700.0 | 30.0 | -0.001867991 | -0.000000000 | 0.000000000 |
| backward | 700.0 | 1200.0 | 30.0 | -0.002166806 | 0.000000000 | 0.000000000 |
| backward | 800.0 | 700.0 | 30.0 | 0.005113715 | 0.000000000 | 0.000000000 |
| backward | 900.0 | 200.0 | 30.0 | 0.005553933 | -0.000000000 | -0.000000000 |

## Interpretation

This first pass proves that the two dataset surfaces can be paired by
operating condition and direction and compared without touching training
campaign state. The reported deltas should be interpreted as diagnostic
signals only because the default run is bounded for interactive use.

The next decision is whether to widen this diagnostic to the full paired
matrix before translating polishing ideas into train-time losses, masks,
auxiliary heads, dirty-to-clean targets, or reduced-point experiments.

## Machine-Readable Artifacts

- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-10-57__wave52a_paired_dataset_diagnostics/pair_metrics.csv`
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-10-57__wave52a_paired_dataset_diagnostics/harmonic_metrics.csv`
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-10-57__wave52a_paired_dataset_diagnostics/summary.json`

## Reproduction

```powershell
python -B scripts/reports/analysis/build_wave52a_paired_dataset_diagnostics.py
```
