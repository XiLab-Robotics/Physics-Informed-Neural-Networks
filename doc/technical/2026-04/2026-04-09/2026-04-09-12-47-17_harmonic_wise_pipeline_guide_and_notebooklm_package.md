# Harmonic-Wise Pipeline Guide And NotebookLM Package

## Overview

This document proposes a guide-local documentation bundle for the
repository-owned harmonic-wise pipeline that reimplements the offline logic of
`reference/RCIM_ML-compensation.pdf`.

The user requested a clear guide that explains, in an educational way, how the
pipeline works end to end and also requested the repository-owned source files
to feed `NotebookLM` for a video guide and presentation workflow.

The deliverable should therefore not stop at a short script note. It should
become a guide-local bundle that explains:

- why the repository introduced the harmonic-wise branch;
- how the branch reconstructs the paper-faithful offline logic;
- how the repository turns TE curves into harmonic targets;
- how the predictor, reconstruction, and benchmark stages interact;
- what is already comparable with the paper and what is still missing;
- how the guide can be reused to brief colleagues, new students, and future
  reviewers.

## Technical Approach

Create a new guide root under `doc/guide/` dedicated to the harmonic-wise
paper-reimplementation pipeline.

The guide will explain the pipeline in the exact staged form already agreed in
project planning:

1. read each TE curve plus its operating-condition metadata;
2. decompose the TE curve into the selected harmonic terms;
3. represent each harmonic with coefficient form (`cos`, `sin`) and explain
   the link to amplitude `A_k` and phase `phi_k`;
4. build a new supervised dataset where each sample is an operating-condition
   point and each target is the harmonic summary of one whole TE curve;
5. train one predictor per harmonic target term;
6. reconstruct the TE curve from the predicted harmonic stack;
7. evaluate the reconstructed curve against the real curve using `MAE`,
   `RMSE`, and mean percentage error;
8. position the result inside the repository's `Track 1` paper-faithful branch
   and explain how it differs from the direct-TE comparison branch.

The guide should be repository-facing, but still educational. It should make
the distinction between:

- the original paper logic;
- the repository-owned implementation choices;
- the currently implemented offline scope;
- the future online compensation scope that is still missing.

The guide should include generated visual material. At minimum:

- one conceptual flow diagram for the data and signal transformation path;
- one implementation-oriented architecture diagram that maps the real
  repository files, outputs, and validation artifacts.

Because the user explicitly asked for `NotebookLM` source files for a video
guide and presentation workflow, the guide root should also include the
standard repository package tracks:

- `assets/concept_video_package/`
- `assets/project_video_package/`

These packages should be built as repository-owned `NotebookLM` sources and
should include the standard source-package documents plus the final structured
prompt files:

- `video_source_brief.md`
- `video_terminology_sheet.md`
- `video_narration_outline.md`
- `video_figure_reference.md`
- `video_fact_boundary_notes.md`
- `concept_video_scope_notes.md` or `project_video_scope_notes.md`
- `notebooklm_concept_video_prompt.md`
- `notebooklm_project_video_prompt.md`

The prompt files should explicitly ask for video-guide and presentation-ready
material for the harmonic-wise pipeline topic.

Per repository rules, if new guide-local figures are generated, they must be
reviewed before any guide PDF is finalized. So the implementation should stop
for user approval after the guide images/diagrams are created and inserted into
the Markdown guide. Only after that approval should the PDF companion be
generated and validated.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/baseline.yaml`
- new guide root under `doc/guide/`
- guide-local `assets/` directory for diagrams and `NotebookLM` packages

## Implementation Steps

1. Create the new guide root under `doc/guide/` with a canonical guide
   Markdown file for the harmonic-wise paper-reimplementation pipeline.
2. Write the guide so it explains the pipeline stages, the paper alignment,
   the repository-specific design choices, and the current offline-only scope.
3. Generate at least two guide-local figures:
   one conceptual flow diagram and one implementation-oriented architecture
   diagram.
4. Insert the figures into the guide and stop for explicit user approval of
   the images before exporting the guide PDF.
5. After image approval, generate and validate the guide-local PDF companion.
6. Create the `NotebookLM` source packages under `assets/` for both the
   neutral concept track and the repository-specific project track.
7. Write the final `NotebookLM` prompts so they are ready to request both a
   video guide and presentation-ready outputs for this topic.
8. Update `doc/README.md` with the new technical document entry and later add
   the guide root to the guide index if the implementation is approved.
