# Wave 5.1 TE Curve Verification Pipeline PDF Asset Path Repair

## Overview

The completed `Wave 5.1` harmonic-prior residual `TE Curve Verification Pipeline` refresh generated the
dated visual report bundle under
`doc/reports/analysis/track2/*/[2026-06-15]/`. The real styled PDF export did
not render several `Wave 5.1` collage images even though the referenced `PNG`
files exist and are readable from the filesystem.

The observed failure is consistent with Windows-side styled PDF rendering
hitting very long asset paths after the report builder copied `Wave 5.1` images
under verbose auto-generated source-group directories such as
`assets/auto_forward_wave3_harmonic_prior_residual_registry/`. The Linux-based
matrix generation can produce the underlying artifacts successfully, but the
final Windows PDF renderer still has to dereference the local report asset
paths.

## Technical Approach

Keep the fix scoped to the visual report export surface rather than rerunning
the heavy `TE Curve Verification Pipeline` matrix. Patch the visual report builders so automatically
generated source-group asset directories use deterministic compact slugs while
preserving human-readable section labels in the Markdown. Then regenerate the
`[2026-06-15]` collage, overlay, and official styled PDFs through the
repository-owned PDF pipeline.

The expected durable outcome is that future `Wave 5.1` or similarly named
registry-backed source groups keep short PDF asset paths without changing the
scientific comparison content, candidate IDs, metrics, or official decision
logic.

No subagent use is planned for this repair.

## Involved Components

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-06-15]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-15]/`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-15]/`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`

## Implementation Steps

1. Inspect the existing builder path-copy logic and identify where source-group
   names become report-local asset directory names.
2. Add a compact, deterministic asset-directory alias for verbose auto source
   groups while leaving visible Markdown labels and candidate names unchanged.
3. Regenerate the dated `Wave 5.1` visual Markdown bundles for
   `best_model_collage_report` and `multi_model_curve_comparison_report`.
4. Re-export the dated collage, overlay, and official report PDFs with the
   repository-owned styled PDF pipeline.
5. Raster-validate representative PDF pages, including the previously broken
   `Wave 5.1` collage pages, and confirm the images render in the real PDF.
6. Run the required Python compile and Markdown warning checks for the touched
   implementation and authored Markdown scope.
