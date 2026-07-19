# Polished Dataset Model Artifacts

This folder contains curated model artifacts trained or exported against
`data/polished_dataset` with schema `polished_point_v1`.

New input-mode retraining artifacts must be separated by operating-variable
mode under dataset-local subfolders, especially `setpoints/` and
`actual_values/`. The current `polished_point_v1` actual-values training
contract uses five inputs:

```text
theta, theta_dot, tau_load, T, direction_flag
```

## Contents

- `paper_reference/rcim_track1/`
  Polished RCIM Model-Bank Reproduction archive, split into `forward/` and
  `backward/` direction roots.
- `setpoints/`
  Curated best model-development exports for the setpoint-input branch. Each
  model family and surface is stored as `<model_family>/<surface>/` with
  provenance in the leaf `reference_inventory.yaml`.
- `actual_values/`
  Curated best model-development exports for the actual-values input branch.
  Each model family and surface is stored as `<model_family>/<surface>/` with
  provenance in the leaf `reference_inventory.yaml`.

## Contract

Artifacts in this tree must come from `polished_dataset` sources only. Do not
place historical simplified artifacts in this root.
