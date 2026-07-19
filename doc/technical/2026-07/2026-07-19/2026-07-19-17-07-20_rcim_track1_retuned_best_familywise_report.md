# RCIM Track1 Retuned Best Familywise Report

## Overview

This document defines the report refresh needed to make the selected retuned
`rcim_track1` component-bank composition explicit in the familywise
`TE Curve Verification Pipeline` report.

The selected retuned composition must use only the polished setpoint archive:

- forward: polished setpoints;
- backward: polished setpoints;
- global: polished setpoints.

## Technical Approach

Extend the `rcim_track1` familywise report builder so it can regenerate a
polished-setpoints-only report that evaluates exactly those three surface banks
and lists the same 19 selected harmonic component ONNX models per surface.

The regular dataset/input-mode sections remain available for auditability. The
new selected section is the human-facing answer for reconstructing the retuned
best component bank from the archived ONNX files.

## Involved Components

- `scripts/reports/analysis/build_track2_familywise_rcim_track1_report.py`
- `doc/reports/analysis/te_curve_verification_pipeline/03_family_reports/rcim_track1/`
- `output/validation_checks/track2_familywise_onnx_report/rcim_track1/`
- `models/polished_dataset/paper_reference/rcim_track1/setpoints/`
- `models/polished_dataset/paper_reference/rcim_track1/actual_values/`

## Implementation Steps

1. Add an explicit selected-retuned group to the RCIM Track1 familywise report
   builder.
2. Resolve forward, backward, and global from polished setpoints only.
3. Regenerate the Markdown report, component inventory, per-curve metrics,
   summary YAML, collage images, and styled PDF export.
4. Validate the real PDF raster output and run scoped Markdown, Python,
   conflict-marker, and Git diff checks.
