# TE Curve Verification Pipeline Periodic MLP Harmonic Report Refresh

## Overview

Refresh the existing `TE Curve Verification Pipeline` best-model collage and multi-model curve
comparison report bundles with the newly trained `periodic_mlp` models that
use explicit harmonic input components.

The requested deliverables are the existing PDF targets:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.pdf`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.pdf`

## Technical Approach

The current `TE Curve Verification Pipeline` report builders already resolve `periodic_mlp`,
`periodic_mlp_fw`, and `periodic_mlp_bw` from the family registries under
`output/registries/families/`. Since the explicit-harmonic campaign closeout
updated those registries, the report refresh should reuse the existing
candidate-resolution path instead of hard-coding checkpoint paths.

The report builders currently create a new timestamped report date folder.
This task needs to update the already approved `[2026-05-20]` report bundles,
so the implementation will add a narrow regeneration override that can write
the refreshed Markdown into the existing report directories while still
creating immutable timestamped validation artifacts under
`output/validation_checks/`.

No subagent use is planned for this task.

## Involved Components

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-20]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-20]/`
- `output/validation_checks/track2_best_model_collage_report/`
- `output/validation_checks/track2_multi_model_curve_comparison_report/`
- `output/registries/families/periodic_mlp*/latest_family_best.yaml`

## Implementation Steps

1. Add explicit report-date or report-directory override support to both
   `TE Curve Verification Pipeline` report builders so they can update the `[2026-05-20]` bundles
   reproducibly.
2. Regenerate the best-model collage report from the current family registries.
3. Regenerate the multi-model curve comparison report from the current family
   registries.
4. Export and validate both styled PDFs through the repository PDF pipeline.
5. Inspect the rendered validation pages for image loading, table fit, clipped
   content, and right-edge pressure.
6. Run scoped Python and Markdown QA on touched scripts and reports.
