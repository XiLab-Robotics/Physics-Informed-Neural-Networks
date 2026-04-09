# Paper Reimplementation Structure Reorganization

## Overview

This document formalizes a repository reorganization for the paper-faithful
reimplementation branch derived from
`reference/RCIM_ML-compensation.pdf`.

The current implementation works, but its files are still placed too close to
the generic training workflows. The result is functional but not sufficiently
discoverable. A reader inspecting the repository cannot immediately distinguish:

- generic model-training infrastructure;
- repository model-family workflows;
- the explicit paper-faithful reimplementation branch.

This should be corrected before the paper branch grows further.

The goal of this task is therefore to reorganize the paper-faithful
reimplementation into a dedicated structure instead of leaving its scripts,
configs, notes, and outputs scattered among generic training assets.

## Technical Approach

### Problem Statement

The first harmonic-wise implementation currently lives in paths such as:

- `scripts/training/run_harmonic_wise_comparison_pipeline.py`
- `scripts/training/harmonic_wise_support.py`
- `config/training/harmonic_wise/presets/baseline.yaml`
- `doc/scripts/training/run_harmonic_wise_comparison_pipeline.md`
- `output/validation_checks/harmonic_wise_comparison/`

Those paths are technically valid, but they read like one more generic
training utility rather than the explicit repository-owned reimplementation of
the benchmark paper.

### Reorganization Goal

The repository should expose the paper-faithful branch as a first-class topic
root with an explicit identity such as:

- `paper_reimplementation`
- or another equally explicit paper-benchmark root chosen during the final
  patch

The important requirement is not the exact final label, but the separation of
concerns. The paper branch should become clearly discoverable across:

- scripts;
- config;
- documentation;
- artifact roots;
- report references.

### Intended Structural Direction

The reorganization should group the paper-faithful branch under dedicated
paper-reimplementation roots rather than leaving it mixed with generic training
helpers.

The planned structure should cover at least:

1. dedicated script root for the paper-faithful branch;
2. dedicated config root for the paper-faithful branch;
3. dedicated script note under `doc/scripts/` aligned with that root;
4. dedicated validation/artifact root that makes the paper branch visible from
   the output tree;
5. updated canonical report references so the colleague-facing reports still
   point to the new paths cleanly.

### Scope Boundary

This reorganization should target the paper-faithful branch only.

It should not yet reorganize:

- the broader generic training infrastructure;
- current campaign launchers;
- direct-TE family training roots;
- the future online/TestRig branch.

### Reporting Constraint

After the reorganization, the repository should still keep the already
approved conceptual distinction:

- `Track 1`: paper-faithful harmonic-wise benchmark;
- `Track 2`: repository direct-TE comparable benchmark.

This task only improves the structure and discoverability of `Track 1`.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/te_model_live_backlog.md`
- `scripts/training/run_harmonic_wise_comparison_pipeline.py`
- `scripts/training/harmonic_wise_support.py`
- `config/training/harmonic_wise/`
- `doc/scripts/training/run_harmonic_wise_comparison_pipeline.md`
- `output/validation_checks/harmonic_wise_comparison/`
- `site/api/training/`

## Implementation Steps

1. Define the dedicated repository root naming for the paper-faithful
   reimplementation branch.
2. Move the current harmonic-wise paper-faithful scripts into that dedicated
   script structure.
3. Move the current harmonic-wise paper-faithful configs into the matching
   dedicated config structure.
4. Move or rewrite the script note under `doc/scripts/` so it follows the same
   topic-root organization.
5. Update the artifact/output root so paper-faithful validation artifacts are
   no longer stored under a generic-looking harmonic-wise location.
6. Update the canonical reports, usage guide, Sphinx API pages, and any path
   references affected by the move.
7. Re-run the paper-faithful baseline from the new canonical location to prove
   that the reorganized branch still works.
