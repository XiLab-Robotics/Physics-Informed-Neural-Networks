# PDF Metric Header Unit Wrapping Rule

## Overview

This document proposes a repository-wide PDF layout rule derived from repeated
campaign-report refinement requests.

The recurring pattern is consistent:

- narrow metric columns should not keep long headers on one line;
- unit labels such as `[deg]`, `[rpm]`, or similar compact measurement suffixes
  should wrap onto a second line when the column is width-constrained;
- the preferred tradeoff is cleaner header wrapping over overly compressed
  numeric columns or visually crowded table headers.

The immediate trigger is the refinement of:

- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.pdf`

## Technical Approach

The rule should be made explicit in repository policy so future styled PDF work
uses the same layout preference by default.

The intended policy statement is:

- when a styled PDF table contains narrow metric columns whose headers include a
  measurement unit, prefer rendering the metric name on the first line and the
  unit label on a second line inside the same header cell

This should become a default PDF-table balancing rule, not an isolated
one-report exception.

## Involved Components

- `AGENTS.md`
- `scripts/reports/generate_styled_report_pdf.py`
- future repository-owned styled PDF reports under `doc/reports/`

## Implementation Steps

1. add an explicit repository rule in `AGENTS.md`
2. keep the rule scoped to styled PDF tables and narrow metric headers
3. preserve the requirement that the full header must remain inside its own
   cell and must never visually spill into the neighboring column
4. continue validating the real exported PDF after applying the rule in future
   reports
