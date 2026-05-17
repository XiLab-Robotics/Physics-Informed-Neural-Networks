# RCIM Exact-Paper Reimplementation Workflow

This subtree is the repository-owned execution surface for the RCIM
paper-reimplementation workflows.

Unlike `recovered_original_workflow/`, this surface does not preserve the
paper-era scripts as copied runtime artifacts. Its role is to expose the
repository-designed reimplementation branches that:

- keep the recovered original family inventory and hyperparameter grids;
- keep the restored historical search protocol required by the paper-faithful
  Track 1 workflow;
- use repository-owned output roots, campaign tooling, and registries;
- support both direct single-run execution and campaign-driven execution.

The recovered-original branch remains documented separately in:

- `recovered_original_workflow/README.md`

## Current Paper-Faithful Status

The repository now exposes two distinct but connected RCIM reproduction
surfaces:

- recovered original workflow:
  `recovered_original_workflow/` keeps the author pipeline close to its
  recovered code shape, with repository-owned path handling and runtime roots;
- faithful exact-model-bank reimplementation:
  `original_dataset_exact_model_bank/` rebuilds the original pipeline protocol
  on the canonical repository dataset for both `forward` and `backward`
  directions.

The faithful Track 1 campaign surface has completed forward and backward
paper-faithful grid-search runs for the current `11`-family bank:

