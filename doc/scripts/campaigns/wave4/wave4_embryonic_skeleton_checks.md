# Wave 4 Embryonic Skeleton Checks

## Purpose

`run_wave4_embryonic_skeleton_checks.ps1` validates the embryonic Wave 4A MMT
diagnostic adapter. It is a dry-run check launcher only. It must not enqueue or
launch training.

## Command

```powershell
.\scripts\campaigns\wave4\run_wave4_embryonic_skeleton_checks.ps1
```

## What It Runs

- Python compile check for the Wave 4A adapter and validator.
- MMT reproduction adapter smoke check.
- Demonstration harmonic summary generation.
- Metadata validation that the skeleton is `implementation-ready` and
  `not campaign-ready`.

## Campaign Boundary

Real Wave 4 training remains blocked until `Wave 4A` diagnostics prove whether
MMT terms are useful as diagnostics, features, calibrated baselines, or weak
PINN losses. `Track 2H` and Wave 3 evidence must also inform the loss policy.
