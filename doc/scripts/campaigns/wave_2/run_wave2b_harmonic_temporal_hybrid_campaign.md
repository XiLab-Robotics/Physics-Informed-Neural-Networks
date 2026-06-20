# Wave 2.2 Harmonic Temporal Hybrid Campaign Launcher

## Overview

This launcher runs the prepared `Wave 2.2` harmonic-temporal hybrid campaign
after explicit operator approval. The package compares periodic temporal
convolution, periodic `GRU`, and periodic `LSTM` sequence models across the
required `global`, `Fw`, and `Bw` direction surfaces.

The launcher does not run `TE Curve Verification Pipeline` verification by itself. Promotion remains a
post-campaign closeout step that must refresh the official `TE Curve Verification Pipeline` matrix and
visual reports.

## Campaign Package

Prepared campaign root:

- `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign`

Prepared queue count:

- `9` YAML files

Families:

- `periodic_temporal_convolution`
- `periodic_gru_sequence`
- `periodic_lstm_sequence`

Harmonic basis:

- `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]`

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave_2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md`

## Practical Use

Run the full prepared campaign from the repository root:

```powershell
.\scripts\campaigns\wave_2\run_wave2b_harmonic_temporal_hybrid_campaign.ps1
```

Optional Python executable override:

```powershell
.\scripts\campaigns\wave_2\run_wave2b_harmonic_temporal_hybrid_campaign.ps1 -PythonExecutable python
```

## Expected Outputs

The shared campaign runner writes campaign artifacts under:

- `output/training_campaigns/wave2/harmonic_temporal_hybrid/wave2b_harmonic_temporal_hybrid_campaign_2026_05_25`

Per-run training artifacts are written under each configured
`output/training_runs/<model_family>/` root with immutable run-instance
directories.

## Operator Notes

The launcher clears stale `pending` and `running` queue copies for the prepared
file names before starting. It does not remove completed or failed historical
queue records.

Training must not be launched until the prepared campaign package is explicitly
approved.
