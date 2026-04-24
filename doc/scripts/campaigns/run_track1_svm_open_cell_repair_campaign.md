# Track 1 SVM Open-Cell Repair Campaign Launcher

## Overview

This launcher executes the dedicated `SVR` repair package for the currently
open `SVM` cells in the canonical `Track 1` benchmark. The package is designed
to improve only the yellow and red `SVM` cells instead of rerunning the full
`SVM` row blindly.

## Included Runs

The launcher executes the following `12` prepared validation configs:

1. `01_track1_svm_amplitude_repair_baseline.yaml`
2. `02_track1_svm_amplitude_repair_seed11.yaml`
3. `03_track1_svm_amplitude_repair_seed23.yaml`
4. `04_track1_svm_amplitude_156_focus.yaml`
5. `05_track1_svm_amplitude_156_240_focus.yaml`
6. `06_track1_svm_amplitude_low_mid_bridge.yaml`
7. `07_track1_svm_phase_repair_baseline.yaml`
8. `08_track1_svm_phase_repair_seed11.yaml`
9. `09_track1_svm_phase_repair_seed23.yaml`
10. `10_track1_svm_phase_240_focus.yaml`
11. `11_track1_svm_phase_162_240_focus.yaml`
12. `12_track1_svm_phase_1_39_bridge.yaml`

## Campaign Rule

- `SVR` remains the only enabled family in every run.
- Amplitude-side runs target only currently open `A_k` cells.
- Phase-side runs target only currently open `phi_k` cells and keep
  `phase_0` excluded.
- The package prioritizes the strongest blockers first:
  `A_156`, `phi_240`, then `162`, then the residual bridge harmonics.

## Practical Use

Launch from the repository root:

```powershell
.\scripts\\campaigns\\track1\\svm\\run_track1_svm_open_cell_repair_campaign.ps1
```

Optional explicit environment arguments:

```powershell
.\scripts\\campaigns\\track1\\svm\\run_track1_svm_open_cell_repair_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

- campaign logs under
  `output/training_campaigns/track1/svm/track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21/logs/`
- validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- canonical benchmark status in
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Related Documents

- `doc/technical/2026-04/2026-04-14/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_preparation.md`
- `doc/reports/campaign_plans/track1/svm/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_plan_report.md`
