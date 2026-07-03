# TE Curve Verification Pipeline Circular Angle Plot Diagnostic

## Overview

This technical document plans a bounded diagnostic for a visual artifact in
`TE Curve Verification Pipeline` plot generation. The reported symptom is a
horizontal or crossing line through Track 2 plots when a curve's angular
position wraps between `360` and `0` degrees. In circular motion those two
positions are equivalent, so the plotter must avoid drawing a straight segment
across the visual domain when the ordered samples cross the wrap boundary.

The initial inspection found that the active visual builders plot raw angular
position arrays directly with Matplotlib:

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`;
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`.

The diagnostic will stay rendering-only: it must not alter model predictions,
metric calculations, candidate ranking, or official promotion policy.

## Technical Approach

The proposed solution is to add a shared circular-angle plotting helper for
Track 2 visual reports. The helper will detect angular discontinuities where
the next plotted angular position is smaller than the previous one by a
wrap-sized jump, split the curve into continuous segments, and plot each
segment separately. This prevents Matplotlib from connecting the last
pre-wrap point to the first post-wrap point with a nonphysical straight line.

The helper should preserve the raw angular position values on the x-axis. It
should not unwrap values past `360` degrees for the default report view because
the standard Track 2 visual vocabulary expects a `0` to `360` degree domain.
If needed for debugging, an alternate unwrapped view can be generated as a
temporary diagnostic artifact, but the candidate production fix should be the
segmented circular plot.

For the requested proof, the diagnostic will generate comparison images for
`harmonic_regression` using the four representative curves selected by the
current report logic:

- one image with the current direct-line plotting behavior;
- one image with circular-angle segmentation applied.

The same selected curve payloads will be used for both images so the only
changed variable is the rendering rule.

## Involved Components

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `doc/reports/analysis/track2/Track 2 Curve Reconstruction And Collage Pipeline.md`
- `output/validation_checks/track2_best_model_collage_report/`
- `doc/reports/analysis/track2/best_model_collage_report/`

No subagent use is planned. If later review of the plotting patch would be
useful, the subagent name, review scope, and approval requirement will be
declared before launch.

## Implementation Steps

1. Reproduce the artifact from the current Track 2 plotting path with a small
   harmonic-regression diagnostic run.
2. Add a local helper that splits x/y arrays at circular angular wrap
   discontinuities before calling `axis.plot`.
3. Apply the helper in the best-model collage builder and the multi-model
   curve-comparison builder.
4. Generate two diagnostic images for `harmonic_regression`: current plotting
   and circular segmented plotting, using the same four selected curves.
5. Visually inspect the generated images and report whether the nonphysical
   crossing line is removed without changing curve shape.
6. Run `python -m py_compile` on modified Python files.
7. Run Markdown warning checks on this technical document and the touched
   Markdown index.
8. Stop for user review before any Git commit.
