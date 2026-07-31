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
  provenance in `reference_inventory.yaml`. The aggregate inventory currently
  contains 113 leaves: 39 forward, 37 backward, and 37 global.
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

## Post-Retraining Curated Additions

The 2026-07-31 refresh added only five Wave 5.2R leaves:

- K01 seed `271828` for `forward`, `backward`, and `global`, classified as the
  cross-surface temporal offline leader;
- H08 seed `161803` for `forward` only, classified as a non-temporal forward
  specialist;
- Stage 15 H04 for `forward` only, classified as an exploratory compact
  grey-box specialist.

Every leaf includes a checkpoint, ONNX model, source-run snapshots, parity
evidence, hashes, role, acceptance status, and known limitations. Archive
presence does not imply TwinCAT runtime qualification. K01 and H08 still
require TwinCAT runtime evidence, while H04 has only static float32
PLC-reference parity and still requires TwinCAT compilation and runtime replay.

Rebuild and validate this exact curated promotion outside `models/` with:

```powershell
conda run --no-capture-output -n pinns_env python scripts/models/export_post_retraining_selected_model_archives.py
```

Use `--promote` only when the three destination family roots do not already
exist. The selection rationale, deferred research components, and future
restart rule are recorded in the associated post-retraining technical
document under `doc/technical/2026-07/2026-07-31/`.

Validate the installed aggregate inventory, all artifact paths, and the hashes
available for the five new leaves with:

```powershell
conda run --no-capture-output -n pinns_env python scripts/models/export_post_retraining_selected_model_archives.py --validate-existing
```
