# RCIM Model-Bank Reproduction Extended Campaign Results PDF Layout Alignment

## Overview

This technical document defines the PDF-layout repair needed for the extended
`RCIM Model-Bank Reproduction` overnight campaign results report.

The first export of
`2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report.md`
showed that the renderer did not apply the campaign-specific table profile that
had already been promoted for the smaller overnight `RCIM Model-Bank Reproduction` report. As a
result, the second table header remained too narrow and visually truncated in
the exported PDF.

## Technical Approach

The repair should reuse the existing `RCIM Model-Bank Reproduction` campaign-results table classes
instead of inventing another one-off layout.

The work should:

1. extend the report-specific page-break and table-class routing so the
   extended campaign report resolves to the same `RCIM Model-Bank Reproduction` table profiles;
2. generalize the wrapped `Delta Vs ... Baseline` header handling so it works
   for the new baseline value `8.774%`;
3. rerender the PDF and validate the real exported pages again.

No Codex subagent is planned for this repair.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/campaign_results/track_1/harmonic_wise/forward/2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report.md`
- `doc/reports/campaign_results/track_1/harmonic_wise/forward/2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report.pdf`
- `.temp/report_pipeline/pdf_validation/2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report/`

## Implementation Steps

1. Extend the renderer routing for the extended `RCIM Model-Bank Reproduction` campaign report stem.
2. Reuse the existing `RCIM Model-Bank Reproduction` table-width classes for all three tables in the
   report.
3. Generalize the wrapped baseline-delta header formatter for both known
   baselines.
4. Re-export the PDF and revalidate the rasterized pages before closing the
   campaign closeout task.
