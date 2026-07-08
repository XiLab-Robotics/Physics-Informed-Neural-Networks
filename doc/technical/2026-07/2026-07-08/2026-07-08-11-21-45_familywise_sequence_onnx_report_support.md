# Familywise Sequence ONNX Report Support

## Overview

The familywise `TE Curve Verification Pipeline` ONNX report builder currently
evaluates exported point-model ONNX files by passing each curve as a two
dimensional feature matrix. The newly completed `temporal_convolution` family
uses sequence-model ONNX exports whose input tensor has rank 3, so the current
builder fails before producing the report.

This change will extend the existing familywise report pipeline so it can
evaluate both point-style and sequence-style ONNX exports while preserving the
current report layout and output structure.

## Technical Approach

The implementation will update
`scripts/reports/analysis/build_track2_familywise_onnx_report.py` in the
existing inference boundary:

- inspect ONNX input metadata rank before each inference call;
- keep the current rank-2 path unchanged for point models;
- support rank-3 sequence models by reshaping each curve feature matrix to the
  exported model input convention;
- retain the existing output flattening and prediction-versus-target shape
  assertion;
- rerun the `temporal_convolution` familywise report generation after the
  script patch.

The implementation will not change model exports, training artifacts,
registries, or the heavy official matrix configuration.

## Involved Components

- `scripts/reports/analysis/build_track2_familywise_onnx_report.py`
- `models/simplified_dataset/setpoints/exported/model_development_export_inventory.yaml`
- `models/polished_dataset/setpoints/exported/model_development_export_inventory.yaml`
- `models/polished_dataset/actual_values/exported/model_development_export_inventory.yaml`
- `doc/reports/analysis/te_curve_verification_pipeline/03_family_reports/`
- `output/validation_checks/track2_familywise_onnx_report/`
- `scripts/reports/pdf/run_report_pipeline.py`

## Implementation Steps

1. Patch the report builder prediction helper to branch on ONNX input rank.
2. Validate the script with `py_compile`.
3. Generate the `temporal_convolution` familywise ONNX report with 12 curves
   per page.
4. Export and raster-validate the real PDF.
5. Visually inspect the section-summary and collage pages.
6. Run scoped Markdown QA and final newline checks for the generated report.
7. Stop before committing unless the user explicitly requests a commit.
