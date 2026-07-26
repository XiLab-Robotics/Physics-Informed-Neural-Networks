# Phase 3 Quasi-Static Compliance PINN Campaign Launcher

## Overview

`scripts/campaigns/wave_5_2/run_phase3_quasi_static_compliance_pinn_campaign.ps1`
validates or launches the approved twelve-run Wave 5.2 Phase 3 campaign.

The campaign compares:

- learned periodic-plus-mean controls on `Fw`, `Bw`, and `global`;
- linear, temperature-conditioned, and nonlinear differential-residual PINNs
  on separate `Fw` and `Bw` surfaces;
- hard direction-specific elastic equations on `Fw` and `Bw`;
- one hard shared-stiffness equation on the paired `global` surface.

Every run uses the exact Phase 0 and Phase 1 common split. Directional arms
contain `675 / 194 / 97` train, validation, and test curves. Global arms
contain the paired `1,350 / 388 / 194` curves without cross-split leakage.

## Primary Paths

- manifest:
  `config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/campaign.yaml`
- queue:
  `config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/`
- planning report:
  `doc/reports/campaign_plans/model_development_waves/wave_5_2/quasi_static_compliance_pinn/2026-07-26-17-16-41_phase3_quasi_static_compliance_pinn_campaign_plan_report.md`
- identifiability audit:
  `output/analysis/pinn_program_compliance/phase3_compliance_audit.yaml`

## Preflight

Run the persisted audit and deterministic model checks without training:

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_quasi_static_compliance_pinn_campaign.ps1 `
  -PreflightOnly
```

Validate one real batch for every queue entry:

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_quasi_static_compliance_pinn_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

## Local Launch

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_quasi_static_compliance_pinn_campaign.ps1
```

An enqueue-only local infrastructure check is also available:

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_quasi_static_compliance_pinn_campaign.ps1 `
  -EnqueueOnly
```

## Remote Launch

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_quasi_static_compliance_pinn_campaign.ps1 `
  -Remote
```

The remote path synchronizes source, configuration, technical and planning
documentation, the Phase 3 audit, and the common split before execution. It
then synchronizes campaign outputs, immutable per-run artifacts, queue end
state, registries, and status artifacts back to the local repository.

## Closeout Rule

Normal closeout produces the campaign results report and validated PDF, updates
the canonical status surfaces, and closes the active campaign. The heavy
`TE Curve Verification Pipeline` remains a separate optional post-closeout
step and is not launched automatically.
