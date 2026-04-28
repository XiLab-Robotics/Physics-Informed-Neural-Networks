# RCIM Original Pipeline To Reimplementation Companion

## Overview

This companion document explains the relationship between the recovered RCIM
original prediction pipeline and the repository exact-paper reimplementation.

It is meant to be read while keeping the code open side by side.

Primary original files:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-main_prediction_v18.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-predictorML_v7.py`

Primary repository reimplementation files:

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`

This document does not try to prove that the repository reimplementation is a
literal line-by-line port. The goal is to explain:

1. what the original code actually does;
2. which parts of `predictorML_v7.py` are active in the `v18` workflow;
3. how the same workflow was redistributed across the repository
   reimplementation;
4. what stayed conceptually faithful and what changed in engineering shape.

## How To Read The Original Code

The original `v18` branch is not a large framework spread across many files.
Its effective prediction workflow is concentrated in two layers:

- `1-main_prediction_v18.py`
  chooses the dataframe, the family list, the loop structure, and the output
  CSV locations;
- `1-predictorML_v7.py`
  contains the actual training, prediction, metric, cross-validation, tuning,
  export, and alternative-regression logic.

If you want to understand the real paper-era flow, do not read all `1500+`
 lines of `predictorML_v7.py` with equal priority. Read it as a multi-branch
utility file whose active `v18` branch is only one subset of the code.

## Original `1-main_prediction_v18.py`

### What The File Is

`1-main_prediction_v18.py` is an operational script, not a reusable framework
entry point. Its job is to:

1. load the recovered prediction dataframe;
2. choose the final paper-side family list;
3. wrap each family through `MLModelMultipleOutput`;
4. train and evaluate the family on a held-out split;
5. write one prediction CSV per family.

### Block-By-Block Behavior

#### Imports

The file imports:

- `pandas` and `os`;
- `MLModelMultipleOutput` from `predictorML_v7.py`;
- the recovered paper family bank:
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

This tells us immediately that the file is not generic. It is a concrete
family-bank runner.

#### Dataframe Load

Inside `main()`, the script:

- reads `dataFrame_prediction_Fw_v14_newFreq.csv`;
- uses `sep=';'` and `decimal=','`;
- keeps only rows with `deg <= 35`;
- resets the dataframe index.

In these recovered prediction CSVs, `deg` is the oil-temperature column. So
`deg <= 35` is an explicit thermal filter that keeps only rows whose oil
temperature is at or below `35` degrees.

Repository consequence:

- the script assumes a paper-era forward-only dataframe already exists;
- no raw-instance reconstruction happens here;
- the `deg <= 35` filter is a real part of the original prediction workflow,
  not just a comment or a generic operating-variable cut.

#### Target Discovery

The script collects targets through:

- every dataframe column containing `ampl`;
- every dataframe column containing `phase`.

So the target surface is discovered from the dataframe header, not hardcoded
target by target inside the runner.

That means the dataframe itself acts as a hidden contract for:

- the harmonic set;
- the target ordering;
- the number of output estimators that will be trained.

#### Output Folder

The script writes into:

- `output_prediction/instV3.8_Fw_allFreq_def/`

This is a relative local folder with a hand-authored naming convention. It is
useful evidence of the original workflow style:

- mutable local outputs;
- no immutable run root;
- no config snapshot;
- no formal run metadata.

#### Family List

The list named `mlModelsList` is the core scientific payload of the file.

It defines one tuned estimator instance per family. This is important:

- the script is not searching here;
- the script is replaying a set of already selected family configurations.

The `ELMRegressor` entry shows that the code surface is slightly wider than the
recovered exact ONNX paper release.

#### Main Loop

For each family estimator, the script:

1. wraps it through `MLModelMultipleOutput`;
2. runs `predictorMLEvalutationOnTrain(dfInput, 0.20)`;
3. saves the returned prediction dataframe to:
   `dfOutTot_prediction_<family>.csv`.

