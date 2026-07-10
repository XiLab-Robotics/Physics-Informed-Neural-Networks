# TwinCAT ONNX Conversion Pipeline

## Purpose

This utility converts repository-exported ONNX models into Beckhoff artifacts
for TwinCAT deployment review.

The default path targets the current TestRig PLC code in
`reference/codes/TestRig`, which uses `Tc3_MLL.FB_MllPrediction` through the
`FB_Predict` wrapper. That path requires Beckhoff XML/BML files generated from
ONNX; it does not load raw ONNX directly in the PLC task.

The optional `TF3820` path prepares Machine Learning Server artifacts for
evaluation, but it is not a drop-in replacement for the current TestRig code.
It changes the PLC API to `FB_MlSvrPrediction` and uses asynchronous
server-backed inference.

## Local Beckhoff Toolbox

The recovered toolbox files are tracked with the conversion pipeline in:

```text
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/
```

Expected files:

```text
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/mllib_toolbox.exe
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/ModelManagerStandalone.exe
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/MLAIPlugin.dll
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/mllib_um.dll
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/mllib_um32.dll
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/ML_TcCOM_Extension.dll
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/ML_TcCOM_Extension.dll.config
scripts/deployment/twincat_onnx_conversion/ModelManagerAPI/PythonPackage/beckhoff_toolbox-3.1.251201-py3-none-any.whl
```

If the toolbox copy is missing, refresh it from the recovered handoff folder:

```powershell
New-Item -ItemType Directory -Force scripts\deployment\twincat_onnx_conversion\ModelManagerAPI | Out-Null
Copy-Item .temp\ModelManagerAPI\mllib_toolbox.exe scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\mllib_toolbox.exe -Force
Copy-Item .temp\ModelManagerAPI\ModelManagerStandalone.exe scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\ModelManagerStandalone.exe -Force
Copy-Item .temp\TcMLExtension\MLAIPlugin.dll scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\MLAIPlugin.dll -Force
Copy-Item .temp\TcMLExtension\mllib_um.dll scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\mllib_um.dll -Force
Copy-Item .temp\TcMLExtension\mllib_um32.dll scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\mllib_um32.dll -Force
Copy-Item .temp\TcMLExtension\ML_TcCOM_Extension.dll scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\ML_TcCOM_Extension.dll -Force
Copy-Item .temp\TcMLExtension\ML_TcCOM_Extension.dll.config scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\ML_TcCOM_Extension.dll.config -Force
New-Item -ItemType Directory -Force scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\PythonPackage | Out-Null
Copy-Item .temp\ModelManagerAPI\PythonPackage\beckhoff_toolbox-3.1.251201-py3-none-any.whl scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\PythonPackage\beckhoff_toolbox-3.1.251201-py3-none-any.whl -Force
```

The `mllib_um.dll` runtime comes from `.temp/TcMLExtension`. Without that DLL,
`mllib_toolbox.exe` starts but cannot execute `onnximport`, `store`, or
`onnxprep`.

## Environment

The repository base environment already carries the normal ONNX dependencies in
`requirements.txt`. For the smaller TwinCAT conversion surface, install:

```powershell
python -m pip install -r requirements-twincat-onnx-conversion.txt
python -m pip install scripts\deployment\twincat_onnx_conversion\ModelManagerAPI\PythonPackage\beckhoff_toolbox-3.1.251201-py3-none-any.whl
```

## Default Smoke Conversion

Run the default feedforward conversion candidate:

```powershell
python -B scripts\deployment\twincat_onnx_conversion\convert_onnx_for_twincat.py `
  --run-onnxruntime-smoke `
  --copy-source-onnx
```

The default source model is:

```text
models/polished_dataset/actual_values/exported/feedforward/forward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/onnx/model.onnx
```

To convert a specific ONNX model:

```powershell
python -B scripts\deployment\twincat_onnx_conversion\convert_onnx_for_twincat.py `
  --onnx models\polished_dataset\actual_values\exported\feedforward\forward\2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values\onnx\model.onnx `
  --run-onnxruntime-smoke `
  --copy-source-onnx
```

## Optional TF3820 Artifacts

Generate Machine Learning Server preparation artifacts in addition to XML/BML:

```powershell
python -B scripts\deployment\twincat_onnx_conversion\convert_onnx_for_twincat.py `
  --prepare-tf3820 `
  --run-onnxruntime-smoke
```

Use these files only for an explicit `TF3820` design review. They do not match
the current TestRig `FB_MllPrediction` PLC runtime path.

## Output Layout

Each run writes to:

```text
output/deployment/twincat_onnx_conversion/<timestamp>_<model_slug>/
```

Expected files:

```text
inspection_summary.json
onnxruntime_smoke.json
conversion_manifest.yaml
source_model.onnx
tf38x0/model.xml
tf38x0/model.bml
tf38x0/info.txt
tf3820/model.json
logs/*.log
```

`conversion_manifest.yaml` is the main review surface. It records source model
identity, dataset metadata from `reference_inventory.yaml` when available,
inspection findings, command results, and generated artifact paths. The runner
always copies the source model into the run directory as `source_model.onnx` and
passes that shorter local path to Beckhoff tooling, because the Beckhoff CLI can
fail on deep Windows paths even when Python can read the same ONNX file.

## Compatibility Checks

Before running Beckhoff conversion, the script inspects the ONNX model for:

- ONNX checker status;
- IR version and opset imports;
- input and output names, types, and shapes;
- operator histogram;
- dynamic dimensions;
- `INT64_MAX` constants used as open-slice sentinels.

The `INT64_MAX` check exists because Beckhoff MLlib 3.1.251201.0 has already
failed on a formally valid ONNX model whose `Constant` node represented an
open-ended slice. The converter reports this condition but does not patch the
model automatically.

## Current Smoke Results

With the DLL files from `.temp/TcMLExtension` copied into the tracked
`ModelManagerAPI` folder, Beckhoff `mllib_toolbox.exe` starts correctly and the
runtime preflight reports `status: ready`.

Validated successful `TF38x0` conversion:

```text
output/validation_checks/rcim_model_bank_reproduction/2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation/onnx_export/MLP/MLPRegressor_ampl0.onnx
```

Generated:

```text
output/deployment/twincat_onnx_conversion/rcim_mlp_ampl0_local_source_with_tcmlextension_dlls/tf38x0/model.xml
output/deployment/twincat_onnx_conversion/rcim_mlp_ampl0_local_source_with_tcmlextension_dlls/tf38x0/model.bml
```

The current PyTorch feedforward smoke model still fails Beckhoff `onnximport`
after the DLL integration. ONNX checker and ONNX Runtime both pass, but
Beckhoff MLlib 3.1.251201.0 reports:

```text
MLLIB_ERROR_INTERNAL_ALLOCATION
ONNX Constant node attributes could not be read.
Could not read ONNX operator node 'Constant'.
```

That failure is now a model-graph compatibility issue, not a missing-runtime or
path-length issue.

## TwinCAT Interpretation

Use `TF38x0` XML/BML outputs for the current TestRig code path:

```text
ONNX -> XML/BML -> FB_MllPrediction -> PredictRef(...)
```

Use `TF3820` artifacts only when planning a PLC architecture update:

```text
ONNX -> JSON + PLCopenXML -> Machine Learning Server -> FB_MlSvrPrediction
```

For tight online TE compensation, the deterministic `TF38x0` path remains the
first implementation target until the asynchronous server path is explicitly
benchmarked against the PLC timing budget.
