# Wave 4 series Dispersion-Aware Modeling Campaign Launcher

## Overview

This launcher validates and runs the prepared `Wave 4.1`
dispersion-aware modeling package.

The package contains `9` runnable queue YAML files: three robust pointwise
losses across `global`, `Fw`, and `Bw` surfaces. The already verified
`Wave 3.3` pointwise-control candidates are the MSE baseline for this robust
probe.

Runtime inputs remain causal point or short-history sequence inputs. No future
curve information or target-curve statistics are supplied to the model.

## Local Preflight

Run this from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1 -PreflightOnly
```

## Local Training

Run this from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1
```

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1 -EnqueueOnly
```

## Remote Training

The operator-facing remote command is:

```powershell
.\scripts\campaigns\track_2\run_track2h_dispersion_aware_modeling_campaign.ps1 -Remote
```

The `-Remote` path uses the repository-owned remote training launcher and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before
launch.

## Expected Queue Matrix

| Loss Profile | Global | Fw | Bw |
| --- | --- | --- | --- |
| `mae_robust` | `01_mae_robust_global.yaml` | `02_mae_robust_fw.yaml` | `03_mae_robust_bw.yaml` |
| `smooth_l1_robust` | `04_smooth_l1_robust_global.yaml` | `05_smooth_l1_robust_fw.yaml` | `06_smooth_l1_robust_bw.yaml` |
| `log_cosh_robust` | `07_log_cosh_robust_global.yaml` | `08_log_cosh_robust_fw.yaml` | `09_log_cosh_robust_bw.yaml` |

## Closeout Boundary

After training finishes, perform normal campaign closeout first: Markdown
result report, PDF export and visual QA, registry synchronization, active
campaign cleanup, and master-summary synchronization. The official `TE Curve Verification Pipeline`
verification refresh remains a separate operator-approved step after closeout.
