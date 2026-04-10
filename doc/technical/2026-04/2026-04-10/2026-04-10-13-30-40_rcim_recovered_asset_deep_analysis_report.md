# RCIM Recovered Asset Deep Analysis Report

## Overview

This document defines the work needed to produce a very deep technical report
about the recovered RCIM ML-compensation assets now integrated into the
repository reference surface.

The goal of the report is not only to list the recovered material, but to
reconstruct as precisely as possible:

- how the paper-era models were organized;
- how the training, prediction, export, and evaluation code was structured;
- how the different recovered code generations relate to each other;
- how the TwinCAT export branch fits into the workflow;
- what remains uncertain;
- what exactly must be reproduced inside the repository to obtain a faithful
  `Track 1` reimplementation.

The final report is intended to become the main implementation-facing
understanding document for the recovered paper assets.

## Technical Approach

The report should be written as a repository-owned deep reference analysis
under `doc/reports/analysis/` with a readable canonical title rather than a
timestamped campaign-style filename.

The analysis must combine:

- recovered asset inspection from
  `reference/rcim_ml_compensation_recovered_assets/`;
- the original paper summary and benchmark documents already present in
  `doc/reference_summaries/` and `doc/reports/analysis/`;
- code-level tracing of the recovered Python pipeline;
- inventory-level understanding of the exact ONNX releases and backup exports;
- explicit separation between fact, recovered evidence, inference, and open
  questions.

The report should be structured to answer four implementation questions:

1. What the recovered paper assets demonstrably contain.
2. How the original paper pipeline appears to have worked end to end.
3. Which parts are exact paper release versus later or backup evolution.
4. What the repository must reproduce to reimplement the paper workflow as
   faithfully as possible in `Track 1`.

The report should explicitly document:

- model families and per-harmonic target organization;
- feature and input assumptions such as `rpm`, `deg`, and `tor`;
- target assumptions such as amplitude and phase per harmonic;
- export formats and their role;
- evaluation logic and metrics path;
- version drift between `original_pipeline`, `latest_snapshot`, and
  `backup_legacy`;
- practical repository consequences for the next `Track 1` iterations.

The report should also state clearly where the recovered material is still
incomplete or not yet runnable, especially around the heavy `instance_v1`
archive and the missing instance-class environment needed for direct reuse of
some pickle artifacts.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- `reference/rcim_ml_compensation_recovered_assets/code/backup_legacy/`
- `reference/rcim_ml_compensation_recovered_assets/backup/onnx_variants/`
- `reference/rcim_ml_compensation_recovered_assets/deployment/twincat_xml/`
- `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

Planned output:

- `doc/reports/analysis/RCIM Recovered Asset Deep Analysis.md`

## Implementation Steps

1. Inspect the recovered asset package in detail and build a precise inventory
   of the exact ONNX models, Python entrypoints, backup branches, and TwinCAT
   exports.
2. Compare the recovered code generations and identify what appears to be the
   exact paper release, what appears to be a later snapshot, and what belongs
   to historical backup evolution.
3. Reconstruct the paper-era workflow step by step:
   dataframe creation, target extraction, model training, export, prediction,
   and evaluation.
4. Extract the exact model-family set, harmonic coverage, input columns,
   target organization, and deployment/export assumptions from the recovered
   material.
5. Document the heavy archive and runtime uncertainties, especially the
   `instance_v1` subtree and the missing class-environment pieces required for
   full replay.
6. Translate the recovered-paper workflow into explicit repository
   consequences for `Track 1`, including what must be reproduced identically
   and what can remain only a documented uncertainty for now.
7. Create the deep analysis report under `doc/reports/analysis/`.
8. Add the new report to the canonical documentation index under `doc/`.
