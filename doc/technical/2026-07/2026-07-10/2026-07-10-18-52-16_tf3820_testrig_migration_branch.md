# TF3820 TestRig Migration Branch

## Overview

This technical plan covers the first implementation attempt for migrating the
TestRig machine-learning prediction path from the current `TF38x0`
`Tc3_MLL.FB_MllPrediction` runtime to the newer `TF3820` Machine Learning
Server path.

The current TestRig reference submodule at `reference/codes/TestRig` points to
branch `4026` of `XiLab-Robotics/TestRig`. That working copy should remain the
stable imported reference. The migration work will use a separate TestRig copy
under `reference/codes/` and a new branch named
`tf3820-machine-learning-server`.

The purpose of the first implementation is not to declare the PLC integration
production-ready. It is to create a compilable, inspectable TwinCAT-side
migration branch that can later be opened and tested on a Beckhoff PLC with the
real `TF3820` runtime, generated `model.json`, generated PLCopen XML, and the
target license configuration.

## Technical Approach

The migration is a runtime-architecture change, not only a model-file format
change. The existing TestRig path loads `XML`/`BML` model files through
`FB_MllPrediction` and calls prediction from the PLC task. The `TF3820` path
uses the Machine Learning Server process and a PLC client function block such
as `FB_MlSvrPrediction`; prediction is asynchronous and must report readiness,
busy, error, and latency state explicitly.

The implementation will proceed conservatively:

- keep `reference/codes/TestRig` unchanged as the current imported reference;
- create a separate working copy under
  `reference/codes/TestRig_TF3820_MachineLearningServer`;
- fetch the current upstream TestRig branch before branching, because the
  current submodule worktree is two commits behind `origin/4026`;
- create or reuse the branch `tf3820-machine-learning-server` in the new copy;
- preserve the existing `TF38x0` prediction path where practical;
- add side-by-side `TF3820` PLC function blocks and programs rather than
  destructively replacing the current compensation path in the first pass;
- keep the external TestRig TE contract visible: speed, torque, oil
  temperature, reducer angle, encoder zeroing assumptions, and `DataValid`
  provenance remain separate from opaque model inference;
- start with a single feedforward representative model path, because this
  family fails the current `TF38x0` importer but passes the `TF3820`
  preparation route;
- keep harmonic TE reconstruction inspectable instead of hiding it inside a
  monolithic black-box block unless a later PLC test shows that the generated
  model output contract requires that structure.

The first branch will focus on a PLC wrapper and integration skeleton. Exact
API names and field names for `Tc3_MlServer` will be verified against the
installed TwinCAT libraries and Beckhoff documentation during implementation.
If a symbol cannot be verified locally, the code will be left clearly marked as
a TwinCAT compile-check item rather than silently guessed.

No training campaign or model retraining is part of this task.

## Involved Components

- `reference/codes/TestRig`
  Stable imported TestRig reference submodule. This path remains unchanged.
- `reference/codes/TestRig_TF3820_MachineLearningServer`
  New dedicated TestRig working copy for the migration branch.
- `reference/codes/TestRig_TF3820_MachineLearningServer/PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning/`
  Expected location for the side-by-side `TF3820` PLC prediction wrapper and
  TE orchestration block.
- `reference/codes/TestRig_TF3820_MachineLearningServer/PLC_project/`
  TwinCAT PLC project files that may need library references, POU references,
  task assignment, or generated PLCopen XML imports.
- `scripts/deployment/twincat_onnx_conversion/convert_onnx_for_twincat.py`
  Existing repository converter that produces `TF3820` `model.json` and
  `model_plcopen.xml` artifacts from ONNX.
- `output/deployment/twincat_onnx_conversion/family_matrix_20260710_shape_fixed/`
  Current evidence bundle proving that all 37 representative model families
  pass the `TF3820` `onnxprep` route after local shape freezing where needed.
- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Current reference analysis for the existing `TF38x0` TestRig ML path.
- `doc/reports/analysis/twincat_onnx_conversion/[2026-07-10]/family_compatibility_matrix.md`
  Current family compatibility matrix for deciding why this branch targets
  `TF3820`.

## Implementation Steps

1. Confirm the repository is in a suitable state for creating a new reference
   working copy and record any pre-existing uncommitted changes.
2. Fetch the upstream TestRig repository and create
   `reference/codes/TestRig_TF3820_MachineLearningServer` from
   `https://github.com/XiLab-Robotics/TestRig.git`.
3. Create branch `tf3820-machine-learning-server` from the latest available
   `origin/4026` baseline in the new working copy.
4. Inspect the generated `TF3820` artifacts for the feedforward representative,
   especially the `model_plcopen.xml` shape/type contract and the generated
   `model.json` server configuration.
5. Inspect the current PLC files in the new TestRig copy:
   `FB_Predict.TcPOU`, `ML_Transmission_Error.TcPOU`, `Predict_ML.TcPOU`,
   task files, project references, and the PLC project file.
6. Add a side-by-side `TF3820` prediction wrapper that mirrors the current
   `FB_Predict` responsibilities while exposing asynchronous state,
   prediction latency, server status, and clear error codes.
7. Add a side-by-side TE integration block or program wrapper that can call the
   new `TF3820` predictor without deleting the current `TF38x0` path.
8. Add or stage the generated PLCopen XML / model configuration integration
   material needed for the feedforward smoke path, keeping large generated
   model artifacts outside the TestRig branch unless they are required for
   TwinCAT compile or import.
9. Document the exact PLC-side assumptions that still require real TwinCAT
   compile validation, including library names, license/runtime requirements,
   server AMS Net ID, local versus remote server choice, and CPU versus CUDA
   execution provider.
10. Run available static checks from Git and repository tooling. Full TwinCAT
    compile and runtime validation will be deferred to the Beckhoff PLC
    workstation.
11. Report the changed TestRig branch, the new files, the remaining TwinCAT
    compile-check items, and the manual validation sequence for the PLC.
