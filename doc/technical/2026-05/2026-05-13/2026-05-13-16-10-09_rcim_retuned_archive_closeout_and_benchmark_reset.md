# RCIM Retuned Archive Closeout And Benchmark Reset

## Overview

This note plans the closeout of the recovered-original RCIM retune work into a
curated repository archive and a refreshed benchmark report surface.

The immediate operator request is to validate the retuned model artifacts
created by the recovered-original launcher, promote archive-grade models into
`models/paper_reference/rcim_retuned/`, generate a detailed PDF report, and
reset `doc/reports/analysis/RCIM Paper Reference Benchmark.md` around the new
paper-original, paper-retuned, and Track 1 comparison structure.

The active campaign state is `cancelled`, so no currently running campaign file
is in scope for mutation during this closeout. No Codex subagent is planned for
this work.

## Technical Approach

The closeout will use a validation-first promotion flow.

1. Build a family-by-family source inventory from the committed
   `output/training_campaigns/rcim_original/{forward,backward}/` bundles.
2. For every candidate family and direction, accept only export surfaces with:
   `20` ONNX files, `20` Python pickle files, and `0` ONNX export-error
   sidecars.
3. Promote accepted artifacts into `models/paper_reference/rcim_retuned/` using
   the same archive contract already used by
   `models/paper_reference/rcim_original/`:
   `README.md`, `reference_inventory.yaml`, `dataset_snapshot_manifest.yaml`,
   `data/`, `onnx/amplitude`, `onnx/phase`, `python/amplitude`,
   `python/phase`, and `source_runs/<run_instance_id>/`.
4. Preserve enough source-run material to recreate or audit the archive:
   launcher summaries, stage summaries, retune best-parameter summaries,
   cross-validation summaries, prediction CSVs, logs, and runtime dataframe
   snapshots.
5. Generate a detailed Markdown report under `doc/reports/analysis/` and export
   it to PDF with
   `scripts/reports/pdf/generate_styled_report_pdf.py`; validate the real PDF
   with the repository PDF validation tooling.
6. Rewrite `doc/reports/analysis/RCIM Paper Reference Benchmark.md` around the
   new canonical structure:
   forward and backward copies of Tables `2`, `3`, `4`, and `5`;
   paper-original, paper-retuned, and Track 1 variants for each table;
   reset Track 1 status cells to empty/unfilled markers so the new Track 1
   pass can be filled progressively from the refreshed baseline.

The Track 1 colored markers will compare against the best available baseline:

- forward Track 1 cells compare against the better value between
  `paper original` and `paper retuned`;
- backward Track 1 cells compare against `paper retuned`, because the paper has
  no backward original tables.

## Involved Components

- `output/training_campaigns/rcim_original/forward/`
- `output/training_campaigns/rcim_original/backward/`
- `models/paper_reference/rcim_original/`
- `models/paper_reference/rcim_retuned/`
- `models/paper_reference/README.md`
- `models/README.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `scripts/tooling/markdown/markdown_style_check.py`
- `scripts/tooling/markdown/run_markdownlint.py`

Initial artifact scan found these archive-grade backward export sources:

| Family | Preferred source bundle | Export status |
| --- | --- | --- |
| `DT` | `2026-05-09-09-21-57__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `RF` | `2026-05-09-12-32-07__bw_export_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `SVR` | `2026-05-09-23-42-54__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `ET` | `2026-05-12-11-08-07__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `ERT` | `2026-05-12-11-08-07__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `GBM` | `2026-05-12-18-22-27__bw_export_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `HGBM` | `2026-05-12-18-22-27__bw_export_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `MLP` | `2026-05-11-09-19-07__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `XGBM` | `2026-05-11-09-19-07__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `ELM` | `2026-05-11-11-38-49__bw_export_bundle` | `20` ONNX, `20` PKL, `0` errors |
| `LGBM` | `2026-05-11-16-05-54__bw_retune_bundle` | `20` ONNX, `20` PKL, `0` errors |

The implementation pass will repeat the same validation for forward retuned
sources before promoting anything under `rcim_retuned/forward/`.

## Implementation Steps

1. Create a reusable inventory script or narrowly scoped closeout helper that
   reads source bundles, counts exported ONNX and PKL files, detects
   `*.export_error.txt`, and records the accepted source bundle for each
   family and direction.
2. Build `models/paper_reference/rcim_retuned/` with the same family archive
   layout used by `rcim_original`, including direction-level `forward/` and
   `backward/` roots.
3. Copy accepted ONNX and PKL exports into the family archive `onnx/` and
   `python/` amplitude/phase folders, preserving target naming.
4. Copy dataset snapshots and source-run artifacts into `data/` and
   `source_runs/<run_instance_id>/`.
5. Generate `README.md`, `reference_inventory.yaml`, and
   `dataset_snapshot_manifest.yaml` for each promoted family archive.
6. Create a detailed retuned-model closeout report with source bundles,
   metrics, best hyperparameters, export completeness, and known recovery
   notes.
7. Export the report to PDF through
   `scripts/reports/pdf/generate_styled_report_pdf.py` and validate the real
   PDF deliverable.
8. Rewrite `RCIM Paper Reference Benchmark.md` to remove obsolete Track 1
   dashboards and keep the new Tables `2`-`5` structure as the canonical
   baseline.
9. Run Markdown QA on all touched authored Markdown.
10. Run Sphinx with warnings as errors because this changes user-facing
    documentation and report surfaces.
11. Report the promoted archive roots, validation results, PDF path, and any
    family/direction gaps before any commit.
