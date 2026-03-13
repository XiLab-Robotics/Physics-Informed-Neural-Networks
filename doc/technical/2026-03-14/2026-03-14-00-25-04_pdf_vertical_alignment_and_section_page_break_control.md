# PDF Vertical Alignment And Section Page-Break Control

## Overview

The latest campaign-results PDF table refinement solved the remaining width and semantic-wrap issues, but two presentation defects are still visible:

- table cells are not consistently centered vertically, especially when one row contains both single-line and multi-line cells;
- some major sections such as `Phase 2 Results` and `Cross-Campaign Ranking` can start near the bottom of a page, print one short fragment, and then continue on the next page.

The user requested a stronger layout rule:

- keep the current horizontal alignments;
- center all table-cell content vertically inside the cell;
- when a major section would begin too low on a page and immediately continue on the next page, move the whole section start to the next page instead.

The goal of this pass is to enforce cleaner vertical alignment in tables and more disciplined section-level page breaks in the styled campaign PDF.

## Technical Approach

The correction should remain inside the existing styled PDF exporter:

- `scripts/reports/generate_styled_report_pdf.py`

### Vertical Table Alignment

The current table base style still uses `vertical-align: top` on generic body cells, while only some specialized table classes override parts of that behavior.

This should be normalized so that:

1. all result-table cells are vertically centered by default;
2. multi-line identifier cells and single-line metric cells share the same visual center line;
3. the chosen horizontal alignment remains unchanged.

The fix should be applied at the main table-cell CSS level so future campaign tables inherit the correct behavior automatically.

### Section Page-Break Control

The current section card style still allows internal page breaks in many cases because the section container is configured too permissively.

For sections such as:

- `Phase 2 Results`
- `Cross-Campaign Ranking`

the desired behavior is:

1. if the section fits cleanly on the next page, start it on the next page instead of leaving a short orphaned fragment at the bottom of the current one;
2. avoid printing the section title and one short paragraph on one page while the main table or body continues on the next;
3. preserve normal flow for sections that are genuinely too tall to fit on one page.

This likely requires a stronger combination of:

- `break-inside: avoid-page` on section-level cards when feasible;
- page-break protection for section headers and the first content block;
- selective avoidance rather than globally forcing every long section onto a new page.

### Persistent Rule Update

The repository rules should be tightened so future styled PDF validation explicitly checks:

- vertical centering inside table cells;
- section-start orphaning near the bottom of a page;
- whether major analytical/result sections should have been moved to the next page.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index that must reference this technical note.
- `AGENTS.md`
  Persistent repository instructions that should be updated after approval.
- `doc/guide/project_usage_guide.md`
  Usage guidance that should reflect the stricter vertical-alignment and page-break checks after approval.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF exporter that needs the alignment and page-break refinement.
- `doc/reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.pdf`
  The target PDF artifact to regenerate and validate again.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, normalize vertical centering for table cells in the styled PDF exporter.
3. Strengthen section-level page-break handling so section starts such as `Phase 2 Results` and `Cross-Campaign Ranking` do not get stranded across two pages.
4. Regenerate the mixed campaign HTML preview and PDF.
5. Validate the real exported PDF again, explicitly checking vertical centering and section-start page flow.
6. Update the persistent repository rules so future styled PDF reviews must catch these issues before task closure.
