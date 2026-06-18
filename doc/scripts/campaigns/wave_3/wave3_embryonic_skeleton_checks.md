# Wave 3 Embryonic Skeleton Checks

## Purpose

`run_wave3_embryonic_skeleton_checks.ps1` validates the embryonic Wave 3
harmonic-prior residual implementation. It is a dry-run check launcher only.
It must not enqueue or launch training.

## Command

```powershell
.\scripts\campaigns\wave_3\run_wave3_embryonic_skeleton_checks.ps1
```

## What It Runs

- Python compile check for the Wave 3 model and validator.
- Model factory construction for `wave3_harmonic_prior_residual`.
- Point and sequence forward smoke checks.
- Metadata validation that the skeleton is `implementation-ready` and
  `not campaign-ready`.

## Campaign Boundary

Real Wave 3 training remains blocked until `Track 2H` results choose the loss
policy and a later campaign plan approves queue size, surfaces, launch mode,
and active-campaign state updates.
