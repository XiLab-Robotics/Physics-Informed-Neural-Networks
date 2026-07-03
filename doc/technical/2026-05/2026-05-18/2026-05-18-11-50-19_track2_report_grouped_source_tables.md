# TE Curve Verification Pipeline Report Grouped Source Tables

## Overview

This technical document formalizes a readability refinement for the canonical
`TE Curve Verification Pipeline` report after the comparison matrix was extended to include:

- accepted `RCIM Model-Bank Reproduction` reference banks;
- recovered original forward reference banks;
- retuned forward and backward reference banks;
- exported `Wave 1` models.

The current report ranks all eligible candidates together within the forward
and backward sections. That is useful for the absolute leaderboard, but it is
hard to inspect source-specific behavior. The report should group the detailed
tables by source family: original, retuned, RCIM Model-Bank Reproduction, and Wave 1.

No subagent use is planned. If subagent use becomes useful later, this document
must be updated with the proposed subagent name, delegated task boundary, and
approval requirement before any subagent is launched.

## Technical Approach

Update the TE Curve Verification Pipeline Markdown report generator so the canonical report contains
source-grouped sections for both forward and backward comparisons.

The report should preserve the current global leaderboard behavior while adding
readable grouped tables:

- `Original Forward Models`
  - includes only `rcim_original` forward candidates;
  - no backward original table is generated.
- `Retuned Forward Models`
  - includes `rcim_retuned` forward candidates.
- `Retuned Backward Models`
  - includes `rcim_retuned` backward candidates.
- `RCIM Model-Bank Reproduction Forward Models`
  - includes `rcim_track1` forward candidates.
- `RCIM Model-Bank Reproduction Backward Models`
  - includes `rcim_track1` backward candidates.
- `Wave 1 Forward Models`
  - includes `Wave 1` forward and global candidates evaluated on forward
    curves.
- `Wave 1 Backward Models`
  - includes `Wave 1` backward and global candidates evaluated on backward
    curves.

Each grouped table should stay sorted by mean percentage error within that
group. The global Wave 1 breakdown section should remain available because it
answers a different question: how each global model behaves across forward,
backward, and combined directions.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  - update Markdown report generation helpers to group comparison rows by
    source label and direction.
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`
  - regenerate the canonical report with grouped source tables.
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`
  - regenerate or update the latest TE Curve Verification Pipeline validation report with the same
    grouped table layout.
- `doc/README.md`
  - register this technical document.

## Implementation Steps

1. Extend the TE curve-verification report builder with a reusable grouped-table helper keyed
   by candidate source label and direction.
2. Preserve the candidate inventory and global model direction breakdown.
3. Replace the flat forward and backward comparison sections with grouped
   subsections for original, retuned, RCIM Model-Bank Reproduction, and Wave 1 candidates.
4. Regenerate the canonical TE curve-verification report and latest validation report from
   the existing validation summary or rerun the current matrix if needed.
5. Run Python syntax checks for touched scripts.
6. Run Markdown QA on touched Markdown files.
7. Run commit preflight, then commit the approved curve-verification matrix extension and
   grouped report layout together.
