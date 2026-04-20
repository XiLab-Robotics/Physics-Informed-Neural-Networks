# Track 1 SVR Reference Grid Search Repair Campaign Launcher

## Overview

This launcher executes the first `SVR` repair package that uses the recovered
paper-reference `GridSearchCV` path.

The package is designed to re-test the remaining `SVM` yellow cells under the
true paper-faithful tuning rule rather than under repository seed/split sweeps.

## Included Runs

The launcher executes the following `4` prepared validation configs:

1. `01_track1_svr_reference_grid_amplitude_pair.yaml`
2. `02_track1_svr_reference_grid_amplitude_40_only.yaml`
3. `03_track1_svr_reference_grid_amplitude_240_only.yaml`
4. `04_track1_svr_reference_grid_phase_162_only.yaml`

## Campaign Rule

- `SVR` remains the only enabled family in every run.
- All runs force `paper_reference_grid_search`.
- Amplitude-side runs target only `40` and `240`.
- The phase-side run targets only `162` and keeps `phase_0` excluded.
- The package is deterministic and narrow by design.

## Practical Use

Launch from the repository root:

```powershell
.\scripts\\campaigns\\track1\\svm\\run_track1_svr_reference_grid_search_repair_campaign.ps1
```

Optional explicit environment arguments:

```powershell
.\scripts\\campaigns\\track1\\svm\\run_track1_svr_reference_grid_search_repair_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

- campaign logs under
  `output/training_campaigns/track1/svm/track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48/logs/`
  These logs are expected to grow live during execution.
- validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- canonical benchmark status in
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Related Documents

- `doc/technical/2026-04/2026-04-14/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_preparation.md`
- `doc/reports/campaign_plans/track1/svm/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md`
