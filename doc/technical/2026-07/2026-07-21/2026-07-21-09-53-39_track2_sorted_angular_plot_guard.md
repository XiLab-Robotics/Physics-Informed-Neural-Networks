# Track 2 Sorted Angular Plot Guard

## Overview

The recently generated Track 2 candidate plots can still render nonphysical
line jumps when `angular_position_deg` is not already ordered from `0` to
`360` degrees before plotting. A prior diagnostic fixed the circular wrap
connection problem through segmented circular plotting, but the bounded
candidate plot builder still plots raw payload order directly.

This change will add a reusable plotting guard so Track 2 visual reports sort
angular positions and reorder the aligned curve vectors before drawing. The
guard must preserve the data alignment between angular position, measured TE,
and predicted TE, and it must fail clearly when a curve payload is malformed.

## Technical Approach

The implementation will use the existing Track 2 plotting utility as the
central enforcement point:

- extend `scripts/reports/analysis/track2_circular_plotting.py` with a helper
  that converts angular position and one or more aligned curve arrays to finite,
  shape-checked, stable-sorted arrays;
- use `np.argsort(..., kind="stable")` so equal angular samples keep their
  original relative order while all companion arrays are reordered with the same
  index vector;
- optionally collapse duplicate angular positions only where the caller needs
  unique samples; plotting should primarily sort and segment, not silently
  discard valid points;
- update `plot_circular_angle_curve()` and the bounded candidate plot builder
  so generated Track 2 plots always pass through the sorted circular plotting
  path;
- add validation output or assertions that make non-finite, mismatched, or
  undersized curve arrays visible.

## Involved Components

- `scripts/reports/analysis/track2_circular_plotting.py`
- `scripts/reports/analysis/build_track2_candidate_curve_plots.py`
- existing generated Track 2 plot summaries under
  `doc/reports/campaign_results/track_2/verification_plots/`
- targeted QA commands for Python compilation and Markdown checks

No subagent is planned for this change.

## Implementation Steps

1. Add a reusable angular sorting helper in the shared Track 2 circular plotting
   module.
2. Route the bounded candidate curve plot builder through the shared helper
   instead of direct `axis.plot(...)` calls.
3. Regenerate a small representative plot set from the latest patched
   polished-setpoint expansion and confirm the plot summaries still point to
   real PNG files.
4. Run `python -m py_compile` on modified Python files.
5. Run Markdown QA on this technical document and `doc/README.md`.
