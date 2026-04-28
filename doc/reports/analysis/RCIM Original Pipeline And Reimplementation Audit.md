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
| Dataframe creation | `original_pipeline/0-main_createDFforPrediction.py` | Yes | The full author-supplied root now ships `statistic.py`, `instance_v5.py`, `instances_V3/`, and the shipped caches needed by the dataframe-generation stage. |
| Prediction and export | `original_pipeline/1.1-main_prediction_v17.py` and `original_pipeline/1-main_prediction_v18.py` | Yes | The full author-supplied root now ships both the export-oriented `v17` branch and the tuned-family `v18` branch together with `predictorML_v7.py`. |
| Evaluation | `original_pipeline/2-main_evaluatePrediction_v4.py` | Yes | The full author-supplied root now ships `instance_v4.py`, `instance_v5.py`, prediction outputs, and evaluation artifacts in one operational folder. |

## Material Code Differences

### 1. Input Data Surface

Recovered original workflow:

- dataframe creation is raw-instance driven through `instances_V3/`;
- prediction consumes shipped `Fw` and `Bw` dataframe CSVs;
- in the recovered prediction CSVs, `deg` represents oil temperature;
- the shipped `Fw` and `Bw` CSVs already contain only `deg = 25, 30, 35`;
- the recovered original runners still apply `deg <= 35`, but in this shipped
  author release that line is empirically redundant;
- the shipped training and evaluation scripts are still forward-coded in
  practice.

Repository reimplementation:

- the exact-paper validation branch can still use the recovered CSV;
- the original-dataset branch rebuilds the feature-target table from the
  canonical repository dataset and explicit directional manifests;
- forward and backward handling are represented explicitly at the configuration
  and artifact-path level.

Why it matters:

- the recovered workflow is tied to author-shaped dataframe snapshots rather
  than to the repository's canonical dataset builders;
- the authors' own release confirms that the thermal cutoff line can be legacy
  residue from earlier dataframe versions;
- the repository workflow is designed to regenerate the dataset surface rather
  than treat the shipped CSVs as the only canonical source.

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

Recovered author-shipped `1.1-main_prediction_v17.py`:

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
  exact ONNX paper bank, original `v18` code, and the author-shipped `v17`
  export branch;
- the repository reimplementation already made one explicit interpretation:
  the canonical exact-paper bank is the ten-family set, not the `ELM`
  experiment branch.

### 3. Hyperparameter Governance

Recovered original `v18`:

- hardcodes one tuned estimator instance per family directly inside
  `1-main_prediction_v18.py`.

Recovered author-shipped `v17`:

- uses mostly default constructors for the narrowed family list;
- per author guidance, this is the whole-dataset export route.

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
- the author explicitly confirmed this stage is used to rework
  `output_prediction` into the paper tables;
- the shipped evaluator remains forward-coded in practice through
  `output_prediction/instV3.8_Fw_allFreq_def/` and `predicted_TE_Fw...`
  methods.

Repository reimplementation:

- evaluates family-level aggregate metrics and per-target rankings directly
  from the dataframe splits;
- compares generated ONNX artifacts against the recovered bank;
- does not depend on the missing paper-era `instance_v4.py` or `instance_v5.py`
  classes.

Why it matters:

- the repository branch is fully self-owned in its evaluation code path;
- the recovered workflow is now materially complete, but its evaluation branch
  is still operationally narrower and more historically specific than the
  repository-owned analysis path.

### 6. Direction Handling

Recovered workflow:

- the full author-supplied root ships both `Fw` and `Bw` CSVs;
- `0-main_createDFforPrediction.py` is currently set to generate `Bw` in the
  shipped file;
- `1-main_prediction_v18.py` and `1.1-main_prediction_v17.py` are both still
  forward-coded in the shipped surface;
- `2-main_evaluatePrediction_v4.py` is also still forward-coded in practice.

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

The recovered original material is now sufficient to inspect and likely rerun
the main paper-era dataframe, training/export, and evaluation scripts from one
author-supplied root.

The current repository reimplementation is still not just a style rewrite. It
contains deliberate engineering substitutions in:

- dataset regeneration;
- family-bank normalization;
- direction handling;
- artifact discipline;
- evaluation packaging and independence from the historically specific
  paper-era script outputs.

The new recovered-workflow runner closes one gap:

- we can now execute the copied original prediction logic in a controlled repo
  surface;
- and we can compare that behavior against the current repository branch
  without editing the archived recovered files.
