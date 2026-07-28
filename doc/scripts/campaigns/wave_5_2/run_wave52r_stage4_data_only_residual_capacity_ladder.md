# Run Wave 5.2R Stage 4 Data-Only Residual Capacity Ladder

## Purpose

This launcher validates and executes the eighteen-run Stage 4 screening
campaign on `polished_dataset`, setpoint inputs, and forward curves only.

The package compares:

- six parameter-matched direct R1 controls;
- compact and deep R2-R5 hybrid arms;
- weak and moderate R2 residual-energy penalties;
- partial and full R5 anchor-unfreeze ablations.

It does not run the heavy TE Curve Verification Pipeline.

## Prerequisites

- Conda environment `pinns_env`;
- frozen common split manifest;
- Stage 4 causal setpoint PF-A anchor;
- all eighteen immutable queue YAML files;
- approved technical document and campaign plan.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage4_data_only_residual_capacity_ladder.ps1 -PreflightOnly
```

## Real-Dataset One-Batch Validation

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage4_data_only_residual_capacity_ladder.ps1 -PreflightOnly -RunOneBatchValidation
```

This validates the full training stack separately for all eighteen queue
entries without launching the campaign.

## Local Campaign

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage4_data_only_residual_capacity_ladder.ps1
```

## Remote-Compatible Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage4_data_only_residual_capacity_ladder.ps1 -Remote -PreflightOnly
```

This exercises the same required-path and deterministic validation path while
selecting the remote-compatible launcher branch. It does not contact the
remote workstation.

## Remote Campaign

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage4_data_only_residual_capacity_ladder.ps1 -Remote
```

The remote branch delegates synchronization and execution to
`run_remote_training_campaign.ps1`. It sends source, configuration,
documentation, the causal anchor, calibration evidence, and split manifest,
then synchronizes campaign outputs, per-run artifacts, queue state,
registries, and status evidence after completion.

## Enqueue-Only Verification

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage4_data_only_residual_capacity_ladder.ps1 -EnqueueOnly
```

Use this local-only mode to verify queue materialization without running model
training.

## Expected Outputs

- immutable run instances under
  `output/training_runs/data_only_residual_capacity/`;
- campaign package under `output/training_campaigns/`;
- queue state under
  `config/training/queue/data_only_residual_capacity/`;
- campaign leaderboard, best-run YAML, and best-run Markdown;
- post-campaign Stage 4 full-curve evaluation and closeout report.

## Stop Conditions

The launcher stops on:

- missing campaign evidence;
- deterministic validator failure;
- any one-batch failure;
- any queue-run failure;
- remote synchronization or execution failure.
