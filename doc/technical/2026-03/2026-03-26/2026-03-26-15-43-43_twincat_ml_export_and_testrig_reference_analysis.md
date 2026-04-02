# TwinCAT ML Export And TestRig Reference Analysis

## Overview

The user requested a focused investigation of the current TwinCAT machine-learning
deployment path used in the TestRig project.

The immediate goals are:

- add the `TestRig` repository as a reference submodule so the TwinCAT source
  files are directly available inside this repository;
- inspect the TwinCAT machine-learning PLC code located under
  `PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning`;
- reconstruct how the current prediction and TE-compensation pipeline works;
- preserve that analysis in this repository under `doc/reference_codes/`;
- verify whether a newer practical deployment path now exists beyond the
  previously documented ONNX -> TwinCAT XML conversion flow, especially given
  that earlier material reported limited model compatibility.

This work is documentation-heavy and deployment-oriented. It does not introduce
new ML models or new training workflows by itself, but it is expected to guide
future export and PLC-integration design choices.

## Technical Approach

The work should proceed in four stages after explicit approval.

### 1. Import The TestRig PLC Reference

Add the external repository as a Git submodule under `reference/` using a
stable and descriptive path so the TwinCAT files remain outside the main
canonical project implementation while still being versioned as a reference.

The imported code should be treated as reference material, not as directly
editable project implementation.

### 2. Perform A Targeted TwinCAT Code Reading

Read and analyze at least the following files from the imported TestRig
repository:

- `Predict_ML.TcPOU`
- `ML_Transmission_Error.TcPOU`
- `FB_Predict.TcPOU`

The analysis should reconstruct:

- task ownership and execution timing assumptions;
- data flow across the main program and both function blocks;
- model input preparation and prediction invocation;
- TE reconstruction and compensation logic;
- any PLC-side assumptions about XML model structure, dimensions, frequency
  terms, scaling, enable flags, or runtime guards.

### 3. Preserve Repository-Owned Analysis Notes

Create a new reference-code note under `doc/reference_codes/` dedicated to the
TwinCAT/TestRig ML pipeline.

That note should capture:

- the role of each TwinCAT file;
- the end-to-end inference path;
- the deployment assumptions extracted from the PLC code;
- practical constraints relevant to this repository's future export design;
- open questions or uncertainties that may need later confirmation from videos
  or additional source material.

### 4. Verify The Current Deployment Landscape

Investigate whether Beckhoff/TwinCAT now supports a more current or broader
model-import path than the older ONNX -> TwinCAT XML workflow described in the
paper and prior guidance.

This verification should explicitly check:

- whether the older converter workflow is still the main supported path;
- whether broader ONNX operator/model compatibility is now documented;
- whether newer TwinCAT ML or inference tooling changes the practical export
  route;
- whether the repository should keep targeting only the subset of model classes
  previously validated in the paper.

The final outcome should separate confirmed facts from inferred conclusions.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `reference/`
  Root location for imported external reference material.
- `.gitmodules`
  Git submodule registry that will need an additional entry after approval.
- `reference/codes/`
  Existing home for imported reference repositories and code assets.
- `doc/reference_codes/README.md`
  Index for repository-owned reference-code analysis notes.
- `doc/reference_codes/`
  Destination for the new TwinCAT/TestRig analysis document.
- `reference/RCIM_ML-compensation.pdf`
  Existing paper summary source for the historical TwinCAT deployment path.
- `reference/Report Machine Learning.pdf`
  Existing report summary source for the prior PLC integration flow and
  constraints.
- `reference/<testrig-submodule>/PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning/`
  Expected imported TwinCAT code location to inspect after approval.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before adding the TestRig submodule or
   performing the detailed analysis.
3. After approval, add the TestRig repository as a reference submodule under
   `reference/`.
4. Inspect the three requested TwinCAT POUs and reconstruct the data flow and
   runtime behavior.
5. Create a repository-owned analysis note in `doc/reference_codes/` summarizing
   the extracted behavior and deployment constraints.
6. Verify the current TwinCAT/Beckhoff export path and ONNX-import status using
   up-to-date official documentation and clearly distinguish confirmed support
   from assumptions.
7. Report the completed findings and stop for user review before any commit.
