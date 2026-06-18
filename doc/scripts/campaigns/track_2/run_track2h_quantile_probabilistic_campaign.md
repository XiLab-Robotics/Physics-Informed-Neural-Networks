# Track 2H Quantile Probabilistic Campaign Launcher

## Overview

`scripts/campaigns/track_2/run_track2h_quantile_probabilistic_campaign.ps1`
launches the approved second `Track 2H` dispersion-aware package. The package
contains six queue entries:

- `quantile_p10_p50_p90` for `global`, `Fw`, and `Bw`;
- `gaussian_nll` for `global`, `Fw`, and `Bw`.

The deterministic curve used for standard TE metrics is `p50` for quantile
runs and `mu` for Gaussian runs.

## Commands

Preflight validation only:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -PreflightOnly
```

Preflight plus one-batch loss/output validation:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

Local enqueue-only verification:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -EnqueueOnly
```

Local campaign launch:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1
```

Remote campaign launch:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -Remote
```

## Notes

The launcher validates the prepared package before any local or remote launch.
It does not run official `Track 2` verification. That refresh remains a
separate operator-launched step after campaign closeout.
