# Track 1 SVR Reference Grid Search Repair Campaign Remote Launcher

## Overview

This launcher executes the approved `Track 1` `SVR` reference-grid repair
campaign on the stronger LAN workstation through the canonical repository-owned
remote training workflow.

It reuses the exact same campaign package already prepared for the local
operator launcher, but moves the heavy runtime to the remote workstation while
keeping the local repository as the canonical review and bookkeeping surface.

## Included Runs

The remote launcher executes the following `4` prepared exact-paper configs:

1. `01_track1_svr_reference_grid_amplitude_pair.yaml`
2. `02_track1_svr_reference_grid_amplitude_40_only.yaml`
3. `03_track1_svr_reference_grid_amplitude_240_only.yaml`
4. `04_track1_svr_reference_grid_phase_162_only.yaml`

## Remote Defaults

By default the launcher uses:

- `RemoteHostAlias = xilab-remote`
- `RemoteRepositoryPath = C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`
- `RemoteCondaEnvironmentName = standard_ml_lan_node`

If your LAN workstation uses different values, pass them explicitly or set:

- `STANDARDML_REMOTE_TRAINING_REPO_PATH`
- `STANDARDML_REMOTE_TRAINING_CONDA_ENV`

## Practical Use

Launch from the repository root:

```powershell
.\scripts\campaigns\run_track1_svr_reference_grid_search_repair_campaign_remote.ps1
```

Explicit remote arguments:

```powershell
.\scripts\campaigns\run_track1_svr_reference_grid_search_repair_campaign_remote.ps1 `
  -RemoteHostAlias xilab-remote `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName standard_ml_lan_node
```

## Outputs To Monitor

- local remote tracking files under `doc/running/`
- local remote logs under `.temp/remote_training_campaigns/`
- synchronized campaign artifacts under `output/training_campaigns/`
- synchronized validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`

## Related Documents

- `doc/technical/2026-04/2026-04-15/2026-04-15-14-14-36_track1_svr_remote_lan_campaign_execution.md`
- `doc/reports/campaign_plans/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
