# RCIM ML Compensation Recovered Assets

This root stores the generic recovered RCIM asset package associated with the
RCIM ML-compensation paper and adjacent paper-era experimentation.

The root stays generic because it contains:

- generic recovered code snapshots and backup material;
- deployment-facing recovered exports;
- heavy archived instance material;
- forward-only benchmark artifacts such as the exact ONNX paper release and
  the shipped `Fw` dataframe.

It is intended as a repository-owned reference surface for:

- exact recovered forward-only ONNX model exports;
- original recovered paper workflow code;
- later recovered code snapshots that appear to postdate the exact paper
  release;
- backup ONNX bundles and backup code variants;
- recovered TwinCAT XML exports;
- archived instance pickle material used by the paper pipeline.

## Provenance Groups

### Exact Paper ONNX Models

- [models/exact_onnx_paper_release/](./models/exact_onnx_paper_release/)

Recovered exact ONNX exports grouped by family and by target type.

Important interpretation:

- these recovered exact ONNX models correspond to the `forward` branch only;
- they must not be treated as interchangeable with the missing
  backward-specific models implied by the generalized notation in the paper.

- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `LGBM`
- `MLP`
- `RF`
- `SVR`
- `XGBM`

The exact-paper ONNX area contains `201` files for about `0.125 GB`.

The intended harmonic targets are split into:

- `ampl/`
- `phase/`

The recovered harmonic indices are:

- `0`
- `1`
- `3`
- `39`
- `40`
- `78`
- `81`
- `156`
- `162`
- `240`

Expected baseline count is `200` models:

- `10` families
- `10` amplitude models
- `10` phase models

One duplicate recovered artifact is preserved as evidence instead of being
silently removed:

- `RF/ampl/RandomForestRegressor_ampl240.onnx`
- `RF/ampl/RandomForestRegressor_ampl240 (1).onnx`

### Canonical Original Repository Root

- [code/original_pipeline/](./code/original_pipeline/)

This folder now contains the full recovered original RCIM workflow root sent by
the authors.

Observed top-level contents include:

- `0-main_createDFforPrediction.py`
- `1-main_prediction_v18.py`
- `1.1-main_prediction_v17.py`
- `2-main_evaluatePrediction_v4.py`
- `predictorML_v7.py`
- `statistic.py`
- `instance_v4.py`
- `instance_v5.py`
- `instances_V3/`
- `dataFrame_prediction_Fw_v14_newFreq.csv`
- `dataFrame_prediction_Bw_v14_newFreq.csv`
- `output_prediction/`
- `evaluation/`
- author `README.md`

This root is now the strongest recovered code evidence because it includes:

- executable scripts;
- cached `.pickle` inputs;
- generated model and evaluation artifacts;
- direct author guidance on the intended usage split between `v17` and `v18`.

### Split Late Pipeline Fragment

- [code/backup_split_original_pipeline_fragment/](./code/backup_split_original_pipeline_fragment/)

This subtree preserves the split recovered staged workflow that previously
lived under the misleading `code/original_pipeline/` name.

It contains the recovered staged workflow fragments for:

- dataframe creation;
- prediction;
- evaluation.

Key files:

- `0-dfCreation/0-main_createDFforPrediction.py`
- `1-prediction/1-main_prediction_v18.py`
- `1-prediction/1-predictorML_v7.py`
- `2-evaluation/2-main_evaluatePrediction_v4.py`
- `2-evaluation/2-main_evaluateSignals.py`
- `0-requirements.txt`

Main implementation facts extracted from this fragment:

- the learning targets are harmonic-wise `ampl` and `phase` outputs;
- the working input columns are `rpm`, `deg`, and `tor`;
- the generated dataframe is `Fw`-specific and therefore forward-only;
- the workflow exports ONNX models for scikit-learn, XGBoost, and LightGBM
  families;
- the recovered `v18` script includes tuned concrete models for the main paper
  family set and also includes an `ELMRegressor` dependency that is not part
  of the exact ONNX paper release.

### Latest Snapshot Fragment

- [code/backup_latest_snapshot_fragment/](./code/backup_latest_snapshot_fragment/)

This subtree preserves the later working snapshot that previously lived under
the old `code/latest_snapshot/` name. It contains:

