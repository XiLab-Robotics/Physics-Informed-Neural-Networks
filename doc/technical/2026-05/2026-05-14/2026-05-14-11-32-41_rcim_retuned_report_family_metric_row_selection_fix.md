# RCIM Retuned Report Family Metric Row Selection Fix

## Overview

The recovered-original RCIM retuned closeout report and the canonical `RCIM Paper
Reference Benchmark` currently build the `Paper Retuned` Tables `2`-`5` from the
accepted eval-stage `summaryCrossValidation+_3.8_allFreq.csv` artifacts.

Inspection of the forward retuned archives showed that some accepted eval
summary files contain multiple family rows because several families shared one
source bundle or inherited appended legacy summary files. The closeout reader
currently consumes the first CSV row only. This can assign the wrong metrics to
families such as `RF`, `ERT`, `GBM`, `HGBM`, and `XGBM`.

The model artifacts themselves are not the first suspected failure point: the
archive inventories still expose the expected ONNX and Python pickle counts.
The immediate issue is report metric extraction.

## Technical Approach

Update the closeout/report metric reader so it selects the row whose `0_method`
matches the requested family code instead of blindly reading the first row.
Keep a strict failure mode when the requested family is absent, because a silent
fallback would corrupt benchmark tables again.

After the reader fix, regenerate the retuned closeout Markdown/PDF and the
canonical benchmark tables from the existing accepted artifacts only. No retune,
eval, export, model regeneration, or campaign-state mutation is planned.

## Involved Components

- `scripts/reports/closeout/closeout_rcim_retuned_reference_archive.py`
- `doc/reports/analysis/rcim_retuned_reference_closeout/[2026-05-13]/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `doc/README.md`

## Implementation Steps

1. Modify the closeout metric reader to accept the expected family code from the
   `SourceSelection` record and select the matching `0_method` row.
2. Add a small diagnostic guard that reports the available family rows when the
   requested family row is missing.
3. Regenerate the retuned closeout Markdown report and the canonical benchmark
   tables from the archived source runs.
4. Regenerate the styled closeout PDF and validate the real PDF output.
5. Run Markdown QA on the touched Markdown files.
6. Review the corrected forward `Paper Retuned` Tables `2`-`5`, with specific
   attention to previously duplicated rows such as `MLP`/`XGBM`, `ET`/`ERT`,
   and `GBM`/`HGBM`.

No subagent use is planned.
