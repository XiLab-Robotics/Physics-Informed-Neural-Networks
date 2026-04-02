# Overview

This document defines a targeted PDF-layout correction for the project-status
report:

- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.pdf`

The current exported PDF is readable, but three major sections should start on
their own new page instead of continuing in the current flow:

- `Why The Work Was Done In This Order`
- `Gaps, Risks, And Cleanup Notes`
- `Conclusion`

The goal is to improve presentation quality and section emphasis without
rewriting the substance of the report.

## Technical Approach

## 1. Apply A Targeted Markdown-Level Page-Break Correction

The repository already owns a styled PDF exporter with section-aware page-break
support.

For this task, the safest approach is to modify only the report Markdown so the
three requested sections are emitted in a way that the styled exporter treats as
new-page starts.

This keeps the correction local to the report artifact and avoids broad changes
to the exporter rules that could affect other reports unintentionally.

## 2. Preserve Report Content Exactly Unless Layout Requires Minor Structural Help

The requested change is presentational.

Therefore:

- section titles should remain the same;
- section content should remain the same;
- only the section boundary behavior should change unless a small local layout
  helper is needed to keep the page flow clean.

## 3. Re-Export And Revalidate The Real PDF

After the Markdown correction:

1. regenerate the PDF;
2. validate the real exported PDF through the repository report pipeline;
3. confirm that the three target sections now begin on their own page and that
   no new clipping, table-fit, or page-break regressions were introduced.

## 4. Planned Subagent Usage

Planned subagent use during implementation:

- none required.

This is a local report-layout adjustment and can be completed directly.

## Involved Components

- `README.md`
- `doc/technical/2026-03/2026-03-27/2026-03-27-19-05-09_project_status_report_pdf_section_page_break_adjustment.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.pdf`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before modifying the report.
3. Add the minimal page-break control needed for the three requested sections.
4. Re-export the styled PDF.
5. Revalidate the real exported PDF.
6. Run Markdown QA on the touched Markdown files and confirm normal final-newline state.
