# Original ONNX Forward TE Curve Verification Pipeline Collage PDF And Standalone Plotter

## Overview

This technical document defines the implementation path for a narrow `TE Curve Verification Pipeline`
report that evaluates only the recovered paper-original forward `ONNX` model
bank stored under
`reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`.

The requested deliverables are:

- a simple `TE Curve Verification Pipeline` Markdown and PDF report with collage plots for the
  original paper best forward model only;
- explicit loading of the `19` `ONNX` models that compose the paper-best
  forward harmonic target set;
- evaluation on the canonical held-out `TE Curve Verification Pipeline` forward curve set;
- a lightweight standalone script with hardcoded `ONNX` model path strings,
  dataset loading, per-curve `19` target prediction, curve reconstruction, and
  one-at-a-time `matplotlib` plot generation.

The work is evaluation-only. It does not launch training, create campaign
state, modify protected campaign files, or change accepted model registries.

Context7 was attempted for `ONNX Runtime` Python API documentation, but the
configured Context7 token returned `Invalid or expired OAuth token`. The
implementation will therefore use the already validated local
`onnxruntime.InferenceSession` usage in
`scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_original_onnx_release_parity_validation.py`
as the primary API reference.

No subagent is planned for this task.

## Technical Approach

The implementation will add a focused repository-owned report script instead
of widening the existing full `TE Curve Verification Pipeline` collage report. This keeps the output
simple and prevents the paper-original `ONNX` diagnostic from being mixed with
Wave 1, Wave 2.1, Wave 2.3, retuned, RCIM Model-Bank Reproduction, or global/backward candidates.

The report path will:

1. load the standard `TE Curve Verification Pipeline` configuration from
   `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`;
2. read the selected harmonic list from the configuration;
3. build the canonical curve records through the same support functions used
   by the existing `TE Curve Verification Pipeline` report builders;
4. keep only forward curve records;
5. resolve the `LGBM` paper-original forward `ONNX` target paths from the
   recovered release root;
6. assert that exactly `19` target models are used;
7. run each target model on the curve-level operating input vector;
8. convert the predicted `19` target vector into harmonic coefficient
   dictionaries;
9. reconstruct each predicted transmission-error curve with the same harmonic
   reconstruction convention used by the current paper-reference evaluation;
10. compute raw `TE Curve Verification Pipeline` curve metrics;
11. select four deterministic representative curves and save a collage;
12. write a compact metrics CSV, validation summary YAML, Markdown report, and
    styled PDF export.

The standalone plotter will intentionally avoid the full candidate registry and
reporting stack. It will expose the model bank as a hardcoded list of `19`
path strings at the top of the file, then perform the direct sequence:

1. load `ONNX` sessions;
2. enumerate forward held-out curve files from the canonical dataset;
3. for each curve, build the `speed`, `torque`, and `oil temperature` input;
4. run the `19` model sessions in a loop;
5. reconstruct the predicted curve;
6. plot measured versus predicted transmission error with `matplotlib`;
7. save or show one figure per curve depending on command-line flags.

The standalone script may import small local dataset helpers if needed, but it
will avoid campaign infrastructure, registry lookups, and dynamic candidate
configuration. The important property is that the model list is explicit and
portable.

## Involved Components

The implementation is expected to touch or create:

- `scripts/reports/analysis/build_track2_original_onnx_fw_collage_report.py`
  for the simple report, collage assets, and PDF-ready Markdown generation;
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/plot_original_onnx_fw_track2_curves.py`
  for the lightweight standalone hardcoded-ONNX plotter;
- `doc/reports/analysis/track2/original_onnx_fw_collage_report/[2026-06-05]/`
  for the Markdown report, PDF, and report-local collage assets;
- `output/validation_checks/track2_original_onnx_fw_collage_report/` for
  metrics CSV and validation summary artifacts;
- `doc/guide/project_usage_guide.md` for the new runnable user-facing command;
- `site/` Sphinx output verification if the guide or API docs are affected;
- `doc/README.md` for this technical document and final report registration.

The implementation will reuse behavioral references from:

- `scripts/reports/analysis/build_track2_best_model_collage_report.py` for
  deterministic four-curve selection and collage plot styling;
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_original_onnx_release_parity_validation.py`
  for recovered `ONNX` release loading and inference;
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py`
  for harmonic target dictionary conversion and curve reconstruction;
- `scripts/reports/pdf/run_report_pipeline.py`,
  `scripts/reports/pdf/generate_styled_report_pdf.py`, and
  `scripts/reports/pdf/validate_report_pdf.py` for PDF export and QA.

## Implementation Steps

1. Inspect the recovered `ONNX` release tree and identify the exact `19`
   `LGBM` forward paper-best target models.
2. Implement the standalone hardcoded-path plotter first, because it is the
   clearest verification that the `19` target predictions and reconstruction
   path work without registry machinery.
3. Implement the focused `TE Curve Verification Pipeline` collage report builder using the same curve
   records, metric computation, and collage selection policy as the existing
   official report.
4. Run the standalone plotter in a bounded smoke mode to generate a few plots.
5. Run the report builder for the full forward `TE Curve Verification Pipeline` set and generate the
   Markdown report, collage PNG, metrics CSV, and validation summary.
6. Export the Markdown report to a styled PDF using repository report tooling.
7. Validate the exported PDF with the repository PDF validation script and
   inspect the real PDF output for plot visibility, clipping, margins, and
   table fit.
8. Update `doc/README.md` and `doc/guide/project_usage_guide.md`.
9. Run Markdown QA on touched Markdown files.
10. Run Python compilation checks on new or modified scripts.
11. Run Sphinx with `-W` if portal-facing guide or API documentation changes.
