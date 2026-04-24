# RCIM Forward Backward Artifact Reorganization And Generic Recovered Root Restore

## Overview

The current repository state over-specializes the recovered RCIM asset root.
The folder
`reference/rcim_ml_compensation_recovered_assets/` now implies that
all recovered code and generic recovered material are forward-only, which is
too strong. The recovered package contains generic recovered code snapshots and
paper-era auxiliary material; only specific artifacts such as the current
exact-paper model bank, the shipped `Fw` dataframe, and the current repository
reimplementation outputs are forward-specific.

The repository therefore needs a second-pass reorganization with two goals:

1. restore the generic recovered root naming under
   `reference/rcim_ml_compensation_recovered_assets/`;
2. propagate the real `forward` versus future `backward` separation into the
   artifact surfaces that are actually direction-specific:
   campaigns, validation reports, campaign results, paper-reference models,
   and output roots.

This work is larger than a pure rename. It is a taxonomy correction across the
paper-reimplementation surfaces so future backward work can be added cleanly
without mixing unrelated files in flat directories.

## Technical Approach

The reorganization should be executed as one coherent repository migration.
The guiding rule is:

- generic recovered source material stays under the generic recovered root;
- direction-specific outputs, model banks, campaign configs, reports, and
  validation artifacts are split explicitly into `forward` and `backward`
  branches where appropriate.

The first rollback step is to restore:

- `reference/rcim_ml_compensation_recovered_assets/`

and remove the over-specific physical root name introduced in the previous
migration.

Then the direction-specific separation should be applied to the repository
artifact surfaces. The current forward work completed so far is the strict
paper-side `10 x 19` forward branch. That means the immediate taxonomy should
reserve sibling space for future backward work rather than encoding everything
into one flat folder.

The intended design is:

- generic recovered source package under `reference/`;
- direction-specific campaign config branches under
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/`;
- direction-specific validation report branches under
  `doc/reports/analysis/validation_checks/`;
- direction-specific campaign-result branches under
  `doc/reports/campaign_results/track1/`;
- direction-specific paper-reference model branches under
  `models/paper_reference/rcim_track1/`;
- direction-specific output branches under
  `output/training_campaigns/` and `output/validation_checks/`.

This migration should also improve folder fan-out. The current exact-paper
validation-report surface still contains many flat report files directly under
`doc/reports/analysis/validation_checks/` and large monolithic folders under
`track1/exact_paper/`. These should be regrouped by domain and by related run
bundles so the directory layout remains navigable.

Finally, the technical note should explicitly capture one backlog consequence:
future backward exact-paper data should be rebuilt from the original dataset
under `data/datasets/`, and the paper-reference model paths and manifests must
be prepared for that future branch now.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/`
- `reference/rcim_ml_compensation_recovered_assets/`
- `reference/README.md`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/`
- `doc/reports/analysis/validation_checks/`
- `doc/reports/campaign_results/track1/`
- `models/paper_reference/rcim_track1/`
- `output/training_campaigns/`
- `output/validation_checks/`
- `scripts/paper_reimplementation/rcim_ml_compensation/`
- `scripts/reports/`
- `doc/reference_summaries/`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/guide/project_usage_guide.md`
- `site/`

## Implementation Steps

1. Restore the recovered generic root from
   `reference/rcim_ml_compensation_recovered_assets/` back to
   `reference/rcim_ml_compensation_recovered_assets/`, and update the
   recovered-root documentation so it distinguishes generic recovered assets
   from direction-specific artifacts.
2. Define the canonical forward/backward taxonomy for exact-paper artifacts.
   The current forward branch should become the canonical first branch and the
   backward branch should be provisioned as a reserved sibling path.
3. Reorganize
   `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
   into grouped subfolders with a direction-aware layout. The existing exact
   paper work completed so far should move under a forward-specific subtree.
4. Reorganize
   `doc/reports/analysis/validation_checks/` so flat exact-paper report files
   are grouped into sensible subfolders, and further split
   `track1/exact_paper/` into a more navigable hierarchy with explicit
   forward/backward space.
5. Reorganize `doc/reports/campaign_results/track1/` to propagate the same
   forward/backward distinction used for exact-paper campaign closeouts.
6. Reorganize `models/paper_reference/rcim_track1/` so the current `10 x 19`
   ONNX and Python model banks are explicitly stored as the forward branch,
   with reserved sibling space and manifests for future backward banks.
7. Reorganize `output/training_campaigns/` and `output/validation_checks/`,
   especially the exact-paper and harmonic-wise RCIM roots, so direction-aware
   grouping is consistent with configs, reports, and model references.
8. Update all scripts, reports, guides, Sphinx pages, manifests, and support
   modules that describe, generate, or consume these paths.
9. Add the future backlog note that backward exact-paper data should be
   rebuilt from the original dataset under `data/datasets/`, and prepare the
   model-reference path structure accordingly without implementing the backward
   data rebuild in this same task.
