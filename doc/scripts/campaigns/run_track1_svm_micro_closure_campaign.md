# Track 1 SVM Micro-Closure Campaign Launcher

## Overview

This launcher executes the dedicated `SVR` micro-closure package for the last
residual yellow `SVM` cells in the canonical `Track 1` benchmark.

The package is designed to finish the `SVM` row with the smallest campaign
surface used so far.

## Included Runs

The launcher executes the following `8` prepared validation configs:

1. `01_track1_svm_amplitude_micro_closure_baseline.yaml`
2. `02_track1_svm_amplitude_micro_closure_seed23.yaml`
3. `03_track1_svm_amplitude_micro_closure_split15.yaml`
4. `04_track1_svm_amplitude_40_only.yaml`
5. `05_track1_svm_amplitude_240_only.yaml`
6. `06_track1_svm_phase_micro_closure_baseline.yaml`
7. `07_track1_svm_phase_micro_closure_split15.yaml`
8. `08_track1_svm_phase_micro_closure_seed23.yaml`

## Campaign Rule

- `SVR` remains the only enabled family in every run.
- Amplitude-side runs target only `40` and `240`.
- Phase-side runs target only `162` and keep `phase_0` excluded.
- The package minimizes scope while still probing the residual cells through
  seed and split variation.

## Practical Use

Launch from the repository root:

```powershell
.\scripts\campaigns\run_track1_svm_micro_closure_campaign.ps1
```

Optional explicit environment arguments:

```powershell
.\scripts\campaigns\run_track1_svm_micro_closure_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

- campaign logs under
  `output/training_campaigns/track1_svm_micro_closure_campaign_2026_04_14_21_42_47/logs/`
- validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- canonical benchmark status in
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Related Documents

- `doc/technical/2026-04/2026-04-14/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_preparation.md`
- `doc/reports/campaign_plans/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_plan_report.md`
