# Track 2 Forward Reference Curve Comparison Report

## Overview

This technical document plans a dedicated non-training `Track 2` report that
compares the forward curve collages and numerical curve differences for these
five already available forward candidates:

- `paper_original_best_Fw`
- `paper_retuned_best_Fw`
- `paper_original_best_Fw_original_onnx_release`
- `rcim_original_simplified_onnx_Fw`
- `rcim_original_plc_hgbm_onnx_Fw`

The requested report will collect the same representative collage style used
by the historical best-model report and the original `ONNX` collage report,
then add a cross-model verification similar to the previous chat-level
diagnostic: aggregate Track 2 metrics, pairwise point-by-point predicted-curve
differences, and representative-collage curve differences.

The work will not train models and will not run the full heavy Track 2 matrix.
It will reuse the existing candidate outputs where available and regenerate
only the lightweight forward curve payloads needed for direct model-to-model
curve comparison.

## Technical Approach

The report will use `paper_original_best_Fw` as the main parity anchor because
the prior diagnostic showed that the recovered original `ONNX` release is
nearly identical to this repository paper-original candidate at reconstructed
curve level. The comparison will then quantify how far the retuned and sparse
variants move away from that anchor and whether the visual differences visible
in the collages match the aggregate metrics.

The implementation will create a focused report builder under
`scripts/reports/analysis/`. The builder will:

1. Load or regenerate the five candidate prediction payloads on the canonical
   forward held-out `Track 2` curves.
2. Copy or regenerate deterministic collage images for every candidate into a
   single dated report bundle.
3. Compute per-candidate aggregate metrics over the same forward curve set.
4. Compute pairwise predicted-curve differences for all candidate pairs using
   common curve identities and aligned angle grids.
5. Compute a smaller table for the representative four collage curves.
6. Write a Markdown report and export it to a styled PDF with the repository PDF
   pipeline.

The pairwise curve-difference table will include at least:

- mean curve-difference `MAE [deg]`;
- `P95` curve-difference `[deg]`;
- max curve-difference `[deg]`;
- global difference `RMSE [deg]`;
- mean Pearson correlation.

The representative-curve table will include the per-candidate `MAE` against the
measured curve and compact pairwise deltas from the selected anchor candidates.
If table width becomes tight in PDF, the builder will apply the established
table-layout rule: narrow identifier columns only where safe, wrap units onto
second header lines, and keep metric columns balanced.

## Involved Components

- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-28]/`:
  historical `paper_original_best_Fw` and `paper_retuned_best_Fw` collage
  source.
- `doc/reports/analysis/track2/original_onnx_fw_collage_report/[2026-06-05]/`:
  historical full original `ONNX` forward collage source.
- `doc/reports/analysis/track2/sparse_original_onnx_variants/[2026-06-08]/`:
  sparse simplified and PLC-oriented original `ONNX` collage source.
- `output/validation_checks/track2_best_model_collage_report/`:
  existing best-model collage report output root.
- `output/validation_checks/track2_original_onnx_fw_collage_report/`:
  existing original `ONNX` report output root.
- `output/validation_checks/track2_sparse_original_onnx_variants/`:
  existing sparse original `ONNX` report output root.
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`:
  source pattern for the historical best-model collage report.
- `scripts/reports/analysis/build_track2_original_onnx_fw_collage_report.py`:
  source pattern for the full original `ONNX` collage report.
- `scripts/reports/analysis/build_track2_sparse_original_onnx_variants_report.py`:
  source pattern for the sparse original `ONNX` report.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`:
  candidate loading, curve reconstruction, and report-support code.
- `scripts/reports/pdf/run_report_pipeline.py`:
  styled PDF export and validation entry point.

## Implementation Steps

1. Inspect the existing three report builders and the output bundle schemas for
   the five requested candidates.
2. Add a dedicated builder for the combined forward-reference curve comparison
   report under `scripts/reports/analysis/`.
3. Reuse existing images where they are exact matches; regenerate only missing
   deterministic collage assets if required.
4. Compute aggregate candidate metrics and all pairwise curve-difference
   metrics over the common forward curve set.
5. Generate a dated Markdown report and companion assets under
   `doc/reports/analysis/track2/forward_reference_curve_comparison/[2026-06-08]/`.
6. Export and validate the real PDF, including visual checks for table width,
   wrapped metric headers, image fit, and page breaks.
7. Register the report and script in the appropriate documentation indexes if
   new user-facing report tooling is added.
8. Run Python compilation, scoped Markdown QA, PDF pipeline validation, and
   Sphinx `-W` if Sphinx documentation is touched.

No subagent is planned for this implementation.
