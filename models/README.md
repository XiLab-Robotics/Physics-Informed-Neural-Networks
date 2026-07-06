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
  Polished RCIM Model-Bank Reproduction paper-reference archive. It contains
  the compatible forward and backward RCIM banks retrained or validated against
  the polished dataset.
- `polished_dataset/exported/`
  Polished model-development exports from the completed 36-run early-wave and
  108-run full-wave campaigns. The inventory records 144 run archives:
  48 `global`, 48 `forward`, and 48 `backward`, each with a Python artifact and
  ONNX export.
- `simplified_dataset/paper_reference/`
  Historical simplified paper-reference archives using the existing naming
  roots such as `rcim_original`, `rcim_retuned`, and `rcim_track1`.
- `simplified_dataset/exported/`
  Historical simplified model-development exports that were already present in
  the repository artifact root before this dataset split.

Project-authored Python source code lives under `scripts/`, not under
`models/`.
