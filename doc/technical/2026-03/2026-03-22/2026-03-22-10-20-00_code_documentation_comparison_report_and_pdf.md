# Code Documentation Comparison Report And PDF

## Overview

This document defines the isolated work needed to transform the existing documentation-platform evaluation into a more decision-oriented deliverable.

The user requested:

- a comparison table;
- a PDF deliverable;
- concrete examples for each candidate documentation approach;
- examples grounded on a small real portion of this repository where possible.

The goal is to help choose how to set up a future repository-wide code documentation system that could later support a command such as:

- `aggiorna documentazione codice`

This task is still in isolated mode and must therefore avoid shared-file edits until the synchronized integration phase.

## Technical Approach

### Scope Of The New Deliverable

The new deliverable should be a standalone analytical report that complements:

- `doc/technical/2026-03/2026-03-22/2026-03-22-10-05-00_code_documentation_platform_evaluation.md`

The new report should include:

1. a compact comparison matrix;
2. a more detailed prose comparison;
3. example output concepts for each main candidate;
4. repository-specific examples showing how a small subset of the current codebase would be documented;
5. a recommendation section;
6. a styled PDF export.

### Recommended Report Type

The report should be authored as an analytical report rather than as a general guide.

Recommended future output:

- Markdown report under `doc/reports/analysis/`
- PDF export aligned with the repository PDF standards

Because the repository is still in isolated mode, the actual report generation should wait until approval.

### Candidate Set To Compare

The report should compare at minimum:

- `MkDocs + Material + mkdocstrings`
- `Sphinx + autodoc/autosummary/apidoc`
- `Sphinx + AutoAPI`
- `Doxygen`
- `pdoc`
- `pydoctor`

The `Doxygen + Breathe` hybrid may be mentioned as an advanced variant, but it does not need to dominate the comparison matrix.

### Example Strategy

The examples should avoid full implementation and instead illustrate how each tool would represent a repository slice.

Recommended repository slices:

- one small Python module from `scripts/`
- one existing Markdown guide under `doc/`
- possibly one configuration-oriented page linked from `config/`

The examples should answer:

- what the source input would look like;
- how the generated documentation page would be structured;
- what the final navigation model would likely look like.

### PDF Requirement

The final deliverable should include a styled PDF export.

That PDF must later follow the repository standards already defined for analytical PDFs:

- white background;
- restrained blue accents;
- rounded section cards;
- safe A4 margins;
- validated final export.

### Isolated-Mode Constraint

During this planning stage:

- no shared README files should be modified;
- no final report path should be treated as canonical yet;
- only standalone planning artifacts should be added.

## Involved Components

- `doc/technical/2026-03/2026-03-22/2026-03-22-10-05-00_code_documentation_platform_evaluation.md`
  Existing evaluation document that will be the basis for the comparison report.
- `scripts/`
  Source tree from which small repository-grounded examples can be drawn.
- `doc/`
  Existing documentation tree for guide and portal examples.
- future analytical report target after approval:
  - `doc/reports/analysis/`
- future PDF export path after approval:
  - `doc/reports/analysis/`
- `readme.temp.md`
  Isolated handoff log that should record this additional planned deliverable.

## Implementation Steps

1. Create this standalone technical planning document.
2. Wait for explicit user approval before generating the comparison report and PDF.
3. After approval, create the analytical comparison report with:
   - the compact comparison matrix;
   - detailed pros and cons;
   - supported formats;
   - official links;
   - repository-grounded examples for each candidate.
4. Export the report to PDF and validate the real PDF output.
5. Update the isolated handoff so the synchronized integration phase knows the final report and PDF exist.
