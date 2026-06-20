# Wave 5.2 Embryonic Skeleton Checks

## Purpose

`run_wave4_embryonic_skeleton_checks.ps1` validates the embryonic Wave 5.2A MMT
diagnostic adapter. It is a dry-run check launcher only. It must not enqueue or
launch training.

## Command

```powershell
.\scripts\campaigns\wave_4\run_wave4_embryonic_skeleton_checks.ps1
```

## What It Runs

- Python compile check for the Wave 5.2A adapter and validator.
- MMT reproduction adapter smoke check.
- Demonstration harmonic summary generation.
- Metadata validation that the skeleton is `implementation-ready` and
  `not campaign-ready`.

## Campaign Boundary

Real Wave 5.2 training remains blocked until `Wave 5.2A` diagnostics prove whether
MMT terms are useful as diagnostics, features, calibrated baselines, or weak
PINN losses. `Wave 4 series` and Wave 5.1 evidence must also inform the loss policy.