- `SVR`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`, `ELM`.

Track 1 is closed at this layer as the repository-owned faithful full-bank
reproduction of the recovered RCIM paper pipeline. Closure means the
forward/backward searches were run, accepted archives were promoted, and
Tables `2`-`5` were repopulated. It does not mean the benchmark is an
all-green optimized clone.

Accepted model archives from those campaigns are promoted to:

- `models/paper_reference/rcim_track1/forward/`
- `models/paper_reference/rcim_track1/backward/`

The canonical RCIM Tables `2`-`5` comparison surface is:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

Within practical limits imposed by modern library versions and missing
historical runtime state, this is the repository's literal or near-literal
reimplementation of the original RCIM ML-compensation model-bank pipeline:
same paper input schema, same harmonic target surface, same family-wise
multioutput training shape, restored `GridSearchCV(...)` plus historical
`cross_validate(...)` replay, and original-style per-target `Python + ONNX`
exports.

## Folder Structure

- `exact_paper_model_bank/`
  Strict recovered-CSV exact-paper family-bank validation.
- `original_dataset_exact_model_bank/`
  Direction-specific exact-paper family-bank validation rebuilt from the
  canonical repository dataset.
- `harmonic_wise_comparison/`
  Repository-owned harmonic-wise comparison and playback workflow.
- `reference_family_vs_feedforward/`
  Track 2 comparison between one archived reference bank and the feedforward
  best model.
- `recovered_original_workflow/`
  Direct recovered-original code surface rebuilt from the newly recovered full
  original root, with its own dedicated README and historical launcher model.

## Practical Workflow Split

The main distinction inside this subtree is between two exact-paper execution
branches.

### `exact_paper_model_bank/`

Use this branch when the operator wants the strict recovered-data exact-paper
surface:

- target schema anchored to the recovered paper-era CSV assets;
- exact-paper family inventory;
- exact-paper shared training support;
- repository-owned evaluation and export outputs.

Main entrypoint:

- `exact_paper_model_bank/run_exact_paper_model_bank_validation.py`

### `original_dataset_exact_model_bank/`

Use this branch when the operator wants the same exact-paper model-family
surface, but rebuilt from the canonical repository dataset:

- repository canonical dataset root;
- explicit `forward` or `backward` direction support;
- same exact-paper family inventory and grid-search surface;
- same shared best-parameter registry and stage-aware operator flow.

Main entrypoint:

- `original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`

Auxiliary entrypoint:

- `original_dataset_exact_model_bank/generate_original_dataset_exact_smoke_configs.py`

## Shared Exact-Paper Pipeline

Both exact-paper branches now flow through the same shared exact-paper training
surface.

The canonical shared implementation lives in:

- `exact_paper_model_bank/exact_paper_model_bank_support.py`
- `original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`

In practical operator terms, the shared exact-paper flow is:

1. Load one YAML config.
2. Build the exact-paper dataset bundle for the selected scope.
3. Resolve the exact-paper family registry and hyperparameter search settings.
4. Run the paper-faithful search stage:
   - `train_test_split(..., random_state=0)`
   - `GridSearchCV(...)`
   - historical `cross_validate(...)` replay on the search wrapper
   - target-wise historical `cross_validate(...)` replay on the best wrapped
     estimators
   - for `SVR`, keep the paper-faithful `rbf` branch and replace the
     historical `SVR(kernel="linear")` branch with the same pragmatic
     `StandardScaler + LinearSVR` fallback already adopted in the
     recovered-original workflow
5. Evaluate the trained family bank unless disabled.
6. Export per-target Python plus ONNX artifacts unless disabled.
7. Persist the repository-owned best-parameter summary and update the shared
   best-parameter registry.

The exact-paper canonical family surface now includes `11` families:

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
- `ELM`

## Stage Model

The two exact-paper Python runners now expose the same operator stage model:

- `search`
  Run the search protocol, then optionally chain evaluation and export.
- `eval`
  Rebuild the selected family bank from stored best parameters and run only
  evaluation.
- `export`
  Rebuild the selected family bank from stored best parameters and run only
  export.
- `loadbest`
  Load one stored exact-paper best-parameter summary or the shared registry,
  then rebuild the family bank without repeating search.

Common optional controls:

- `--best-parameter-summary-path`
- `--best-parameter-registry-path`
- `--no-eval`
- `--no-export`
- `--grid-search-verbose-override`
- `--historical-cross-validate-verbose-override`

## Best-Parameter Flow

The exact-paper reimplementation now keeps a repository-owned best-parameter
surface so the operator can separate expensive search from later replay
stages.

Per-run summary:

- `best_parameter_summary.yaml`
  written inside the run output directory when best parameters are available.

Shared registry:

- `output/registries/program/track1_exact_paper_best_hyperparameters.yaml`

The intended operator flow is:

1. Run `search` once for the desired scope.
2. Reuse the generated `best_parameter_summary.yaml`, or rely on the shared
   registry if coverage already exists.
3. Run `loadbest`, `eval`, or `export` without repeating the full search.

For `SVR`, the stored best-parameter payload now serializes the selected exact
variant explicitly so replay can rebuild either:

- the paper-faithful `SVR(kernel="rbf")` branch; or
- the pragmatic `Pipeline(StandardScaler(), LinearSVR(...))` fallback branch.

For `LGBM`, the exact-paper shared family factory now also forces:

- `verbosity=-1`
- `force_col_wise=True`

so long-running Track 1 search runs keep repository-owned progress lines
readable instead of flooding the console with native LightGBM chatter.

For `ELM`, the exact-paper shared export helper now mirrors the
recovered-original repo-owned ONNX converter registration so the Track 1
`ELMRegressor` family can emit per-target `Python + ONNX` artifacts.

## Export Artifact Contract

The exact-paper export surface now mirrors the recovered original workflow more
closely.

Every exact-paper export stage materializes:

- one run-level family-bank bundle:
  `paper_family_model_bank.pkl`;
- one per-target Python estimator artifact under `python_export/`; and
- one per-target ONNX artifact under `onnx_export/`.

This means the operator can compare the repository reimplementation against the
recovered original workflow both through:

- the repository-owned full family bundle; and
- the original-style per-target `Python + ONNX` export surface.

## Canonical Python Commands

The examples below use the direct Python runners. Replace config paths with the
prepared YAML for the desired scope.

### Strict Recovered-CSV Exact-Paper Surface

Search with live verbosity and keep downstream evaluation plus export enabled:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py `
  --config-path "config\paper_reimplementation\rcim_ml_compensation\exact_paper_model_bank\your_config.yaml" `
  --output-suffix exact_paper_search `
  --stage search `
  --grid-search-verbose-override 3 `
  --historical-cross-validate-verbose-override 10
