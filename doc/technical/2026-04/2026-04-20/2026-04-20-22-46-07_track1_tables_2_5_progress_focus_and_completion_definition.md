# Track 1 Tables 2-5 Progress Focus And Completion Definition

## Overview

This technical document formalizes the canonical progress surface for `Track 1`
status summaries and completion checks.

From this point onward, repository-owned summaries of `Track 1` state should
use the four colored full-matrix replication tables in
`doc/reports/analysis/RCIM Paper Reference Benchmark.md` as the primary
reference:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

These four tables are the canonical readout of `Track 1` advancement because
they expose the family-by-family paper-replication status through the green,
yellow, and red markers already used across the benchmark workflow.

This document also fixes the `Track 1` completion rule: the track is not
considered concluded when an individual campaign wave or closeout report
finishes. It is considered concluded only when the four tables are closed
across the full family bank, meaning `19` accepted exact-paper models for each
of the `10` algorithm families.

## Technical Approach

The repository should distinguish three different notions that were partially
blended in some recent `Track 1` technical documents:

1. campaign-wave closeout;
2. benchmark refresh after an accepted result change;
3. overall `Track 1` completion.

The first two are intermediate maintenance steps. The third is the actual
program-level finish line.

The canonical interpretation going forward is:

- `Track 1` progress summaries should describe advancement by referencing the
  colored state of `Table 2-5`;
- wave-level closeout documents may report a completed batch, but they must
  not imply that `Track 1` itself is finished unless the four tables are fully
  closed;
- the practical closure target is `10` algorithm families multiplied by `19`
  target-specific models per family:
  - `10` amplitude models;
  - `9` phase models;
- the practical full-closeout target is therefore `190` accepted family-target
  models represented in the canonical table surface.

Recent `Track 1` technical documents that refer to "final closeout" should be
interpreted as campaign or wave closeout only, unless they explicitly state
that the `Table 2-5` full-matrix surface is fully closed.

No subagent is planned for this documentation alignment. The scope is a local
policy clarification across the technical-document surface.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/technical/2026-04/2026-04-18/2026-04-18-11-02-15_track1_remaining_family_partial_closeout_and_benchmark_refresh.md`
- `doc/technical/2026-04/2026-04-18/2026-04-18-16-29-35_track1_remaining_family_final_closeout_after_xgbm_lgbm_reruns.md`
- `doc/technical/2026-04/2026-04-18/2026-04-18-16-47-12_track1_full_matrix_replication_table_refresh_after_closeout.md`
- `doc/technical/2026-04/2026-04-18/2026-04-18-17-11-45_track1_partial_closeout_family_row_backfill_in_full_matrix_tables.md`
- `doc/technical/2026-04/2026-04-19/2026-04-19-00-25-58_track1_remaining_family_cellwise_final_closeout.md`
- `doc/technical/2026-04/2026-04-19/2026-04-19-11-23-44_track1_remaining_family_residual_cellwise_closure_final_closeout.md`
- `doc/technical/2026-04/2026-04-20/README.md`
- `doc/README.md`

## Implementation Steps

1. Create this technical policy document with the canonical `Table 2-5`
   progress definition.
2. Update the most relevant `Track 1` technical documents so they explicitly
   treat `Table 2-5` as the reference surface for state summaries.
3. Clarify in those documents that campaign or wave closeout does not by
   itself mean `Track 1` completion.
4. State the explicit `Track 1` finish condition as `19` accepted models for
   each of the `10` algorithm families.
5. Register this new document from the day-local index and from `doc/README.md`.
6. Run repository Markdown warning checks on the touched Markdown scope before
   closing the task.
