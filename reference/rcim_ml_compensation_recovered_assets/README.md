# RCIM ML Compensation Recovered Assets

This folder contains the recovered asset package associated with the RCIM
ML-compensation paper and adjacent paper-era experimentation.

It is intended as a repository-owned reference surface for:

- exact recovered ONNX model exports;
- original recovered paper workflow code;
- later recovered code snapshots that appear to postdate the exact paper
  release;
- backup ONNX bundles and backup code variants;
- recovered TwinCAT XML exports;
- archived instance pickle material used by the paper pipeline.

## Provenance Groups

### Exact Paper ONNX Models

- [models/exact_onnx_paper_release/](./models/exact_onnx_paper_release/)

Recovered exact ONNX exports grouped by family and by target type:

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

### Original Recovered Paper Pipeline

- [code/original_pipeline/](./code/original_pipeline/)

This subtree contains the recovered staged workflow:

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

Main implementation facts extracted from this snapshot:

- the learning targets are harmonic-wise `ampl` and `phase` outputs;
- the working input columns are `rpm`, `deg`, and `tor`;
- the workflow exports ONNX models for scikit-learn, XGBoost, and LightGBM
  families;
- the recovered `v18` script includes tuned concrete models for the main paper
  family set and also includes an `ELMRegressor` dependency that is not part
  of the exact ONNX paper release.

### Latest Recovered Code Snapshot

- [code/latest_snapshot/](./code/latest_snapshot/)

This subtree appears to be a later working snapshot, not the exact paper
release. It contains:

- `main_prediction_v17.py`
- `predictorML_v7.py`
- `dataFrame_prediction_Fw_v14_newFreq.csv`
- `requirements.txt`
- `output_prediction/`

Compared with the original recovered pipeline, this snapshot is narrower and
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

This latest snapshot does not include the same explicit `SVR` and `ELM`
coverage seen in `1-main_prediction_v18.py`.

### Backup Legacy Code

- [code/backup_legacy/](./code/backup_legacy/)

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

This confirms that the backup subtree contains meaningful historical evolution,
not just redundant copies.

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
2. The exact recovered model families match the paper family set used in the
   repository benchmark discussion.
3. The pipeline was organized as a staged process:
   dataframe creation, model prediction/export, and offline evaluation.
4. TwinCAT-facing export was a real implementation branch, not just a paper
   claim.
5. The recovered codebase evolved over multiple internal generations, so the
   repository must keep a clear distinction between:
   exact paper assets, later snapshots, and historical backups.

## Relationship To This Repository

This asset package supports the repository in three different ways:

- `Track 1`
  Exact paper-faithful reimplementation and verification.
- `Paper Reference Benchmark`
  Evidence-backed comparison between the paper workflow and the repository
  offline results.
- `Future TwinCAT Preparation`
  Deployment-facing understanding of how model exports may need to be
  structured for PLC-friendly execution.
