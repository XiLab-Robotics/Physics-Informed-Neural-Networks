# Tree Regression Training Script

## Overview

This script is the tree-based structured-baseline training entry point for the Transmission Error project.

It trains the current tabular `scikit-learn` baselines under the same artifact and registry conventions used by the neural workflows.

The script is stored in:

- `scripts/training/train_tree_regressor.py`

## Main Role

The script coordinates the static tree-regression workflow:

1. load the YAML training configuration;
2. build the TE dataset splits through the shared datamodule path;
3. flatten the curve datasets into point-wise NumPy arrays;
4. instantiate the requested tree estimator;
5. fit the estimator on the train split;
6. evaluate validation and test splits;
7. save the serialized model, the common metrics snapshot, and the markdown report;
8. update the family and program best-result registries.

## Main Components Used

### `scripts/training/tree_regression_support.py`

Provides:

- curve-dataset flattening into tabular arrays;
- estimator construction for the supported tree families;
- common metric computation;
- serialized model save/load helpers;
- metrics snapshot helpers aligned with the shared artifact schema.

### `scripts/training/transmission_error_datamodule.py`

Reuses the current TE dataset split logic so the tree baselines see the same train, validation, and held-out test curves used by the neural models.

### `config/training/wave1_structured_baselines/campaigns/...`

Provides the current Wave 1 tree candidates, including:

- `random_forest`
- `hist_gradient_boosting`

## Outputs

The script writes its outputs under the configured training-run root, currently:

- `output/training_runs/tree/`

Typical generated artifacts include:

- `training_config.yaml`
- `run_metadata.yaml`
- `tree_model.pkl`
- `metrics_summary.yaml`
- `training_test_report.md`
- updated family/program registries under:
  - `output/registries/families/tree/`
  - `output/registries/program/`

Each physical run writes into an immutable directory such as:

- `output/training_runs/tree/2026-03-17-21-35-00__te_tree_random_forest/`

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_tree_regressor.py `
  --config-path config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/09_random_forest_tabular.yaml
```

Use this script when:

- the selected configuration uses `experiment.model_type: random_forest`;
- the selected configuration uses `experiment.model_type: hist_gradient_boosting`;
- the campaign runner dispatches a tree model type automatically.

The script shares the same comparison and registry contract used by the neural runs, so the tree baselines can be ranked directly against the other Wave 1 structured candidates.
