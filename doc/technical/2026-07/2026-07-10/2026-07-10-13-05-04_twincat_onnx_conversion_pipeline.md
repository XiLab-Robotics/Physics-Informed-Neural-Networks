# TwinCAT ONNX Conversion Pipeline

## Overview

This technical document plans a repository-owned TwinCAT-facing ONNX
conversion pipeline for exported transmission-error models.

The immediate trigger is the need to run repository-exported ONNX models inside
the existing TestRig PLC code under `reference/codes/TestRig`, which currently
uses Beckhoff `Tc3_MLL.FB_MllPrediction` through the `FB_Predict` wrapper.

The first implementation target is a simple feedforward ONNX export, because it
is the lowest-risk candidate for the current Beckhoff `TF38x0` ML/NN Inference
Engine path. More complex sequence and mixture-density models remain useful for
offline analysis, but they already show operator and shape patterns that may
not be accepted by the deterministic PLC runtime.

## Technical Approach

The approved implementation should create a compact conversion toolchain under a
new deployment-oriented repository location, provisionally:

- `scripts/deployment/twincat_onnx_conversion/`
- `doc/scripts/deployment/twincat_onnx_conversion/`
- `requirements-twincat-onnx-conversion.txt`

The pipeline should preserve two Beckhoff paths as separate outputs.

### Primary Path: TF38x0 ML/NN Inference Engine

This is the compatibility path for the current TestRig PLC code.

The current imported PLC reference uses:

- `FB_MllPrediction`;
- Beckhoff XML/BML description files;
- `PredictRef(...)` with named multi-engine references such as `engine_1`;
- explicit PLC-side harmonic reconstruction.

The official Beckhoff documentation confirms that raw ONNX is not directly
loaded by the `TF38x0` runtime. ONNX must be converted to Beckhoff-specific
`XML` or `BML` with Model Manager tooling before PLC runtime loading.

The implementation should therefore wrap the tracked local Beckhoff tool copy
in:

```text
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/mllib_toolbox.exe onnximport <model.onnx> <model.xml>
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/mllib_toolbox.exe store <model.xml> <model.bml>
```

The pipeline should keep the recovered Beckhoff Model Manager API assets in the
same tracked deployment directory as the conversion helper so the workflow is
repeatable from a repository checkout without depending on the incorrect
upstream documentation path. The copied assets should include:

- `mllib_toolbox.exe`;
- `ModelManagerStandalone.exe`;
- `MLAIPlugin.dll`;
- `mllib_um.dll`;
- `mllib_um32.dll`;
- `ML_TcCOM_Extension.dll`;
- `ML_TcCOM_Extension.dll.config`;
- `PythonPackage/beckhoff_toolbox-3.1.251201-py3-none-any.whl`.

The first smoke conversion should target a current simple feedforward ONNX,
preferably:

```text
models/polished_dataset/actual_values/exported/feedforward/forward/
2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/onnx/model.onnx
```

If that model fails, the fallback should be a repository RCIM model-bank `MLP`
or another simple feedforward export with fixed shape and supported operators.

### Secondary Path: TF3820 Machine Learning Server

This is not a drop-in replacement for the current TestRig PLC code, but the
implementation should make it visible as an evaluation path.

The official Beckhoff documentation describes `TF3820` as loading ONNX files via
the Machine Learning Server, with Model Manager producing:

- JSON metadata;
- PLCopenXML input/output data type descriptions.

The CLI path is:

```text
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/mllib_toolbox.exe onnxprep <model.onnx>
```

The pipeline should optionally generate these artifacts for the same model, but
the documentation must state that this changes the PLC integration surface from
`FB_MllPrediction` to `FB_MlSvrPrediction` and changes execution semantics to
asynchronous server-backed inference.

### ONNX Inspection And Compatibility Checks

Before Beckhoff conversion, the pipeline should inspect each ONNX model and
write a machine-readable summary containing:

- model path and SHA-256;
- ONNX IR version and opset imports;
- input and output names, element types, and shapes;
- operator histogram;
- dynamic dimension detection;
- `INT64_MAX` constants used as open slice sentinels;
- candidate Beckhoff route:
  - `tf38x0_candidate`;
  - `tf3820_candidate`;
  - `inspection_only`.

The `.temp/Beckhoff_ONNX_MLlib_Chat_Handoff.md` note shows a concrete failure
where Beckhoff MLlib 3.1.251201.0 failed on a formally valid ONNX model because
a `Constant` node contained `9223372036854775807` as an open-slice sentinel.
The repository pipeline should detect and report that pattern before invoking
Beckhoff tooling. Automatic patching should be a separate explicit mode, not
the default first pass.

### Output Layout

For each conversion run, the tool should write under a timestamped output root,
for example:

```text
output/deployment/twincat_onnx_conversion/<timestamp>_<model_slug>/
```

Expected files:

- copied or linked source ONNX;
- `inspection_summary.json`;
- `conversion_manifest.yaml`;
- `tf38x0/model.xml` when `onnximport` succeeds;
- `tf38x0/model.bml` when `store` succeeds;
- `tf38x0/info.txt` from Beckhoff `info`;
- `tf3820/model.json` and generated PLCopenXML when `onnxprep` is requested;
- `logs/*.log` for every Beckhoff command.

