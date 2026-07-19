# Simplified Dataset Model Artifacts

This folder contains the historical simplified or pre-polished model artifacts
under an explicit dataset-local root.

## Contents

- `paper_reference/`
  Historical simplified paper-reference archives, including `rcim_original`,
  `rcim_retuned`, and `rcim_track1`.
- `setpoints/`
  Curated best model-development exports for the simplified setpoint-input
  branch. Each model family and surface is stored as
  `<model_family>/<surface>/` with provenance in the leaf
  `reference_inventory.yaml`.

## Contract

Artifacts in this tree are kept separate from polished-dataset artifacts.
