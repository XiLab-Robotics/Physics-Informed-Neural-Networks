# Wave 2C Residual Harmonic Temporal Hybrid Campaign Launcher

## Overview

This launcher runs the prepared `Wave 2C` residual harmonic temporal hybrid
campaign after explicit operator approval. The package compares residual
harmonic `GRU` and residual harmonic `LSTM` sequence models across the required
`global`, `Fw`, and `Bw` direction surfaces and across sparse plus dense
harmonic-basis tiers.

The launcher does not run `Track 2` verification by itself. Promotion remains a
post-campaign closeout step that must refresh the official `Track 2` matrix and
visual reports.

## Campaign Package

Prepared campaign root:

- `config/training/wave2c_residual_harmonic_temporal_hybrid/campaigns/2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign`

Prepared queue count:

- `18` YAML files

Families:

- `residual_harmonic_gru_sequence`
- `residual_harmonic_lstm_sequence`

Harmonic basis tiers:

- `sparse_rcim`: `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]`
- `dense_240`: explicit inclusive list `0..240`
- `dense_360`: explicit inclusive list `0..360`

## Planning Report

This launcher is tied to:

- `doc/reports/campaign_plans/wave_2/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md`

## Practical Use

Run the full prepared campaign from the repository root:

```powershell
.\scripts\campaigns\wave_2\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1
```

Run the same prepared campaign on the configured LAN remote workstation:

```powershell
.\scripts\campaigns\wave_2\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 -Remote
```

Optional Python executable override:

```powershell
.\scripts\campaigns\wave_2\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 -PythonExecutable python
```

Optional remote overrides:

```powershell
.\scripts\campaigns\wave_2\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 `
  -Remote `
  -RemoteHostAlias xilab-remote `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName pinns_env
```

The `-Remote` path delegates to
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`. It syncs
`scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before launch,
then syncs the manifest-declared campaign outputs, per-run training artifacts,
queue end state, and affected registries back into the local repository.

When `PINNS_REMOTE_TRAINING_REPO_PATH` is not set, the launcher defaults to the
validated LAN clone path:

- `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`

## Expected Outputs

The shared campaign runner writes campaign artifacts under:

- `output/training_campaigns/wave2/residual_harmonic_temporal_hybrid/wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27`

Per-run training artifacts are written under each configured
`output/training_runs/<model_family>/` root with immutable run-instance
directories.

## Operator Notes

The launcher clears stale `pending` and `running` queue copies for the prepared
file names before starting. It does not remove completed or failed historical
queue records.

Training must not be launched until the prepared campaign package is explicitly
approved.
