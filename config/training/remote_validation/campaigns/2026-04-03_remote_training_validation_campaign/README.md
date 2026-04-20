# Remote Training Validation Campaign

## Overview

This campaign package defines the first real LAN-backed validation of the
repository-owned remote training workflow.

The package is intentionally narrow and exercises both major runtime paths:

- CPU-heavy tree regressors;
- GPU-oriented Lightning feedforward runs.

## Included Configurations

1. `01_random_forest_remote_medium.yaml`
   Stronger bounded random forest intended to revisit the earlier local memory
   ceiling without jumping directly to an unbounded fit.
2. `02_random_forest_remote_aggressive.yaml`
   More aggressive random forest intended to test whether the stronger remote
   workstation can keep the family competitive.
3. `03_hist_gbr_remote_deep.yaml`
   Deeper histogram gradient boosting follow-up against the current tree
   leader.
4. `04_feedforward_high_compute_remote.yaml`
   Existing high-compute feedforward preset repackaged for the remote
   validation campaign.
5. `05_feedforward_stride1_big_remote.yaml`
   Full-density larger-model feedforward stress case reused for remote GPU and
   artifact-sync validation.

## Campaign Identity

- Campaign name: `remote_training_validation_campaign_2026_04_03_17_54_21`
- Planning report:
  `doc/reports/campaign_plans/infrastructure/2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md`

## Usage

Use the dedicated launcher:

```powershell
.\scripts\\campaigns\\infrastructure\\run_remote_training_validation_campaign.ps1 `
  -RemoteRepositoryPath "C:\Work\StandardML - Codex"
```

If the current workstation already stores
`STANDARDML_REMOTE_TRAINING_REPO_PATH` and
`STANDARDML_REMOTE_TRAINING_CONDA_ENV`, the launcher can be called without
extra arguments.

Operational rule:

- treat this launcher as the command handed to the user after campaign
  preparation;
- the user starts it manually from the repository root;
- the user later reports campaign start and completion through the persistent
  campaign-state workflow.
