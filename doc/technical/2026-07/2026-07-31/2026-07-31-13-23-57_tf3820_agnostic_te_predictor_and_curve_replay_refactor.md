# TF3820 Agnostic TE Predictor And Curve Replay Refactor

## Overview

This technical document records the approved refactor of the standalone
TwinCAT `TF3820` validation project under
`reference/codes/TwinCAT_TF3820_StandaloneModelTest`.

The current project has two PLC programs:

- `P_TF3820StandaloneModelTest` owns the 37 model-runner instances, accepts
  manual or fixed inputs, and exposes the raw prediction tensor;
- `P_TF3820CurveReplay` reads curve CSV files, drives the standalone program,
  reconstructs one deterministic transmission-error value, compares it with
  the measured value, and exposes Scope signals.

Both programs currently run in the same PLC task, and the replay program writes
directly into the standalone program. Temporal runners also depend on
`GVL_TF3820Replay`. This coupling is acceptable for the first validation
harness but is not suitable for copying the predictor into the TestRig.

The approved target is one public function block,
`FB_TF3820TransmissionErrorPredictor`, that hides model-specific tensor shapes,
temporal history, and output reconstruction. TestRig code will select a model
through an enumeration, initialize it, start or stop prediction, provide the
physical inputs, and receive one `REAL` transmission-error output.

The user approved this plan on 2026-07-31 and explicitly requested immediate
implementation after this document was saved and registered. No subagent is
planned or authorized for this work.

## Technical Approach

### Public Predictor Contract

The new function block will expose an intentionally small public API:

- model selection through `E_TF3820StandaloneModelId`;
- an initialization command that starts the asynchronous TF3820 configuration;
- simple start and stop prediction commands;
- a sample-valid input that separates PLC task rate from meaningful sample
  rate;
- explicit physical inputs for angle, angular velocity, torque, temperature,
  and direction;
- one normalized `fTE : REAL` output;
- a TE-valid pulse plus configuration, busy, pending, and error diagnostics.

TF3820 model configuration cannot complete synchronously inside `FB_init`.
Initialization will therefore be represented by a simple cyclic command and a
`bConfigured` acknowledgement. The selected model must remain stable while the
function block is configured or predicting. A model change requires stop,
reset or deconfiguration, and a new initialization command.

### Model-Agnostic TE Reconstruction

The wrapper will absorb every model-output convention:

- scalar and Gaussian models use output index `0`;
- the quantile model uses output index `1`, representing `p50`;
- K2 and K3 mixture-density models use the numerically stable softmax-weighted
  component expectation;
- all remaining deterministic scalar models use output index `0`.

Callers will not receive or interpret the internal prediction tensor during
normal operation. A raw tensor may remain available only as a diagnostic
output if it does not complicate the public TestRig contract.

### Temporal Input Ownership

Temporal history will move from `GVL_TF3820Replay` into the predictor instance.
Each valid sample will shift the internal 33-sample history and append the
current physical inputs. Temporal inference will remain disabled until all 33
history positions contain real samples. The first temporal result therefore
uses samples `0` through `32`; later predictions use a one-sample sliding
window.

This design allows the same function-block instance to operate in:

- the manual standalone test;
- the CSV curve replay;
- the final TestRig program.

The `bSampleValid` contract must remain explicit because the TestRig ML task,
drive task, and dataset angular sampling do not necessarily have the same
cadence.

### Two Programs As Test Harnesses

`P_TF3820StandaloneModelTest` will become a manual demonstration program. It
will instantiate the public predictor, provide fixed or online-editable
inputs, and expose the normalized TE and runtime status. Model execution logic
and output interpretation will no longer live in the program.

`P_TF3820CurveReplay` will become an automatic validation harness. It will:

1. open each deployed curve CSV;
2. read the physical model inputs and measured TE;
3. submit every valid row to its predictor instance;
4. retain the measured TE associated with each requested prediction;
5. collect the normalized predicted TE;
6. calculate predicted-minus-measured error;
7. expose measured TE, predicted TE, error, angle, and validity for Scope YT.

The replay will process all curve files intentionally deployed in the replay
pack. Full-dataset replay remains possible, but the default workflow will keep
using a bounded reproducible pack because the complete 969-curve forward
dataset is approximately 3.46 GB.

### Export Boundary

TestRig source code will interact with one top-level predictor FB, but the FB
cannot compile as a single isolated `.TcPOU`. It depends on:

- the model-selection enumeration;
- model-specific input and output DUTs;
- the 37 TF3820 runner function blocks;
- Beckhoff `Tc3_MlServer`, `Tc2_Standard`, and supporting libraries.

The delivery will therefore include a PLCopen import package or an explicitly
documented multi-object import set. The usage surface remains one FB instance,
while its compile-time dependencies are imported together.

### Commenting Standard

PLC declarations and implementations will receive frequent English comments.
Comments will be placed above the relevant line or logical block. Repeated
assignments that serve one purpose, such as tensor packing or output clearing,
will share one comment above the group instead of receiving redundant comments
on every line.

The following areas require dense comment coverage:

- public inputs, outputs, and internal state;
- rising-edge commands;
- configure, deconfigure, reset, and prediction states;
- physical-input packing and temporal-window updates;
- TF3820 calls and asynchronous completion;
- raw-output extraction and deterministic TE reconstruction;
- CSV parsing, replay state transitions, curve boundaries, and Scope timing;
- error paths and recovery requirements.

