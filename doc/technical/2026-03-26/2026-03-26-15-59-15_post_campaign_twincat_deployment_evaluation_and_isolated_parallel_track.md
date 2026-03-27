# Post-Campaign TwinCAT Deployment Evaluation And Isolated Parallel Track

## Overview

After the active training campaign is finished and the backlog becomes
modifiable again, the repository should formalize a dedicated workstream for
TwinCAT deployment evaluation of the TE models produced in this project.

The user requested that this future work be planned now and implemented after
campaign completion.

The planned direction has two coordinated branches:

- keep the current Beckhoff legacy deployment path as the primary operational
  target;
- in parallel, evaluate the newer Beckhoff Machine Learning Server path in a
  separate and explicitly isolated track.

The legacy branch remains the mainline because it is aligned with the existing
TestRig TwinCAT code and current compensation structure.

The parallel branch is justified because the older TwinCAT converter accepted
only a subset of model types successfully in prior work, while the newer
`TF3820/TF3830` path may offer broader practical ONNX intake and a different
deployment tradeoff profile.

## Technical Approach

The future work should begin only after the active campaign is closed or the
user explicitly authorizes integration-safe follow-up work.

The proposed approach is to create a dedicated backlog item and then execute the
initial evaluation in isolated mode so campaign-sensitive repository files are
not disturbed.

### 1. Main Deployment Branch - Legacy TwinCAT Inference Engine

Preserve the current operational target based on:

- `TF38x0 | TwinCAT 3 ML/NN Inference Engine`
- `FB_MllPrediction`
- Beckhoff proprietary `XML/BML` model artifacts

This branch should remain the main deployment candidate because:

- it matches the imported TestRig PLC code;
- it preserves the current compensation architecture already implemented in
  TwinCAT;
- it is more naturally aligned with deterministic PLC-side execution than the
  newer server-based path.

The evaluation should explicitly test which of the repository model families can
be exported and converted successfully with the legacy toolchain.

### 2. Parallel Deployment Branch - TwinCAT Machine Learning Server

Create a clearly separate evaluation track based on:

- `TF3820 | TwinCAT 3 Machine Learning Server`
- `TF3830 | TwinCAT 3 Machine Learning Server Client`
- `FB_MlSvrPrediction`
- `ONNX + JSON + PlcOpenXml`

This branch should not replace the legacy target initially.

Instead, it should be treated as an alternative deployment path to evaluate:

- whether the newer Beckhoff path accepts a broader set of our ONNX models;
- whether it reduces the conversion limitations previously seen with the legacy
  XML/BML converter;
- whether its asynchronous server-based execution is acceptable for TE
  compensation use cases.

### 3. Isolated-Mode Execution During Ongoing Campaign Activity

If campaign execution is still ongoing and the user wants early parallel
preparation, the recommended execution mode is isolated mode.

That isolated track should be used for:

- technical planning notes;
- export-tooling sketches;
- model-compatibility test matrices;
- Beckhoff deployment comparison notes;
- small test harnesses or helper scripts that do not need immediate integration.

The isolated track should avoid touching:

- active campaign files;
- queue state;
- registries;
- campaign launchers;
- campaign reports;
- other files protected by the active campaign state.

This allows meaningful progress while preserving the campaign baseline.

### 4. Comparative Evaluation Framework

The planned work should compare the two deployment branches on at least four
axes:

- model compatibility;
- deployment artifact workflow;
- runtime behavior and timing suitability;
- maintainability and engineering complexity.

The evaluation should not stop at "conversion succeeded" or "conversion
failed".

It should instead record:

- which repository model families export cleanly to ONNX;
- which ONNX models are accepted by the legacy Beckhoff converter;
- which ONNX models are accepted by the Machine Learning Server workflow;
- what additional metadata or interface-description files are required;
- whether inference timing, determinism, and integration complexity remain
  suitable for PLC-side compensation.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Existing repository-owned note describing the current TestRig TwinCAT ML
  pipeline and the newer Beckhoff server alternative.
- `doc/running/active_training_campaign.yaml`
  Campaign-state file that must be respected before any backlog or integration
  work touches protected campaign files.
- `isolated/active/<session_id>/`
  Recommended execution root for future parallel preparation while the campaign
  is still running.
- `reference/codes/TestRig/`
  Imported TwinCAT reference code that defines the current legacy deployment
  baseline.
- future backlog location
  The repository backlog should receive a dedicated deployment-evaluation item
  after campaign completion or explicit user approval.
- future TwinCAT deployment evaluation notes
  The future implementation will likely need dedicated analytical notes,
  comparison tables, and export-test records.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait until the active campaign is finished or until the user explicitly
   authorizes safe follow-up work against the backlog.
3. Add a dedicated backlog item for `TwinCAT deployment evaluation` once the
   backlog becomes modifiable again.
4. Define a model-compatibility matrix covering the repository model families
   that should be tested against:
   - legacy `TF38x0` conversion and runtime;
   - newer `TF3820/TF3830` server-based workflow.
5. If work starts before full campaign closure, open an isolated-mode session
   and keep all preparatory work inside that session root.
6. Implement the legacy-branch export and compatibility checks as the primary
   branch.
7. Implement the `TF3820/TF3830` evaluation as a separate parallel branch and
   compare artifact flow, compatibility, runtime behavior, and engineering
   tradeoffs.
8. Produce a repository-owned comparison result that states:
   - strengths of the legacy branch;
   - strengths of the newer server branch;
   - known limitations of each branch;
   - recommended deployment target for this project;
   - conditions under which the secondary branch becomes worth adopting.
9. Report the completed post-campaign evaluation and stop for user review before
   any commit.
