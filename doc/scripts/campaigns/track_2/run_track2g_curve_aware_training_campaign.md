# Wave 3.3 Curve-Aware Training Campaign Launcher

## Overview

This launcher validates and runs the prepared Wave 3.3 curve-aware training
package.

The package contains 12 runnable queue YAML files: four loss profiles across
`global`, `Fw`, and `Bw` surfaces. Runtime inputs remain causal point or
short-history sequence inputs. Curve grouping is used only for training loss
aggregation and offline verification.

## Local Preflight

Run this from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1 -PreflightOnly
```

## Local Training

Run this from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1
```

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1 -EnqueueOnly
```

## Remote Training

The operator-facing remote command is:

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1 -Remote
```

The `-Remote` path uses the repository-owned remote training sync wrapper and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before
launch.
