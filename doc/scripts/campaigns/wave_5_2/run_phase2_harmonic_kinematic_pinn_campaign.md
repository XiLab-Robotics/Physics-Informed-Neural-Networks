# Phase 2 Harmonic-Kinematic PINN Campaign Launcher

## Overview

`scripts/campaigns/wave_5_2/run_phase2_harmonic_kinematic_pinn_campaign.ps1`
validates or launches the approved eight-run Wave 5.2 Phase 2 campaign.

The campaign tests four bounded roles on separate `Fw` and `Bw` surfaces:

- a parameter-matched explicit Fourier control;
- an implicit harmonic-head PINN with oscillator residuals;
- the PINN with periodic value and slope closure;
- the periodic PINN with a frozen Phase 1 Bauer surface anchor.

All eight canonical restart arms use point stride `8`. The Phase 0 minimum
audited curve of `10,799` rows still retains at least `1,350` samples,
preserving more than `2.8` times the `480`-sample Nyquist minimum for output
order `240`.

The runtime-bounded canonical package uses `4` curves per batch, at most
`4,096` points distributed across each full curve, `64` physics collocation
points per batch, and at most `24` epochs with patience `5`. This retains at
least `10,800` physics collocation evaluations per epoch while avoiding the
`144`-second epoch measured by the superseded diagnostic configuration.

## Primary Paths

- manifest:
  `config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/campaign.yaml`
- queue:
  `config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/`
- planning report:
  `doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md`
- analytical anchor:
  `output/analysis/polynomial_fourier_benchmark/phase1_coefficient_models.yaml`

## Preflight

Run deterministic primitive checks without training:

```powershell
.\scripts\campaigns\wave_5_2\run_phase2_harmonic_kinematic_pinn_campaign.ps1 `
  -PreflightOnly
```

Validate one real batch for every queue entry:

```powershell
.\scripts\campaigns\wave_5_2\run_phase2_harmonic_kinematic_pinn_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

## Local Launch

```powershell
.\scripts\campaigns\wave_5_2\run_phase2_harmonic_kinematic_pinn_campaign.ps1
```

An enqueue-only local infrastructure check is also available:

```powershell
.\scripts\campaigns\wave_5_2\run_phase2_harmonic_kinematic_pinn_campaign.ps1 `
  -EnqueueOnly
```

## Remote Launch

```powershell
.\scripts\campaigns\wave_5_2\run_phase2_harmonic_kinematic_pinn_campaign.ps1 `
  -Remote
```

The remote path synchronizes source, configuration, documentation, portal
metadata, and the frozen Phase 1 coefficient surface before execution. It then
synchronizes campaign outputs, immutable per-run artifacts, queue end state,
registries, and status artifacts back to the local repository.

## Closeout Rule

Normal closeout produces the campaign results report and validated PDF, updates
the canonical status surfaces, and closes the active campaign. The heavy
`TE Curve Verification Pipeline` remains a separate optional post-closeout
step and is not launched automatically.
