# `run_wave52r_stage12_advanced_constraint_optimization.ps1`

## Purpose

Prepare, validate, or execute the Wave 5.2R Stage 12 advanced constraint
optimization campaign on `polished_dataset`, setpoints, and `Fw`.

## Local Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -Run
```

Recover failed local entries after correcting an implementation fault:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -ResumeFailed
```

The recovery command preserves completed run artifacts, trains only missing
candidate IDs, rebuilds the complete leaderboard and gates, and records initial
versus residual failures separately.

## Remote Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -Remote -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -Remote -Run
```

The remote path delegates to the repository-owned remote campaign
infrastructure, synchronizes source, configuration, and documentation before
launch, then returns campaign outputs, run artifacts, queue state, registries,
and status files.

## Execution Boundary

`-PreflightOnly` must not train. `-Run` is valid only while the technical
document and campaign plan remain approved and the frozen Stage 0, H04, and K01
provenance checks pass.
