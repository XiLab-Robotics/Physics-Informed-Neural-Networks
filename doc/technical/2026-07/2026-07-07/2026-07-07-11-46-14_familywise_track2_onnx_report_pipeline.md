# Familywise TE Curve Verification ONNX Report Pipeline

## Overview

This document defines a dedicated familywise `TE Curve Verification Pipeline`
report workflow for the dataset input-mode retraining program introduced by
commit `6b050b99cc250b264f379209164f5583191cb0a2`.

The first target family is `tree`, after completion and export of these three
campaign groups:

- `simplified_dataset` with `setpoints`;
- `polished_dataset` with `setpoints`;
- `polished_dataset` with `actual_values`.

Each group currently exposes three exported `tree` ONNX models under `models/`:
`global`, `forward`, and `backward`. The report workflow must load those ONNX
models from their inventory paths, evaluate them against the dataset-matched
held-out test curves, compute curve-level metrics for each model, and generate
human-browsable report bundles grouped by model family.

This workflow is separate from the protected official full directional matrix.
It should not modify
`config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
unless a later approval explicitly expands the scope.

No Codex subagent is planned for the first implementation pass.

## Technical Approach

Create a repository-owned familywise report pipeline that discovers exported
model-development artifacts from:

- `models/simplified_dataset/setpoints/exported/model_development_export_inventory.yaml`;
- `models/polished_dataset/setpoints/exported/model_development_export_inventory.yaml`;
- `models/polished_dataset/actual_values/exported/model_development_export_inventory.yaml`.

The pipeline will accept a `--model-family tree` argument and, later, any other
family once its three dataset/input-mode campaign groups have finished and their
ONNX exports exist.

For each dataset/input-mode group, the pipeline will:

1. validate that exactly one `global`, one `forward`, and one `backward` ONNX
   entry exist for the requested family;
2. load each ONNX model through ONNX Runtime using CPU execution unless the
   repository later adds an explicit provider option;
3. build the dataset-matched test curve records with existing
   `transmission_error_dataset` and `reference_family_vs_feedforward_support`
   helpers;
4. evaluate `forward` models only on forward curves, `backward` models only on
   backward curves, and `global` models on both forward and backward curves;
5. compute per-curve and aggregate metrics including at least curve `MAE`,
   curve `RMSE`, mean percentage error, P95 mean percentage error, signed mean
   offset, absolute mean offset, and peak-to-peak error;
6. select configurable deterministic representative curves per requested page,
   favoring readable coverage across speed, torque, oil temperature, direction,
   and error regimes;
7. generate one configurable collage page for `forward`, one for `backward`, and
   one for `global` for each dataset/input-mode group;
8. write the exact model identifiers and ONNX paths into the Markdown report
   and machine-readable summary.

The report folder will be organized for human browsing under:

`doc/reports/analysis/te_curve_verification_pipeline/03_family_reports/<family>/[YYYY-MM-DD]/`

The machine-readable artifacts will be stored under:

`output/validation_checks/track2_familywise_onnx_report/<family>/<run_instance_id>/`

The `tree` report bundle should include these sections in this order:

1. `simplified_dataset` + `setpoints`;
2. `polished_dataset` + `setpoints`;
3. `polished_dataset` + `actual_values`.

Each section should contain:

- a model inventory table with `run_name`, `run_instance_id`, `surface`,
  `dataset_schema`, `input_mode`, `onnx_model_path`, and `python_model_path`;
- an aggregate metrics table for the three surface models;
- one `forward` configurable curve collage page;
- one `backward` configurable curve collage page;
- one `global` configurable curve collage page;
- links to per-curve CSVs and the validation summary YAML.

The report is diagnostic and family-specific. It should not promote or reject
official winners by itself. If a later official decision is needed, it must
flow through the multi-index curve-first selection policy and the official
decision report path.

## Involved Components

- `models/<dataset>/<input_mode>/exported/model_development_export_inventory.yaml`
  provides the authoritative ONNX and source-run paths.
- `models/<dataset>/<input_mode>/exported/<family>/<surface>/<run_instance_id>/`
  provides the concrete ONNX, Python model, reference inventory, and source-run
  snapshots to cite in the report.
- `data/simplified_dataset` must be used for `simplified_dataset` reports.
- `data/polished_dataset` must be used for both polished report groups.
- `scripts/datasets/transmission_error_dataset.py` provides dataset loading
  and dataset-name normalization.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  provides existing curve-record construction and metric utilities where
  reusable.
- `scripts/reports/analysis/track2_circular_plotting.py` provides circular TE
  plotting helpers for wrap-safe curve visuals.
- A new report script under `scripts/reports/analysis/` will own the
  familywise ONNX evaluation and report generation entry point.
- A new PowerShell launcher under `scripts/campaigns/track_2/` can provide a
  repeatable local and `-Remote` operator command if the first script-level
  implementation needs to run on Aries or another workstation.
- A launcher note under `doc/scripts/campaigns/track_2/` will be added if a
  dedicated launcher is created.
- `doc/guide/project_usage_guide.md` and the Sphinx `site/` tree must be
  updated if the approved implementation adds a durable user-facing command.

The current protected campaign-state list includes prior polished refresh
files. The planned first pass avoids those protected paths. If implementation
requires editing any file listed in `doc/running/active_training_campaign.yaml`,
the work must stop with a `CRITICAL WARNING` and wait for explicit approval.

## Implementation Steps

1. Reconfirm `doc/running/active_training_campaign.yaml`, the `models/`
   inventories, and `git status --short` before implementation.
2. Implement the familywise ONNX report script with explicit arguments for
   family, report date, curves per page, dataset/input-mode groups, output
   root, and report root.
3. Add inventory validation that fails fast when a required ONNX path is
   missing, duplicated, or not exported.
4. Add ONNX Runtime loading with input/output name introspection and strict
   feature-width checks against the selected dataset/input-mode contract.
5. Reuse existing dataset and curve-record helpers for dataset-matched held-out
   test curves.
6. Compute per-curve metrics and aggregate metrics for each model and surface.
7. Generate configurable curve collage PNGs and copy report-local assets beside the
   Markdown bundle.
8. Write the familywise Markdown report, summary YAML, per-curve CSVs, and
   model inventory CSV.
9. Add a dedicated launcher and launcher note only if needed for repeatable
   local or `-Remote` execution.
10. Run the pipeline for `tree` only after the technical document is approved.
11. Export and validate the report PDF if the approved scope treats this as a
   final analytical report deliverable rather than a Markdown-only diagnostic.
12. Run `py_compile` for modified Python files, Markdown warning checks for
   touched Markdown, and Sphinx validation if user-facing docs or portal scope
   are updated.
13. Stop after reporting completion. Do not create a Git commit until the user
   explicitly approves it.
