# Track 2 Official Model Verification Report

## Overview

Create a serious official `Track 2` verification report that becomes the
canonical review surface for newly trained TE models.

The report will consolidate the current numerical comparison matrix, visual
model-collage verification, multi-model curve-overlay verification, and future
`Track 2` campaign results into one maintained report package. The first
version will explicitly combine these existing deliverables:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.pdf`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.pdf`

The official report should answer whether each newly introduced model family is
actually competitive against the accepted reference surfaces, not only whether
its training metrics look good in isolation.

No subagent use is planned for this task.

## Technical Approach

Add a new canonical report bundle under the `Track 2` analysis topic instead of
overloading either visual companion report. The proposed target is:

- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/track2_official_model_verification_report.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/track2_official_model_verification_report.pdf`

The report will treat `Track 2 Directional Model Comparison.md` as the primary
metric matrix and the two `[2026-05-20]` visual reports as companion evidence.
It will also include a maintained campaign-results ledger so future `Track 2`
campaigns can append:

- campaign result report path;
- affected model family and direction surface;
- promoted or rejected candidate;
- comparison baseline used;
- key Track 2 metrics;
- visual verification artifact paths;
- final decision and follow-up action.

The first implementation should be documentation-first and script-assisted. If
the existing report builders already expose enough machine-readable outputs,
the official report can be assembled from their Markdown, CSV, YAML, and PDF
artifacts. If not, add a narrow repository-owned builder script that reads
those existing artifacts and writes the official Markdown reproducibly.

The official PDF must be exported and validated through the repository PDF
pipeline, with the real PDF checked for table fit, image rendering, page
breaks, and right-edge pressure.

## Involved Components

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.md`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.pdf`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.md`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.pdf`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/README.md`
- `scripts/reports/analysis/`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `output/validation_checks/track2_best_model_collage_report/`
- `output/validation_checks/track2_multi_model_curve_comparison_report/`
- future `doc/reports/campaign_results/track2/` reports, when `Track 2`
  campaigns are introduced.

## Implementation Steps

1. Inspect the current `Track 2` directional matrix, best-model collage report,
   multi-model curve comparison report, and their validation-check outputs.
2. Define the official report structure:
   - executive verdict;
   - baseline and direction rule;
   - pipeline-by-pipeline result summary;
   - current best reference and current best repository-owned candidates;
   - visual-verification evidence from the collage and overlay PDFs;
   - campaign-results ledger for future `Track 2` updates;
   - closeout decision and next operational branch.
3. Create the new official report bundle under
   `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/`.
4. Add or reuse a repository-owned report builder if reproducible regeneration
   cannot be done cleanly from the existing Markdown and machine-readable
   artifacts.
5. Export the official report to PDF with the styled PDF pipeline.
6. Validate the real PDF, including embedded images, table fit, clipped
   content, page starts, and right-edge pressure.
7. Register the new official report in `doc/README.md`.
8. Update `doc/running/te_model_live_backlog.md` so `Track 2` points to the new
   official verification report as the accepted closeout surface.
9. Update `doc/reports/analysis/Training Results Master Summary.md` if the new
   official verdict changes the summarized current best model status or the
   interpretation of campaign outcomes.
10. Run scoped Markdown QA on touched Markdown files and Sphinx/PDF validation
    if the final approved changes affect the documentation portal scope.