Operationally, this means one family run performs:

- one train/test split;
- one fitted multioutput family bank;
- one test-set prediction pass;
- one per-target metric pass;
- one summary CSV update;
- one prediction CSV output.

## What `predictorML_v7.py` Actually Contains

`predictorML_v7.py` is not a single algorithm. It is a layered local
prediction framework with multiple historical branches.

Its main classes are:

- `MLModel`
- `MLModelChainedMultipleOutput`
- `MLModelMultipleOutput`
- `MLModelMultiOutputCombined`
- `MLPipeline`
- `MinimumDistanceRegressor`

Only one of those branches is central to `1-main_prediction_v18.py`.

## The Active `v18` Path Inside `predictorML_v7.py`

### `MLModelMultipleOutput`

The `v18` workflow uses `MLModelMultipleOutput`.

This class wraps the passed base estimator as:

- `MultiOutputRegressor(model)`

This is the most important modeling choice in the original code.

It means:

- one family run does not fit one single joint model;
- it fits one estimator per target column;
- all those target-specific estimators share the same family type.

For example, if the target matrix has `20` columns, then:

- `SVR` family run -> `20` SVR estimators;
- `RF` family run -> `20` random-forest estimators;
- and so on.

### `predictorMLEvalutationOnTrain`

This is the active `v18` method.

Its behavior is:

1. build feature matrix `X = ['rpm', 'deg', 'tor']`;
2. resolve targets:
   - `phase` only if `method == 'phase'`;
   - `ampl` only if `method == 'ampl'`;
   - both if `method` is anything else such as `'tot'`;
3. split with:
   - `test_size = 0.20`
   - `random_state = 0`;
4. fit the wrapped `MultiOutputRegressor`;
5. predict on the held-out test set;
6. compute per-target:
   - `MSE`
   - `RMSE`
   - `MAE`
   - `MAPE`;
7. append those metrics to `summaryEvalutationOnTrain+_*.csv`;
8. build one prediction dataframe with:
   - `rpm`
   - `deg`
   - `tor`
   - `prev_<target_name>` for every predicted target.

This prediction dataframe is what the outer `v18` script writes as the final
family output.

### What The `v18` Path Does Not Use

The same class also contains alternative methods:

- `predictorML`
  simple train/test prediction without the richer evaluation-on-train summary;
- `predictorMLCrossValidationWithHyperparameter`
  explicit tuning path through `GridSearchCV`;
- `predictorMLCrossValidation`
  cross-validation path without the same evaluation-on-train output style;
- `predictorML_allForExport`
  fit on all rows to export deployable models;
- `predictorML_TestForExport`
  lightweight prediction helper for prepared test data;
- `predictorMLVariableTrain`
  study the effect of shrinking train-set size.

So `predictorML_v7.py` is not just the `v18` branch. It is a wider
experiment-and-export surface, and `v18` selects only one route through it.

## The Rest Of `predictorML_v7.py`

### `MLModel`

`MLModel` is the simpler base wrapper:

- single estimator;
- no `MultiOutputRegressor`;
- basic training, prediction, export, and cross-validation logic.

It is useful for understanding the common code style, but it is not the main
`v18` path.

### `MLModelChainedMultipleOutput`

This branch uses:

- `RegressorChain(model)`

It reflects an alternative idea:

- predict targets in a chained dependency structure instead of independently.

This is conceptually interesting but not the dominant paper branch used in
`v18`.

### `MLModelMultiOutputCombined`

This class is a different paradigm again.

It is designed for situations where one may want:

- different target estimators inside one combined multioutput surface.

This is closer to a "best model per target" perspective, but it is not the
active `v18` route.

### `MLPipeline`

This branch wraps a model inside:

- `StandardScaler()`
- followed by the estimator

It is a more classical sklearn pipeline wrapper and appears oriented toward
single-target or leave-one-out experimentation rather than the central
paper-family replay.

