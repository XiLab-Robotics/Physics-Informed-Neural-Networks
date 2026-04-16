# Track 1 SVR Reference Grid Search Repair Campaign Remote Launcher

## Overview

This launcher executes the approved `Track 1` `SVR` reference-grid repair
campaign on the stronger LAN workstation while preserving the behavior of the
local exact-paper launcher.

The remote wrapper now adds only the remote-specific steps:

- LAN preflight;
- source sync to the remote repository clone;
- remote execution of the same exact-paper per-config workflow used by the
  local launcher;
- repository-relative artifact sync back to the local repository.

The per-run execution loop, log naming, and exact-paper failure semantics are
therefore the same as the local launcher.

The remote wrapper now also provides terminal-only runtime observability for
long silent exact-paper fits:

- progress/status updates while the current remote config is still running;
- an immediate `Config 1/4` progress context before the first remote runner
  line arrives;
- immediate visibility of the active config and its remote per-run log path;
- `Ctrl+C` cleanup that attempts to stop the remote exact-paper process tree.

The remote exact-paper wrapper now also keeps single-writer ownership of each
per-run `.log` file. The remote child output is streamed once, persisted once,
and any per-run logging failure must abort the wrapper immediately instead of
leaving a long silent operator session after the real child has already died.

## Included Runs

The remote wrapper executes the same `4` prepared exact-paper configs as the
local launcher:

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

- remote wrapper log under `.temp/remote_training_campaigns/`
- synchronized campaign artifacts under `output/training_campaigns/`
- synchronized validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- synchronized exact-paper validation reports under
  `doc/reports/analysis/validation_checks/`

After sync-down, the main campaign logs are the same files produced by the
local launcher:

- `output/training_campaigns/<campaign_name>/logs/*.log`

While the remote run is still in progress, the terminal progress line is the
main liveness signal if the active per-run log has not emitted its first exact-
paper line yet.

## Related Documents

- `doc/technical/2026-04/2026-04-15/2026-04-15-14-14-36_track1_svr_remote_lan_campaign_execution.md`
- `doc/technical/2026-04/2026-04-15/2026-04-15-23-32-44_remote_exact_paper_launcher_parity_restoration.md`
- `doc/reports/campaign_plans/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md`
