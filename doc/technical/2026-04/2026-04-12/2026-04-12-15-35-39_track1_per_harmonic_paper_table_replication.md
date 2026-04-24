# Track 1 Per-Harmonic Paper Table Replication

## Overview

This technical document redefines the completion bar for `Track 1`.

The repository should no longer treat `Track 1` as complete when the
paper-faithful branch only reaches a good reconstructed-TE offline result.
Instead, `Track 1` should close only when the repository reproduces the
paper-style per-harmonic training and reaches the paper-tabulated target
values for each harmonic component.

The target scope remains the exact recovered RCIM harmonic set:

- `0`
- `1`
- `3`
- `39`
- `40`
- `78`
- `81`
- `156`
- `162`
- `240`

For each harmonic, the repository must treat the relevant harmonic outputs as
paper-facing prediction targets and compare the repository result directly
against the paper table rather than only against the current repository
baseline.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The repository already contains a strict exact-paper branch under
`scripts/paper_reimplementation/rcim_ml_compensation/` that reproduces the
paper family bank, the recovered input schema `rpm, deg, tor`, the exact
`ampl_k` / `phase_k` target set, and the per-target ONNX export surface.

However, the current exact branch is still organized as a family-wise
validation flow that emits:

- a family-level aggregate ranking;
- a target-wise winner registry;
- an exact-paper support export surface.

That is close to the paper workflow, but it is not yet the final repository
closure criterion requested for `Track 1`.

This task should therefore promote the exact-paper branch from a generic
family-bank validation into a per-harmonic replication workflow with these
properties:

1. preserve the recovered paper family inventory and hyperparameters;
2. keep the exact paper feature schema and target schema;
3. materialize canonical per-target comparison artifacts for every harmonic
   component;
4. serialize a repository-owned `paper vs repository` comparison table that
   makes the closure status inspectable;
5. report explicit `matched` / `not_matched` status per harmonic target and
   aggregate `Track 1` closure status from that table.

The current implementation uses `MultiOutputRegressor`, which fits one
independent regressor per target. Based on current scikit-learn documentation,
that wrapper is valid when one independent estimator per target is intended,
but it does not model cross-target correlation. For the repository, this means
the existing exact branch can remain operationally useful while still exposing
per-target estimators. The missing step is therefore not a mandatory switch in
estimator semantics, but canonical per-target artifact generation and paper
table comparison.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `doc/README.md`

## Implementation Steps

1. Add a canonical repository-owned representation of the paper per-harmonic
   target expectations so the exact branch can compare repository results
   against the paper table directly.
2. Extend the exact-paper support module to build stable per-target comparison
   artifacts from the held-out validation results already produced by the exact
   family bank.
3. Emit a canonical summary table that records, for each target, the paper
   expected model family or family set, the repository winning family, the
   repository target metric, and the current `matched` / `not_matched` status.
4. Emit a higher-level per-harmonic closure table that collapses the amplitude
   and phase target evidence into a single harmonic-facing status when the
   paper comparison is expressed at the harmonic level.
5. Update the exact-paper Markdown validation report so the per-target and
   per-harmonic paper-comparison results are visible without reading only raw
   YAML.
6. Run the exact-paper validation workflow to regenerate the canonical output
   artifacts if the code changes require fresh validation evidence.
7. Run Markdown warning checks on the touched Markdown files and confirm clean
   trailing newline state before closing the task.
