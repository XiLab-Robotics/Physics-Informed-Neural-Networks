# Wave 3.1 Closeout PDF Refinement And Skill Rule

## Overview

This technical document plans the refinement of the generated `Wave 3.1`
campaign closeout PDF and the repository-local skill update requested after
the closeout report was produced.

The immediate PDF correction is to start the `Execution Summary` section on a
fresh page in the `Wave 3.1` campaign results PDF. The broader workflow
correction is to make campaign closeout automatically include real PDF layout
review and repair after generation, instead of treating PDF export as done when
the file exists.

## Technical Approach

The PDF change will be implemented in the repository-owned styled PDF exporter
so the `Wave 3.1` closeout report receives a section page break before
`Execution Summary`. The report will then be re-exported and raster-validated.

The skill change will update the repository-local `campaign-architect` skill
because that skill owns the campaign closeout workflow. The updated skill will
state that every campaign closeout that generates a PDF must:

- run the styled PDF export;
- raster-validate the real PDF;
- visually inspect representative rendered pages;
- repair table widths, section page starts, clipping, wrapping, and spacing
  before finalizing;
- use the `styled-report-pdf-qa` skill when PDF layout or validation is part
  of the closeout.

This does not change campaign results or training artifacts.

## Involved Components

- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.pdf`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `.codex/skills/campaign-architect/SKILL.md`
- `.codex/skills/styled-report-pdf-qa/SKILL.md`
- `doc/README.md`

## Implementation Steps

1. Add a report-specific page break rule before `Execution Summary` for the
   `Wave 3.1` closeout report in the styled PDF exporter.
2. Update the `campaign-architect` skill so campaign closeout always includes
   post-export PDF layout review and repair when a PDF is produced.
3. Re-export the `Wave 3.1` campaign results PDF.
4. Raster-validate the exported PDF and visually inspect the rendered pages.
5. Run Markdown QA on touched authored Markdown files.
6. Compile the touched Python exporter.
7. Report the PDF path, validation status, and the new closeout-skill rule.
