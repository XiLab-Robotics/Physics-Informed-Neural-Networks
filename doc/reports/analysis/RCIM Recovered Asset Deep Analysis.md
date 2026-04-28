# RCIM Recovered Asset Deep Analysis

## Overview

This report consolidates the recovered RCIM paper assets now stored under
[`reference/rcim_ml_compensation_recovered_assets`](../../../reference/rcim_ml_compensation_recovered_assets/README.md).
Its goal is not simple archival bookkeeping. The goal is to reconstruct, as
precisely as the recovered evidence allows, how the paper-era models were
generated, evaluated, exported, and prepared for deployment so that
`Track 1` can be reimplemented in a paper-faithful way inside this repository.

The recovered package is strong enough to reconstruct the main methodology and
most of the practical training/export flow. It is not a perfectly frozen,
self-consistent release tag. Some files clearly come from adjacent workflow
generations. This report therefore separates:

- recovered facts;
- implementation-facing inferences;
- unresolved uncertainties.

Important clarification adopted after direct author feedback:

- the current repository root name is legacy only;
- the recovered assets currently stored there correspond to the paper's
  `forward` branch only;
- the paper's generalized notation later collapses forward and backward into
  one symbolic treatment, but the underlying trained models remain
  direction-specific.

## Executive Summary

The recovered material shows that the paper workflow was fundamentally
harmonic-wise and target-wise:

- operating-condition inputs were `rpm`, `deg`, and `tor`;
- targets were harmonic `ampl_k` and `phase_k`;
- the final harmonic set of the exact recovered ONNX bank is
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- training code used family-level `MultiOutputRegressor` wrappers, which means
  one family launch internally fit one estimator per target;
- export logic then wrote one ONNX file per target, per family;
- evaluation code produced both total-signal metrics and per-component metrics,
  which is exactly the information needed to choose the best family for each
  harmonic target.
- the shipped recovered dataframe and the shipped recovered model bank are
  forward-only artifacts.

The strongest practical conclusion is this:

- the recovered assets do not support reusing our current `Track 1` pipeline as
  "close enough";
- they support implementing a second, stricter paper-faithful branch inside
  `Track 1` that mirrors the original RCIM asset logic much more closely.

The second major conclusion is this:

- the paper likely did not train `200` independent hand-authored scripts;
- it likely trained family-wide multi-output banks and selected the best
  per-target exported ONNX models after evaluation.

That distinction matters because it makes exact reimplementation much more
practical than "train thousands of separate scripts".

The third major conclusion is this:

- the repository's recovered bank must currently be treated as the
  forward-only half of the paper methodology;
- the missing backward-side branch should be considered conceptually parallel,
  not interchangeable.

## What The Recovered Reference Actually Says

### Asset Surface

The recovered package contains five materially different evidence classes:

- exact paper-era ONNX deployables;
- original pipeline code for dataframe creation, prediction, and evaluation;
- a later export-oriented snapshot;
- older backup code from a previous harmonic generation;
- TwinCAT XML exports and large archived instance pickles.

The exact ONNX bank is the strongest evidence of the final deployment-facing
model surface. The original pipeline code is the strongest evidence of the
training and evaluation flow. The latest snapshot and backup legacy code are
best treated as version-history evidence, not as the canonical paper release.

### Exact ONNX Model Bank

The exact recovered ONNX bank is stored under
[`models/exact_onnx_paper_release`](../../../reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release).

Recovered family roots:

- `DT`
- `ERT`
- `ET`
- `GBM`
- `HGBM`
- `LGBM`
- `MLP`
- `RF`
- `SVR`
- `XGBM`

Recovered final target structure:

- `ampl_0`
- `ampl_1`
- `ampl_3`
- `ampl_39`
- `ampl_40`
- `ampl_78`
- `ampl_81`
- `ampl_156`
- `ampl_162`
- `ampl_240`
- `phase_0`
- `phase_1`
- `phase_3`
- `phase_39`
- `phase_40`
- `phase_78`
- `phase_81`
- `phase_156`
- `phase_162`
- `phase_240`

Observed counts:

- expected paper-faithful bank: `10 families x 20 targets = 200 ONNX files`
- recovered count: `201`
- cause: `RF/ampl` contains a duplicate
  `RandomForestRegressor_ampl240 (1).onnx`

The duplicate is byte-identical to `RandomForestRegressor_ampl240.onnx`, so it
is archival noise, not a second real variant.

The full exact ONNX bank is lightweight:

- total size: about `118.84 MB`
- largest single file: about `2.86 MB`

