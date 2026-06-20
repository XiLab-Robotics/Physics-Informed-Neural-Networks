# Target A Offline Closeout

## Overview

This technical document plans the documentation-only closeout of `Target A`.

`Target A` is the offline paper-comparable TE-curve prediction target. The
current `TE Curve Verification Pipeline` comparison has enough direction-qualified evidence to close
it without launching a new training campaign:

- forward is paper-comparable and uses `paper_retuned_best_Fw`, which reaches
  `4.109%` mean percentage error against the paper's `4.7%` offline target;
- backward has no paper-original reference surface, so the approved rule uses
  `paper_retuned_best_Bw` as the canonical paper-derived backward baseline at
  `7.572%` mean percentage error;
- `RCIM Model-Bank Reproduction` remains closed as faithful full-dataset reproduction evidence, not
  as the optimized winner;
- end-to-end online compensation remains outside `Target A` and belongs to
  `Target B`.

## Technical Approach

The implementation will update canonical project documentation so `Target A`
is no longer treated as open or missing after the backward retuned-baseline rule
has been formalized.

The closeout wording will be direction-qualified:

- `Target A` status: `closed_offline_direction_qualified`;
- forward verdict: met against the paper-comparable `4.7%` offline threshold;
- backward verdict: closed against the formalized retuned backward baseline;
- residual gap: online compensation remains open under `Target B`.

No training, model archive refresh, or registry mutation is planned.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/README.md`

No subagent is planned. If subagent use becomes useful later, it must be
declared and approved before launch.

## Implementation Steps

1. Update the live backlog to mark `Target A` as closed in the offline
   direction-qualified sense.
2. Update the `TE Curve Verification Pipeline` report interpretation so its closeout states the
   forward and backward `Target A` verdicts explicitly.
3. Update the master summary so project status and gap summaries no longer
   imply that offline `Target A` is open.
4. Preserve `Target B` as the remaining online compensation benchmark.
5. Run Markdown QA on all touched Markdown files.
6. Report completion and wait for explicit commit approval.
