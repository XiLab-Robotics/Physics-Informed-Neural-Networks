# RCIM Model-Bank Reproduction Reporting Template Alignment To Paper Table Closure

## Overview

This technical document defines the last consistency step required after the
documentation-only `RCIM Model-Bank Reproduction` objective change.

The repository now states correctly that `RCIM Model-Bank Reproduction` is a paper-table
replication branch and not a winner-centric harmonic-wise campaign branch.
However, the reporting and summary generators still contain wording and layout
assumptions that can reintroduce the old interpretation in future outputs.

This task will align the relevant report-generation path so future `RCIM Model-Bank Reproduction`
outputs default to:

- canonical paper-table cell closure language;
- per-target and per-harmonic status language;
- support-branch wording for the shared offline evaluator;
- explicit de-emphasis of campaign-local winners as the primary readout.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The repository already contains two different `RCIM Model-Bank Reproduction` output surfaces:

1. the exact-paper table-replication branch;
2. the harmonic-wise support branch used for TE-level diagnostic progress.

The current inconsistency is that some generated summaries and campaign-facing
report surfaces still make the harmonic-wise support branch look like the
canonical `RCIM Model-Bank Reproduction` closure path.

This task will therefore update the relevant generation logic so that:

- `RCIM Model-Bank Reproduction` generated summaries explicitly state the exact-paper table report
  as the canonical closure source;
- harmonic-wise `RCIM Model-Bank Reproduction` outputs label their local winner only as a
  `support-branch winner`;
- future generated status text prioritizes:
  - open cells;
  - closed cells;
  - harmonic-level closure;
  - next repair priorities;
- winner-centric wording is preserved only where campaign bookkeeping still
  requires a local winner artifact, not as the primary user-facing objective.

The immediate generator most clearly in scope is the master summary generator.
Depending on the code shape, this task may also require small wording or table
selection adjustments in other reporting helpers if they currently force
winner-first language for `RCIM Model-Bank Reproduction`.

## Involved Components

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `scripts/reports/generate_training_results_master_summary.py`
- `scripts/training/run_training_campaign.py`
- `scripts/reports/generate_styled_report_pdf.py`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-13/README.md`

## Implementation Steps

1. Inspect the current report-generation code paths that still emit
   winner-centric `RCIM Model-Bank Reproduction` wording.
2. Update the generators so `RCIM Model-Bank Reproduction` summaries default to the canonical
   paper-table closure framing.
3. Keep campaign-local winner serialization intact where needed for artifact
   bookkeeping, but rename the user-facing interpretation to
   `support-branch winner` when the report is part of the harmonic-wise support
   branch.
4. Ensure any future `RCIM Model-Bank Reproduction` summary text names the exact-paper table report
   as the primary closure source.
5. Regenerate or partially regenerate the affected repository-owned canonical
   summary output if needed to confirm the updated wording is real rather than
   only theoretical.
6. Run Markdown warning checks on the touched Markdown scope and any needed
   verification on touched Python files before closing the task.
