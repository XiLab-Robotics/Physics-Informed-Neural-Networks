# Polished Dataset Model Artifacts

This folder contains curated model artifacts trained or exported against
`data/polished_dataset` with schema `polished_point_v1`.

## Contents

- `paper_reference/rcim_track1/`
  Polished RCIM Model-Bank Reproduction archive, split into `forward/` and
  `backward/` direction roots.
- `exported/`
  Model-development export archive built from the completed polished early-wave
  and full-wave campaigns. The summary inventory records 144 runs:
  48 `global`, 48 `forward`, and 48 `backward`.
- `artifact_inventory.yaml`
  Dataset-local inventory with artifact counts and source provenance.

## Contract

Artifacts in this tree must come from `polished_dataset` sources only. Do not
place historical simplified artifacts in this root.
