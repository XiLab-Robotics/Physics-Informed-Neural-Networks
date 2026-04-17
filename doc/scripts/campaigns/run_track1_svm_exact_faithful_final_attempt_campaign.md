# Track 1 SVM Exact-Faithful Final Attempt Campaign Launcher

## Overview

This launcher executes the approved final strict paper-faithful `SVR` campaign
for the residual `SVM` yellow cells in canonical `Track 1`.

The launcher is intentionally narrow:

- it keeps `SVR` as the only enabled family;
- it keeps `paper_reference_grid_search` as the only search mode;
- it does not widen the recovered paper hyperparameter grid;
- it reruns only the residual targets `40`, `240`, and `162`.

## Included Runs

The launcher executes these `4` prepared exact-paper configs:

1. `01_track1_svr_exact_faithful_amplitude_pair_repeat.yaml`
2. `02_track1_svr_exact_faithful_amplitude_40_repeat.yaml`
3. `03_track1_svr_exact_faithful_amplitude_240_repeat.yaml`
4. `04_track1_svr_exact_faithful_phase_162_repeat.yaml`

## Practical Use

Launch from the repository root:

```powershell
.\scripts\campaigns\run_track1_svm_exact_faithful_final_attempt_campaign.ps1
```

Explicit Conda environment:

```powershell
.\scripts\campaigns\run_track1_svm_exact_faithful_final_attempt_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env
```

## Outputs To Monitor

- campaign logs under
  `output/training_campaigns/track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20/logs/`
- validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- exact-paper validation reports under
  `doc/reports/analysis/validation_checks/`

## Related Documents

- `doc/technical/2026-04/2026-04-17/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_preparation.md`
- `doc/reports/campaign_plans/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md`
