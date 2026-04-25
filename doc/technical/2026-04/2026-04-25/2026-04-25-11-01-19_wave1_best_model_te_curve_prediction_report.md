# Wave 1 Best Model TE Curve Prediction Report

## Overview

This document plans a non-training evaluation workflow that loads the current
best model from each completed `Wave 1` model family, runs those models on a
held-out TE-curve subset, plots predicted TE curves against the measured TE
curves, and writes a comparison report.

The workflow must not start a new training campaign. It is an offline
evaluation and visualization pass over existing model artifacts and the
canonical Wave 1 dataset split.

## Technical Approach

The implementation will use the family registries under
`output/registries/families/*/latest_family_best.yaml` as the source of truth
for model selection instead of hardcoding run names. The current Wave 1
families are:

| Family | Best Run | Model Type |
| --- | --- | --- |
| `tree` | `te_hist_gbr_tabular` | `hist_gradient_boosting` |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` |
| `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | `feedforward` |
| `periodic_mlp` | `te_periodic_mlp_h04_standard` | `periodic_mlp` |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | `harmonic_regression` |

The script will preserve the existing Wave 1 split semantics. The working
interpretation of "20% del dataset di test" is: sample 20% of the canonical
Wave 1 test-curve subset for plotting. This avoids changing the split used by
the already-trained family-best models. If the intended meaning is a new test
split equal to 20% of the full dataset, the implementation must be adjusted
before approval because that would create a different comparison surface.

Before implementing library-specific loading and inference code, Context7 must
be queried for the current PyTorch, PyTorch Lightning, NumPy, scikit-learn, and
Matplotlib API details that affect checkpoint loading, tensor conversion,
model evaluation mode, and plotting/export behavior.

The script should generate one timestamped artifact directory containing:

- a machine-readable prediction summary;
- per-curve CSV files with angle, measured TE, and each model prediction;
- comparison plots with all model predictions overlaid against the measured TE
  curve;
- a Markdown analysis report summarizing selected curves, model sources, and
  aggregate curve-error metrics.

## Involved Components

- `config/datasets/transmission_error_dataset.yaml`
- `scripts/datasets/transmission_error_dataset.py`
- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/tree_regression_support.py`
- `scripts/models/model_factory.py`
- `output/registries/families/*/latest_family_best.yaml`
- `output/training_runs/<family>/<run_instance_id>/`
- planned script: `scripts/reports/plot_wave1_best_model_te_curves.py`
- planned artifacts:
  `output/validation_checks/wave1_best_model_te_curve_prediction/<run_instance_id>/`
- planned report:
  `doc/reports/analysis/wave1_best_model_te_curve_prediction/[2026-04-25]/wave1_best_model_te_curve_prediction_report.md`

## Implementation Steps

1. Verify the active campaign state remains non-running and do not touch
   protected campaign files.
2. Query Context7 for the relevant PyTorch, PyTorch Lightning, NumPy,
   scikit-learn, and Matplotlib API details before writing inference code.
3. Inspect the existing dataset loader, datamodule, model factory, tree
   loading support, and any existing curve-comparison report scripts to reuse
   established repository behavior.
4. Add a reusable script that resolves family-best registries, loads each
   model artifact, reconstructs the canonical test-curve subset, samples 20%
   of those curves by deterministic seed, and predicts TE over each curve.
5. Export per-curve plots, per-curve prediction tables, aggregate metrics, and
   a Markdown report under the planned artifact and report locations.
6. Run a narrow smoke execution against a small curve count first, then run the
   requested 20% test-curve evaluation if dependencies and artifacts are
   present.
7. Run Markdown warning checks on touched authored Markdown files and verify
   final newline hygiene.
8. Stop after implementation and verification; do not create a Git commit
   until explicitly approved.

No subagent is planned for this implementation. If a subagent becomes useful,
the exact delegated scope must be declared and approved before launch.
