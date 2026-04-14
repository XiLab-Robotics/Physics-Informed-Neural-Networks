# Track 1 Full-Matrix Family Reproduction Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the `Track 1`
exact-paper family-reproduction campaign.

It orchestrates `20` exact-paper validation runs through:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

## Included Runs

The dedicated launcher forwards these YAML files:

1. `01_track1_svm_amplitude_full_matrix.yaml`
2. `02_track1_svm_phase_full_matrix.yaml`
3. `03_track1_mlp_amplitude_full_matrix.yaml`
4. `04_track1_mlp_phase_full_matrix.yaml`
5. `05_track1_rf_amplitude_full_matrix.yaml`
6. `06_track1_rf_phase_full_matrix.yaml`
7. `07_track1_dt_amplitude_full_matrix.yaml`
8. `08_track1_dt_phase_full_matrix.yaml`
9. `09_track1_et_amplitude_full_matrix.yaml`
10. `10_track1_et_phase_full_matrix.yaml`
11. `11_track1_ert_amplitude_full_matrix.yaml`
12. `12_track1_ert_phase_full_matrix.yaml`
13. `13_track1_gbm_amplitude_full_matrix.yaml`
14. `14_track1_gbm_phase_full_matrix.yaml`
15. `15_track1_hgbm_amplitude_full_matrix.yaml`
16. `16_track1_hgbm_phase_full_matrix.yaml`
17. `17_track1_xgbm_amplitude_full_matrix.yaml`
18. `18_track1_xgbm_phase_full_matrix.yaml`
19. `19_track1_lgbm_amplitude_full_matrix.yaml`
20. `20_track1_lgbm_phase_full_matrix.yaml`

All files live under:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-14_track1_full_matrix_family_reproduction_campaign/`

## Campaign Rule

Each run enables exactly one paper family and one target group:

- amplitude runs keep only amplitude targets and populate one row of paper
  Table `3`;
- phase runs keep only phase targets and populate one row of paper Tables `4`
  and `5`;
- phase runs exclude `phase_0` so the prepared campaign stays aligned with the
  paper-facing matrix scope.

## Practical Use

Run the canonical family-reproduction launcher from the repository root:

```powershell
.\scripts\campaigns\run_track1_full_matrix_family_reproduction_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\campaigns\run_track1_full_matrix_family_reproduction_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

Each run writes under:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`

Each run also produces a validation report under:

- `doc/reports/analysis/validation_checks/`

The launcher writes per-run console logs under:

- `output/training_campaigns/track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51/logs/`

## Related Documents

- `doc/reports/campaign_plans/2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-14/2026-04-14-13-42-10_track1_full_matrix_family_campaign_preparation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.md`
