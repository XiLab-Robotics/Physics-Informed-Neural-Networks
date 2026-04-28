# RCIM Original Pipeline And Reimplementation Audit

## Overview

This report audits the code-level differences between:

- the recovered RCIM original workflow copies now stored under
  `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`;
- the current repository reimplementation under
  `scripts/paper_reimplementation/rcim_ml_compensation/`.

The goal is to state precisely:

1. which parts of the recovered workflow are directly runnable;
2. which parts still depend on external original-style inputs even though the
   missing code dependencies have now been restored;
3. where the repository reimplementation intentionally diverges from the
   recovered code.

## Recovered Workflow Status

| Stage | Recovered Source | Directly Runnable Now | Main Reason |
| --- | --- | --- | --- |
| Dataframe creation | `original_pipeline/0-dfCreation/` | Yes | The restored `instance_v5.py` dependency now allows the copied statistic-driven dataframe stage to run when an original-style instance directory is supplied. |
| Prediction and export | `latest_snapshot/` training branch | Yes | The repository wrapper now treats `main_prediction_v17.py` plus `predictorML_v7.py` as the canonical recovered-original training stage. |
| Evaluation | `original_pipeline/2-evaluation/` | Yes | The restored `instance_v4.py` and `instance_v5.py` dependencies now allow the copied evaluation logic to run when an original-style instance directory and prediction CSVs are supplied. |

## Material Code Differences

### 1. Input Data Surface

Recovered original workflow:

- dataframe creation is raw-instance driven through `instances_v3/`;
- prediction consumes `dataFrame_prediction_Fw_v14_newFreq.csv`;
- in the recovered prediction CSVs, `deg` represents oil temperature;
- the recovered original runners apply `deg <= 35`, so the prediction branch
  keeps only rows whose oil temperature is at or below `35` degrees;
- the shipped recovered code and CSV are forward-specific.

Repository reimplementation:

- the exact-paper validation branch can still use the recovered CSV;
- the original-dataset branch rebuilds the feature-target table from the
  canonical repository dataset and explicit directional manifests;
- forward and backward handling are represented explicitly at the configuration
  and artifact-path level.

Why it matters:

- the recovered workflow is tied to one shipped forward dataframe snapshot;
- that shipped snapshot is further narrowed by the original thermal cutoff
  `deg <= 35`;
- the repository workflow is designed to regenerate the dataset surface rather
  than treat the CSV as the only canonical source.

### 2. Family Registry

Recovered original `1-main_prediction_v18.py`:

- `SVR`
- `MLPRegressor`
- `RandomForestRegressor`
- `DecisionTreeRegressor`
- `ExtraTreeRegressor`
- `ExtraTreesRegressor`
- `GradientBoostingRegressor`
- `HistGradientBoostingRegressor`
- `XGBRegressor`
- `LGBMRegressor`
- `ELMRegressor`

Recovered latest snapshot `main_prediction_v17.py`:

- `DecisionTreeRegressor`
- `ExtraTreeRegressor`
- `ExtraTreesRegressor`
- `RandomForestRegressor`
- `GradientBoostingRegressor`
- `HistGradientBoostingRegressor`
- `XGBRegressor`
- `LGBMRegressor`
- `MLPRegressor`

Repository exact-paper reimplementation:

- keeps the ten paper families;
- normalizes `SVM` to `SVR`;
- excludes `ELM` from the canonical exact-paper family bank because it is not
  part of the recovered exact ONNX release.

Why it matters:

- the recovered source contains at least three family surfaces:
  exact ONNX paper bank, original `v18` code, and later `v17` snapshot;
- the repository reimplementation already made one explicit interpretation:
  the canonical exact-paper bank is the ten-family set, not the `ELM`
  experiment branch.

### 3. Hyperparameter Governance

Recovered original `v18`:

- hardcodes one tuned estimator instance per family directly inside
  `1-main_prediction_v18.py`.

Recovered latest `v17`:

- uses mostly default constructors for the narrowed family list.

Repository reimplementation:

- moves recovered family definitions into
  `exact_paper_model_bank_support.py`;
- keeps the paper-family hyperparameters explicit, named, and centrally
  inspectable;
- adds alias maps and paper-table mappings for later benchmark comparison.

Why it matters:

- the repository implementation centralizes the paper interpretation instead of
  leaving it embedded in one script-local list.

### 4. Execution Discipline

Recovered original workflow:

- writes into mutable relative folders such as `output_prediction/...`;
- relies on local current-working-directory assumptions;
- mixes execution logic and artifact naming in one script.

Repository reimplementation:

- writes immutable validation artifacts under `output/validation_checks/...`;
- snapshots config and metadata;
- emits Markdown and YAML summaries;
- keeps launch behavior separate from support utilities.

Why it matters:

- the repository branch is designed for repeatable audit trails and campaign
  integration, not only for one local prediction export pass.

### 5. Evaluation Surface

Recovered original workflow:

- evaluates both aggregate reconstructed-signal errors and per-component
  errors;
- stores paper-facing tables through ad hoc CSV exports;
- depends on missing `Instance` implementations for signal reconstruction.

Repository reimplementation:

- evaluates family-level aggregate metrics and per-target rankings directly
  from the dataframe splits;
- compares generated ONNX artifacts against the recovered bank;
- does not depend on the missing paper-era `instance_v4.py` or `instance_v5.py`
  classes.

Why it matters:

- the repository branch is fully self-owned in its evaluation code path, while
  the recovered workflow still contains an unrecovered legacy dependency gap.

### 6. Direction Handling

Recovered workflow:

- the copied dataframe creator and shipped CSV are explicitly `Fw`;
- the latest snapshot also ships a `Bw` CSV, but the main runnable path remains
  forward-centered.

Repository reimplementation:

- the original-dataset exact branch makes direction an explicit configuration
  dimension through `forward` and `backward` manifests and target prefixes.

Why it matters:

- this is one of the clearest places where the repository went beyond merely
  replaying the recovered files and formalized the paper's direction split into
  a stable program structure.

## New Repository-Owned Reconstruction Surface

The repository now contains a dedicated recovered-workflow reconstruction root:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

This surface intentionally separates:

- copied recovered evidence files;
- the repository-owned runner;
- the current repository reimplementation.

That separation makes the comparison more trustworthy because the copied source
can now be inspected directly under `scripts/` without silently mutating the
reference archive.

## Practical Conclusion

The recovered original material is sufficient to reconstruct a directly
runnable prediction/export branch, but it is not sufficient to reconstruct the
entire paper pipeline without compatibility work because the archived
`instance_v4.py` and `instance_v5.py` implementations are missing.

The current repository reimplementation is therefore not just a style rewrite.
It already contains deliberate engineering substitutions in:

- dataset regeneration;
- family-bank normalization;
- direction handling;
- artifact discipline;
- evaluation independence from the missing legacy instance classes.

The new recovered-workflow runner closes one gap:

- we can now execute the copied original prediction logic in a controlled repo
  surface;
- and we can compare that behavior against the current repository branch
  without editing the archived recovered files.
