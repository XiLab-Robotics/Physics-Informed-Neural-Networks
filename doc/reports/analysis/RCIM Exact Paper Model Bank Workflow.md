# RCIM Exact Paper Model Bank Workflow

## Overview

This report explains the exact paper-faithful RCIM model-bank workflow now
implemented under
`scripts/paper_reimplementation/rcim_ml_compensation/`.

Its role is different from the existing repository-owned harmonic-wise branch:

- the existing harmonic-wise branch is a repository-aligned offline
  reimplementation focused on `Target A`;
- this exact model-bank branch is the stricter reproduction path derived from
  the recovered paper assets.

The goal is to recreate the original paper family bank as faithfully as the
recovered evidence allows, so the repository can later reproduce paper-style
tables per family and per target `A_k` / `phi_k`.

Important scope clarification:

- the currently recovered repository-owned exact-paper bank is the
  `forward-only` bank;
- the paper notation is generalized, but the currently recovered assets do not
  provide the backward-side bank;
- current `Track 1` exact-paper replication therefore targets the paper's
  forward tables and forward model bank only.

## What This Workflow Implements

The exact branch mirrors the recovered paper methodology:

- input features are exactly `rpm`, `deg`, and `tor`;
  In the recovered prediction CSVs, `deg` is the oil-temperature column;
- targets are harmonic-wise `ampl_k` and `phase_k`;
- the currently recovered dataframe source is `Fw` forward-only;
- the target set is the recovered RCIM harmonic bank:
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- each model family is trained through `MultiOutputRegressor`;
- the canonical training mode now applies the recovered paper-side
  `GridSearchCV` path on top of the family wrapper instead of fitting only the
  base estimator directly;
- export happens as one ONNX artifact per target and per family;
- evaluation produces both:
  - family-level aggregate metrics;
  - per-target ranking tables.

This is the closest repository-owned approximation of the recovered paper
training and export logic.

## Model Inventory

The implemented exact paper family bank is:

- `SVR`
- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

These are the families recovered from the exact paper ONNX bank.

The branch intentionally excludes `ELM` from the canonical exact-bank
implementation because `ELM` appears in one recovered training script but is
absent from the recovered exact ONNX release.

## Operating Principle

The workflow is not a direct TE-curve predictor.

Instead it does this:

1. load the recovered dataframe generated for paper-era prediction;
2. keep only rows whose `deg` value is at or below `35`, meaning oil
   temperature up to `35` degrees in the recovered original workflow;
3. keep only the exact operating-condition inputs `rpm`, `deg`, `tor`;
4. select the `20` harmonic targets made of amplitudes and phases;
5. split the dataframe with `test_size = 0.20` and `random_state = 0`;
6. wrap each family estimator with `MultiOutputRegressor`;
7. apply the recovered paper-reference `GridSearchCV` path to that wrapper;
8. keep the best recovered search result per family;
9. evaluate each family on the held-out split;
10. export one ONNX model per fitted target estimator;
11. build a target-wise winner registry.

This means one family launch is operationally simple, but internally still
produces one fitted estimator per harmonic target.

## Why The MultiOutput Strategy Matters

This design reproduces an important property of the paper workflow:

- training is organized family-wise;
- deployment is organized target-wise.

That combination is what makes the recovered ONNX bank look like a set of
single-target models even though the training code is structured around
`MultiOutputRegressor`.

Repository consequence:

- the exact branch can stay maintainable;
- the final comparison tables can still be per-target and per-family, exactly
  where the paper logic needs them.

## Advantages In This Repository

- It reproduces the recovered paper model surface more faithfully than the
  older harmonic-wise branch.
- It gives us a stable baseline for per-target winner selection.
- It creates an inspectable ONNX export bank aligned with the recovered paper
  release.
- It keeps the paper-faithful branch clearly separated from repository direct-TE
  comparison work.

## Limitations And Risks

- It depends on recovered assets rather than a perfectly frozen original
  workspace.
