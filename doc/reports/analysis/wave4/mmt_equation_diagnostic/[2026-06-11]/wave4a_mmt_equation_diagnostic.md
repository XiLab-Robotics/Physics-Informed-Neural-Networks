# Wave 4A MMT Equation Diagnostic

## Overview

This diagnostic runs the repository-owned `MMT_TEModeling` equation-chain demonstration through the `Wave4MMTDiagnosticAdapter` and summarizes its mean, peak-to-peak value, and harmonic content.

This is a diagnostic-only artifact. It is not a PINN loss, not a calibrated
analytical baseline, and not a training campaign result.

## Summary

| Field | Value |
| --- | ---: |
| Run ID | `2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic` |
| Sample Count | 720 |
| RTE Mean [arcsec] | -565.628931 |
| RTE Peak To Peak [arcsec] | 525.201502 |
| Campaign Readiness | `not_campaign_ready` |

## Dominant Demonstration Harmonics

| Harmonic | Amplitude [arcsec] | Track 2 Suspicious Group |
| ---: | ---: | --- |
| 18 | 152.451356 | no |
| 342 | 34.358914 | no |
| 78 | 25.198140 | no |
| 114 | 23.733271 | no |
| 228 | 20.154402 | no |
| 306 | 18.248470 | no |
| 42 | 17.787605 | no |
| 36 | 17.386865 | no |
| 264 | 14.068604 | no |
| 150 | 12.770179 | no |
| 72 | 11.644816 | no |
| 192 | 11.517365 | no |

## Track 2 Suspicious Harmonic Probe

| Harmonic | Amplitude [arcsec] | Top Demonstration Harmonic |
| ---: | ---: | --- |
| 0 | 565.628931 | no |
| 1 | 0.000000 | no |
| 156 | 5.414472 | no |
| 162 | 4.236382 | no |
| 240 | 2.188343 | no |

## Interpretation

The MMT equation chain is now callable as a diagnostic and can produce auditable harmonic signatures. This is useful for deciding whether MMT terms should become diagnostic-only, feature-generator, calibrated baseline, or weak-loss material.
The current demonstration is not dataset-calibrated. Any relationship between the displayed harmonic amplitudes and Track 2 failure modes is therefore a hypothesis, not evidence of causality.
The next Wave 4A requirement remains the parameter inventory: which MMT inputs are known from the rig, fixed by reducer geometry, calibrated on training conditions only, or unavailable.

## Machine-Readable Artifacts

- `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/wave4a_mmt_demo_curve.csv`
- `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/wave4a_mmt_harmonic_summary.csv`
- `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/wave4a_mmt_equation_diagnostic_summary.yaml`

## Reproduction

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py
```
