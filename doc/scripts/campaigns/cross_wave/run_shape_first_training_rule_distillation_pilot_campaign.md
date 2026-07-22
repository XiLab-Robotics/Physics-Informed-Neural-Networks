# Shape-First Training Rule Distillation Pilot Launcher

## Overview

`scripts/campaigns/cross_wave/run_shape_first_training_rule_distillation_pilot_campaign.ps1`
validates or launches the approved two-arm shape-first training-rule
distillation pilot.

The pilot is intentionally scoped to `polished_dataset` with `setpoints` inputs
and the `Fw` surface. It keeps both a time-windowed candidate and a
non-windowed candidate active, then requires a later bounded
`TE Curve Verification Pipeline` screen before any promotion decision.

## Primary Paths

- manifest:
  `config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/campaign.yaml`
- queue configs:
  `config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/queue/001_shape_first_distilled_periodic_gru_sequence_fw.yaml`
  `config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/queue/002_shape_first_distilled_periodic_mlp_harmonic_fw.yaml`
- planning report:
  `doc/reports/campaign_plans/cross_wave/shape_first_training_rule_distillation/2026-07-22-13-14-28_shape_first_training_rule_distillation_pilot_campaign_plan_report.md`
- technical document:
  `doc/technical/2026-07/2026-07-22/2026-07-22-12-54-02_shape_first_training_rule_distillation.md`

## Preflight

Check that the package paths resolve without launching training:

```powershell
.\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1 `
  -PreflightOnly
```

Run one-batch validation without launching a campaign:

```powershell
.\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

## Local Launch

Launch the local pilot campaign:

```powershell
.\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1
```

Queue the local pilot without training:

```powershell
.\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1 `
  -EnqueueOnly
```

## Remote Launch

Launch the pilot through the repository-owned remote campaign workflow:

```powershell
.\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1 `
  -Remote
```

The remote path syncs source, config, docs, site metadata, requirements, and
`AGENTS.md` before launch through
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`.

## Closeout Rule

Normal pilot closeout must inspect campaign artifacts and then evaluate the
trained artifacts with a bounded curve-first screen against both the accepted
windowed GRU and best non-windowed harmonic forward baselines.
