# Track 1 Open-Cell Closeout PDF Table Layout Micro Rebalance

## Overview

This technical document defines a narrow PDF-layout correction for the final
`Track 1` open-cell full-matrix closeout report:

- source Markdown:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report.md`
- target PDF:
  `doc/reports/campaign_results/track1/exact_paper/2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report.pdf`

The user requested a report-PDF-only table rebalance with these exact goals:

1. in `Family Representative Outcome`, tighten `Family` and `Scope`;
2. in the same table, widen `Best Run`;
3. wrap `Score` onto a second line inside `Closure Score`;
4. make `Met`, `Near`, and `Open` use the same width;
5. in `Canonical Benchmark Outcome`, make all four columns share the same
   width.

The intent is to preserve the report content and only improve the final PDF
table readability.

## Technical Approach

The repository already contains report-specific table-width logic inside
`scripts/reports/generate_styled_report_pdf.py`. This task will adjust that
exporter logic for the exact normalized header patterns used by the two target
tables in the closeout report.

The implementation will:

1. inspect the current report-specific width-distribution rules used by the
   styled PDF exporter for similar campaign-results tables;
2. add or adjust the narrow layout branch that matches:
   - `Family | Best Run | Scope | Closure Score | Met | Near | Open`
   - `Surface | Harmonics Met | Total Harmonics | Open Harmonics`
3. keep the source Markdown report semantically unchanged unless a tiny header
   formatting adjustment is strictly necessary for the requested line break;
4. regenerate the target PDF with the repository-owned export pipeline;
5. validate the real exported PDF with the repository-owned rasterization
   validator before considering the task complete.

The change will stay local to this report-export workflow and will not alter
scientific results, campaign bookkeeping, or benchmark semantics.

## Involved Components

- `doc/reports/campaign_results/track1/exact_paper/2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/technical/2026-04/2026-04-21/README.md`
- `doc/README.md`

## Implementation Steps

1. Register this micro-fix document in the technical indices.
2. Update the styled PDF exporter rules for the two target tables.
3. Regenerate the final closeout PDF from the canonical Markdown report.
4. Validate the regenerated PDF through the repository PDF validator.
5. Run Markdown QA on the touched authored Markdown files.
6. Report the resulting PDF fix and validation outcome before any commit.