### `MinimumDistanceRegressor`

This is a custom nearest-neighbor-like baseline:

- compute train/test distances;
- choose the nearest train sample;
- return its target vector as prediction.

This is best read as a local comparison baseline, not the main paper workflow.

## What The Original Workflow Really Is

If you strip away the extra branches, the active original `v18` workflow is:

1. start from a prepared forward dataframe;
2. keep only `deg <= 35`, meaning only rows with oil temperature up to
   `35` degrees;
3. use inputs `rpm`, `deg`, `tor`;
4. use all harmonic amplitude and phase targets;
5. for each family in the selected final list:
   - wrap through `MultiOutputRegressor`;
   - split `80/20`;
   - fit;
   - predict test rows;
   - score each target separately;
   - save metrics;
   - save predicted targets.

That is the real baseline that the repository reimplementation needs to be
compared against.

## Repository Reimplementation: Equivalent High-Level Flow

The repository equivalent is split across:

- `run_exact_paper_model_bank_validation.py`
- `exact_paper_model_bank_support.py`

The high-level pipeline is still recognizably the same:

1. load the recovered paper dataframe;
2. keep the exact paper input features `rpm`, `deg`, `tor`;
3. resolve the harmonic target list;
4. split into train and test;
5. build one `MultiOutputRegressor` family bank per enabled family;
6. evaluate on the held-out split;
7. export one ONNX per family-target estimator;
8. write structured artifacts and reports.

So the reimplementation preserves the central modeling idea, but changes the
execution architecture.

## Original-To-Reimplementation Mapping

### Dataset Load

Original:

- direct `read_csv(...)` inside `1-main_prediction_v18.py`

Reimplementation:

- `load_exact_paper_dataframe`
- `build_exact_paper_dataset_bundle`

Main change:

- the reimplementation makes dataframe loading a named, reusable stage;
- it also validates the input surface instead of just consuming it.

### Input Feature Contract

Original:

- hardcoded `X = ['rpm', 'deg', 'tor']` inside the predictor methods

Reimplementation:

- `resolve_paper_input_feature_name_list`

Main change:

- the same feature contract exists, but the repository version asserts it
  explicitly.

### Target Resolution

Original:

- discover target columns through names containing `ampl` or `phase`

Reimplementation:

- `resolve_target_name_list`
- `resolve_exact_target_scope`

Main change:

- the same naming logic is preserved;
- the repository version adds validation and optional scope modes:
  - `all`
  - `amplitudes_only`
  - `phases_only`

### Train/Test Split

Original:

- performed inside `predictorMLEvalutationOnTrain`

Reimplementation:

- performed inside `build_exact_paper_dataset_bundle`

Main change:

- same mathematical split concept;
- different ownership boundary in the code.

### Family Loop

Original:

- explicit Python loop in `1-main_prediction_v18.py`

Reimplementation:

- `fit_exact_family_model_bank`

Main change:

- the same family-bank loop exists;
- it is now a dedicated stage with structured progress logging and fit
  summaries.

### MultiOutput Training

Original:

- `MLModelMultipleOutput` wraps the base estimator with `MultiOutputRegressor`

Reimplementation:

- `fit_exact_family_model_bank` also wraps each base estimator with
  `MultiOutputRegressor`

Main change:

- the core modeling concept is preserved;
- the repository version adds optional tuning control, threadpool control, and
  fit summaries.

### Evaluation

Original:

- `predictorMLEvalutationOnTrain`

Reimplementation:

- `evaluate_exact_family_model_bank`

Main change:

- both compute per-target errors on a held-out split;
- the repository version returns structured family summaries and target-wise
  ranking registries instead of relying on one ad hoc summary CSV format.

### Export

Original:

- `exportModel`

Reimplementation:

- `export_exact_family_onnx_bank`

Main change:

