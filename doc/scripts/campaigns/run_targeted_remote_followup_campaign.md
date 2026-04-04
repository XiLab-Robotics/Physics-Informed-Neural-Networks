# Targeted Remote Follow-Up Campaign Launcher

## Overview

This note documents the next selective LAN-remote campaign prepared after the
first validated remote execution path.

The campaign deliberately focuses on the three branches that still have
credible value on the stronger workstation:

- `residual_harmonic_mlp`
- `feedforward`
- `hist_gradient_boosting`

It deliberately excludes `random_forest`, because the previous remote campaign
already showed that the family remains operationally heavy and not attractive
enough relative to histogram boosting.

## Included Runs

The dedicated launcher forwards these five YAML files:

1. `01_residual_h12_deep_long_remote.yaml`
2. `02_residual_h12_deep_dense_remote.yaml`
3. `03_feedforward_high_compute_long_remote.yaml`
4. `04_feedforward_stride1_high_compute_long_remote.yaml`
5. `05_hist_gbr_remote_refined.yaml`

All files live under:

- `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/`

## Purpose Of Each Block

### Residual-Harmonic Follow-Up

This block tests whether the strongest current neural family still improves
under:

- a longer optimization budget;
- a denser angular-sampling regime.

### Feedforward Follow-Up

This block tests whether the refreshed plain-MLP family anchor still improves
under:

- a longer schedule on the current best remote preset;
- a full-density stride-1 regime with the same core architecture.

### Tree Follow-Up

This block remains intentionally narrow:

- one bounded `hist_gradient_boosting` refinement around the current tree
  leader.

## Preconditions

The operator assumptions remain the same as the validated remote campaign path:

1. `ssh xilab-remote` already works from the current workstation;
2. the remote repository clone exists at
   `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`;
3. the remote Conda environment `standard_ml_lan_node` exists;
4. the remote environment still exposes CUDA-enabled PyTorch;
5. the dataset path expected by the repository configs is available on the
   remote machine.

## Remote Verification Checklist

Run these checks on the remote workstation before launch if the node was not
used recently:

```powershell
Set-Location "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
git checkout standard-ml-codex
conda run -n standard_ml_lan_node python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
Test-Path ".\data\datasets"
```

The expected GPU check outcome is:

- `torch.cuda.is_available()` -> `True`

## Local Launch Command

If the local environment variables are already stored, launch from the
repository root with:

```powershell
.\scripts\campaigns\run_targeted_remote_followup_campaign.ps1
```

If you prefer the explicit form, use:

```powershell
.\scripts\campaigns\run_targeted_remote_followup_campaign.ps1 `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName "standard_ml_lan_node" `
  -RemoteHostAlias "xilab-remote"
```

## What To Monitor During The Run

Watch these local files while the remote campaign is active:

- `doc/running/remote_training_campaign_status.json`
- `doc/running/remote_training_campaign_checklist.md`
- `.temp/remote_training_campaigns/`

After completion, verify the synced results under:

- `output/training_campaigns/`
- `output/training_runs/residual_harmonic_mlp/`
- `output/training_runs/feedforward/`
- `output/training_runs/tree/`
- `output/registries/families/`
- `output/registries/program/`

## Related Documents

- `doc/reports/campaign_plans/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/reports/campaign_results/2026-04-03-22-35-07_remote_training_validation_campaign_results_report.md`
