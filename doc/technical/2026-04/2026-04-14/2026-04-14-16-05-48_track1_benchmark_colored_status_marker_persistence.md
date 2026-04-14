# Track 1 Benchmark Colored Status Marker Persistence

## Overview

This document covers a narrow but permanent repair of the canonical
`Track 1` benchmark maintenance flow for:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

The immediate issue is that the `Full Paper-Matrix Replication` section no
longer preserves the intended colored status markers in the
`Repository-side analogous matrix:` tables. The previous repository-owned copy
stored in `.temp/old.md` shows the expected canonical rendering:

- `🟢` reached or beaten
- `🟡` near target / acceptable follow-up
- `🔴` still materially open

The current benchmark update path degraded those markers in the full-matrix
section, so the canonical report is no longer aligned with the intended visual
dashboard semantics.

## Technical Approach

The repair must not be a one-off manual edit only. The repository needs a
stable maintenance rule so future `Track 1` campaign updates keep the colored
markers automatically.

The implementation will therefore:

1. restore the colored markers in the affected `Repository-side analogous
   matrix:` tables and in the legend block of
   `RCIM Paper Reference Benchmark.md`;
2. identify the current repository-owned update path that rewrites or
   normalizes those table cells;
3. replace the non-persistent marker normalization with a UTF-8-safe permanent
   rule that always emits `🟢`, `🟡`, and `🔴`;
4. preserve this rule for future campaign-driven benchmark refreshes so the
   marker colors continue to evolve with new results instead of falling back to
   ASCII placeholders or mojibake.

Important maintenance rule after the fix:

- whenever a new `Track 1` campaign materially changes the full-matrix results,
  the benchmark refresh logic must update the cell values and also recompute the
  correct colored marker for each cell;
- future updates must not rewrite those colored markers to `G/Y/R`, `??`, or
  broken mojibake sequences.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- the repository-owned script or helper path currently used to normalize or
  refresh the benchmark full-matrix section
- `doc/README.md`

No subagent usage is planned for this task.

## Implementation Steps

1. Restore the canonical colored markers in the current benchmark file.
2. Patch the responsible repository-owned update logic so it emits UTF-8-safe
   colored markers permanently.
3. Confirm that the benchmark file keeps the colored markers after the repair.
4. Run scoped Markdown QA on the touched Markdown files.
5. Report completion without creating a commit unless explicitly requested.
