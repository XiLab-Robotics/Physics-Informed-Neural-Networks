# Dataset-Separated Model Artifact Roots

> Superseded in part by
> `doc/technical/2026-07/2026-07-06/2026-07-06-14-47-17_hard_dataset_model_archive_migration.md`.
> The dataset-root creation remains valid, but the compatibility-preserving
> decision to keep duplicate top-level `models/exported/`,
> `models/paper_reference/`, and `models/checkpoints/` roots has been replaced
> by a strict dataset-first migration requirement.

## Overview

Create explicit dataset-separated model artifact roots under `models/` so the
polished-dataset models are physically separate from the earlier simplified or
historical model artifacts.

The requested target layout is:

- `models/polished_dataset/`
- `models/simplified_dataset/`

The immediate goal is to make the polished RCIM Model-Bank Reproduction ONNX
exports easy to identify and impossible to confuse with the older simplified
or paper-reference model archives. The work must preserve traceability back to
the source validation runs and avoid silently overwriting existing model
folders.

No subagent is planned for this implementation.

## Technical Approach

The implementation will create dataset-named roots under `models/` and place
curated model artifacts below those roots. The first pass will avoid deleting
or moving existing legacy-compatible folders such as `models/exported/` and
`models/paper_reference/`; instead, it will copy or mirror the accepted
artifacts into the explicit dataset roots and update documentation to mark the
dataset roots as the preferred human-facing structure.

The polished RCIM ONNX exports will be copied from the completed polished
validation outputs:

- forward source:
  `output/validation_checks/rcim_model_bank_reproduction/2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation/`
- backward source:
  `output/validation_checks/rcim_model_bank_reproduction/2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation/`

The polished destination will keep forward and backward surfaces separate, for
example:

- `models/polished_dataset/paper_reference/rcim_model_bank_reproduction/forward/`
- `models/polished_dataset/paper_reference/rcim_model_bank_reproduction/backward/`

Each polished surface should include at least:

- `onnx/` copied from the source `onnx_export/` tree;
- `python/` copied from the source `python_export/` tree when present;
- provenance files copied from the source run, including
  `training_config.yaml`, `validation_summary.yaml`, and
  `best_parameter_summary.yaml`;
- a small README explaining dataset identity, source run, direction surface,
  and file counts.

The simplified destination will provide an explicit home for the current
simplified or historical model artifacts already under `models/`, for example:

- `models/simplified_dataset/exported/`
- `models/simplified_dataset/paper_reference/`

This pass will preserve the existing top-level `models/exported/` and
`models/paper_reference/` paths for compatibility unless the user explicitly
approves a later hard migration.

## Involved Components

- `models/README.md`
- `models/exported/`
- `models/paper_reference/`
- `models/polished_dataset/`
- `models/simplified_dataset/`
- polished RCIM source validation directories under
  `output/validation_checks/rcim_model_bank_reproduction/`
- `doc/README.md`

The active campaign state was checked before this document was written. The
campaign is marked completed, and this task should not modify the protected
campaign files listed in `doc/running/active_training_campaign.yaml`.

## Implementation Steps

1. Re-check `git status` and the polished source validation directories after
   approval.
2. Create `models/polished_dataset/` and `models/simplified_dataset/` with
   README files describing the dataset contract.
3. Copy the polished forward and backward RCIM ONNX export trees into
   `models/polished_dataset/paper_reference/rcim_model_bank_reproduction/`.
4. Copy polished provenance files beside each curated surface.
5. Mirror the current simplified or historical model artifact roots into
   `models/simplified_dataset/` without deleting the legacy-compatible top
   level roots.
6. Add or update inventories with file counts and source paths so the polished
   and simplified roots are auditable.
7. Update `models/README.md` so the preferred layout is dataset-first and the
   legacy-compatible roots are clearly documented.
8. Run a file-count verification comparing polished source ONNX counts against
   the curated polished destinations.
9. Run Markdown QA on touched Markdown files.
10. Stop before any commit and report the resulting artifact layout for user
    review.
