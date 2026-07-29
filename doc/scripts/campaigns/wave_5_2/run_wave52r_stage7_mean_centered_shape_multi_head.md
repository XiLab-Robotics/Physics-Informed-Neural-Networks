# Run Wave 5.2R Stage 7 Mean And Centered-Shape Multi-Head

## Purpose

Prepare, preflight, and execute the Stage 7 matched mean/shape decomposition
campaign on `polished_dataset`, setpoint inputs, and `Fw`.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -PreflightOnly
```

## Local Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -Run
```

## Remote Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -Remote -PreflightOnly
```

## Remote Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage7_mean_centered_shape_multi_head.ps1 `
  -Remote -Run
```

The remote path synchronizes source, configuration, documents, frozen Stage 5
evidence, and the H04 checkpoint before execution. It retrieves campaign
outputs, every immutable run, Stage 7 analysis, queue configuration, and
persistent campaign state afterward.

## Expected Artifacts

- queue YAML under
  `config/training/mean_centered_shape_multi_head/campaigns/`;
- campaign results under `output/training_campaigns/`;
- immutable runs under
  `output/training_runs/mean_centered_shape_multi_head/`;
- preflight and closeout evidence under
  `output/analysis/wave_5_2r/stage7_mean_centered_shape_multi_head/`;
- persistent state in `doc/running/active_training_campaign.yaml`.

## Decision Boundary

The launcher does not run the TE Curve Verification Pipeline. Normal closeout
must first record the campaign result, validated PDF, status synchronization,
and Stage 8 handoff.
