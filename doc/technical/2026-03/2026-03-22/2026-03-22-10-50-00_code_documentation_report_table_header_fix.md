# Code Documentation Report Table Header Fix

## Overview

This document records the fix for a real PDF layout defect in the code-documentation comparison report.

The user identified that two header cells in the `Decision Matrix` table overlapped in the exported PDF.

The task is to correct the source report so the exported PDF no longer shows header collision and then revalidate the real PDF output.

## Technical Approach

The issue is caused by the combination of:

- a wide seven-column comparison table;
- two long adjacent header labels;
- fixed-width PDF table rendering in the repository report exporter.

The most reliable fix is to shorten the conflicting headers in the Markdown source rather than trying to treat the symptom only at the renderer layer.

The planned header adjustments are:

- `Default Visual Quality`
  -> `Visual Quality`
- `Runtime Import Risk`
  -> `Import Risk`

This keeps the meaning clear while reducing horizontal pressure in the table header row.

The report should then be re-exported to PDF and revalidated through the repository-owned PDF raster-validation workflow.

## Involved Components

- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.md`
  Markdown source of the comparison report.
- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.pdf`
  Exported PDF artifact to regenerate and validate.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF exporter.
- `scripts/reports/run_report_pipeline.py`
  Pipeline runner used for PDF validation.

## Implementation Steps

1. Update the Markdown table headers with shorter labels.
2. Re-export the report PDF with the correct subtitle and category.
3. Re-run PDF validation.
4. Inspect the rasterized validation images to confirm that the header overlap is gone.
