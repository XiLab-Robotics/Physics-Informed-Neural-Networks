# Track 1 MLP Closeout PDF Targeted Pair Outcome Rebalance

## Overview

This technical document covers a narrow PDF-only layout refinement for the
final exact-paper `MLP` family closeout report:
`doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.pdf`.

The requested changes are specific to the rendered PDF layout of the
`Targeted Pair Outcome` section:

- force `Targeted Pair Outcome` onto a new page;
- reduce the width of `Pair`;
- reduce the width of `Campaign Best`;
- enlarge `Baseline`;
- enlarge `Accepted`;
- keep `Baseline`, `Campaign Best`, and `Accepted` at the same width.

The scope is intentionally limited to PDF presentation quality. It must not
change campaign semantics, accepted benchmark values, or Markdown report
content beyond what is strictly necessary to trigger the page break and target
the intended table in the styled exporter.

## Technical Approach

The implementation will reuse the repository-owned styled PDF pipeline already
used for the prior `Track 1` closeout layout repairs.

The work will proceed in two parts:

1. update the report Markdown only if a stable page-break marker is required
   ahead of `Targeted Pair Outcome`;
2. adjust the table-width specialization logic in
   `scripts/reports/generate_styled_report_pdf.py` so the renderer recognizes
   the `Targeted Pair Outcome` header row and applies the requested width
   redistribution.

After the renderer update, the report PDF will be regenerated through the
canonical pipeline and validated on the real exported PDF.

## Involved Components

- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/README.md`

## Implementation Steps

1. Inspect the current `Targeted Pair Outcome` table structure and the existing
   PDF table-width specialization rules.
2. Add the narrowest possible renderer rule for the `Pair | Baseline |
   Campaign Best | Accepted | Source | Result` table.
3. Add or adjust the report-local page-break trigger so `Targeted Pair Outcome`
   starts on a fresh page in the final PDF.
4. Regenerate the PDF through the canonical report pipeline.
5. Validate the real exported PDF and confirm the table now:
   - starts on a new page;
   - uses a narrower `Pair`;
   - uses a narrower `Campaign Best`;
   - gives equal width to `Baseline`, `Campaign Best`, and `Accepted`.
6. Run Markdown QA on every touched repository-authored Markdown file.
