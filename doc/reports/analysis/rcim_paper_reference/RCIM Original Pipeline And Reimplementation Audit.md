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

Current closure status:

- the recovered original workflow is preserved as a near-literal runnable copy
  under
  `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`;
- the faithful original-dataset exact-model-bank reimplementation lives under
  `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`;
- completed Track 1 forward and backward paper-faithful campaigns now promote
  accepted artifacts to `models/paper_reference/rcim_track1/`;
- the repository-owned RCIM Tables `2`-`5` benchmark surface is
  `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`.
- Track 1 is closed as the populated full-dataset faithful reproduction
  surface; yellow and red cells are retained as numerical-gap evidence under
  the faithful protocol.

## Recovered Workflow Status

| Stage | Recovered Source | Directly Runnable Now | Main Reason |
| --- | --- | --- | --- |
| Dataframe creation | `original_pipeline/0-main_createDFforPrediction.py` | Yes | The full author-supplied root now ships `statistic.py`, `instance_v5.py`, `instances_V3/`, and the shipped caches needed by the dataframe-generation stage. |
| Prediction and export | `original_pipeline/1.1-main_prediction_v17.py` and `original_pipeline/1-main_prediction_v18.py` | Yes | The full author-supplied root now ships both the full-dataset export `v17` branch and the paper-style tuned `v18` branch together with `predictorML_v7.py`. |
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

- keeps the ten original paper-table families;
- normalizes `SVM` to `SVR`;
- also includes `ELM` as an operational Track 1 family because it is present in
  the recovered original code and now has repository-owned Python plus ONNX
  export support.

Why it matters:

- the recovered source contains at least three family surfaces:
  exact ONNX paper bank, original `v18` code, and the author-shipped `v17`
  export branch;
- the repository reimplementation keeps the ten-family paper-table order for
  direct paper comparison while also archiving and reporting `ELM` as the
  recovered-code operational extension.

### 3. Hyperparameter Governance

Recovered original `v18`:

- hardcodes one tuned estimator instance per family directly inside
  `1-main_prediction_v18.py`.

Recovered author-shipped `v17`:

- uses mostly default constructors for the narrowed family list;
- per author guidance, this is the whole-dataset export route;
- when a new dataset or a restricted dataset slice is used, the intended next
  step is to start from the `v17` structure and replace
  `predictorML_allForExport(...)` with
  `predictorMLCrossValidationWithHyperparameter(...)`.

Repository reimplementation:

- moves recovered family definitions into
  `exact_paper_model_bank_support.py`;
- keeps the paper-family hyperparameters explicit, named, and centrally
  inspectable;
- restores the paper-style `GridSearchCV(...)` plus historical
  `cross_validate(...)` replay protocol;
- adds alias maps and paper-table mappings for benchmark comparison.

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
- keeps launch behavior separate from support utilities;
- promotes accepted closeout artifacts into
  `models/paper_reference/rcim_track1/`.

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
- completed forward and backward Track 1 campaigns now provide archived
  paper-reference models and benchmark tables for both directions.

Why it matters:

- this is one of the clearest places where the repository went beyond merely
  replaying the recovered files and formalized the paper's direction split into
  a stable program structure.
- the completed Track 1 backward campaign now follows that interpretation at
  repository-pipeline level: it treats backward as an explicit
  direction-scoped exact-model-bank surface, trains it through the restored
  search protocol, exports per-target artifacts, and archives accepted results
  under `models/paper_reference/rcim_track1/backward/`.

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

The current campaign-ready reconstruction root is:

- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`

It is the repository-owned faithful pipeline surface used to train and export
the Track 1 model banks that populate:

- `models/paper_reference/rcim_track1/`
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`

## Practical Conclusion

The recovered original material is now sufficient to inspect and likely rerun
the main paper-era dataframe, training/export, and evaluation scripts from one
author-supplied root.

The current repository reimplementation is still not just a style rewrite. It
contains deliberate, documented engineering substitutions in:

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

The completed Track 1 paper-faithful campaign cycle closes the next gap:

- accepted forward and backward exact-model-bank artifacts are now archived in
  `models/paper_reference/rcim_track1/`;
- Tables `2`-`5` are repopulated for both directions and the closed status is
  no longer gated by all-green benchmark coloring.
- Tables `2`-`5` are now regenerated from those accepted artifacts in
  `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`.
