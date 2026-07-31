# Forward Polished Setpoints TF3820 Model Catalog Refresh

## Overview

This technical document defines the refresh of the standalone TwinCAT `TF3820`
model catalog from the canonical forward model artifacts under
`models/polished_dataset/setpoints`.

The live source inventory contains 36 trained model-family directories. Every
family exposes one canonical forward ONNX model at
`<family>/forward/onnx/model.onnx`. The current standalone TwinCAT project
contains 37 prepared packages under `ML_models`, including `rcim_track1`, which
is not present in the requested source root. The refresh will therefore rebuild
the destination strictly from the 36 canonical forward setpoint families and
remove destination-only model packages.

Each refreshed family must remain runnable through the existing reusable
`FB_TF3820TransmissionErrorPredictor`. The work includes TF3820 preparation of
the ONNX model, generation of the matching JSON and PLCopen XML artifacts, and
synchronization of the PLC enumeration, generated tensor DUTs, model runners,
predictor dispatch, output reconstruction, project compile inventory, import
pack, and user documentation.

The active training campaign is completed, and none of its protected files are
in this change scope. This task does not train or select models. No subagent is
planned or authorized.

## Technical Approach

### Canonical Model Discovery

The export workflow will discover immediate family directories under
`models/polished_dataset/setpoints` and require exactly one source artifact per
family at `forward/onnx/model.onnx`. Backward and global artifacts will be
excluded.

The discovery step will fail on missing or duplicate forward artifacts and will
record source-relative paths and SHA-256 hashes. The destination catalog will
be derived from this inventory rather than from a hard-coded family list, so a
future family addition or removal is visible and reproducible.

### TF3820 Preparation And Artifact Replacement

Each source ONNX model will be inspected and prepared with the repository-owned
Beckhoff Model Manager workflow. The required family-local output contract is:

```text
ML_models/<family>/model.onnx
ML_models/<family>/model.json
ML_models/<family>/model_plcopen.xml
```

The refresh will be staged in a temporary generated directory and validated
before replacing the maintained `ML_models` content. The final folder set must
match the canonical 36-family inventory exactly; `rcim_track1` and any other
destination-only package will not be retained.

TF3820 preparation will preserve fixed non-batch tensor dimensions, model input
and output names, floating-point types, and the preprocessing embedded in each
ONNX graph. Physical input values will remain angle, speed, signed torque,
temperature, and direction where required by the model contract. Temporal
models will retain the predictor-owned 33-sample real-history window.

### Generated PLC Catalog Synchronization

The harness generator will be updated or reused so that the prepared artifact
inventory is the single source for:

- `E_TF3820StandaloneModelId` members and stable numeric values;
- model-specific input and output DUT declarations extracted from PLCopen XML;
- one `FB_<Family>Tf3820Runner` per family;
- model paths and runner instances in
  `FB_TF3820TransmissionErrorPredictor`;
- configure, reset, prediction, and model-selection dispatch branches;
- deterministic TE reconstruction for scalar, Gaussian, quantile, and
  mixture-density output contracts;
- PLC project compile items and the TestRig predictor import pack.

Existing enum values will be preserved where the family still exists. New
families, if discovered during implementation, will receive appended stable
values. Removed families will be removed from the enum and all dispatch and
compile surfaces. Generated identifiers and GUIDs will remain deterministic.

### Verification Boundary

Every prepared ONNX file will be checked structurally and, where supported by
the local runtime, exercised with ONNX Runtime. JSON and PLCopen tensor shapes
will be compared with the source ONNX contract. Static PLC checks will verify
that every enum member has exactly one package, runner, predictor dispatch, and
compile item, with no stale family references.

The isolated TwinCAT PLC build will be run when the local XAE environment is
available. A successful static or isolated build proves source integration but
does not prove target download, TF3820 licensing, Machine Learning Server
configuration, ADS communication, or runtime prediction. Those remain a
separate commissioning gate on the Beckhoff target.

## Involved Components

- `models/polished_dataset/setpoints/`
  Read-only canonical source of the 36 forward ONNX model families.
- `scripts/deployment/twincat_onnx_conversion/convert_onnx_for_twincat.py`
  Beckhoff artifact preparation, source inspection, and conversion evidence.