```

Replay one stored best-parameter summary without repeating search:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py `
  --config-path "config\paper_reimplementation\rcim_ml_compensation\exact_paper_model_bank\your_config.yaml" `
  --output-suffix exact_paper_loadbest `
  --stage loadbest `
  --best-parameter-summary-path "output\validation_checks\...\best_parameter_summary.yaml"
```

Run only export from stored best parameters:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py `
  --config-path "config\paper_reimplementation\rcim_ml_compensation\exact_paper_model_bank\your_config.yaml" `
  --output-suffix exact_paper_export_only `
  --stage export `
  --best-parameter-summary-path "output\validation_checks\...\best_parameter_summary.yaml"
```

### Original-Dataset Exact-Paper Surface

Search on one prepared original-dataset config:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py `
  --config-path "config\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\your_config.yaml" `
  --output-suffix original_dataset_search `
  --stage search `
  --grid-search-verbose-override 3 `
  --historical-cross-validate-verbose-override 10
```

Reuse registry-backed best parameters and skip export:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py `
  --config-path "config\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\your_config.yaml" `
  --output-suffix original_dataset_loadbest `
  --stage loadbest `
  --no-export
```

Run only evaluation from one explicit saved summary:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py `
  --config-path "config\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\your_config.yaml" `
  --output-suffix original_dataset_eval_only `
  --stage eval `
  --best-parameter-summary-path "output\validation_checks\...\best_parameter_summary.yaml"
```

## Campaign Surface

The exact-paper reimplementation also exposes campaign preparation plus launch
tooling. For the current Track 1 paper-faithful branch, the canonical launcher
note lives in:

- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`

The main PowerShell launcher is:

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`

Preparation command:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py
```

Canonical remote launch:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 -Remote
```

One family at a time, with the exact-paper equivalent of the original
`Retune` stage:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "MLP" `
  -Stage Search `
  -Remote
```

Observed launch with verbose search monitoring:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "RF" `
  -Stage Search `
  -GridSearchVerboseOverride 3 `
  -HistoricalCrossValidateVerboseOverride 10 `
  -Remote
```

Registry-backed replay without repeating search:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Backward `
  -Families "RF" `
  -Stage LoadBest `
  -NoExport `
  -Remote
```

Multiple families in one invocation:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "MLP,RF,GBM" `
  -Stage Search `
  -Remote
```

## Output Layout

Typical exact-paper outputs are written under:

- `output/validation_checks/`
- `output/training_campaigns/track1/exact_paper/`
- `output/registries/program/`
- `doc/reports/analysis/validation_checks/`

Operator-relevant artifacts include:

- `validation_summary.yaml`
- `paper_family_model_bank.pkl`
- `best_parameter_summary.yaml`
- Markdown validation report under `doc/reports/analysis/validation_checks/`
- campaign logs under the selected campaign output root

Persistent campaign state lives in:

- `doc/running/active_training_campaign.yaml`

## Relationship With The Recovered-Original Branch

The recovered-original branch and the exact-paper reimplementation are related
but intentionally distinct.

- `recovered_original_workflow/`
  preserves the copied original runtime logic plus the repository-owned
  launcher modernization around it.
- the exact-paper reimplementation branches
  keep the recovered original family inventory, grid definitions, and restored
  historical search protocol, but run inside a repository-owned validation and
  campaign framework.

When the goal is paper-faithful Track 1 execution inside the repository-owned
campaign system, this README is the operational surface to follow. New
restricted-dataset or all-green optimization studies should be added as
separate branches so the closed full-dataset faithful baseline remains
auditable.
