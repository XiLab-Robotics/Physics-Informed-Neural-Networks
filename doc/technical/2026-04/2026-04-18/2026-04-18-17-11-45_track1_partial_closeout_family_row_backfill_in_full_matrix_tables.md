# Track 1 Partial Closeout Family Row Backfill In Full-Matrix Tables

## Overview

This task repairs a remaining synchronization gap in the canonical `Track 1`
benchmark report. The partial closeout of the interrupted remaining-family
campaign correctly stated that the completed seven-family rerun materially
refreshed the row-reproduction evidence for `MLP`, `RF`, `DT`, `ET`, `ERT`,
`GBM`, and `HGBM`. However, the four family-by-family colored full-matrix
tables were not fully backfilled at that time.

The goal is to re-check those seven family rows against the accepted
partial-closeout outputs and update the canonical matrices in
`doc/reports/analysis/RCIM Paper Reference Benchmark.md` where any value or
`🟢/🟡/🔴` marker still reflects the older pre-refresh state.

## Technical Approach

The implementation remains narrow and benchmark-focused:

1. inspect the partial-closeout artifacts and accepted validation summaries for
   the seven completed rerun families:
   - `MLP`
   - `RF`
   - `DT`
   - `ET`
   - `ERT`
   - `GBM`
   - `HGBM`
2. compare those accepted values against the current family-by-family rows in
   the canonical benchmark report for:
   - `Table 2 - Amplitude MAE Full-Matrix Replication`
   - `Table 3 - Amplitude RMSE Full-Matrix Replication`
   - `Table 4 - Phase MAE Full-Matrix Replication`
   - `Table 5 - Phase RMSE Full-Matrix Replication`
3. patch only the rows that are still stale, leaving already synchronized rows
   untouched;
4. preserve the existing color-threshold policy:
   - `🟢` reached or beaten;
   - `🟡` still above paper but within `25%`;
   - `🔴` materially above paper;
5. run Markdown QA on the touched benchmark file before closing the task.

No subagent is planned for this task. The scope is local, deterministic, and
does not justify delegation.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report.md`
- accepted exact-paper validation summaries for the seven completed rerun
  families
- `doc/technical/2026-04/2026-04-18/README.md`
- `doc/README.md`

## Implementation Steps

1. Resolve the accepted partial-closeout source runs for the seven completed
   families.
2. Extract the effective amplitude and phase metrics used by the canonical
   benchmark.
3. Compare the current benchmark rows against those accepted values.
4. Patch stale family rows in the four full-matrix benchmark tables.
5. Run repository Markdown warning checks on the touched Markdown scope.
