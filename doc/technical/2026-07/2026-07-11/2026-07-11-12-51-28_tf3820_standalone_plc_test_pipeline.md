# TF3820 Standalone PLC Test Pipeline

## Overview

This technical plan covers the next TwinCAT deployment step: create an
independent PLC test pipeline for `TF3820` Machine Learning Server models,
separate from the full TestRig project.

The user goal is to validate the new `TF3820` model-execution path on a clean
or empty Beckhoff PLC project before integrating it into the real TestRig
compensation logic. The pipeline should generate or load test inputs, execute
prepared ONNX-derived artifacts through `FB_MlSvrPrediction`, and expose
prediction outputs, latency, and error state for all representative ONNX model
families.

The first local build attempts against the current TestRig migration branch
found an environment/build-automation issue before reaching PLC code
diagnostics:

- `TcXaeShell.exe /Build` returned immediately without a useful build log;
- `devenv.exe /Build` left a GUI process running and reported TwinCAT/HMI
  package load failures;
- direct `.tsproj` build produced the same package-load issue.

Therefore this task also includes creating a smaller TwinCAT project surface
that avoids the TestRig HMI dependency and is suitable for deterministic
compile/build validation from this workstation.

## Technical Approach

The standalone pipeline will be treated as a deployment-test harness, not as a
new training workflow. It will reuse the existing ONNX conversion outputs under:

```text
output/deployment/twincat_onnx_conversion/family_matrix_20260710_shape_fixed/
```

The harness will be designed around `TF3820` semantics:

- each model is prepared as `model.onnx`, `model.json`, and
  `model_plcopen.xml`;
- the PLC side uses `Tc3_MlServer.FB_MlSvrPrediction`;
- configuration creates a server session from `model.json`;
- prediction is asynchronous and must expose pending, ready, error,
  `nErrorCode`, and `nMaxInferenceDuration`;
- input/output DUTs must match the generated PLCopen XML for each tested
  model shape.

The implementation should avoid depending on the real TestRig task structure,
I/O mapping, HMI project, experiment state machine, or motor/sensor function
blocks. The first screen of validation is a minimal PLC runtime that can run on
a blank target with only TwinCAT and `TF3820` installed.

The standalone project will support two input modes:

- deterministic synthetic input generation from fixed ranges for smoke tests;
- optional curve-driven playback from a small tracked test curve or generated
  CSV fixture that follows the polished actual-values contract:
  `theta`, `theta_dot`, `tau_load`, `T`, and `direction_flag`.

Because the 37 model families have different input/output shapes, the first
implementation will generate a model catalog from conversion manifests and
group models by compatible PLCopen I/O shape. Shape-specific wrappers can then
be generated or staged explicitly instead of forcing every family through the
single feedforward `[1,5] -> [1,1]` wrapper.

No subagent is planned for this implementation.

## Involved Components

- `reference/codes/TestRig_TF3820_MachineLearningServer`
  Existing TestRig-side migration branch. This remains the integration target,
  but the standalone pipeline should not depend on it.
- `output/deployment/twincat_onnx_conversion/family_matrix_20260710_shape_fixed/`
  Source of tested `TF3820` artifacts and model-family manifests.
- `scripts/deployment/twincat_onnx_conversion/convert_onnx_for_twincat.py`
  Existing converter used to prepare each ONNX model for `TF3820`.
- `scripts/deployment/twincat_onnx_conversion/run_family_compatibility_matrix.py`
  Existing family-matrix runner that can be reused as the source inventory for
  all representative ONNX families.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest`
  Proposed new reference-owned TwinCAT project or submodule/worktree location
  for the standalone PLC harness.
- `doc/scripts/deployment/twincat_onnx_conversion/`
  Documentation location for usage commands and validation notes.
- `doc/guide/project_usage_guide.md`
  User-facing guide that may need an update if the standalone harness becomes
  a maintained runnable workflow.

## Implementation Steps

1. Keep the current TestRig branch untouched while building the standalone
   harness.
2. Inspect the available TwinCAT command-line build surfaces on this
   workstation and record the reliable command, or document the package-load
   blocker if no headless build is possible.
3. Create a minimal TwinCAT PLC-only project or importable PLC project surface
   under `reference/codes/TwinCAT_TF3820_StandaloneModelTest`.
4. Add a PLC wrapper for `FB_MlSvrPrediction` that can configure, deconfigure,
   and predict with `model.json` artifacts.
5. Generate or include shape-specific DUTs from `model_plcopen.xml` for the
   first supported shape group, starting with the feedforward `[1,5] -> [1,1]`
   contract.
6. Add a deterministic input generator for actual-values TE models:
   `theta`, `theta_dot`, `tau_load`, `T`, and `direction_flag`.
7. Add optional playback of a small curve fixture so the same PLC code can be
   exercised against a real-looking TE curve.
8. Create a model catalog that maps family name, model path, JSON path,
   PLCopen XML path, input shape, output shape, and wrapper support status.
9. Extend support family-by-family by grouping models with compatible shapes
   and adding explicit wrappers where required.
10. Run XML validity checks, repository Markdown checks, and every available
    TwinCAT command-line build check.
11. Report which part is verified locally, which part requires real PLC/XAE
    validation, and the exact commands to run on the Beckhoff target.