- `scripts/deployment/twincat_onnx_conversion/build_tf3820_standalone_harness.py`
  Deterministic PLC catalog and runner generation.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/ML_models/`
  Refreshed family-local TF3820 packages.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/DUTs/`
  Model enum and generated tensor contracts.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/POUs/Model Runners/`
  Generated model-specific prediction blocks.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/POUs/FB_TF3820TransmissionErrorPredictor.TcPOU`
  Public predictor, model dispatch, temporal history, and TE reconstruction.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/TF3820StandalonePLC.plcproj`
  PLC compile inventory.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/scripts/prepare_testrig_predictor_import_pack.py`
  Import-package generation for the reusable TestRig predictor boundary.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/README.md`
  Maintained catalog, deployment, and operator instructions.
- `doc/guide/project_usage_guide.md` and `site/guide/project_usage_guide.md`
  Canonical repository and Sphinx usage surfaces if the model catalog or
  commands change.

## Implementation Steps

1. Register this technical document from `doc/README.md` and wait for explicit
   user approval.
2. Revalidate the clean state of the parent repository and TwinCAT submodule,
   then capture the exact canonical forward-family inventory and source hashes.
3. Extend the conversion workflow, if needed, to batch-prepare every discovered
   forward polished-setpoint ONNX model into a temporary family matrix.
4. Run ONNX structural checks, optional ONNX Runtime smoke inference, Beckhoff
   TF3820 preparation, and tensor-contract validation for every family.
5. Generate the complete model catalog and PLC source tree from the validated
   matrix while preserving stable identifiers for retained families.
6. Compare the staged and maintained catalogs, then replace `ML_models` and
   remove packages that are absent from the canonical 36-family source.
7. Synchronize the model enum, generated DUTs, runners, public predictor
   declarations and dispatch, TE reconstruction branches, and PLC compile
   inventory.
8. Regenerate the TestRig predictor import pack and update the standalone and
   canonical usage documentation where catalog counts or commands changed.
9. Validate XML syntax, source hashes, ONNX/JSON/PLCopen tensor agreement,
   one-to-one family coverage, model paths, enum and dispatch completeness,
   temporal-runner contracts, and output reconstruction branches.
10. Run Python syntax checks, Markdown style and Markdownlint checks, the
    warning-free Sphinx build when its source changes, and the isolated PLC
    build where available.
11. Report static/build evidence separately from target runtime evidence and
    stop for user review before any Git commit.

## Implementation Outcome

The approved refresh was implemented on 2026-07-31.

- The canonical source discovery found 36 forward polished-setpoint families.
  No previously unknown family identifier was present; all 36 retained enum
  identifiers already existed in the standalone project.
- Every maintained ONNX package differed from its current canonical source and
  was regenerated through the Beckhoff TF3820 preparation route.
- `ML_models` now contains exactly the 36 canonical families, each with
  `model.onnx`, `model.json`, and `model_plcopen.xml`.
- The destination-only `rcim_track1` package, its enum member, tensor DUTs,
  runner, predictor dispatch, and compile items were removed. Retained enum
  numeric values were not renumbered.
- Seventeen refreshed temporal contracts changed from `[1, 33, 4]` to
  `[1, 33, 5]`. Their PLC input DUTs and runner tensor packing now include the
  aligned `direction_flag` history and fallback values.
- All 30 temporal models now receive angle, speed, signed torque, temperature,
  and direction through the predictor-owned real 33-sample history.
- `model_catalog.json` records the canonical source path, source SHA-256,
  TF3820-prepared SHA-256, tensor shapes, enum, runner, and target JSON path for
  every family.
- The TestRig predictor import pack was regenerated with 111 PLC source
  objects.

## Validation Evidence

- ONNX Runtime smoke inference passed for all 36 canonical source models.
- Beckhoff `onnxprep` completed for all 36 models and generated JSON plus
  PLCopen XML artifacts.
- The maintained catalog validator passed with 36 source/package/catalog
  families, 36 enum members, 36 runners, 30 temporal models, and 144 parsed
  family-local XML objects.
- Source hashes, prepared hashes, JSON tensor shapes, PLCopen-derived DUT
  shapes, model paths, enum members, predictor branches, and PLC compile items
  matched one-to-one.
- The isolated PLC-only TwinCAT build completed with `LastBuildInfo=0` and
  generated a 540,743-byte TMC containing the public predictor and the final
  Wave 5.1 enum symbol, with no removed RCIM symbol.

The isolated build is static integration evidence only. Target activation,
TF3820 licensing, ADS communication, runtime model configuration, inference,
Scope replay, and TestRig timing remain commissioning gates on the intended
Beckhoff target.
