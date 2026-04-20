# Track 1 Second Iteration Harmonic-Wise Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the comprehensive
second `Track 1` harmonic-wise campaign.

It exists because this branch is not a standard training-family campaign driven
through `scripts/training/run_training_campaign.py`.

Instead, it orchestrates multiple paper-reimplementation validation runs
through:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

## Included Runs

The dedicated launcher forwards these eight YAML files:

1. `01_full_rcim_baseline_reference.yaml`
2. `02_h013_engineered_stage1.yaml`
3. `03_h013_random_forest_diagnostic.yaml`
4. `04_h01340_engineered_stage2.yaml`
5. `05_h0134078_engineered_stage3.yaml`
6. `06_full_rcim_no_engineering_reference.yaml`
7. `07_full_rcim_engineered_balanced.yaml`
8. `08_full_rcim_engineered_deeper.yaml`

All files live under:

- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-09_track1_second_iteration_harmonic_wise_campaign/`

## Purpose Of Each Block

### Full-RCIM Anchors

These runs keep the branch honest against the full harmonic coverage required
by the RCIM paper.

They answer:

- whether the baseline can be reproduced cleanly;
- whether improved predictor settings still help on the full RCIM set;
- whether engineered features are materially useful after full promotion.

### Reduced Harmonic Progression

These runs isolate the practically dominant harmonic groups:

- `0,1,39`
- `0,1,39,40`
- `0,1,39,40,78`

They answer whether the predictor becomes materially better before the branch
returns to the full RCIM harmonic set.

### RandomForest Diagnostic

This run is diagnostic only.

It answers whether the staged setup itself is helping, even without relying
only on histogram boosting.

It is not intended as a deployment-promotion candidate.

## Practical Use

Run the canonical harmonic-wise campaign launcher from the repository root:

```powershell
.\scripts\\campaigns\\track1\\harmonic_wise\\run_track1_second_iteration_harmonic_wise_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\\campaigns\\track1\\harmonic_wise\\run_track1_second_iteration_harmonic_wise_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

Each run writes under:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

Each run also produces a validation report under:

- `doc/reports/analysis/validation_checks/`

The launcher will also refresh:

- `doc/reports/analysis/Training Results Master Summary.md`

## Related Documents

- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-09-18-56-03_track1_second_iteration_harmonic_wise_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-09/2026-04-09-18-56-03_track1_second_iteration_campaign_preparation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.md`