This matters because it confirms that the paper-facing deployable strategy was
made of many small, inspectable single-target artifacts rather than a single
opaque monolith.

### Original Pipeline Reconstruction

The split late pipeline fragment currently available for inspection is stored
under
[`code/backup_split_original_pipeline_fragment`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment).

Its recovered structure is:

- `0-dfCreation/0-main_createDFforPrediction.py`
- `0-dfCreation/0-statistic.py`
- `1-prediction/1-main_prediction_v18.py`
- `1-prediction/1-predictorML_v7.py`
- `2-evaluation/0-statistic.py`
- `2-evaluation/2-main_evaluatePrediction_v4.py`
- `2-evaluation/2-main_evaluateSignals.py`
- `0-requirements.txt`

This reconstructs a clear staged pipeline:

1. read raw instance archives;
2. compute or load selected FFT components;
3. build a dataframe with operating variables plus `ampl/phase` targets;
4. train multiple model families on those targets;
5. export ONNX per target;
6. evaluate both total reconstruction quality and per-target errors;
7. derive paper-style comparison tables.

### Dataframe Creation Stage

The dataframe creation stage is centered on:

- [`0-main_createDFforPrediction.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/0-dfCreation/0-main_createDFforPrediction.py)
- [`0-statistic.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/0-dfCreation/0-statistic.py)

Observed facts:

- the script reads `instances_v3/`;
- it calls `read_all_fft(inputPath)`;
- it generates the dataframe through `genDfWithAmplEPhase('Fw')`;
- it writes `dataFrame_prediction_Fw_v14_newFreq.csv`.

This is one of the clearest recovered proofs that the currently stored
training/evaluation branch is forward-side only.

The recovered dataframe header from the later snapshot matches the exact
10-harmonic RCIM set and contains:

- `rpm`
- `deg`
- `tor`
- `10 amplitude targets`
- `10 phase targets`

Recovered dataset facts from the shipped CSV snapshot:

- row count: `969`
- target columns: `20`
- temperature values present after filtering: `25`, `30`, `35`

Important implementation-facing interpretation:

- `deg` is almost certainly temperature in degrees Celsius, not angular
  position, because the filenames and the paper operating variables align to
  `rpm / torque / oil temperature`;
- the training problem is therefore not angle-conditioned TE prediction;
  it is operating-condition-conditioned harmonic-target prediction.

### Prediction Stage

The prediction stage is centered on:

- [`1-main_prediction_v18.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/1-prediction/1-main_prediction_v18.py)
- [`1-predictorML_v7.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/1-prediction/1-predictorML_v7.py)

Recovered facts from `1-main_prediction_v18.py`:

- it reads `dataFrame_prediction_Fw_v14_newFreq.csv`;
- it filters `deg <= 35`;
- it predicts all columns containing `ampl` or `phase`;
- it uses `MLModelMultipleOutput(..., 'tot')`;
- it calls `predictorMLEvalutationOnTrain(dfInput, 0.20)`;
- it writes outputs to `output_prediction/instV3.8_Fw_allFreq_def/`.

These recovered names are internally consistent with a forward-only branch and
should not be read as direction-agnostic assets.

Recovered final tuned model list in `v18`:

- `SVR(C=1, epsilon=0.0001, gamma=1.1e-06, kernel='rbf')`
- `MLPRegressor(activation='tanh', early_stopping=True,
  hidden_layer_sizes=(200, 50), learning_rate='adaptive', solver='adam',
  random_state=0)`
- `RandomForestRegressor(criterion='squared_error', max_depth=14,
  min_samples_split=3, n_estimators=90, random_state=0)`
- `DecisionTreeRegressor(criterion='squared_error', max_depth=16,
  min_samples_split=6, random_state=0)`
- `ExtraTreeRegressor(criterion='squared_error', max_depth=15,
  min_samples_split=5, random_state=0)`
- `ExtraTreesRegressor(criterion='squared_error', max_depth=15,
  min_samples_split=3, n_estimators=60, random_state=0)`
- `GradientBoostingRegressor(criterion='squared_error', learning_rate=0.1,
  max_depth=14, min_samples_split=14, n_estimators=36, random_state=0)`
- `HistGradientBoostingRegressor(random_state=0, learning_rate=0.21,
  max_depth=11, max_leaf_nodes=27)`
- `XGBRegressor(reg_lambda=20, alpha=0.01, max_depth=16,
  colsample_bytree=0.8, random_state=0)`
- `LGBMRegressor(learning_rate=0.39, max_depth=12, subsample=0.1,
  random_state=0)`
