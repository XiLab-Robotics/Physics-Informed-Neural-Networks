# Run Wave 5.2R Stage 13 Synthetic Weak-Form Oracle Lane

## Purpose

This launcher validates and executes the bounded Stage 13 analytical oracle
campaign for `polished_dataset`, setpoint inputs, and `Fw`. The campaign
certifies implementation and synthetic detection power only; it cannot promote
a real-data model.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -PreflightOnly
```

## Local Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -Run
```

## Remote Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -Remote -PreflightOnly
```

## Remote Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -Remote -Run
```

The remote path synchronizes scripts, configuration, documentation, frozen
Stage 0 and Stage 5 analytical evidence, then returns the campaign outputs,
validation checks, analysis artifacts, queue state, and active-campaign state.

## Outputs

- `output/training_campaigns/<run_instance_id>/`
- `output/validation_checks/synthetic_weak_form_oracle_lane/<run_instance_id>/`
- `output/analysis/wave_5_2r/stage13_synthetic_weak_form_oracle_lane/`
- `doc/running/active_training_campaign.yaml`