The manifest must preserve dataset identity, source model family, surface, input
contract, and conversion status. This is important because the repository now
keeps `polished_dataset` and `simplified_dataset` model archives separate.

## Involved Components

- `.temp/ModelManagerAPI/`
  Local recovered Beckhoff Model Manager API source folder. The official install
  path documented by Beckhoff may be wrong for this checkout, but the recovered
  files are present locally.

- `.temp/TcMLExtension/`
  Local recovered Beckhoff runtime DLL source folder containing `mllib_um.dll`
  and related TcML extension files required by `mllib_toolbox.exe`.

- `scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/`
  Tracked repository copy of the recovered Beckhoff Model Manager API files used
  by the conversion runner.

- `.temp/Beckhoff_ONNX_MLlib_Chat_Handoff.md`
  Prior diagnostic handoff documenting the `INT64_MAX` open-slice failure
  pattern seen with Beckhoff MLlib 3.1.251201.0.

- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning/`
  Current PLC reference implementation using `FB_MllPrediction`.

- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Existing repository-owned analysis of the TestRig PLC ML path and Beckhoff
  runtime options.

- `models/polished_dataset/actual_values/exported/feedforward/`
  Preferred first feedforward ONNX candidate for conversion smoke testing.

- `scripts/deployment/twincat_onnx_conversion/`
  Proposed implementation location for the conversion runner and support code.

- `doc/scripts/deployment/twincat_onnx_conversion/`
  Proposed user-facing README location for installation, commands, expected
  artifacts, and TwinCAT-side interpretation.

- `requirements-twincat-onnx-conversion.txt`
  Proposed dependency surface for the conversion utility. Expected packages are
  `onnx`, `onnxruntime`, `numpy`, `PyYAML`, and the local Beckhoff wheel.

## Implementation Steps

1. Create and register this technical document.
2. Wait for explicit user approval before implementing repository scripts,
   copying Beckhoff toolbox assets, changing requirements, or running conversion
   smoke tests.
3. Create the deployment script directory and a local vendor/tooling copy of the
   recovered Model Manager API files.
4. Add a requirements file documenting both normal Python dependencies and the
   local Beckhoff wheel installation command.
5. Implement an ONNX inspection helper that detects operator support risks,
   dynamic shapes, and open-slice `INT64_MAX` constants.
6. Implement a conversion runner around `mllib_toolbox.exe` for:
   - `onnximport` to XML;
   - `store` XML to BML;
   - `info` on generated artifacts;
   - optional `onnxprep` for TF3820 JSON and PLCopenXML.
7. Add a README covering setup, exact commands, output layout, and the decision
   boundary between deterministic `TF38x0` and asynchronous `TF3820`.
8. Run the first smoke test on a simple feedforward ONNX model and record the
   generated manifest and logs.
9. Run Python syntax checks and Markdown warning checks on the touched scope.
10. Report the conversion result and stop for review before any commit.

## Current Documentation Findings

The implementation should be grounded in these confirmed Beckhoff facts:

- `TF38x0` conversion requires ONNX to be converted to Beckhoff XML/BML before
  TwinCAT runtime loading.
- Beckhoff XML/BML supports multi-engine organization, and `PredictRef(...)`
  can address a named engine without latency once the description file is
  loaded.
- `TF38x0` supports selected model types such as SVM, PCA, k-Means, Random
  Forest, MLP, Decision Tree, Extra Tree(s), Gradient Boosting, Hist Gradient
  Boosting, XGBoost, and LightGBM, with license and setup-version differences.
- `TF3820` Machine Learning Server loads ONNX files through a server/client
  architecture and prepares JSON plus PLCopenXML interface descriptions.
- `TF3820` supports ONNX Opset 21 according to the current documentation, but
  does not support dynamic input/output shapes except for a leading dynamic
  batch dimension.
- `TF3820` inference is asynchronous and user-mode/server-backed, so it is not
  equivalent to the deterministic in-process `TF38x0` PLC runtime used by the
  current TestRig code.

## Approval Boundary

No subagent is planned for the first implementation pass.

Approval of this document authorizes only the scoped pipeline, README,
requirements update, toolbox copy, and one feedforward smoke conversion. It does
not authorize rewriting the PLC TestRig code or switching the PLC integration
from `FB_MllPrediction` to `FB_MlSvrPrediction`.

## Sources

- Beckhoff, `TF38x0 | Creation and conversion of ONNX`:
  <https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8327536651.html>
- Beckhoff, `TF38x0 | Conversion from ONNX to XML and BML`:
  <https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/13583063819.html>
- Beckhoff, `TF38x0 | Beckhoff ML XML`:
  <https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8436762635.html>
- Beckhoff, `TF38x0 | Machine learning models supported`:
  <https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8353052299.html>
- Beckhoff, `TF3820 | Overview`:
  <https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17276122123.html>
- Beckhoff, `TF3820 | Preparing ONNX for use with TwinCAT Machine Learning Server`:
  <https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17289310091.html>
- Beckhoff, `TF3820 | ONNX Support`:
  <https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17311427723.html>
- Beckhoff, `TF3820 | Python interface`:
  <https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17314850571.html>
- Beckhoff, `TF3820 | Command Line Interface`:
  <https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17314851723.html>