- `ELMRegressor(n_neurons=250, random_state=0)`

Important consequences:

- `ELM` appears in the training script, but not in the exact ONNX paper bank;
- therefore `ELM` was likely an experimented branch retained in code but not
  promoted into the final released paper model bank.

### Actual Training Formulation

The most important recovered implementation detail is inside
[`1-predictorML_v7.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/1-prediction/1-predictorML_v7.py).

The file shows that the paper code did not rely on a custom monolithic
multi-target network. Instead it used scikit-learn wrappers:

- `MultiOutputRegressor`
- `RegressorChain`
- plain single-output estimators
- optional `GridSearchCV`
- `cross_validate`

For the main paper-like prediction path, `MLModelMultipleOutput` is the
important class:

- it wraps the base estimator with `MultiOutputRegressor(model)`;
- inputs are explicitly `X = dfInput[['rpm', 'deg', 'tor']]`;
- targets are selected as `phase`, `ampl`, or both;
- train/test split is `train_test_split(..., test_size=0.20, random_state=0)`.

This is a crucial clarification for `Track 1`:

- the code launches one family object at a time;
- `MultiOutputRegressor` then clones that estimator internally per target;
- the workflow therefore still trains one estimator per target, but through a
  family-level wrapper rather than many hand-written scripts.

This is almost certainly why the recovered release surface is a bank of
single-target ONNX files even though the training code looks "multi-output".

### Export Logic

The export logic in `MLModelMultipleOutput.exportModel(...)` iterates through
`self.model.estimators_` and writes one ONNX file per target.

Special conversion branches exist for:

- `XGBRegressor`
- `LGBMRegressor`

Generic scikit export is used for the rest through `skl2onnx`.

This means the final paper-facing artifact surface is:

- not one model per family;
- but one model per family per target.

That aligns exactly with the recovered ONNX bank.

### Evaluation Stage

The evaluation stage is centered on
[`2-main_evaluatePrediction_v4.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_split_original_pipeline_fragment/2-evaluation/2-main_evaluatePrediction_v4.py).

Recovered facts:

- it loads predicted CSVs from `output_prediction/...`;
- it reconstructs predicted TE through `instance_v4.Instance`;
- it computes `MSE`, `RMSE`, `MAE`, and `MAPE`;
- it records both:
  - total-signal metrics;
  - per-component metrics for each `ampl_k` and `phase_k`;
- it exports paper-ready tables split by:
  - error type;
  - `ampl` versus `phase`.

This is one of the most valuable recovered pieces because it clarifies how the
paper likely chose the final target-wise winners:

- train the full family bank;
- compute per-target metrics;
- select the best family for each harmonic target afterward.

No recovered script currently proves an automatic selector step, so the final
selection mechanism should be treated as an implementation-facing inference,
not as a fully proven fact. However, the exported metrics and the exact ONNX
bank make this inference very strong.

### Latest Snapshot Meaning

The later snapshot fragment under
[`code/backup_latest_snapshot_fragment`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_latest_snapshot_fragment)
is not the same codebase as the original pipeline.

Recovered facts:

- `main_prediction_v17.py` is export-oriented;
- it uses `predictorML_allForExport(dfInput)`;
- it exports models immediately with `exportModel(...)`;
- it keeps only `9` families:
  `DT`, `ET`, `ERT`, `RF`, `GBM`, `HGBM`, `XGBM`, `LGBM`, `MLP`;
- it does not include `SVR`;
- it does not include `ELM`;
- it writes to `output_prediction/instV3.2_Fw/`.

Additional facts:

- the shipped snapshot output folder already contains prediction CSVs for those
  `9` families;
- `predictorML_v7.py` in the latest snapshot is not identical to the original
  `1-predictorML_v7.py`.

Meaning:

- this snapshot is useful as evidence of a later export-oriented working state;
- it should not be treated as the canonical paper training/evaluation release.

### Backup Legacy Evolution

The early backup code under
[`code/backup_legacy_early_snapshot`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_legacy_early_snapshot)
is extremely useful for understanding workflow evolution.

The strongest evidence is
[`instance_v2.py`](../../../reference/rcim_ml_compensation_recovered_assets/code/backup_legacy_early_snapshot/instance_v2.py).

Recovered facts:

- the older harmonic set was `0, 1, 40, 80, 120, 160, 200`;
- the instance object stored:
  - FW/BW signals;
  - FFT arrays;
  - filtered amplitudes;
  - filtered phases;
  - operating conditions `rpm`, `deg`, `tor`;
- reconstruction was done by summing cosine harmonics from amplitude and phase.

