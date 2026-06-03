# Track 2F Offset-Aware Probe Campaign Launcher

## Overview

This launcher validates the prepared Track 2F offset-aware probe package.

The package contains nine descriptor entries across `global`, `Fw`, and `Bw`
surfaces:

- three `posthoc_direction_torque_offset_baseline` validation entries;
- three `sequential_residual_offset_probe` learned-probe placeholders;
- three `multi_head_shape_offset_probe` learned-probe placeholders.

The learned probe entries are intentionally guarded because the current
training runner does not yet implement their model types. The launcher can
therefore validate the prepared package and write baseline-status artifacts,
but it must not be treated as approval to start learned Track 2F training.

## Local Preflight

Run this from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1 -PreflightOnly
```

This validates descriptor count, surface/intervention coverage, Track 2E
reference availability, and prepared campaign state.

By default, the launcher runs validation through `conda run -n pinns_env
python` so the repository YAML dependencies are available. Use
`-PythonExecutable` only when pointing at another Python environment that has
the same dependencies installed.

## Baseline-Status Validation

Run this from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1
```

This writes a lightweight status bundle under:

`output/validation_checks/track2f_offset_aware_probe/2026-06-03_track2f_offset_aware_probe_prelaunch`

The status bundle records which entries are runnable as non-training post-hoc
baselines and which entries are blocked pending model-type implementation.

## Remote Guard

The operator-facing remote command is recorded for continuity:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1 -Remote
```

At this stage the command exits with a guard message instead of using the
remote training sync wrapper. The guard is deliberate: launching through the
standard remote training path would hand unsupported Track 2F model types to
`scripts/training/run_training_campaign.py`.

The remote path should be enabled only after a later approved implementation
adds the sequential residual-offset and multi-head shape/offset model types.
