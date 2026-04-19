# Styled PDF Persistent Preview Cleanup Fix

## Overview

The current styled PDF exporter behaves differently depending on whether
`--keep-html` is used.

When `--keep-html` is enabled, the generated preview HTML is written next to the
target PDF and Chrome headless can access it correctly.

When `--keep-html` is not enabled, the exporter writes the preview HTML into a
temporary `.temp/report_pipeline/...` directory. In the current environment,
that branch can lead Chrome headless to print an `ERR_FILE_NOT_FOUND` page into
the PDF even though the report generation itself succeeded.

The fix should keep the original styled export pipeline intact while removing
the fragile temporary-preview location from the default path.

## Technical Approach

Change the preview-HTML path policy in
`scripts/reports/generate_styled_report_pdf.py` so that the generated preview
HTML is always written next to the output PDF, using the same stable
`*_preview.html` location currently used by `--keep-html`.

The difference between the two modes should then become only a cleanup policy:

- when `--keep-html` is enabled, keep the generated preview HTML;
- when `--keep-html` is not enabled, delete the same preview HTML after the PDF
  export finishes successfully or after the run exits.

This preserves the original Chrome-headless styled rendering path while
avoiding the inaccessible temporary-file location that currently causes the
blank error PDF.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.md`
- `doc/technical/2026-04/2026-04-19/README.md`
- `doc/README.md`

## Implementation Steps

1. Update `resolve_output_html_path()` so the default preview location is the
   persistent sibling `*_preview.html` path next to the output PDF instead of a
   temporary `.temp/report_pipeline/...` directory.
2. Keep `--output-html-path` behavior unchanged so explicit caller-provided HTML
   targets still work as before.
3. Keep `--keep-html` behavior semantically unchanged, but implement it only as
   a decision to skip deletion of the sibling preview HTML.
4. Update the cleanup branch in `main()` so the preview HTML is deleted only
   when `--keep-html` is not requested.
5. Re-run the styled PDF export manually on the residual closeout report to
   verify that the Chrome-headless path produces the real styled PDF without
   requiring `--keep-html`.
6. Run Markdown warning checks on the touched Markdown scope and confirm normal
   single-final-newline state before closing the task.