- `main_prediction_v17.py`
- `predictorML_v7.py`
- `dataFrame_prediction_Fw_v14_newFreq.csv`
- `dataFrame_prediction_Bw_v14_newFreq.csv`
- `requirements.txt`

The shipped CSVs and training entrypoints in this snapshot fragment are
direction-specific recovered artifacts.

Compared with the split late pipeline fragment, this snapshot is narrower and
appears focused on export and prediction runs for:

- `DecisionTreeRegressor`
- `ExtraTreeRegressor`
- `ExtraTreesRegressor`
- `RandomForestRegressor`
- `GradientBoostingRegressor`
- `HistGradientBoostingRegressor`
- `XGBRegressor`
- `LGBMRegressor`
- `MLPRegressor`

This latest snapshot fragment does not include the same explicit `SVR` and
`ELM` coverage seen in `1-main_prediction_v18.py`.

Author clarification now captured in the repository:

- this `v17` branch is the structure used to export final models trained on
  the whole dataset;
- to retune hyperparameters on a new dataset, the intended branch is to start
  from the `v17` structure and replace `predictorML_allForExport` with
  `predictorMLCrossValidationWithHyperparameter`.

### Early Legacy Backup Code

- [code/backup_legacy_early_snapshot/](./code/backup_legacy_early_snapshot/)

This subtree preserves older backup material:

- `instance_v2.py`
- `predictorML.py`
- `predictorPolyFunc.py`
- `statistic.py`
- notebook and CSV artifacts
- historical output predictions

This backup code is useful because it exposes an earlier harmonic workflow and
an older `Instance` implementation.

One important difference from the exact-paper ONNX release is visible here:

- backup `instance_v2.py` hardcodes an earlier frequency list
  `0, 1, 40, 80, 120, 160, 200`
- exact recovered paper ONNX models use the later harmonic set
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`

This confirms that the early backup subtree contains meaningful historical
evolution, not just redundant copies.

### Backup ONNX Variants

- [backup/onnx_variants/](./backup/onnx_variants/)

This subtree contains `124` ONNX files for about `0.084 GB`, including:

- earlier single-model exports;
- combined-model experiments;
- MLP and GBR mixed bundles;
- sample ONNX files;
- a recovered `modello_completo/` branch.

These files are preserved as secondary historical evidence and should not be
mistaken for the exact paper release unless a file is explicitly cross-mapped.

### TwinCAT XML Exports

- [deployment/twincat_xml/](./deployment/twincat_xml/)

This subtree preserves the recovered TwinCAT XML exports:

- `gbr_singleModel_ampl_0.xml`
- `gbr_singleModel_ampl_1.xml`
- `gbr_singleModel_phase_0.xml`
- `gbr_singleModel_phase_1.xml`

These files matter because they show a recovered Beckhoff MLlib deployment path
for paper-era gradient-boosting components.

### Instance Archives

- [data/instance_archives/README.md](./data/instance_archives/README.md)

The `instance_v1` subtree is the heavy recovered archive and should be handled
as data-like reference material, not as lightweight code.

## What This Package Says About The Paper Workflow

The recovered assets support these repository-relevant conclusions:

1. The paper workflow is genuinely harmonic-wise and predicts amplitude and
   phase components rather than only direct TE curves.
2. The currently recovered repository-owned asset bank corresponds to the
   `forward` branch only, even though the paper notation is generalized to
   cover both forward and backward formulations.
3. The exact recovered model families match the paper family set used in the
   repository benchmark discussion.
4. The pipeline was organized as a staged process:
   dataframe creation, model prediction/export, and offline evaluation.
5. TwinCAT-facing export was a real implementation branch, not just a paper
   claim.
6. The recovered codebase evolved over multiple internal generations, so the
   repository must keep a clear distinction between:
   exact paper assets, later snapshots, and historical backups.
7. The full author-supplied original root confirms that the workflow relied on
   cached `instances_V3` `.pickle` files for faster reuse, while still being
   designed to create those caches from CSV inputs when absent.

## Relationship To This Repository

This asset package supports the repository in three different ways:

- `Track 1`
  Exact paper-faithful `forward` reimplementation and verification.
- `Paper Reference Benchmark`
  Evidence-backed comparison between the paper workflow and the repository
  offline results.
- `Future TwinCAT Preparation`
  Deployment-facing understanding of how model exports may need to be
  structured for PLC-friendly execution.
