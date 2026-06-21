# Polished Dataset Stage 1 Smoke Campaign Launcher

## Overview

`scripts/campaigns/cross_wave/run_polished_dataset_stage1_smoke_campaign.ps1`
prepares and runs the operator-controlled compatibility gate for the new
default `polished_dataset`.

The eight-entry smoke matrix covers pointwise neural, tree, harmonic,
periodic temporal, residual harmonic temporal, curve-aware, harmonic-prior,
and latent-state execution classes. Paper-original and paper-retuned
workflows are excluded.

## Preflight

Validate paths, exclusions, dataset schema, and config overrides without
training:

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_stage1_smoke_campaign.ps1 -PreflightOnly
```

Include one-batch datamodule and model validation:

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_stage1_smoke_campaign.ps1 -PreflightOnly -RunOneBatchValidation
```

## Local Training

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_stage1_smoke_campaign.ps1
```

Use `-EnqueueOnly` to verify queue materialization without starting training.

## Remote Training

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_stage1_smoke_campaign.ps1 -Remote
```

Remote mode synchronizes source, configuration, documentation, portal files,
and dependency metadata before execution. It then synchronizes campaign
outputs, per-run artifacts, queue state, registries, and status artifacts back
through the repository-owned remote campaign infrastructure.

The remote workstation must already contain the Git-managed
`data/polished_dataset/` tree.

## Package Inputs

- campaign manifest:
  `config/training/polished_dataset_retraining/campaigns/2026-06-21_polished_dataset_stage1_smoke/campaign.yaml`
- planning report:
  `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-06/2026-06-21/2026-06-21-03-26-07_polished_dataset_default_and_program_retraining.md`
- package validator:
  `scripts/campaigns/cross_wave/validate_polished_dataset_stage1_smoke_package.py`

## Execution Boundary

The launcher runs only Stage 1. After it finishes, report completion to Codex
for normal campaign closeout. Later retraining stages and the final
`TE Curve Verification Pipeline` refresh remain separate operator-approved
steps.

The launcher uses the dedicated queue root
`config/training/queue/polished_dataset_stage1_smoke/` so unrelated pending
campaign entries cannot be consumed.
