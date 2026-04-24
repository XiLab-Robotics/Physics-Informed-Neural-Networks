# Track 1 Exact-Paper Open-Cell Repair Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the next `Track 1`
exact-paper open-cell repair campaign.

It orchestrates multiple exact-paper validation runs through:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

## Included Runs

The dedicated launcher forwards these YAML files:

1. `01_exact_open_cell_refresh_full_bank.yaml`
2. `02_exact_open_cell_low_order_repair.yaml`
3. `03_exact_open_cell_high_order_tree_repair.yaml`
4. `04_exact_open_cell_paper_family_reference.yaml`
5. `05_exact_open_cell_phase_gap_bridge.yaml`
6. `06_exact_open_cell_tree_control_bank.yaml`

All files live under:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/open_cell_repair/shared/2026-04-13_track1_exact_paper_open_cell_repair_campaign/`

## Purpose Of Each Block

### Refresh Full Bank

This run refreshes the all-family exact-paper baseline so the campaign starts
from a fresh canonical comparison artifact.

### Low-Order Repair

This run targets the still-open low-order paper cells around harmonics `0`,
`1`, `3`, and `39`, where `SVR`, `RF`, `GBM`, `HGBM`, and `LGBM` are the most
relevant paper-facing families.

### High-Order Tree Repair

This run isolates the high-order tree surface around `RF`, `ET`, and `ERT`,
especially for the remaining `162` and `240` gaps.

### Paper-Family Reference

This run keeps only the family codes that the paper actually selects in Table
`6`.

### Phase-Gap Bridge

This run re-checks the open phase-side cells without unrelated families.

### Tree-Control Bank

This run keeps a broad non-`SVR` tree-heavy control surface to verify whether
the `SVR` branch is helping only where the paper expects it to.

## Practical Use

Run the canonical exact-paper open-cell repair launcher from the repository
root:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_exact_paper_open_cell_repair_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_exact_paper_open_cell_repair_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

## Outputs To Monitor

Each run writes under:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`

Each run also produces a validation report under:

- `doc/reports/analysis/validation_checks/`

The launcher writes per-run console logs under:

- `output/training_campaigns/track1/exact_paper/forward/uncategorized/shared/track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53/logs/`

## Related Documents

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-13/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_preparation.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.md`
