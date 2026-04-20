# Track 1 Full-Matrix Replication Table Refresh After Closeout

## Overview

This document formalizes a missing closeout step for `Track 1` campaign
reporting. After the final `XGBM` and `LGBM` reruns, the canonical benchmark
report was refreshed at the addendum level, but the family-by-family
full-matrix replication tables remained partially stale. In particular, the
colored comparison surfaces for Tables `2-5` were not fully updated to reflect
the latest `XGBM/LGBM` improvements.

The goal of this task is to refresh the four canonical comparative tables in
`doc/reports/analysis/RCIM Paper Reference Benchmark.md` and to codify the
rule that every future `Track 1` closeout must update those tables whenever a
campaign changes the accepted family results.

These four tables are also the canonical reference surface for future `Track 1`
state summaries and progress statements.

## Technical Approach

The implementation stays intentionally narrow:

1. Refresh the four full-matrix comparative sections in the canonical benchmark
   report:
   - `Table 2 - Amplitude MAE Full-Matrix Replication`
   - `Table 3 - Amplitude RMSE Full-Matrix Replication`
   - `Table 4 - Phase MAE Full-Matrix Replication`
   - `Table 5 - Phase RMSE Full-Matrix Replication`
2. Replace stale `XGBM/LGBM` row values and colored status markers with the
   latest accepted post-rerun metrics already serialized in the validation
   summaries and campaign closeout artifacts.
3. Add an explicit maintenance rule to the benchmark so future `Track 1`
   closeouts update both:
   - the addendum-style summary sections;
   - the canonical family-by-family colored replication tables.
4. Treat full `Track 1` completion as separate from any single closeout wave:
   the track is complete only when the `Table 2-5` surface is closed for all
   `10` algorithm families with `19` accepted models per family.
5. Run repository Markdown QA on the touched Markdown scope before closing the
  task.

No subagent is planned for this task. The scope is small, local, and directly
inspectable.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/technical/2026-04/2026-04-18/README.md`
- `doc/README.md`
- Latest exact-paper validation summaries for:
  - `track1_xgbm_amplitude_full_matrix`
  - `track1_xgbm_phase_full_matrix`
  - `track1_lgbm_amplitude_full_matrix`
  - `track1_lgbm_phase_full_matrix`

## Implementation Steps

1. Re-read the latest accepted `XGBM` and `LGBM` validation summaries.
2. Recompute the correct green/yellow/red markers against the paper thresholds.
3. Patch the four family-by-family full-matrix tables in the benchmark report.
4. Add the persistent closeout-maintenance note for future `Track 1` campaign
   completions.
5. Record in the touched documentation that `Track 1` progress and completion
   are judged through the `Table 2-5` surface, with `10 x 19` accepted models
   as the finish condition.
6. Run Markdown warning checks on the touched Markdown files and resolve any
   issues before closing the task.
