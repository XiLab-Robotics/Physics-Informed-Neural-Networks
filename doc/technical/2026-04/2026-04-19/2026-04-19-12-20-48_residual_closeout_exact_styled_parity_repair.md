# Residual Closeout Exact Styled Parity Repair

## Overview

The residual closeout report
`2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report`
does not yet match the visual style of the earlier canonical exact-paper
closeout bundles such as:

- `2026-04-19-00-43-47_track1_remaining_family_cellwise_final_closeout_campaign_results_report`

The user requirement is stricter than merely producing a valid PDF through the
same script entry point. The repaired deliverable must match the established
styled closeout look and layout discipline of the earlier exact-paper campaign
results PDFs.

## Technical Approach

Use the earlier canonical closeout Markdown/PDF pair as the concrete reference
style target and repair the residual closeout package along two axes:

1. align the residual closeout Markdown structure with the section and table
   patterns that the styled PDF renderer already handles well for prior
   exact-paper closeout reports;
2. restore a renderer path inside `generate_styled_report_pdf.py` that keeps
   the report on the real styled export branch rather than a visibly different
   fallback rendering path.

The repair is considered successful only if the regenerated residual closeout
PDF reads as the same report family as the earlier exact-paper closeouts,
including the hero block, section cards, table balance, and overall page
composition.

## Involved Components

- `doc/reports/campaign_results/track1/exact_paper/2026-04-19-00-43-47_track1_remaining_family_cellwise_final_closeout_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-19-00-43-47_track1_remaining_family_cellwise_final_closeout_campaign_results_report.pdf`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.md`
- `doc/reports/campaign_results/track1/exact_paper/2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/technical/2026-04/2026-04-19/README.md`
- `doc/README.md`

## Implementation Steps

1. Compare the residual closeout Markdown structure against the earlier
   canonical exact-paper closeout Markdown and identify the structural
   differences that lead to a different styled PDF layout.
2. Reshape the residual closeout Markdown so its sections and tables follow the
   same styled-report patterns used by the earlier closeout bundle.
3. Repair `generate_styled_report_pdf.py` so the residual report is exported on
   the same styled branch used by the earlier closeout, not on a visibly
   different fallback path.
4. Regenerate the residual closeout PDF through
   `generate_styled_report_pdf.py`.
5. Validate the real PDF with `validate_report_pdf.py` and compare the raster
   output against the earlier canonical closeout for practical style parity.
