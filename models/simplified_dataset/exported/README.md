# Exported Model Archive

This folder stores curated deployment-facing exports copied from completed
training artifacts together with provenance needed to trace each promoted
winner.

## Wave 1 Directional HPO Archive

- Source campaign: `wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11`
- Surface contract: one family folder, then `global/`, `forward/`, and `backward/`.
- Each scope folder exposes both `python/` and `onnx/` copies of the HPO-selected winner.
- Machine-readable inventory: `models\exported\wave1_directional_hpo_export_inventory.yaml`

## Family Folders

- `tree/global/`
- `tree/forward/`
- `tree/backward/`
- `harmonic_regression/global/`
- `harmonic_regression/forward/`
- `harmonic_regression/backward/`
- `feedforward/global/`
- `feedforward/forward/`
- `feedforward/backward/`
- `periodic_mlp/global/`
- `periodic_mlp/forward/`
- `periodic_mlp/backward/`
- `residual_harmonic_mlp/global/`
- `residual_harmonic_mlp/forward/`
- `residual_harmonic_mlp/backward/`
