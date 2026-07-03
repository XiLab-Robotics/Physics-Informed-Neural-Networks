# Polished-Dataset TE Curve Verification Pipeline Refresh Plan

## Overview

This plan prepares the official `TE Curve Verification Pipeline` refresh for
the completed polished-dataset retraining closeouts. It does not execute the
heavy matrix. The prepared launcher will be run by the operator after this
package is validated.

## Scope

The refresh covers:

- polished `RCIM Model-Bank Reproduction` forward and backward model-bank
  exports;
- polished model-development registry candidates across the `global`, `Fw`,
  and `Bw` surfaces;
- the canonical matrix report, best-model collage report, multi-model curve
  comparison report, official verification report, and matching PDF exports.

## Candidate Sources

| Source label | Candidate scope | Expected count |
| --- | --- | ---: |
| `polished_rcim_model_bank_reproduction` | RCIM model-bank families over `Fw` and `Bw` | 20 |
| `polished_model_development_registry` | 36 model-development families over `global`, `Fw`, and `Bw` | 108 |

The final matrix also retains the existing historical reference and previous
registry-backed comparison sources.

## Execution Plan

1. Generate RCIM-compatible `reference_inventory.yaml` files from the polished
   RCIM `validation_summary.yaml` exports.
2. Run the full direction-aware matrix with output suffix
   `polished_dataset_te_curve_verification_refresh_2026_07_02`.
3. Regenerate the best-model collage report for report date `2026-07-02`.
4. Regenerate the multi-model curve-comparison report for report date
   `2026-07-02`.
5. Validate visual source coverage for the polished registry source.
6. Build the official model-verification report from the matrix, collage, and
   overlay summaries.
7. Export the three reports to PDF through the repository PDF pipeline.

## Launch Commands

Local:

```powershell
.\scripts\campaigns\track_2\run_polished_dataset_track2_verification_refresh.ps1
```

Remote:

```powershell
.\scripts\campaigns\track_2\run_polished_dataset_track2_verification_refresh.ps1 -Remote
```

## Completion Criteria

- The matrix run exits with code `0`.
- The canonical matrix report includes the polished source sections.
- The collage, overlay, and official report Markdown files exist under dated
  `[2026-07-02]` folders.
- The PDF pipeline exports and validates the three real PDFs.
- Codex performs post-run closeout only after the operator reports completion.
