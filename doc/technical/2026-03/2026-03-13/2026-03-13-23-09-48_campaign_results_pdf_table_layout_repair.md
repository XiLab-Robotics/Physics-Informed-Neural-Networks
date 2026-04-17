# Campaign Results PDF Table Layout Repair

## Overview

The current campaign-results PDF
`doc/reports/campaign_results/mixed_training/2026-03-13-20-54-54_mixed_training_campaign_results_report.pdf`
contains multiple table-layout defects that are visible in the user's review screenshots:

- the `Historical Reference Set` table compresses the `Config` column too aggressively and pushes the rightmost metric headers into an unusable layout;
- the `Phase 1 Results`, `Phase 2 Results`, and `Phase 3 Results` tables repeat the same issue, with metric columns consuming too much width while `Config` wraps badly;
- the `Cross-Campaign Ranking` tables do not overlap, but their width allocation is still poor because `Config` is too narrow and the metric columns are much wider than needed;
- the previous validation step did not catch these issues early enough, which means the current PDF-validation workflow is not strict enough.

The immediate goal is to repair the current PDF layout. The broader goal is to make this class of table-formatting error something that the workflow detects automatically before a report task is considered complete.

## Technical Approach

The fix should stay inside the existing styled-report pipeline so that future campaign reports benefit automatically:

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/mixed_training/2026-03-13-20-54-54_mixed_training_campaign_results_report.md`

### Table Width Rebalancing

The current exporter applies a generic fixed-width table profile to campaign-result tables. That profile is not appropriate for the actual content mix in this report:

- run names in `Config` are significantly longer than metric headers;
- metric values are short numeric strings and do not need wide columns;
- runtime / epoch columns also require less width than currently assigned.

The repair should therefore introduce table-specific width strategies for campaign-results tables. The expected direction is:

1. assign a meaningfully wider first column for `Config`;
2. reduce the width reserved for numeric metric columns;
3. keep metric headers readable without forcing huge empty horizontal space;
4. preserve centered alignment for comparison-heavy numeric columns where it improves scanability;
5. avoid pushing the last header cell into the right border.

### Table-Class Specialization

The exporter already supports specialized table classes for the split configuration matrix in the analysis report. A similar approach should be extended to campaign-results tables so different table families can receive appropriate width maps.

The likely families are:

- historical-reference comparison tables;
- phase-result comparison tables;
- compact ranking tables.

This should avoid trying to force all tables through a single generic width profile.

### Validation Workflow Upgrade

The previous validation was insufficient. It checked the output path and a preview path, but it did not reliably prove that the actual exported PDF tables had acceptable column balance.

The corrected workflow should explicitly require:

1. checking every exported table in the real PDF output, not only the source Markdown or preview HTML;
2. verifying that no table shows crushed identifier columns, oversized metric columns, clipped headers, or right-edge pressure;
3. treating failed or inconclusive PDF raster validation as an incomplete task, not as a successful validation;
4. encoding this stricter rule in the repository instructions so the agent is expected to catch these layout issues without user intervention.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index that must reference this technical note.
- `AGENTS.md`
  Persistent workflow rules that should be updated after approval so future PDF validation is stricter and table-balance issues are caught proactively.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled report exporter that needs the table-layout correction.
- `doc/reports/campaign_results/mixed_training/2026-03-13-20-54-54_mixed_training_campaign_results_report.md`
  Canonical Markdown source of the affected report.
- `doc/reports/campaign_results/mixed_training/2026-03-13-20-54-54_mixed_training_campaign_results_report.pdf`
  Affected PDF artifact to regenerate and validate again.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, inspect the current exporter table-class logic and add specialized width handling for the affected campaign-results tables.
3. Regenerate the HTML preview and PDF for the mixed campaign results report.
4. Validate the regenerated PDF table-by-table, focusing on `Historical Reference Set`, `Phase 1/2/3 Results`, `Best Test MAE`, and `Best Test RMSE`.
5. Update the persistent repository rules so table-balance and true PDF validation failures must be caught before a PDF-report task is closed.
6. Report completion and wait for explicit user approval before creating any Git commit.
