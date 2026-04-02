# Analysis Report Directory Reorganization And Universal Model Report Naming

## Overview

This document defines a repository-wide reorganization of `doc/reports/analysis/` to make the analysis reports easier to browse and to remove timestamp-based naming from the model explanatory reports.

The current folder mixes several different report types in a single flat directory:

- model explanatory reports;
- analytical one-off reports;
- training-analysis reports;
- model-family comparison reports;
- shared report assets.

This makes the directory harder to scan, and the timestamp-prefixed model report filenames are not reader-friendly. The user explicitly requested readable, universal names such as `FeedForward Network`, without creation dates in the visible report names.

The goal of this pass is therefore to reorganize `doc/reports/analysis/` by report purpose, promote stable human-readable names for the model reports, and update the repository references so the report pipeline still works.

## Technical Approach

### 1. Introduce Stable Category Folders Under `doc/reports/analysis/`

The flat analysis root should be replaced by a small set of stable subfolders with clear intent.

The proposed structure is:

- `doc/reports/analysis/model_explanatory/`
- `doc/reports/analysis/training_analysis/`
- `doc/reports/analysis/analytical_studies/`
- `doc/reports/analysis/family_studies/`

This keeps the directory readable while preserving the semantic distinction between the different report classes already present in the repository.

### 2. Give The Model Reports Universal Human-Readable Names

The four explanatory model reports should stop exposing creation timestamps in their filenames.

The proposed stable names are:

- `FeedForward Network`
- `Harmonic Regression`
- `Periodic Feature Network`
- `Residual Harmonic Network`

Each model should therefore get its own discoverable folder, for example:

- `doc/reports/analysis/model_explanatory/FeedForward Network/FeedForward Network.md`
- `doc/reports/analysis/model_explanatory/FeedForward Network/FeedForward Network.pdf`

The same pattern should be applied to the other three model families.

### 3. Reorganize The Other Existing Analysis Reports By Purpose

The non-model reports should also be moved into more meaningful categories.

The intended mapping is:

- `2026-03-12-13-18-30_feedforward_trial_analytical_report.md`
  -> `doc/reports/analysis/analytical_studies/FeedForward Trial Analytical Report.md`
- `2026-03-12-13-38-17_training_configuration_analysis_report.md`
  -> `doc/reports/analysis/training_analysis/Training Configuration Analysis.md`
- `2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  -> `doc/reports/analysis/training_analysis/Training Configuration Analysis.pdf`
- `2026-03-17-15-46-01_te_model_family_analysis_report.md`
  -> `doc/reports/analysis/family_studies/TE Model Family Analysis.md`

This preserves meaning while making the top-level analysis folder much less noisy.

### 4. Move The Model Diagram Assets Into A Stable Discoverable Home

The current shared asset path `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/` also exposes a dated naming scheme.

This pass should move those explanatory SVG assets into a stable non-dated location under the model explanatory report area, for example:

- `doc/reports/analysis/model_explanatory/assets/`

The diagram generator and the Markdown reports must then be updated to use the new stable asset paths.

### 5. Update Pipeline And Documentation References

Because the report locations are used by tooling and documentation, the reorganization is not complete unless the path references are updated.

This pass should update at least:

- `scripts/reports/run_report_pipeline.py`
  so the model explanatory preset paths point to the new stable Markdown report locations;
- `doc/guide/project_usage_guide.md`
  so report-generation examples and path references match the new structure;
- `README.md`
  so the main report index points to the new locations.

The historical technical documents may still mention the older paths as historical references, but the active repository surfaces and workflows should point to the reorganized structure.

## Involved Components

The work will affect:

- `doc/reports/analysis/`
  through directory creation plus report and asset relocation;
- the four model explanatory Markdown and PDF files;
- the four non-model analysis reports currently stored at the analysis root;
- the model explanatory SVG asset directory;
- `scripts/reports/run_report_pipeline.py`
  for updated preset report paths;
- `doc/guide/project_usage_guide.md`
  for updated report-location and pipeline examples;
- `README.md`
  for the main report index.

Depending on the final move strategy, some additional documentation references may also be updated when they are active workflow entry points.

## Implementation Steps

1. Create the new stable analysis subfolder structure by report purpose.
2. Move the four model explanatory reports into per-model folders with universal human-readable names.
3. Move the non-model analysis reports into purpose-specific folders with readable stable names.
4. Move the model explanatory SVG assets into a stable non-dated asset location.
5. Update the four model explanatory Markdown files so their image references point to the new asset paths.
6. Update `scripts/reports/run_report_pipeline.py` to use the new stable report locations.
7. Update `doc/guide/project_usage_guide.md` and `README.md` to use the reorganized paths.
8. Validate that the moved files are still discoverable and that the report pipeline paths resolve correctly.
