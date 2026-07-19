# Model Artifact Folder

This folder stores model artifacts under explicit dataset roots. Top-level
artifact buckets such as `paper_reference/`, `exported/`, and `checkpoints/`
are intentionally not used here, so polished and simplified artifacts cannot be
mixed by path.

## Dataset Roots

- `polished_dataset/`
  Contains artifacts trained or exported against `data/polished_dataset` with
  schema `polished_point_v1`.
- `simplified_dataset/`
  Contains the historical simplified or pre-polished artifacts copied into an
  explicit dataset-local root.

## Current Layout

- `polished_dataset/paper_reference/rcim_track1/`
  Official polished RCIM Model-Bank Reproduction archives split by input mode.
  `setpoints/` and `actual_values/` each contain `global`, `forward`, and
  `backward` surfaces with 570 ONNX files and 570 Python pickle files.
- `polished_dataset/setpoints/`
  Curated best model-development exports for the polished setpoint branch.
  Leaf folders use `<model_family>/<surface>/` directly and keep source-run
  provenance in `reference_inventory.yaml`.
- `polished_dataset/actual_values/`
  Curated best model-development exports for the polished actual-values branch.
  Leaf folders use `<model_family>/<surface>/` directly and keep source-run
  provenance in `reference_inventory.yaml`.
- `simplified_dataset/paper_reference/`
  Historical simplified paper-reference archives using the existing naming
  roots such as `rcim_original`, `rcim_retuned`, and `rcim_track1`.
- `simplified_dataset/setpoints/`
  Curated best model-development exports for the simplified setpoint branch.
  Leaf folders use `<model_family>/<surface>/` directly and keep source-run
  provenance in `reference_inventory.yaml`.

Project-authored Python source code lives under `scripts/`, not under
`models/`.
