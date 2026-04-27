# Overview

This technical document defines a dedicated repository workflow to make the
recovered original RCIM paper material runnable without modifying the archived
reference files under:

- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`

The goal is to create a repository-owned execution surface under `scripts/`
that uses copied working material derived from those references, keeps the
original evidence preserved, and makes the staged paper workflow runnable from
inside this repository.

The second goal is to produce a code-level comparison surface between:

- the recovered original workflow; and
- the current repository reimplementation under
  `scripts/paper_reimplementation/rcim_ml_compensation/`.

This task is not yet a new training campaign. It is a workflow-reconstruction
and implementation-audit task that should produce a stable runnable sandbox
plus a documented list of material differences.

## Technical Approach

The implementation will preserve a strict separation between immutable
reference evidence and runnable repository-owned copies.

The planned direction is:

1. keep `reference/rcim_ml_compensation_recovered_assets/...` read-only as the
   canonical evidence surface;
2. create a dedicated script subtree that contains repository-owned copies of
   the relevant original pipeline files;
3. add a thin repository wrapper layer around those copies so the staged flow
   can be run from the project root with explicit inputs and output roots;
4. verify the runnable copy path stage by stage:
   - dataframe creation;
   - prediction/export;
   - evaluation;
5. audit the runnable original path against the current repository
   reimplementation by mapping:
   - dataset assumptions;
   - feature and target schema;
   - family registry and hyperparameters;
   - train/test split behavior;
   - export logic;
   - evaluation outputs;
   - artifact layout.

The working assumption is that the recovered `original_pipeline/` subtree is
the best source for the staged paper workflow, while `latest_snapshot/`
provides the shipped forward dataframe, a later narrowed predictor surface, and
useful execution evidence for the same family bank.

The repository-owned runnable subtree should not be a blind raw dump. It should
preserve the paper-era logic as closely as practical while adding the minimum
wrappers and path normalization needed to execute it safely in this repo.

## Involved Components

Primary reference inputs:

- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- `doc/reports/analysis/RCIM Recovered Asset Deep Analysis.md`
- `doc/technical/2026-04/2026-04-10/2026-04-10-16-12-21_rcim_exact_model_reimplementation_plan.md`

Current repository implementation surface to compare against:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`

Planned new repository-owned runnable surface:

- a dedicated subtree under `scripts/` containing copied original-pipeline
  files;
- a matching note under `doc/scripts/` that explains how to run the recovered
  workflow copies;
- optional lightweight config or wrapper files needed to launch the copied
  stages reproducibly from the repository root.

No subagent use is planned. If that changes later, explicit user approval will
be requested before any launch.

## Implementation Steps

1. Create a dedicated repository-owned subtree under `scripts/` for the copied
   RCIM original workflow material, keeping the reference roots untouched.
2. Copy the minimum relevant files from `original_pipeline/` and
   `latest_snapshot/` into that subtree with a structure that still mirrors the
   recovered staged flow.
3. Add thin repository wrappers or path guards so the copied workflow can run
   from the repository root without editing the archived reference copies.
4. Smoke-check the runnable copied workflow and record which stages already run
   unchanged and which require compatibility shims.
5. Build a structured code-difference audit between the runnable copied
   original workflow and the current repository reimplementation.
6. Summarize the material differences in a repository document, with emphasis
   on behavioral differences rather than only file diffs.
7. If the runnable copied workflow is stable enough, expose one canonical
   launch command and one canonical output root for future validation use.
