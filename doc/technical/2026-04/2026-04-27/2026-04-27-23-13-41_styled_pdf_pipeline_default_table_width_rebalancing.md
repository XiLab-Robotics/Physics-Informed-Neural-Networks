# Styled PDF Pipeline Default Table Width Rebalancing

## Overview

The current styled PDF pipeline still relies too often on report-specific width
patches after the first export. In practice, the first generated PDF often
ships with crushed identifier columns, oversized numeric columns, or
imbalanced summary tables, and only becomes correct after a manual follow-up
rebalance request.

This document formalizes a pipeline improvement so the default renderer
classification in `scripts/reports/generate_styled_report_pdf.py` produces
balanced table widths on the first export for recurring report patterns.

## Technical Approach

The fix should stay inside the repository-owned styled PDF renderer instead of
adding one-off report repairs after export. The implementation should:

1. review the recurring report-table shapes that currently need manual
   intervention;
2. promote those recurring shapes into reusable width profiles with stable
   class mappings;
3. expand the table classification logic so new reports inherit the correct
   layout automatically from header and section context;
4. keep report-specific exceptions only where a fully generic profile would be
   misleading or unsafe.

The intent is to shift from reactive report-by-report fixes toward proactive
first-pass table balancing.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/`
- `site/`

## Implementation Steps

1. inspect the existing table-class registry and the current hard-coded
   report-specific overrides;
2. identify the recurring table families that should map to shared default
   width profiles;
3. refactor the renderer so these profiles are selected automatically from
   header patterns plus section context;
4. regenerate the affected PDF deliverables and validate the real exports;
5. run Markdown QA on touched documentation and a warning-free Sphinx build;
6. keep the manual handoff command unchanged, but reduce the need for
   post-export width fixes.
