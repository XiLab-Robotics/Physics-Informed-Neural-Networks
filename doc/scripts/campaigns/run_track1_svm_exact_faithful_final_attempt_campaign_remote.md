# Track 1 SVM Exact-Faithful Final Attempt Campaign Remote Launcher

## Overview

This launcher executes the approved final strict paper-faithful `SVR` campaign
on the stronger LAN workstation while preserving the same per-config execution
behavior as the local exact-paper launcher.

The remote wrapper adds only:

- LAN preflight;
- source sync to the remote repository clone;
- remote execution of the same local exact-paper launcher;
- repository-relative artifact sync back to the local repository.

## Included Runs

The remote wrapper executes the same `4` prepared exact-paper configs as the
local launcher:

1. `01_track1_svr_exact_faithful_amplitude_pair_repeat.yaml`
2. `02_track1_svr_exact_faithful_amplitude_40_repeat.yaml`
3. `03_track1_svr_exact_faithful_amplitude_240_repeat.yaml`
4. `04_track1_svr_exact_faithful_phase_162_repeat.yaml`

## Remote Defaults

By default the launcher uses:

- `RemoteHostAlias = xilab-remote`
- `RemoteRepositoryPath = C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`
- `RemoteCondaEnvironmentName = standard_ml_lan_node`

## Practical Use

Launch from the repository root:

```powershell
.\scripts\\campaigns\\track1\\svm\\run_track1_svm_exact_faithful_final_attempt_campaign_remote.ps1
```

Explicit remote arguments:

```powershell
.\scripts\\campaigns\\track1\\svm\\run_track1_svm_exact_faithful_final_attempt_campaign_remote.ps1 `
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

## Related Documents

- `doc/technical/2026-04/2026-04-17/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_preparation.md`
- `doc/reports/campaign_plans/track1/svm/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md`
