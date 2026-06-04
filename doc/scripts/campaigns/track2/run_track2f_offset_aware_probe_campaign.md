# Track 2F Offset-Aware Probe Campaign Launcher

## Overview

This launcher validates the prepared Track 2F offset-aware probe package.

The package contains nine descriptor entries across `global`, `Fw`, and `Bw`
surfaces and three runnable sequential residual-offset queue YAML files:

- three `posthoc_direction_torque_offset_baseline` validation entries;
- three `sequential_residual_offset_probe` training entries;
- three `multi_head_shape_offset_probe` learned-probe placeholders.

The multi-head entries remain guarded because that model type is intentionally
deferred to a later technical gate.

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

## Local Sequential Probe Training

Run this from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1
```

This validates the package, enqueues the three sequential residual-offset
training YAML files, and starts the local campaign runner.

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1 -EnqueueOnly
```

## Remote Sequential Probe Training

The operator-facing remote command is recorded for continuity:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1 -Remote
```

This uses the canonical remote training sync wrapper for the three runnable
sequential residual-offset queue YAML files. It does not launch the multi-head
placeholder entries.