- both export one ONNX per family-target estimator;
- the repository version adds:
  - explicit export configuration;
  - recovered-reference comparison;
  - export error capture;
  - special handling for edge cases such as empty-support-vector `SVR`.

### Final Outputs

Original:

- family prediction CSVs
- summary CSVs

Reimplementation:

- immutable output root
- config snapshot
- run metadata
- pickled family model bank
- ONNX export root
- YAML validation summary
- Markdown report

Main change:

- the repository version turns the run into an auditable artifact package
  rather than only a local prediction output folder.

## What Stayed Faithful

The reimplementation stays close to the original in these core ways:

- same paper input feature philosophy: `rpm`, `deg`, `tor`;
- same target philosophy: harmonic `ampl_k` and `phase_k`;
- same family-bank mentality;
- same central reliance on `MultiOutputRegressor`;
- same held-out split concept;
- same per-target evaluation mindset;
- same target-wise ONNX export philosophy.

These are not superficial similarities. They preserve the main modeling shape
of the original prediction workflow.

## What Changed In A Material Way

The reimplementation is not only "the same code but cleaner". It also makes
real engineering decisions.

### Configuration Ownership

The original code hides many policies inside the script body.

The reimplementation moves those policies into:

- config files;
- named support functions;
- explicit target-scope and export settings.

### Artifact Discipline

The original code writes mutable local outputs.

The reimplementation writes immutable, report-ready validation artifacts.

### Family-Bank Canonicalization

The original `v18` includes `ELMRegressor`.

The repository exact-paper branch chooses the recovered exact ONNX family bank
as the canonical reference and therefore excludes `ELM` from the main exact
bank.

### Tuning Surface

The original predictor file contains tuning logic, but it is mixed with the
rest of the script ecosystem.

The reimplementation promotes that tuning policy into an explicit and
configurable training strategy.

### Evaluation Packaging

The original code emits useful metrics, but in a local CSV-centric style.

The repository version turns those metrics into:

- family ranking;
- per-target winner ranking;
- structured summaries;
- persistent Markdown reports.

## Important Non-Equivalence To Keep In Mind

It is incorrect to summarize the relationship as:

- "same models, same config, same behavior, only written better"

The more accurate statement is:

- the repository reimplementation preserves the main modeling logic of the
  recovered original prediction pipeline, but redistributes it into explicit
  dataset, fit, evaluation, export, and reporting stages, and it also
  introduces deliberate canonicalization and artifact-discipline choices that
  are not merely cosmetic.

## Reading Order For Side-By-Side Study

If you want to inspect the code manually with two files open, use this order:

1. original `1-main_prediction_v18.py`
   Compare against `run_exact_paper_model_bank_validation.py` to understand the
   high-level orchestration shift.
2. original `predictorMLEvalutationOnTrain` inside `1-predictorML_v7.py`
   Compare against:
   - `build_exact_paper_dataset_bundle`
   - `fit_exact_family_model_bank`
   - `evaluate_exact_family_model_bank`
3. original `exportModel` inside `MLModelMultipleOutput`
   Compare against `export_exact_family_onnx_bank`
4. then return to the rest of `predictorML_v7.py`
   and classify the remaining branches as:
   - active `v18` path;
   - alternative multioutput path;
   - export-only path;
   - tuning path;
   - experimental or historical path.

## Practical Conclusion

The original recovered prediction workflow is narrower than the full
`predictorML_v7.py` file suggests.

The exact-paper repository reimplementation is broader than the short runner
file suggests.

The fairest comparison is therefore:

- original active prediction branch
  versus
- repository exact-paper dataset + family-bank + evaluation + export stages

Under that comparison, the repository implementation is best understood as:

- modeling-faithful in its core training philosophy;
- structurally refactored into explicit pipeline stages;
- stronger in validation packaging, reporting, and export governance;
- not a literal source-level clone of the paper-era script bundle.
