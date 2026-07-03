# TE Curve Verification Pipeline Best Model Collage PDF Report

## Overview

Create a styled `TE Curve Verification Pipeline` PDF report that shows representative TE-curve
prediction plots for the approved best models. The report will focus on visual
comparison, using four-plot collages per model so the oscillation tracking
behavior can be inspected without opening every validation artifact manually.

The report will cover:

- forward reference best models:
  `paper_original_best_Fw`, `paper_retuned_best_Fw`, and `track1_best_Fw`;
- current Wave 1 forward family-best models from the family registries;
- backward reference best models:
  `paper_retuned_best_Bw` and `track1_best_Bw`;
- current Wave 1 backward family-best models from the family registries;
- current Wave 1 global family-best models evaluated on forward and backward
  curves together.

## Technical Approach

Add a repeatable analysis/report script that builds a dated report bundle under
`doc/reports/analysis/te_curve_verification_pipeline/` and machine-readable visual artifacts under
`output/validation_checks/track2_best_model_collage_report/`.

The implementation will reuse existing repository evaluation paths instead of
introducing a separate model-loading stack:

- use the canonical TE Curve Verification Pipeline reference comparison artifacts and support code for
  `paper_original_best_Fw`, `paper_retuned_best_Fw`, `track1_best_Fw`,
  `paper_retuned_best_Bw`, and `track1_best_Bw`;
- use the current family registries under `output/registries/families/` for the
  Wave 1 directional and global best models;
- reuse the Wave 1 TE-curve prediction plotting style, including the updated
  `Measured TE` line weight and dark-gray color;
- select four deterministic representative curves per model/scope and assemble
  one `2x2` collage PNG per model;
- write a Markdown report that embeds the collages and includes a compact
  metrics/source table;
- export the Markdown report to PDF with
  `scripts/reports/pdf/run_report_pipeline.py`;
- validate the real exported PDF with the repository PDF validation tool and
  visually inspect generated validation images for clipped figures, poor page
  breaks, and unreadable captions.

## Involved Components

- `scripts/reports/analysis/plot_wave1_best_model_te_curves.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `output/registries/families/*/latest_family_best.yaml`
- `output/validation_checks/track2_reference_comparison/`
- `output/validation_checks/wave1_high_order_track2_curve_prediction_forward/`
- `output/validation_checks/wave1_high_order_track2_curve_prediction_backward/`
- `doc/reports/analysis/te_curve_verification_pipeline/`
- `doc/README.md`

## Implementation Steps

1. Inspect the latest TE Curve Verification Pipeline reference validation summary and Wave 1
   directional/global registry entries to determine the exact candidate list.
2. Add a repository-owned report builder script for the collage report.
3. Generate deterministic four-curve collages for each requested forward,
   backward, and global model.
4. Write the dated Markdown report with embedded collage images, source
   metadata, and metric summaries.
5. Export the Markdown report to PDF through the styled report pipeline.
6. Validate the real PDF output and inspect the rendered pages for figure fit
   and layout problems.
7. Run scoped Markdown QA on the generated report and report the final artifact
   paths.

No subagent use is planned for this task.
