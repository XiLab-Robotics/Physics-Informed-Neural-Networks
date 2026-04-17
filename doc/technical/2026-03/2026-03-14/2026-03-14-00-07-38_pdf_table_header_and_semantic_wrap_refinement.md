# PDF Table Header And Semantic Wrap Refinement

## Overview

The latest repaired campaign-results PDF improved the overall table balance, but the user identified two remaining formatting defects that still violate the intended report quality:

- in the `Historical Reference Set` table, the `Approx. Wall Time` header visually spills into the following column instead of staying cleanly inside its own cell;
- in the `Phase 3 Results` table, long `Config` values wrap at arbitrary character boundaries, producing endings such as isolated `l` or very short trailing fragments instead of semantically meaningful line breaks such as `big_model`.

The user also requested a stronger persistent layout rule for future table generation:

- aim for broadly balanced column widths across the table;
- if one column needs more room, enlarge it and redistribute the reduction across the other columns without over-compressing them;
- allow wrapping when necessary, but do it without border pressure, overflow, or visually broken word fragments;
- never allow text to escape its own cell or overlap adjacent columns.

The goal of this pass is therefore to eliminate the remaining header spill and introduce more semantic, readable wrapping behavior for long identifier cells.

## Technical Approach

The correction should remain inside the existing styled PDF exporter so the same improvement applies to future campaign reports automatically:

- `scripts/reports/generate_styled_report_pdf.py`

### Header Containment Rule

The current table styles still favor `white-space: nowrap` in header cells. That is acceptable only while the chosen width profile guarantees containment.

For headers such as `Approx. Wall Time`, the exporter should instead:

1. keep the text fully inside its own header cell;
2. prefer a clean internal wrap over visual spill into the next column;
3. avoid squeezed padding that makes the header look too close to cell borders.

This likely requires:

- enabling controlled wrapping for the affected header families;
- slightly rebalancing the historical-reference width profile;
- keeping the line break visually centered and readable.

### Semantic Identifier Wrapping

The `Config` column currently relies on generic character-level wrapping, which is acceptable for safety but produces poor results for snake-case identifiers.

The refined behavior should:

1. avoid arbitrary one- or two-letter trailing fragments;
2. prefer breaks at semantic delimiters such as underscores;
3. keep meaningful units together where possible, for example `big_model`;
4. preserve containment inside the cell without forcing the text against the borders.

The likely implementation direction is to render identifier-like inline code with semantic break opportunities rather than pure character splitting.

### Column Balancing Rule

The new persistent table-balancing rule should be encoded explicitly:

- start from reasonably even column widths;
- let obviously longer content columns grow somewhat;
- shrink obviously short numeric columns somewhat;
- rebalance uniformly rather than collapsing one column too aggressively;
- still permit multi-line cells when needed;
- never accept border pressure, cross-cell spill, or near-overlap with cell edges.

This rule should become part of the future PDF validation expectation, not just a one-off fix.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index that must reference this technical note.
- `AGENTS.md`
  Persistent repository rules that should be updated after approval with the stronger column-balancing and semantic-wrap expectation.
- `doc/guide/project_usage_guide.md`
  Usage guidance that should reflect the stricter table-validation criteria after approval.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF exporter that needs the final table-layout refinement.
- `doc/reports/campaign_results/mixed_training/2026-03-13-20-54-54_mixed_training_campaign_results_report.pdf`
  The PDF artifact to regenerate and validate again.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, refine the historical-reference table so long headers wrap inside their own cells instead of visually crossing column boundaries.
3. Refine `Config` rendering so long identifiers wrap at semantically meaningful boundaries instead of arbitrary short fragments.
4. Rebalance the affected campaign-results table width profiles according to the new column-balancing rule.
5. Regenerate the mixed campaign HTML preview and PDF.
6. Validate the real exported PDF again, explicitly checking header containment, semantic wrapping quality, border clearance, and absence of cross-cell spill.
7. Update the persistent repository rules so future table reviews must catch these issues before task closure.