- It still does not reconstruct the full online compensation branch.
- It relies on optional third-party libraries for `XGBM`, `LGBM`, and ONNX
  export.
- It reproduces the paper model-bank logic, not yet the final target-wise
  winning assembly into a deployed compensation stack.

## Implemented Python Structure

### Main Entry Point

The main runner is:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

Its responsibility is to:

- load the YAML configuration;
- prepare the immutable validation artifact directory;
- build the dataframe split bundle;
- fit the family bank;
- save the model bundle;
- export the ONNX bank;
- write `validation_summary.yaml`;
- write a human-readable Markdown report.

### Support Module

The exact workflow logic lives in:

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

The key responsibilities are:

- loading the recovered dataframe;
- validating the exact feature schema;
- resolving the exact target list;
- creating the recovered family estimators with paper-derived base
  hyperparameters;
- resolving the recovered reference parameter grids;
- fitting one `MultiOutputRegressor` bank per family through the recovered
  `GridSearchCV` path;
- evaluating family-level and per-target metrics;
- exporting per-target ONNX files;
- building the canonical validation summary and report text.

## Main Functions

### Dataset Preparation

- `load_exact_model_bank_config`
- `resolve_enabled_family_list`
- `resolve_paper_input_feature_name_list`
- `load_exact_paper_dataframe`
- `resolve_target_name_list`
- `build_exact_paper_dataset_bundle`

These functions reproduce the paper-faithful input and target schema.

### Family Creation And Training

- `create_exact_paper_base_estimator`
- `build_exact_paper_reference_parameter_grid`
- `resolve_exact_paper_hyperparameter_search_settings`
- `fit_exact_family_model_bank`

These functions encode the recovered family inventory, the recovered
paper-reference search grids, and the exact-paper training strategy.

### Evaluation

- `evaluate_exact_family_model_bank`
- `_safe_mape`

These functions create:

- family-level aggregate ranking;
- per-target ranking;
- the target-wise winner registry used later for paper-style tabulation.

### Export

- `build_exact_target_export_name`
- `_convert_estimator_to_onnx`
- `export_exact_family_onnx_bank`

These functions recreate the deployment-facing artifact surface:

- one ONNX file per family;
- one ONNX file per target.

### Reporting

- `resolve_dependency_version_dictionary`
- `build_exact_model_validation_summary`
- `build_validation_report_path`
- `build_exact_model_report_markdown`

These functions keep the workflow aligned with repository reporting and artifact
discipline.

## Configuration Surface

The canonical configuration is:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`

It defines:

- recovered dataframe path;
- recovered exact ONNX reference root;
- a forward-only recovered paper asset surface under an explicit forward-only
  root name;
- experiment identity;
- exact paper feature schema;
- enabled family list;
- deterministic split settings;
- paper-reference hyperparameter-search settings;
- ONNX export behavior.

The prepared batch campaign package is:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/baseline_reproduction/shared/2026-04-10_exact_paper_model_bank_campaign/`

The canonical launcher is:

- `scripts/campaigns/track1/exact_paper/run_exact_paper_model_bank_campaign.ps1`

## Relationship With The Existing Harmonic-Wise Branch

The two branches should be kept separate.

The existing harmonic-wise branch:

- is repository-owned;
- predicts harmonic terms from the TE dataset pipeline already integrated here;
- is optimized around repository benchmarking and `Target A`.

The exact model-bank branch:

- is stricter and paper-derived;
- uses the recovered dataframe and recovered family bank directly;
- exists to recreate the paper baseline and stabilize target-wise comparison.

They are complementary, not redundant.

## Practical Next Step

The next serious use of this branch is not generic tuning.

The next step is:

- execute the exact family bank;
- compare generated ONNX exports against the recovered exact release;
- build per-target family tables;
- identify whether the repository can recreate the same winning families for
  each `ampl_k` and `phase_k`.

That is the point where `Track 1` stops being only paper-aligned and becomes a
true paper-faithful reproduction branch.
