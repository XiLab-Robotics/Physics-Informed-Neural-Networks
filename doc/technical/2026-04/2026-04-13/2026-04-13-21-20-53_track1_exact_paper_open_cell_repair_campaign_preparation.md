# Track 1 Exact-Paper Open-Cell Repair Campaign Preparation

## Overview

This technical document prepares the next `Track 1` campaign under the new
paper-table-first paradigm.

The campaign objective is no longer to improve a single harmonic-wise campaign
winner under a shared offline evaluator. The objective is to reduce the exact
paper-table gaps that are still open in canonical Tables `3`, `4`, `5`, and
`6`.

The current exact-paper baseline still shows:

- `0/10` harmonics fully closed in Table `6`;
- `7/10` harmonics partially matched;
- `3/10` harmonics not yet matched: `0`, `1`, `240`.

The new campaign should therefore be prepared as a narrow
`open-cell repair campaign` on the exact-paper branch.

## Technical Approach

The campaign should use the existing exact-paper validation runner:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

This runner already supports stable campaign execution through YAML-driven
family subsets and ONNX export modes. It does not currently expose
harmonic-target filtering. For that reason, the repair strategy must be:

1. define run subsets around the paper-relevant model families;
2. execute those subsets on the canonical exact-paper dataset split;
3. read campaign outcome through exact-paper cell closure status, not through a
   winner-only summary.

The prepared batch should therefore combine:

- one refreshed all-family baseline run for exact-paper comparability;
- paper-selected family subsets that attack the currently open cells;
- high-order tree-family subsets for the still-open `ERT` and `RF` regions;
- a final reduced paper-family reference run that contains only the families
  actually selected by the paper in Table `6`.

No subagent is planned for this work. The preparation and implementation scope
remain local to the repository.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/validation_checks/track1/exact_paper/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`

## Implementation Steps

1. Create the campaign planning report centered on open-cell closure in Tables
   `3-6`.
2. After user approval, generate a dedicated exact-paper campaign config
   package under a new campaign directory.
3. After user approval, create the matching PowerShell launcher and launcher
   note.
4. Update `doc/running/active_training_campaign.yaml` to the new prepared
   campaign state.
5. Provide the exact launch command for operator execution.
6. After campaign completion and user approval, write the results report in the
   new cell-closure-first format and synchronize the canonical benchmark
   reports.