## Involved Components

- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/README.md`
  Step-by-step operator, replay, Scope, and TestRig integration guide.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/POUs/`
  New predictor FB and refactored manual program.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/POUs/Replay/`
  Refactored CSV reader and curve-replay program.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/POUs/Model Runners/`
  Existing 37 generated runner blocks, updated for instance-owned temporal
  data and dense operational comments.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/DUTs/`
  Existing model enumeration and tensor contracts.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/GVLs/`
  Existing replay GVL, expected to be removed after temporal history moves
  into the predictor contract.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/PLC_project/TF3820StandalonePLC.plcproj`
  PLC compile inventory.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/Scope_TE_Comparison/`
  Existing ADS Scope project for measured and predicted TE.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/scripts/prepare_curve_replay_pack.py`
  Reproducible replay-pack preparation.
- `doc/guide/project_usage_guide.md`
  Canonical repository usage guide for the maintained harness.
- `site/guide/project_usage_guide.md`
  Sphinx include surface for the canonical usage guide.

Pre-existing changes in
`PLC_project/_CompileInfo/37D45995-80BA-FFF1-872C-FCCE4C3E2843.compileinfo` and
`TwinCAT_TF3820_StandaloneModelTest.tsproj.bak` are outside this work and must
not be overwritten or included in the implementation scope.

## Implementation Steps

1. Register this approved technical document from `doc/README.md`.
2. Define the public `FB_TF3820TransmissionErrorPredictor` contract and add it
   to the PLC project compile inventory.
3. Move model selection and runner dispatch from the standalone program into
   the predictor FB.
4. Move temporal history into the predictor instance and remove runner
   dependence on `GVL_TF3820Replay`.
5. Move scalar, Gaussian, quantile, and mixture-density TE reconstruction into
   the predictor FB.
6. Refactor `P_TF3820StandaloneModelTest` into a manual example that owns one
   predictor instance and exposes only normalized TE plus diagnostics.
7. Refactor `P_TF3820CurveReplay` into an independent automatic test harness
   that owns one predictor instance and retains the measured sample associated
   with each prediction request.
8. Preserve start, stop, curve-boundary reset, inference stride, and 33-sample
   warm-up semantics.
9. Add dense block-level and near-line comments to all modified PLC code and
   consistent operational comments to the generated runner family.
10. Rewrite the standalone `README.md` with separate step-by-step procedures
    for manual testing, replay, Scope, and TestRig import and use.
11. Update `doc/guide/project_usage_guide.md` and the Sphinx-facing usage
    surface where the old single-program description is no longer accurate.
12. Prepare or document the PLCopen multi-object export boundary needed to
    import the predictor and all dependencies.
13. Validate XML syntax, PLC compile-item references, the 37-model dispatch
    map, temporal history coverage, TE reconstruction branches, replay and
    Scope symbols, Python syntax, Markdown quality, and the isolated PLC build.
14. Report verified static/build evidence separately from any runtime or PLC
    activation evidence that was not executed.
15. Stop for user review and explicit approval before creating any commit.

## Implementation Outcome

The approved refactor was implemented on 2026-07-31.

- `FB_TF3820TransmissionErrorPredictor` is now the reusable public inference
  boundary. It owns model selection, asynchronous configuration, prediction
  control, temporal history, runner dispatch, and deterministic TE
  reconstruction.
- `P_TF3820StandaloneModelTest` is now a small manual example that owns one
  predictor instance.
- `P_TF3820CurveReplay` is now an independent automatic harness that owns its
  own predictor, reads every deployed curve, retains measured TE, and exposes
  measured, predicted, and signed-error signals for Scope.
- `GVL_TF3820Replay` was removed. All 30 temporal runners now receive the
  instance-owned `ST_TF3820TemporalHistory` value.
- All 37 enum models are dispatched through the public predictor and return one
  `fTE : REAL` value to the caller.
- Frequent operational comments were added above declarations, asynchronous
  states, tensor-packing blocks, output-copy blocks, replay transitions, and
  error handling.
- `prepare_testrig_predictor_import_pack.py` now creates an explicit source
  import directory, manifest, and ZIP containing the predictor and its
  compile-time PLC dependencies.
- The standalone README and canonical project usage guide now distinguish the
  manual program, curve replay, and final TestRig function-block integration.

## Validation Evidence

The following checks were completed after implementation:

- all 119 project and PLC XML files parsed successfully;
- the PLC project contains 118 compile items and no missing source paths;
- the enum contains 37 models and every model identifier is present in the
  predictor dispatch;
- the runner inventory contains 37 blocks, including 30 blocks that consume
  the instance-owned temporal history;
- no maintained PLC source references `GVL_TF3820Replay`;
- both Python preparation scripts pass syntax compilation;
- the TestRig source import pack contains 114 PLC source objects plus its
  manifest and ZIP;
- an isolated temporary TwinCAT build regenerated
  `TF3820StandalonePLC.tmc`; the TMC contains the public predictor, temporal
  DUT, and replay Scope symbols, and no longer contains the removed replay GVL;
- the complete TwinCAT solution still reaches the known target-configuration
  failure `Check config failed` after PLC compilation.

The isolated build proves static PLC integration only. No target activation,
download, TF3820 license check, ADS session, CSV replay, or runtime inference
was performed. Those checks remain the commissioning gate on the intended
Beckhoff target.
