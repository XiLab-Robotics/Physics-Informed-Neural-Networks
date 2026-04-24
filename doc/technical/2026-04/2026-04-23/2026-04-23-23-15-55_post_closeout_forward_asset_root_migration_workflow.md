# Post-Closeout Forward Asset Root Migration Workflow

## Overview

This document formalizes the deferred post-closeout workflow required to
rename the current RCIM recovered-asset root and to update the still-protected
 campaign and operational path references after the active exact-paper
 `Track 1` campaign is closed.

The repository documentation is now being updated to state that the current
recovered asset package is forward-only. However, the physical root path still
uses the legacy name `reference/rcim_ml_compensation_recovered_assets/`
because the active campaign references that path directly in protected
configuration files. Renaming the root before closeout would create an
inconsistent running state.

## Technical Approach

The migration must be executed only after the active campaign has completed and
its protected files are no longer locked by campaign governance. The intended
target is to move from the current legacy root name to a forward-explicit root
such as:

- `reference/rcim_ml_compensation_recovered_assets/`

The post-closeout migration must be treated as one coherent operation:

- rename the physical asset root;
- update every repository reference that still points to the legacy root;
- explicitly preserve the meaning that the current recovered model bank,
  recovered CSV, and recovered ONNX release are forward-only assets;
- re-run documentation and configuration validation so no stale path remains.

This workflow must not modify active-campaign files before the campaign status
is no longer `running` or `prepared`.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/`
- `reference/README.md`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Recovered Asset Deep Analysis.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/`
- `models/paper_reference/rcim_track1/`
- `output/validation_checks/track2_reference_comparison/`
- Any remaining `site/`, `doc/`, `config/`, `models/`, or `scripts/`
  references to the legacy asset-root path

## Implementation Steps

1. Confirm that `doc/running/active_training_campaign.yaml` no longer marks the
   exact-paper `Track 1` campaign as `running` or `prepared`.
2. Read the campaign state and identify the previously protected config and
   launcher files that still reference
   `reference/rcim_ml_compensation_recovered_assets/`.
3. Rename the physical root to the forward-explicit target path.
4. Update path references in campaign YAMLs, baselines, support modules,
   archived training snapshots, model-reference manifests, documentation, and
   Sphinx-facing pages.
5. Run a repository-wide search for the legacy path string and resolve all
   remaining intentional or stale references.
6. Run the touched Markdown QA scope and the relevant Python verification
   commands for any updated operational scripts.
7. Report the migration outcome and only then consider a Git commit if the
   user explicitly asks for it.
