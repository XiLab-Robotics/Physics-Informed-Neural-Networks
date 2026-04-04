# Targeted Remote Follow-Up Campaign

## Overview

This campaign package defines the next selective LAN-remote follow-up after the
first validated remote training campaign.

The package intentionally excludes `random_forest` and focuses only on the
families that still have credible value on the stronger workstation:

- `residual_harmonic_mlp`
- `feedforward`
- `hist_gradient_boosting`

## Included Configurations

1. `01_residual_h12_deep_long_remote.yaml`
   Longer-budget follow-up of the current best residual-harmonic neural anchor.
2. `02_residual_h12_deep_dense_remote.yaml`
   Denser angular-sampling follow-up of the deeper residual-harmonic branch.
3. `03_feedforward_high_compute_long_remote.yaml`
   Longer-budget extension of the current remote feedforward family best.
4. `04_feedforward_stride1_high_compute_long_remote.yaml`
   Full-density higher-cost feedforward follow-up for the stronger GPU path.
5. `05_hist_gbr_remote_refined.yaml`
   Bounded refinement around the current histogram-gradient-boosting leader.

## Campaign Identity

- Campaign name:
  `targeted_remote_followup_campaign_2026_04_04_11_21_09`
- Planning report:
  `doc/reports/campaign_plans/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md`

## Usage

Use the dedicated launcher:

```powershell
.\scripts\campaigns\run_targeted_remote_followup_campaign.ps1 `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
```

If the current workstation already stores
`STANDARDML_REMOTE_TRAINING_REPO_PATH` and
`STANDARDML_REMOTE_TRAINING_CONDA_ENV`, the launcher can be called without
extra arguments.
