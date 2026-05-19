# TE Model Live Backlog Alignment

## Overview

This technical note plans a documentation-only cleanup of
`doc/running/te_model_live_backlog.md` after the recent RCIM paper-reference,
`Track 1`, `Track 2`, and `Wave 1` work.

The live backlog must reflect that the recovered original RCIM pipeline,
retuned reference archive, and `Track 1` reimplementation are now available as
separate comparison surfaces. `Track 1` must be marked closed under the revised
closure rule: closure means a populated forward/backward faithful full-bank
surface for Tables `2`-`5`, not an all-green optimization result.

The backlog must also show that `Track 2` is now the active closing branch. Its
comparison rules are direction-aware: forward candidates are evaluated on
forward curves, backward candidates on backward curves, and global candidates
with direction-separated reporting. The same directional split must remain the
default rule for `Wave 1` exports and future waves unless a future approved
technical document changes that rule.

## Technical Approach

The change is documentation-only. It will rewrite the operational status,
completed-work summary, next-step section, wave checklist, and decision notes in
the live backlog without touching training code, campaign artifacts, model
archives, or active campaign state.

The update will use these current canonical references:

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/rcim_paper_reference/RCIM Original Pipeline To Reimplementation Companion.md`
- `doc/reports/analysis/rcim_paper_reference/RCIM Original Pipeline And Reimplementation Audit.md`
- `doc/reports/analysis/rcim_paper_reference/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/running/active_training_campaign.yaml`

No subagent is planned for this update.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/README.md`
- this technical note

## Implementation Steps

1. Replace stale current-focus text with the active `Track 2` closeout focus.
2. Add explicit completed sections for recovered original pipeline, retuned
   reference archive, closed `Track 1`, and closed directional `Wave 1`.
3. Make the `Track 2` section the current in-progress branch, with its
   direction-aware candidate and evaluation rules.
4. Update `Next Up` so the planned next step after cleaning and alignment is
   clear.
5. Update wave/future-wave rules so each future wave must produce or justify
   `global`, `forward`, and `backward` surfaces.
6. Run Markdown checks on the touched Markdown scope and fix any warnings.
