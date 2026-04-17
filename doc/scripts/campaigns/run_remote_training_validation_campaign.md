# Remote Training Validation Campaign Launcher

## Overview

This note documents the first real campaign prepared to validate the
repository-owned LAN training workflow on the stronger remote workstation.

The campaign intentionally mixes:

- CPU-heavy tree regressors;
- GPU-oriented Lightning feedforward runs.

That keeps the first remote validation useful even if the main purpose is
workflow verification.

## Included Runs

The dedicated launcher forwards these five YAML files:

1. `01_random_forest_remote_medium.yaml`
2. `02_random_forest_remote_aggressive.yaml`
3. `03_hist_gbr_remote_deep.yaml`
4. `04_feedforward_high_compute_remote.yaml`
5. `05_feedforward_stride1_big_remote.yaml`

All files live under:

- `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/`

## Real Preflight Status On 2026-04-03

The current workstation already passed the first connectivity check:

- `ssh xilab-remote "hostname"` returned `DESKTOP-T7O45HF`
- the remote repository path exists at
  `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`
- the remote clone is currently at commit
  `8ff4bf90e0d7cbdc06778a749e1eb7db5843b8de`
- the existing Conda environment `standard_ml_lan_node` can run the repository
  validation check successfully

The same preflight also surfaced one concrete setup gap on the remote node:

- the remote workstation has an NVIDIA RTX A4000 visible through `nvidia-smi`,
  but the current `standard_ml_lan_node` PyTorch build is CPU-only, so
  `torch.cuda.is_available()` currently returns `False`

This means the launcher is already usable for tree runs and for end-to-end sync
validation, but the feedforward branch should ideally receive a CUDA-enabled
PyTorch install before the first full mixed campaign.

## Step-By-Step Setup

### Remote Workstation

1. Open PowerShell on the remote machine.
2. Confirm the existing repository clone:

```powershell
Set-Location "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
git checkout main
```

3. Reuse the existing LAN node environment and make sure the repository
dependencies are present:

```powershell
conda activate standard_ml_lan_node
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Install CUDA-enabled PyTorch into that same environment before the mixed
campaign:

```powershell
conda activate standard_ml_lan_node
python -m pip install --force-reinstall --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

5. Verify that the remote training environment is usable:

```powershell
conda run -n standard_ml_lan_node python -c "import torch, lightning, sklearn; print(torch.__version__); print(torch.cuda.is_available())"
```

6. Verify that the repository dataset exists inside the clone:

```powershell
Test-Path ".\data\datasets"
```

### Current Workstation

1. Verify the SSH alias:

```powershell
ssh xilab-remote
ssh xilab-remote "hostname"
```

2. Persist the remote training settings locally:

```powershell
[System.Environment]::SetEnvironmentVariable("STANDARDML_REMOTE_TRAINING_REPO_PATH", "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks", "User")
[System.Environment]::SetEnvironmentVariable("STANDARDML_REMOTE_TRAINING_CONDA_ENV", "standard_ml_lan_node", "User")
```

3. Close and reopen PowerShell, then verify them:

```powershell
echo $env:STANDARDML_REMOTE_TRAINING_REPO_PATH
echo $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV
```

4. Confirm the dedicated campaign state is still marked as prepared:

```powershell
Get-Content .\doc\running\active_training_campaign.yaml
```

## Launch Command

This campaign follows the repository operator-handoff model:

1. Codex prepares the campaign package and this dedicated launcher.
2. Codex provides one of the commands below.
3. The user launches the command locally.
4. The user later reports start and completion back through the normal campaign
   workflow.

If the two local environment variables are set, the recommended operator
command from the repository root is:

```powershell
.\scripts\campaigns\run_remote_training_validation_campaign.ps1
```

If you prefer not to persist the local environment variables yet, use this
explicit operator command:

```powershell
.\scripts\campaigns\run_remote_training_validation_campaign.ps1 `
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
- `output/training_runs/tree/`
- `output/training_runs/feedforward/`
- `output/registries/families/tree/`
- `output/registries/families/feedforward/`
- `output/registries/program/`

## Related Documents

- `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/technical/2026-04/2026-04-03/2026-04-03-17-54-21_remote_training_campaign_real_validation_and_setup_guide.md`
