# Phase 3 C1-Fw Stability Repeat Launcher

## Purpose

This launcher executes the two initialization-stability repeats authorized by
the Phase 3 campaign plan after C1-Fw passed the initial bounded curve-first
gate. The two runs preserve the original architecture, data split, loss
weights, and runtime profile while changing only the reproducible training
seed.

## Campaign Scope

- formulation: C1 linear-compliance soft residual;
- surface: Fw;
- seeds: `314159` and `271828`;
- dataset: `polished_dataset`;
- input mode: `setpoints`;
- held-out directional split: 97 curves;
- promotion rule: multi-index curve-first evidence, never scalar MAE alone.

The launcher first validates the shared compliance-PINN implementation. The
optional one-batch mode also validates both seeded queue entries before a full
run.

## Local Commands

Run launcher-only preflight:

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_c1_fw_stability_repeat_campaign.ps1 -PreflightOnly
```

Run preflight plus one-batch validation:

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_c1_fw_stability_repeat_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

Run the local campaign:

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_c1_fw_stability_repeat_campaign.ps1
```

## Remote Command

```powershell
.\scripts\campaigns\wave_5_2\run_phase3_c1_fw_stability_repeat_campaign.ps1 -Remote
```

The remote path reuses the repository-owned remote campaign infrastructure and
syncs the source, configurations, documentation, audit evidence, split
manifest, campaign outputs, per-run artifacts, queue state, registries, and
status artifacts.

## Expected Outputs

- immutable runs under
  `output/training_runs/quasi_static_compliance_pinn/`;
- campaign package under `output/training_campaigns/`;
- queue state under
  `config/training/queue/quasi_static_compliance_pinn/phase3_c1_fw_stability_repeat_2026_07_26/`;
- distinct family registries for both seeded repeats.
