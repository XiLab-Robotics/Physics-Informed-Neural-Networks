# TE Curve Verification Dataset-Surface PDF Export

## Overview

The dataset/surface `TE Curve Verification Pipeline` split reports have been
generated as Markdown report bundles with local visual assets. The remaining
closeout step is to export the generated reports to styled PDFs and validate the
real PDF files through the repository-owned PDF validation workflow.

## Technical Approach

The export will use the existing report PDF pipeline instead of ad hoc browser
commands. Each selected Markdown report will be converted to a same-folder PDF,
then rasterized with the repository PDF validator so layout issues can be
reviewed against real exported pages.

The PDF generator will also be hardened where validation exposes systemic
layout defects: local image paths must resolve independently of the temporary
HTML preview location, and recurring `TE Curve Verification Pipeline` metric
tables must use one balanced column profile instead of narrow per-report table
defaults.

The scope is limited to generated dataset/surface reports and the updated
canonical overview. Intermediate `output/validation_checks` artifacts and
operator logs are not PDF deliverables.

## Involved Components

- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/reports/analysis/te_curve_verification_pipeline/`
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`

## Implementation Steps

1. Resolve the Markdown report set produced by the dataset/surface split run.
2. Export each selected Markdown file to a same-folder styled PDF.
3. Rasterize each exported PDF into validation images under the report pipeline
   temporary validation directory.
4. Inspect representative rendered pages for clipping, table pressure, and
   image-layout regressions.
5. Repair systemic PDF generator issues for asset paths and recurring
   `TE Curve Verification Pipeline` metric table widths.
6. Keep generated PDFs in the report tree and avoid committing temporary
   validation images unless a later review requires them.
