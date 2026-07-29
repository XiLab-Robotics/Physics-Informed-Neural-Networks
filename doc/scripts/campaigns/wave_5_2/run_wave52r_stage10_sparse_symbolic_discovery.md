# Run Wave 5.2R Stage 10 Sparse Symbolic Discovery

## Purpose

This launcher prepares, validates, and executes the bounded Stage 10
condition-harmonic formulation-discovery campaign. It supports local execution
and the repository-owned recoverable remote workflow.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -PreflightOnly
```

## Local Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -Run
```

## Remote Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -Remote -PreflightOnly
```

## Remote Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage10_sparse_symbolic_discovery.ps1 `
  -Remote -Run
```

The remote path synchronizes source, configuration, documentation, the frozen
Stage 5 H04 artifacts, and Stage 9 K01 evidence before execution. It retrieves
the campaign output, per-candidate model artifacts, analysis evidence,
configuration state, and active-campaign state after completion.

## Outputs

- `config/training/sparse_symbolic_formulation_discovery/`
- `output/training_runs/sparse_symbolic_formulation_discovery/`
- `output/training_campaigns/*wave52r_stage10_sparse_symbolic_discovery*`
- `output/analysis/wave_5_2r/stage10_sparse_symbolic_formulation_discovery/`
- `doc/running/active_training_campaign.yaml`

## Interpretation

Passing terms are stable empirical condition-harmonic structure. They are not
declared reducer physics without independent mechanism evidence.
