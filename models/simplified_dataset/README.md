# Simplified Dataset Model Artifacts

This folder contains the historical simplified or pre-polished model artifacts
under an explicit dataset-local root.

## Contents

- `paper_reference/`
  Historical simplified paper-reference archives, including `rcim_original`,
  `rcim_retuned`, and `rcim_track1`.
- `exported/`
  Historical simplified model-development exports that were already present in
  the repository artifact root before the dataset split.
- `artifact_inventory.yaml`
  Dataset-local inventory with file counts and artifact scope notes.

## Contract

Artifacts in this tree are kept separate from polished-dataset artifacts. The
available simplified `exported/` archive is smaller than the polished
144-model-development archive because no completed simplified 48/48/48 campaign
export source was found in the current repository state during this migration.
