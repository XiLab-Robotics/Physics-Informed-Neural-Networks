# Track 1 Extended Overnight Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the larger and
heavier overnight `Track 1` campaign package.

The package is organized as `6` logical blocks and `48` total runs, but it is
still launched through one command and one coordinated queue.

All runs use:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

## Included Blocks

The dedicated launcher forwards all YAML files under:

- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-13_track1_extended_overnight_campaign/`

Logical block order:

1. `Block A`: wide low-order `HGBM` search
2. `Block B`: heavy low-order `HGBM` runs
3. `Block C`: late-harmonic repair expansion
4. `Block D`: low-order plus late-harmonic bridge runs
5. `Block E`: engineered-term recheck under heavy structure
6. `Block F`: narrow `RF` controls

## One Command Launch Surface

Run the entire package from the repository root with one command:

```powershell
.\scripts\\campaigns\\track1\\harmonic_wise\\run_track1_extended_overnight_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\\campaigns\\track1\\harmonic_wise\\run_track1_extended_overnight_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Output Surface

Each coordinated run writes validation artifacts under:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

The launcher writes per-run console logs under:

- `output/training_campaigns/track1/harmonic_wise/track1_extended_overnight_campaign_2026_04_13_13_31_57/logs/`

Each successful run also refreshes:

- `doc/reports/analysis/Training Results Master Summary.md`

## Related Documents

- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-13-13-27-37_track1_extended_overnight_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-13/2026-04-13-13-27-37_track1_extended_overnight_campaign_preparation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.md`
