# Models Archive Path Simplification

## Overview

This technical document plans a repository cleanup for the curated `models/`
archive tree. The current model-development exports are nested under redundant
`exported/` directories and one-run timestamp directories, for example:

`models/polished_dataset/actual_values/feedforward/backward/`

The intended canonical path is shorter and dataset/input-mode first:

`models/polished_dataset/actual_values/feedforward/backward/`

The same rule should be applied to:

- `models/polished_dataset/actual_values/`;
- `models/polished_dataset/setpoints/`;
- `models/simplified_dataset/setpoints/`.

The `models/` archive is intended to contain only the selected best model
artifact for each model family and branch. The run timestamp and run name should
remain available from each leaf `reference_inventory.yaml` rather than being
encoded as an extra directory level.

## Technical Approach

The migration should be evidence-first and manifest-driven. Before moving files,
the implementation must inventory each current leaf under the three affected
archive roots and confirm that every family/surface branch has exactly one
timestamped run directory below `exported/`.

For every validated leaf, move the contents from:

`models/<dataset>/<input_mode>/exported/<family>/<surface>/<run_id>/`

to:

`models/<dataset>/<input_mode>/<family>/<surface>/`

The migration should remove the now-empty `exported/` directories only after
the content move is verified. It should also preserve `reference_inventory.yaml`
inside each final leaf, because that file is the intended provenance source for
run id, source campaign, artifact counts, and source paths.

Repository references must be updated in the same approved implementation pass.
The reference sweep should target exact old model path patterns rather than
blindly rewriting unrelated historical prose. If scripts or reports intentionally
describe past path layouts, keep that history unless the path is used as a live
artifact reference.

No subagent is planned.

## Involved Components

Likely moved model archive roots:

- `models/polished_dataset/actual_values/`;
- `models/polished_dataset/setpoints/`;
- `models/simplified_dataset/setpoints/`.

Likely retained model archive roots:

- `models/polished_dataset/paper_reference/`;
- `models/simplified_dataset/paper_reference/`, if present;
- dataset-local `README.md` files and any non-redundant archive metadata.

Likely updated documentation and code references:

- `models/README.md`;
- `models/polished_dataset/README.md`;
- `models/simplified_dataset/README.md`;
- report builders, selected-model launchers, or registries that resolve models
  under the old `exported/` path;
- `doc/README.md` registration for this technical document.

Protected-file check:

- `doc/running/active_training_campaign.yaml` currently records a completed
  `rcim_track1` polished actual-values campaign.
- The protected campaign file list does not include the target `models/`
  model-development archive roots.
- This cleanup must not modify the listed campaign configs, launcher, launcher
  note, campaign plan, or campaign technical document without separate explicit
  approval.

## Implementation Steps

1. Create and register this technical document.
2. Wait for explicit user approval before moving archive files or rewriting
   live references.
3. Build a migration inventory for the three target archive roots, including
   source path, destination path, file count, byte count, and
   `reference_inventory.yaml` presence.
4. Refuse or stop for manual review if any destination already exists with
   conflicting content or if any family/surface has more than one timestamped
   run directory.
5. Move validated leaf contents to the shorter canonical paths.
6. Remove only empty obsolete `exported/` and timestamp directories created by
   the old layout.
7. Rewrite live repository references from the old paths to the new paths.
8. Verify that every final family/surface leaf still contains
   `reference_inventory.yaml` and the expected artifact files.
9. Run Markdown QA on touched Markdown files and path/reference checks on the
   migrated `models/` tree.
10. Stop and report completion; do not commit until the user explicitly asks.
