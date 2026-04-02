# Report Pipeline Standardization And Tooling Env

## Overview

This document defines the standardization of the report-generation workflow used for:

- explanatory model diagrams;
- styled PDF export;
- real PDF validation through rasterized pages;
- temporary artifact management.

The latest correction cycle exposed a repeated workflow problem:

- the repository already has specialized scripts for diagram generation, PDF export, and PDF validation;
- however, running them end-to-end still requires several manual steps;
- PDF export may require browser execution outside the sandbox;
- PDF validation depends on `PyMuPDF`, which behaves more reliably inside a proper virtual environment than through ad hoc `--target` installs on Windows;
- temporary files and validation artifacts currently spread across `.temp/`, `.tmp_pydeps/`, and `.tmp_pdfenv/` in a way that is functional but not yet standardized.

The goal of this work is to make the report pipeline deterministic, faster to rerun, easier to clean up, and easier to explain.

## Technical Approach

The preferred approach is not to replace the existing scripts, but to stabilize the orchestration around them.

### 1. Keep The Existing Single-Purpose Scripts

The current specialized scripts already map well to the underlying responsibilities:

- `scripts/reports/generate_model_report_diagrams.py`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`

These should remain the canonical low-level entry points.

### 2. Add A Repository-Owned Orchestrator

Add a dedicated orchestration script for the report workflow, for example:

- `scripts/reports/run_report_pipeline.py`

This orchestrator should:

- optionally regenerate diagrams before export;
- export one or more styled PDFs;
- validate the exported PDFs through rasterized page images;
- manage reusable temporary directories and browser profiles;
- optionally clean temporary artifacts at the end;
- expose flags such as:
  - `--reports`
  - `--regenerate-diagrams`
  - `--validate-pdf`
  - `--keep-temp`
  - `--clean-temp`
  - `--use-tool-env`

The purpose is to reduce manual command chaining and make future reruns predictable.

### 3. Use A Persistent Tooling Environment For PDF Validation

For Windows and binary dependencies such as `PyMuPDF`, the preferred mechanism is a dedicated local tooling virtual environment instead of repeated `pip install --target ...`.

Recommended location:

- `.tools/report_pdf_env/`

This environment should be treated as repository-local tooling, not as a primary development environment.

Why this is preferable:

- binary packages are more reliable in a normal virtual environment;
- future report-validation runs become faster because the dependency is already present;
- the repository avoids repeatedly creating ad hoc `.tmp_pydeps/` directories;
- the pipeline becomes easier to document and debug.

### 4. Standardize Temporary Paths

Temporary and validation artifacts should use a single predictable structure.

Recommended roots:

- `.temp/report_pipeline/browser_profiles/`
- `.temp/report_pipeline/html_previews/`
- `.temp/report_pipeline/pdf_validation/<report_name>/`

This should replace scattered one-off temp directories whenever possible.

The orchestrator should be able to:

- keep these folders for debugging when requested;
- clean them when the user wants a fresh rerun.

### 5. Cleanup Workflow

Add explicit cleanup support instead of relying on ad hoc manual removal commands.

Two acceptable options:

1. integrate cleanup flags directly into the orchestrator;
2. add a small dedicated cleanup utility, for example:
   - `scripts/reports/clean_report_pipeline_artifacts.py`

The orchestrator-first option is preferable unless the cleanup logic becomes too broad.

### 6. Documentation And Reproducibility

The report workflow should be documented in a way that makes these distinctions explicit:

- canonical content/report files;
- generated deliverables;
- validation evidence;
- temporary runtime artifacts;
- tooling environment bootstrap.

If the repository formally depends on `PyMuPDF` for required PDF validation, then `requirements.txt` should also be reviewed during implementation so the environment remains reproducible.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  if small integration hooks are needed.
- `scripts/reports/generate_styled_report_pdf.py`
  if some temp-path coordination is centralized.
- `scripts/reports/validate_report_pdf.py`
  if validation-path handling is standardized further.
- a new orchestration entry point under `scripts/reports/`
  for end-to-end report generation and validation.
- `doc/scripts/reports/`
  for script-level documentation of the orchestrator.
- `doc/guide/project_usage_guide.md`
  for the runnable user workflow.
- potentially `requirements.txt`
  if the required validation dependency must be formalized.

## Implementation Steps

1. Introduce a repository-owned orchestrator for the report pipeline.
2. Define the persistent tooling environment policy for PDF validation.
3. Standardize the temporary-path layout under a single report-pipeline root.
4. Integrate diagram generation, PDF export, and PDF validation into the orchestrator.
5. Add explicit cleanup controls for report-pipeline temporary artifacts.
6. Update script-level documentation and the usage guide.
7. Review whether `requirements.txt` must be updated to keep PDF validation reproducible.
