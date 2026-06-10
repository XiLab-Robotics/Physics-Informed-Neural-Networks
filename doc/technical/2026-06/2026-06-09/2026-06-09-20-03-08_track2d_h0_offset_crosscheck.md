# Track 2D h0 Offset Cross-Check

## Overview

Prepare a measured `h0` / curve-mean cross-check against the `Track 2D`
`signed_offset_error_deg` matrix to test whether model offset failures coincide
with extreme measured harmonic-zero behavior, or whether they remain primarily
model/regime dependent.

## Technical Approach

Use the existing `Track 2D` per-curve metric table as the model-error source
and the existing `Track 2` component-offset input table as the measured
component source. Normalize `source_file_path` separators and join rows by
source file, direction, speed, torque, and oil temperature. Filter the component
table to `harmonic_order == 0` and compare:

- signed model offset error against measured signed `h0`;
- absolute model offset error against absolute measured `h0`;
- top-decile overlap between large offset errors and large `h0` magnitude;
- model/surface-specific correlation and outlier quadrants;
- direction and temperature stratification.

The diagnostic should explicitly preserve the current conclusion that `h0` is a
priority suspect, not a confirmed sole cause, unless the overlap/correlation
evidence is strong enough to support a narrower claim.

## Involved Components

- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_per_curve_metrics.csv`
- `output/validation_checks/track2_component_offset_identification/2026-06-09-18-39-13__track2_component_offset_identification_inputs/track2_component_offset_per_curve_components.csv`
- `scripts/reports/analysis/`
- `doc/reports/analysis/track2/component_offset_identification/`
- `doc/README.md`

## Implementation Steps

1. Add a repository-owned analysis script that loads the `Track 2D` and measured
   component-offset tables, validates the join cardinality, and emits a joined
   diagnostic table.
2. Compute per-candidate and per-surface correlations, top-decile overlap
   metrics, and quadrant summaries for large-error/high-`h0`,
   large-error/normal-`h0`, small-error/high-`h0`, and nominal cases.
3. Generate a dated Markdown report under
   `doc/reports/analysis/track2/component_offset_identification/[2026-06-09]/`
   with a concise decision section and machine-readable CSV/YAML companion
   artifacts.
4. Run scoped Markdown QA, Python compile checks, and `git diff --check`.
