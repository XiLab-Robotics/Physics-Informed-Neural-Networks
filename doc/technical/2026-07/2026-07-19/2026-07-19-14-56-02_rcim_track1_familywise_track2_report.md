# RCIM Track1 Familywise Track 2 Report

## Overview

This document defines the repository change needed to generate a familywise
`TE Curve Verification Pipeline` report for `rcim_track1` across the frozen
`simplified_dataset` setpoint archive and the newly promoted polished setpoint
and polished actual-value archives.

The regular familywise ONNX report pipeline assumes one exported ONNX model per
surface. The `rcim_track1` archive is different: each surface stores a
paper-reference model bank with one ONNX and one Python model per harmonic
amplitude or phase target and per estimator family.

## Technical Approach

Extend the report tooling with an `rcim_track1`-specific path that reads the
existing archive inventories and validation summaries, evaluates the archived
ONNX component models, reconstructs full TE curves from the harmonic
amplitude/phase predictions, and emits the same human-facing report structure
used by the standard familywise reports.

The report must keep the same three dataset/input-mode sections:

- `simplified_dataset` with `setpoints`;
- `polished_dataset` with `setpoints`;
- `polished_dataset` with `actual_values`.

For each section, the report must list the exact archive roots and inventory
paths used for the forward, backward, and global surfaces, then provide
aggregate metrics and 12-curve collage pages.

## Involved Components

- `scripts/reports/analysis/build_track2_familywise_onnx_report.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/`
- `models/simplified_dataset/paper_reference/rcim_track1/`
- `models/polished_dataset/paper_reference/rcim_track1/setpoints/`
- `models/polished_dataset/paper_reference/rcim_track1/actual_values/`
- `doc/reports/analysis/te_curve_verification_pipeline/03_family_reports/`
- `output/validation_checks/track2_familywise_onnx_report/`

## Implementation Steps

1. Inspect the existing `rcim_track1` archive inventories and source validation
   summaries for all three dataset/input-mode groups.
2. Add a narrow `rcim_track1` report path that resolves the three surface
   archives from `paper_reference/rcim_track1` instead of the regular
   `input_mode/exported/model_development_export_inventory.yaml` files.
3. Reuse the stored dataset split and feature schema from each source
   validation summary so simplified models are evaluated on the simplified
   dataset and polished models are evaluated on the polished dataset.
4. Load archived ONNX component models from `models/`, reconstruct full TE
   curves from predicted harmonic amplitude/phase values, and compute the
   existing raw, offset, and shape metrics.
5. Generate the Markdown report, machine-readable CSV/YAML artifacts, collage
   images, and styled PDF export.
6. Validate the report with Markdown QA, PDF export validation, visual raster
   inspection, conflict-marker checks, and `git diff --check`.
