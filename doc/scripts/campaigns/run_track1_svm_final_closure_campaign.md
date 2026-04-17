# Track 1 SVM Final Closure Campaign Launcher

## Overview

This launcher executes the dedicated `SVR` final-closure package for the last
residual yellow `SVM` cells in the canonical `Track 1` benchmark.

The package is designed to close the remaining `SVM` row cells instead of
rerunning the full row or reopening already solved surfaces.

## Included Runs

The launcher executes the following `12` prepared validation configs:

1. `01_track1_svm_amplitude_final_closure_baseline.yaml`
2. `02_track1_svm_amplitude_final_closure_seed11.yaml`
3. `03_track1_svm_amplitude_final_closure_seed23.yaml`
4. `04_track1_svm_amplitude_hard_tail_focus.yaml`
5. `05_track1_svm_amplitude_hard_tail_seed11.yaml`
6. `06_track1_svm_amplitude_40_bridge.yaml`
7. `07_track1_svm_amplitude_full_closure_split15.yaml`
8. `08_track1_svm_phase_final_closure_baseline.yaml`
9. `09_track1_svm_phase_final_closure_seed11.yaml`
10. `10_track1_svm_phase_final_closure_seed23.yaml`
11. `11_track1_svm_phase_final_closure_split15.yaml`
12. `12_track1_svm_phase_final_closure_split25.yaml`

## Campaign Rule

- `SVR` remains the only enabled family in every run.
- Amplitude-side runs target only `40`, `156`, and `240`.
- Phase-side runs target only `162` and keep `phase_0` excluded.
- The package concentrates most of the pressure on the hard-tail amplitude
  cells while also probing split sensitivity on the last residual phase
  harmonic.

## Practical Use

Launch from the repository root:

```powershell
.\scripts\campaigns\run_track1_svm_final_closure_campaign.ps1
```

Optional explicit environment arguments:

```powershell
.\scripts\campaigns\run_track1_svm_final_closure_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

- campaign logs under
  `output/training_campaigns/track1_svm_final_closure_campaign_2026_04_14_20_50_01/logs/`
- validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- canonical benchmark status in
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Related Documents

- `doc/technical/2026-04/2026-04-14/2026-04-14-20-50-01_track1_svm_final_closure_campaign_preparation.md`
- `doc/reports/campaign_plans/2026-04-14-20-50-01_track1_svm_final_closure_campaign_plan_report.md`
