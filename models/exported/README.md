# Exported Model Archive

This folder stores curated deployment-facing exports copied from completed
training artifacts together with the provenance needed to trace and
reconstruct each promoted winner.

## Wave 1 Directional Retraining Archive

- Source campaign: `wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Source campaign output directory: `output/training_campaigns/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Surface contract: one family folder, then `global/`, `forward/`, and `backward/`.
- Each scope folder exposes both `python/` and `onnx/` copies of the selected winner.
- Each scope folder also carries `README.md`, `reference_inventory.yaml`, `dataset_snapshot_manifest.yaml`, and `source_runs/<run_instance_id>/` snapshots.
- Machine-readable inventory: `models/exported/wave1_directional_retraining_export_inventory.yaml`

## Family Folders

- `tree/global/`
- `tree/forward/`
- `tree/backward/`
- `residual_harmonic_mlp/global/`
- `residual_harmonic_mlp/forward/`
- `residual_harmonic_mlp/backward/`
- `feedforward/global/`
- `feedforward/forward/`
- `feedforward/backward/`
- `periodic_mlp/global/`
- `periodic_mlp/forward/`
- `periodic_mlp/backward/`
- `harmonic_regression/global/`
- `harmonic_regression/forward/`
- `harmonic_regression/backward/`
