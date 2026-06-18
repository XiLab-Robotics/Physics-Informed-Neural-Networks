# Wave 1 Directional HPO Closeout And Export Refresh

## Overview

The `Wave 1` directional best-hyperparameter search campaign has completed and
its training artifacts were committed in `5cf40ebe2f3625f6e202237d4ed06265f5b9659c`.

The closeout must consolidate both campaign phases:

- bounded grid search for the `6` non-neural `tree` and
  `harmonic_regression` surfaces;
- persisted `Optuna` search for the `9` neural surfaces.

The closeout must also verify that every one of the `15` directional surfaces
has best hyperparameters and that the selected model artifacts are available in
the expected Python-native and ONNX deployment formats.

## Technical Approach

Use the committed campaign artifacts as the source of truth:

- bounded-grid results from
  `output/training_campaigns/wave1/directional_best_hyperparameter_search/2026-05-11-20-07-44_wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_1/`;
- neural `Optuna` study outputs from
  `output/training_campaigns/wave1/directional_best_hyperparameter_search/wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11/optuna_studies/`;
- family registries under `output/registries/families/`;
- current curated deployment archive under `models/exported/`.

The initial audit shows that `best_trial.yaml` / registry sources exist for all
`15` surfaces. It also shows that ONNX files are not stored inside the
individual training-run directories; the deployment-facing ONNX surface is the
curated `models/exported/` archive. Therefore, closeout must refresh or
validate `models/exported/` against the newly selected HPO winners instead of
treating the old directional-retraining archive as automatically current.

The report should distinguish two related but different winner concepts:

- HPO winner per surface, selected by that search surface's objective or grid
  policy;
- canonical family-best winner, selected by the repository family-registry
  policy.

This distinction matters because the global `feedforward` `Optuna` study
completed and has best hyperparameters, but the family registry still points to
the earlier global feedforward directional retraining model because that model
keeps the better canonical family-best score.

## Involved Components

- `doc/reports/campaign_results/wave_1/`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `models/exported/`
- `models/README.md`
- `scripts/reports/closeout/wave1/`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `output/training_campaigns/wave1/directional_best_hyperparameter_search/2026-05-11-20-07-44_wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_1/`
- `output/training_campaigns/wave1/directional_best_hyperparameter_search/wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11/`
- `output/registries/families/`
- `output/registries/program/`

## Implementation Steps

1. Build a closeout audit that loads all `15` surfaces, including bounded-grid
   winners and `Optuna` study winners.
2. Verify best hyperparameters for all `15` surfaces and record them in the
   campaign-results report.
3. Verify native Python model artifacts: `tree` surfaces require `.pkl`, while
   `harmonic_regression` and all neural surfaces require `.ckpt`.
4. Refresh the curated `models/exported/` archive so every HPO-selected surface
   has the correct Python-native artifact and ONNX export.
5. Generate the final campaign-results Markdown report and PDF companion.
6. Update canonical analysis surfaces that summarize the campaign outcome.
7. Run scoped Markdown QA and PDF validation on the generated deliverables.
8. Report completion and wait for explicit commit approval before creating any
   Git commit.