This is important for two reasons:

- it proves the harmonic-wise paper branch evolved from an earlier, simpler
  frequency set into the later exact RCIM set;
- it proves that amplitude/phase TE reconstruction is not just a paper concept
  but was encoded directly in the instance logic itself.

The backup ONNX variants confirm this evolution:

- some artifacts use the older `0,1,40,80,120,160,200` set;
- others use naming patterns closer to the later release;
- several naming conventions coexist.

The correct repository consequence is:

- do not mix `backup_legacy_early_snapshot` or `backup/onnx_variants` with
  the exact paper bank when building the paper-faithful baseline;
- use them only to understand how the workflow evolved and what old branches to
  avoid resurrecting accidentally.

### TwinCAT Deployment Evidence

Recovered TwinCAT XML exports under
[`deployment/twincat_xml`](../../../reference/rcim_ml_compensation_recovered_assets/deployment/twincat_xml)
prove that the paper workflow reached a real PLC-facing export path.

Recovered files:

- `gbr_singleModel_ampl_0.xml`
- `gbr_singleModel_ampl_1.xml`
- `gbr_singleModel_phase_0.xml`
- `gbr_singleModel_phase_1.xml`

Recovered facts from the XML:

- the producer is `Beckhoff MLlib`;
- the exports are tree-ensemble style machine-learning models;
- the files contain explicit split values, split variables, and tree nodes.

This is strong evidence that the paper workflow did not stop at offline Python
evaluation. It had a real deployable, inspectable, TwinCAT-compatible branch.

There is one important inconsistency to preserve honestly:

- `gbr_singleModel_ampl_0.xml` includes `defaultEngine="rf_fp64_engine"` and
  `int64_inputDimension="2"`;
- that is not fully consistent with the main recovered Python path, which uses
  `rpm`, `deg`, and `tor` as three inputs.

This should be recorded as an open question, not forced into certainty. The
most plausible explanations are:

- the XML is from an earlier reduced-input export branch;
- the XML filename and the underlying engine label belong to adjacent versions;
- the XML is a deployment-facing special case, not the exact final paper input
  schema.

## Why This Matters For This Repository

### Current Repository Position

Our current `Track 1` branch already reproduces the high-level concept:

- harmonic-wise offline prediction;
- TE reconstruction;
- offline paper-style benchmarking.

However, the recovered assets show that our current implementation is still not
paper-identical in the important details.

### The Most Important Gap

The paper-faithful recovered path is:

- input features: `rpm`, `deg`, `tor`
- target representation: `ampl_k`, `phase_k`
- family-level `MultiOutputRegressor`
- one exported ONNX per target
- component-wise and total evaluation
- later assembly of the best target-wise bank

Our current repository `Track 1` baseline differs mainly because it was built
as a repository-owned reconstruction path before these exact recovered assets
were available. That means the recovered package now gives us a stricter target
for parity.

### What The Recovered Assets Make Possible

The recovered assets make three new things practical:

- exact family and target inventory parity;
- exact hyperparameter parity for the final paper family list;
- exact export-surface parity through one ONNX per target.

This is the correct foundation for the next serious `Track 1` step.

## What Is Already Implemented Here

The repository already has:

- a canonical paper comparison report in
  [`RCIM Paper Reference Benchmark.md`](./RCIM%20Paper%20Reference%20Benchmark.md);
- a dedicated paper reimplementation root under
  [`scripts/paper_reimplementation/rcim_ml_compensation`](../../../scripts/paper_reimplementation/rcim_ml_compensation);
- a working offline harmonic-wise pipeline;
- a dedicated learning guide bundle for the harmonic-wise paper
  reimplementation;
- recovered asset organization and recovered-asset summary documentation.

This means the project no longer needs to guess the paper branch from the PDF
alone. We can now pivot from "paper-aligned approximation" toward
"asset-grounded faithful reimplementation".

## What Remains Missing, Risky, Or Uncertain

### Incomplete Original Runtime Environment

The original pipeline is not fully runnable as recovered.

Missing or unresolved dependencies include:

- `instance_v5` in dataframe creation and signal evaluation;
- `instance_v4` in prediction evaluation.

This means we can reconstruct the workflow very accurately, but we cannot
simply rerun the original codebase as-is and treat the output as the ground
truth reference.

### Mixed-Version Evidence

The recovered package is not a single frozen release tag.

Signs of version mixing:

- training stage references `instances_v3`;
- evaluation stage references `instances_v2`;
- dataframe creation imports `instance_v5`;
- evaluation imports `instance_v4`;
- latest snapshot differs from original predictor code;
- backup code uses an older harmonic set.

