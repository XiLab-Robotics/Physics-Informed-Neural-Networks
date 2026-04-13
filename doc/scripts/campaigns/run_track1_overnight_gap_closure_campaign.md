# Track 1 Overnight Gap-Closure Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the next overnight
`Track 1` campaign batch.

The package is organized as `4` logical campaign blocks, but it is launched
through one command and one coordinated run list.

All runs use:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

This is intentional. The current overnight objective is to improve the shared
offline evaluator tied to `Target A` while keeping the paper-table gaps visible.

## Included Runs

The dedicated launcher forwards `20` YAML files grouped into:

1. `Campaign A`: low-order `HGBM` ladder
2. `Campaign B`: late-harmonic repair ladder
3. `Campaign C`: `RandomForest` counterfactuals
4. `Campaign D`: engineered-term recovery

All files live under:

- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-13_track1_overnight_gap_closure_campaign/`

## One Command Launch Surface

Run the entire overnight package from the repository root with one command:

```powershell
.\scripts\campaigns\run_track1_overnight_gap_closure_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\campaigns\run_track1_overnight_gap_closure_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Output Surface

Each coordinated run writes validation artifacts under:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

The launcher writes per-run console logs under:

- `output/training_campaigns/track1_overnight_gap_closure_campaign_2026_04_13_01_02_23/logs/`

Each successful run also refreshes:

- `doc/reports/analysis/Training Results Master Summary.md`

## Related Documents

- `doc/reports/campaign_plans/2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-13/2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_preparation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.md`
