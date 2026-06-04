# Track 2F-Bis Harmonic-Offset Probe Campaign Launcher

## Overview

This launcher validates and runs the prepared Track 2F-bis harmonic-offset
probe package.

The package contains six runnable queue YAML files:

- three clean `sequential_residual_offset_probe` control entries;
- three `harmonic_residual_offset_probe` entries with sparse `RCIM` harmonic
  shape and causal residual-offset correction.

Each branch is prepared separately for `global`, `Fw`, and `Bw`.

## Local Preflight

Run this from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -PreflightOnly
```

## Local Training

Run this from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1
```

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -EnqueueOnly
```

## Remote Training

The operator-facing remote command is:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote
```

The `-Remote` path uses the repository-owned remote training sync wrapper and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before
launch.
