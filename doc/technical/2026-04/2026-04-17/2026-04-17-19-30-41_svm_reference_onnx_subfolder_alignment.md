# SVM Reference ONNX Subfolder Alignment

## Overview

The curated `SVM` paper-reference archive currently stores its deployment-side
artifacts directly under:

- `models/paper_reference/rcim_track1/svm_reference_models/amplitude/`
- `models/paper_reference/rcim_track1/svm_reference_models/phase/`

The archive already distinguishes deployment-facing `ONNX` artifacts from the
Python-side fitted-estimator archive under `python/`. This change aligns the
folder layout with that distinction by moving the existing `amplitude/` and
`phase/` ONNX folders under a dedicated `onnx/` subtree.

## Technical Approach

The archive layout will be changed from:

- `svm_reference_models/amplitude/`
- `svm_reference_models/phase/`

to:

- `svm_reference_models/onnx/amplitude/`
- `svm_reference_models/onnx/phase/`

The implementation will preserve the existing filenames and artifact contents.
Only the canonical archive paths and all repository-owned references to those
paths will be updated.

The following surfaces will be kept aligned:

- `reference_inventory.yaml`
- `models/paper_reference/rcim_track1/svm_reference_models/README.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `models/.gitignore`

## Involved Components

- `models/paper_reference/rcim_track1/svm_reference_models/`
- `models/paper_reference/rcim_track1/svm_reference_models/reference_inventory.yaml`
- `models/paper_reference/rcim_track1/svm_reference_models/README.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `models/.gitignore`
- `doc/technical/2026-04/2026-04-17/README.md`
- `doc/README.md`

## Implementation Steps

1. Create the dedicated `onnx/` subtree and move the existing amplitude and
   phase folders under it without changing filenames.
2. Update every repository-owned canonical reference to the archived ONNX
   paths.
3. Verify that the inventory still resolves all `19` model paths correctly.
4. Run Markdown checks on the touched Markdown scope before closing the task.
