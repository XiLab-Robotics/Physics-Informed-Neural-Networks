# Wave1 Recovery Campaign PDF Layout Refinement

## Overview

The current styled PDF export
`doc/reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.pdf`
still contains a set of user-identified layout defects that should be corrected
without changing the analytical content of the report.

The requested corrections are:

- start `Recovery Campaign Ranking` on a new page;
- in `Test-Side Ranking`, widen `Config`, shrink `Rank` and `Family`, widen
  `Test MAE [deg]`, and slightly shrink `Test RMSE [deg]`;
- in `Validation-Side Snapshot`, widen `Config` substantially and shrink
  `Val MAE [deg]`;
- start `Campaign Winner` on a new page;
- in the `Residual Harmonic MLP` table, widen `Config` and shrink
  `Val MAE [deg]`;
- in the `Harmonic Regression` table, widen `Config` and shrink
  `Val MAE [deg]`;
- start `Main Conclusions` on a new page.

The goal of this pass is to regenerate the existing campaign-results PDF with a
cleaner page flow and better column balance while preserving the repository
golden-standard styling and the current report text.

## Technical Approach

The correction should remain inside the existing repository-owned reporting
pipeline:

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md`

### Section-Level Page Break Control

The report already supports explicit page-break styling. That mechanism should
be applied selectively to the three affected major sections:

- `Recovery Campaign Ranking`
- `Campaign Winner`
- `Main Conclusions`

The expected behavior is:

1. each of those sections starts at the top of a fresh PDF page;
2. only the requested sections are forced to a new page;
3. the surrounding report flow remains unchanged.

This can be implemented either by inserting explicit section markers in the
Markdown source or by extending the exporter so these specific headings are
mapped to the existing page-break class during HTML generation.

### Table Width Rebalancing

The affected tables should receive more targeted column-width allocation instead
of relying on one broad profile.

The intended rebalancing is:

1. `Test-Side Ranking`
   - expand `Config`;
   - reduce `Rank`;
   - reduce `Family`;
   - expand `Test MAE [deg]`;
   - slightly reduce `Test RMSE [deg]`.
2. `Validation-Side Snapshot`
   - expand `Config` significantly;
   - reduce `Val MAE [deg]`.
3. `Residual Harmonic MLP`
   - expand `Config`;
   - reduce `Val MAE [deg]`.
4. `Harmonic Regression`
   - expand `Config`;
   - reduce `Val MAE [deg]`.

The implementation should favor table-specific width maps so the fix remains
precise and does not accidentally degrade other existing report layouts.

### Validation Expectation

After approval and implementation, the regenerated PDF must be checked on the
real exported file, not only on the Markdown or preview HTML.

The validation pass should explicitly confirm:

- each requested section truly starts on a fresh page;
- `Config` columns are no longer visually crushed in the affected tables;
- the narrowed columns remain readable and keep headers inside their own cells;
- the right edge stays balanced without clipped borders or overcrowded numeric
  columns.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index that should reference this technical note.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF exporter that controls heading page breaks and table width maps.
- `scripts/reports/run_report_pipeline.py`
  Existing orchestration entry point to regenerate and validate the report.
- `doc/reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md`
  Canonical Markdown source of the affected report.
- `doc/reports/campaign_results/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.pdf`
  Target PDF artifact to regenerate and validate again.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. Wait for explicit user approval before changing the exporter or report
   source.
3. After approval, add selective page-break handling for
   `Recovery Campaign Ranking`, `Campaign Winner`, and `Main Conclusions`.
4. Rebalance the affected table width profiles so the requested `Config` and
   metric columns have cleaner proportions.
5. Regenerate the Wave 1 recovery campaign HTML preview and PDF through the
   existing report pipeline.
6. Validate the real exported PDF page by page against the requested layout
   changes and the repository PDF golden standard.
7. Report completion and wait for explicit user approval before creating any
   Git commit.
