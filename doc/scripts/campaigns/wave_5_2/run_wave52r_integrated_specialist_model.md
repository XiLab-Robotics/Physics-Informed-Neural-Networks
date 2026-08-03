# Run Wave 5.2R Integrated Specialist Model

## Purpose

This launcher validates and, only after campaign-plan approval, executes the
empirical Wave 5.2R integrated-specialist ablation campaign. It preserves K01
as the frozen causal baseline, routes H08 only as a centered forward residual,
and tests H04, Stage 12 objective hypotheses, and Stage 10 condition-library
controls independently before any conditional combination.

The package contains three replay entries, eighteen mandatory single-branch
runs, and three conditional `A08` runs. It performs no training when invoked
without `-Run` or with `-PreflightOnly`.

## Current Campaign State

The technical document and campaign plan were approved. The remote campaign
completed `24 / 24` entries on `2026-08-03`, and normal closeout is complete.
The commands below remain the reproducibility and preflight entry points; a
new run would be a separate explicit operator action.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -PreflightOnly
```

## Remote Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -Remote -PreflightOnly
```

## Local Run After Approval

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -Run
```

## Remote Run After Approval

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -Remote -Run
```

The remote launcher synchronizes the required source, configuration,
documentation, split evidence, local preflight evidence, and frozen
K01/H04/H08 checkpoints. The remote preflight regenerates its own validation
summary, so that self-generated path is not treated as a prerequisite. The
generated Sphinx tree and unrelated historical documentation are deliberately
excluded because they are not training dependencies and would make the
transport archive unnecessarily large. Every protected campaign document is
still synchronized explicitly. The remote machine must already contain
`data/polished_dataset`. After completion
the launcher returns validation evidence, the campaign bundle, every
integrated-specialist run directory, artifact inventory, and active-campaign
state.

## Outputs

- `output/validation_checks/wave52r_integrated_specialist_model/`
- `output/training_runs/integrated_specialist_models/<run_instance_id>/`
- `output/training_campaigns/<campaign_run_instance_id>/`
- `doc/running/active_training_campaign.yaml`

## Interpretation Boundary

Campaign rank is provisional and cannot promote a model. Normal closeout and
the optional, separately approved TE Curve Verification Pipeline must precede
any offline-leader decision. Export and TwinCAT runtime qualification remain
additional gates.
