# Overview

This document defines the next targeted layout refinement for the project-status
report PDF:

- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.pdf`

The user wants the page-break emphasis moved from `Conclusion` to
`High-Level Future Roadmap`.

Desired final layout behavior:

- keep `Why The Work Was Done In This Order` on a dedicated new page;
- do not force `Gaps, Risks, And Cleanup Notes` onto a new page;
- force `High-Level Future Roadmap` to start on a new page;
- do not force `Conclusion` onto a new page.

## Technical Approach

## 1. Change Only The Report-Specific Forced-Break Slug Set

The report exporter already handles this layout through the
`REPORT_SPECIFIC_FORCED_PAGE_BREAK_SECTION_SLUGS` mapping.

For this task, the narrowest safe change is:

- keep `why-the-work-was-done-in-this-order`;
- add `high-level-future-roadmap`;
- remove `conclusion`.

This keeps the correction local to the project-status report and avoids broad
layout side effects for other reports.

## 2. Preserve Report Content

The requested change is purely presentational.

Therefore:

- report headings stay unchanged;
- report content stays unchanged;
- only the section start behavior changes.

## 3. Re-Export And Revalidate The Real PDF

After the report-specific forced-break list is updated:

1. regenerate the PDF;
2. validate the real exported PDF;
3. confirm that:
   - `Why The Work Was Done In This Order` still starts on a new page;
   - `High-Level Future Roadmap` now starts on a new page;
   - `Conclusion` no longer starts on a forced new page;
   - no new layout regressions were introduced.

## 4. Planned Subagent Usage

Planned subagent use during implementation:

- none required.

This is a local report-layout adjustment and can be completed directly.

## Involved Components

- `README.md`
- `doc/technical/2026-03-27/2026-03-27-19-20-37_project_status_report_move_forced_page_break_from_conclusion_to_roadmap.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before changing the report-specific page-break behavior.
3. Move the forced new-page behavior from `conclusion` to `high-level-future-roadmap`.
4. Re-export the project-status PDF.
5. Revalidate the real exported PDF and confirm the final page-flow behavior.
6. Run Markdown QA on the touched Markdown files and confirm normal final-newline state.
