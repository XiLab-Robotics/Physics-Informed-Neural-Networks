# RCIM Model-Bank Reproduction Objective Redefinition To Paper Table Replication

## Overview

This technical document formalizes the required objective change for `RCIM Model-Bank Reproduction`.

`RCIM Model-Bank Reproduction` must no longer be treated as a campaign-style search for one global
winner under the repository-owned shared offline evaluator. That criterion is
useful for the repository harmonic-wise benchmark branch, but it is not the
closure criterion requested for the paper-faithful RCIM branch.

From this point forward, the canonical `RCIM Model-Bank Reproduction` objective is:

- reproduce the paper-facing tables per harmonic target;
- evaluate progress by table-cell completion rather than by campaign winner;
- report status per algorithm, per harmonic, and per target family of
  quantities:
  - `A_k`;
  - `phi_k`;
- distinguish clearly between:
  - cells that already meet the paper target;
  - cells that still miss the paper target;
  - harmonic rows that are fully closed, partially closed, or still open.

The exact recovered RCIM branch under
`scripts/paper_reimplementation/rcim_ml_compensation/` already contains the
correct implementation direction for this objective through the canonical paper
table comparison workflow. The repository documentation now needs to be
realigned so future `RCIM Model-Bank Reproduction` planning, execution, and interpretation all use
that criterion consistently.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The documentation update will promote the exact-paper table-replication
criterion into the canonical definition of `RCIM Model-Bank Reproduction`.

The main rule change is:

- the repository-owned harmonic-wise shared-evaluator metric remains useful as
  support evidence;
- however, it is no longer the primary success criterion for `RCIM Model-Bank Reproduction`;
- the primary `RCIM Model-Bank Reproduction` success criterion becomes the canonical paper-table
  replication status serialized by the exact-paper workflow.

Future `RCIM Model-Bank Reproduction` plans and reports should therefore be rewritten to answer
questions such as:

1. which `A_k` cells already meet the paper target in the canonical table;
2. which `phi_k` cells already meet the paper target in the canonical table;
3. which harmonic rows are fully matched, partially matched, or not yet
   matched;
4. which paper-listed model family is expected for each target;
5. which repository family currently holds the best achieved value for that
   same target;
6. what numeric gap remains against the paper value for each still-open cell.

This task will update planning and analysis documents so they stop framing
`RCIM Model-Bank Reproduction` around:

- one promoted campaign winner;
- one best shared-evaluator score;
- one global `Target A` figure as the main closure gate.

Instead, they will frame `RCIM Model-Bank Reproduction` around:

- canonical Tables `3`, `4`, `5`, and `6`;
- per-target and per-harmonic closure status;
- explicit open-cell repair priorities.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/rcim_paper_reference/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/validation_checks/rcim_model_bank_reproduction/track1/exact_paper/forward/shared/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track_1/harmonic_wise/2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_plan_report.md`
- `doc/reports/campaign_plans/track_1/harmonic_wise/2026-04-13-13-27-37_track1_extended_overnight_campaign_plan_report.md`
- `doc/reports/campaign_results/track_1/harmonic_wise/forward/2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track_1/harmonic_wise/forward/2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report.md`
- `doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Harmonic-Wise Paper Reimplementation Pipeline.md`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-13/README.md`

## Implementation Steps

1. Update the canonical analysis documents so `RCIM Model-Bank Reproduction` is defined as a
   paper-table replication branch rather than a shared-evaluator winner search.
2. Rewrite the active `RCIM Model-Bank Reproduction` campaign-plan documents so their objectives,
   candidate tables, and success criteria are expressed as paper-table cell
   closure and open-cell repair priorities.
3. Rewrite the completed recent `RCIM Model-Bank Reproduction` campaign-results reports so their
   primary outcome is expressed as:
   - completed paper-table cells;
   - still-open cells;
   - harmonic-level closure status;
   - remaining repair priorities.
4. Update the guide and index documents so future readers do not confuse the
   exact-paper `RCIM Model-Bank Reproduction` branch with the repository-owned shared-evaluator
   branch.
5. Preserve the shared offline evaluator only as supporting diagnostic context
   when it helps explain a result, not as the canonical `RCIM Model-Bank Reproduction` winner gate.
6. Run Markdown warning checks on the touched Markdown scope and resolve every
   warning before closing the task.