Repository consequence:

- exact methodological reimplementation is feasible;
- exact bit-for-bit rerun of the paper workspace is still uncertain.

### ELM Discrepancy

`ELMRegressor` appears in the original `v18` training script but is absent from
the exact final ONNX bank.

Repository consequence:

- do not treat `ELM` as part of the canonical paper-faithful final family set;
- keep it only as an optional historical branch if ever needed.

### `phase_0` And DC Handling

The recovered bank includes `phase_0` targets, even though the DC component
phase is usually trivial or fixed.

The older `instance_v2.py` explicitly sets phase for `k=0` to zero.

Repository consequence:

- exact parity may require carrying `phase_0` as a formally present target;
- practical simplification may later replace it with a constant, but not before
  parity validation.

### `instance_v1` Archive Meaning

The large `instance_v1` archive contains:

- `913` `.pickle` files;
- about `4.68 GB` total size;
- filenames indexed by `rpm`, `Torque`, and `deg`.

A quick pickle opcode inspection shows references to:

- module name `instance_v4`
- class name `Instance`

That strongly supports this interpretation:

- `instance_v1` is an archive of serialized operating-condition instances;
- it is not primarily a bank of trained ML models.

This is important because the user hypothesis about `.pkl` models was
reasonable, but the recovered evidence currently points more strongly to stored
instance objects and signal archives than to estimator pickles.

## Exact Consequences For Track 1 Reimplementation

The recovered assets imply that the next strict `Track 1` branch should do the
following.

### 1. Reimplement The Exact Paper Target Space

Treat the canonical paper target set as:

- `ampl_k` and `phase_k`
- over `k = 0, 1, 3, 39, 40, 78, 81, 156, 162, 240`

Do not use reduced harmonic debugging sets as the final paper-faithful target.

### 2. Mirror The Exact Input Space

Use operating-condition inputs:

- `rpm`
- `deg`
- `tor`

Do not mix in angle-conditioned TE-direct predictors inside the paper-faithful
branch. Those belong to the repository comparison track, not the reproduction
track.

### 3. Mirror The Family Bank

The exact paper-faithful family bank should be:

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

This family set should be the reference bank for paper-faithful parity work.

### 4. Mirror The Training Formulation

The closest faithful reimplementation is:

- one family launch at a time;
- `MultiOutputRegressor(base_estimator)` over the full target list;
- internal per-target estimator fitting handled by scikit-learn;
- deterministic `train_test_split(..., test_size=0.20, random_state=0)`.

This is the right compromise between:

- faithfulness to the recovered code;
- practical maintainability inside our repository.

### 5. Mirror The Export Surface

Export one ONNX per family per target.

That means the faithful repository branch should generate:

- family banks;
- not only reconstructed curves or family-level bundles.

### 6. Mirror The Evaluation Surface

The faithful evaluation branch should report both:

- total TE reconstruction metrics;
- per-target `ampl_k` and `phase_k` metrics.

Without the per-target metrics, we cannot replicate the family-selection logic
that the recovered paper workflow strongly implies.

### 7. Add A Target-Wise Winner Registry

The recovered workflow strongly suggests a final selection layer:

- best family for `ampl_0`
- best family for `phase_0`
- ...
- best family for `ampl_240`
- best family for `phase_240`

This repository should therefore add an inspectable target-wise registry rather
than keeping `Track 1` as a single-family-only benchmark.

## Recommended Next Steps

The next implementation order should be:

1. create a strict `Track 1` sub-branch for exact paper-family reproduction;
2. add the exact RCIM target schema `ampl/phase` instead of only the current
   repository harmonic parameterization;
3. implement the exact family bank and recovered tuned hyperparameters;
4. export one ONNX per target and compare the generated bank against the
   recovered exact ONNX release;
5. reproduce the paper-style component tables;
6. build a target-wise winner selector and registry;
7. only after that, reconcile this strict branch with the current repository
   harmonic-wise baseline and decide what stays canonical.

## Final Assessment

The recovered RCIM assets are now strong enough to move `Track 1` from a
paper-aligned approximation into a much stricter paper-faithful
reimplementation program.

They do not give us a perfectly runnable frozen workspace. They do give us the
following with high confidence:

- the final harmonic set;
- the final family bank;
- the actual training wrapper strategy;
- the exact ONNX deployment surface;
- the component-wise evaluation logic;
- the TwinCAT export reality of the paper branch.

That is enough to define the next serious phase of `Track 1` with much less
guesswork than before.
