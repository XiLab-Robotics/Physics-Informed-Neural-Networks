# Overview

This document defines a follow-up layout refinement for the project-status
report PDF:

- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.pdf`

The previous layout correction correctly moved three sections to dedicated new
pages, but the user now wants one of those page breaks relaxed:

- keep `Why The Work Was Done In This Order` on a dedicated new page;
- remove the forced new page for `Gaps, Risks, And Cleanup Notes`;
- keep `Conclusion` on a dedicated new page.

The user explicitly noted that enough space is now available before
`Gaps, Risks, And Cleanup Notes`, so the forced break is no longer desirable.

## Technical Approach

## 1. Remove Only The One Unnecessary Report-Specific Forced Break

The report exporter currently handles this layout through report-specific forced
page-break section slugs.

For this task, the narrowest safe change is:

- keep the report-specific forced break entries for:
  - `why-the-work-was-done-in-this-order`
  - `conclusion`
- remove the report-specific forced break entry for:
  - `gaps-risks-and-cleanup-notes`

This keeps the change local, reversible, and consistent with the existing
exporter mechanism.

## 2. Preserve Report Content

The requested change is purely presentational.

Therefore:

- section titles must remain unchanged;
- report text must remain unchanged;
- only the page-break behavior should be modified.

## 3. Re-Export And Revalidate The Real PDF

After removing the unnecessary forced break:

1. regenerate the PDF;
2. validate the real exported PDF;
3. confirm that:
   - `Why The Work Was Done In This Order` still starts on a new page;
   - `Gaps, Risks, And Cleanup Notes` no longer starts on a forced new page;
   - `Conclusion` still starts on a new page;
   - no new layout regressions were introduced.

## 4. Planned Subagent Usage

Planned subagent use during implementation:

- none required.

This is a local report-layout adjustment and can be completed directly.

## Involved Components

- `README.md`
- `doc/technical/2026-03-27/2026-03-27-19-13-28_project_status_report_remove_gap_section_forced_page_break.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before modifying the exporter behavior again.
3. Remove the report-specific forced break for `gaps-risks-and-cleanup-notes`.
4. Re-export the project-status PDF.
5. Revalidate the real exported PDF and confirm the final page-flow behavior.
6. Run Markdown QA on the touched Markdown files and confirm normal final-newline state.
