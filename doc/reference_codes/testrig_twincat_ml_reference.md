# TestRig TwinCAT ML Reference

## Role In This Project

This note captures the TwinCAT-side machine-learning deployment path currently
implemented in the imported `TestRig` reference repository under
`reference/codes/TestRig`.

The purpose of the note is to make the Beckhoff PLC pipeline inspectable from
inside this repository before designing future export or deployment workflows
for transmission-error compensation.

## Inspected Files

- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning/Predict_ML.TcPOU`
- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning/ML_Transmission_Error.TcPOU`
- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/03_MachineLeraning/FB_Predict.TcPOU`
- `reference/codes/TestRig/PLC_project/Plc_Task_MLPredictor.TcTTO`
- `reference/codes/TestRig/PLC_project/POUs/Experiments/ToKeep/TransmissionError/P_Experiment_Cam_Correction_TE_ML.TcPOU`
- `reference/codes/TestRig/PLC_project/PLC_project.plcproj`
- `reference/codes/TestRig/PLC_project/PLC_project.tmc`

## High-Level Architecture

The TestRig implementation splits the PLC-side ML flow into three layers:

- `Predict_ML`
  Thin task-bound main program that exposes TwinCAT I/O-mapped variables and
  delegates all logic to `ML_Transmission_Error`.
- `ML_Transmission_Error`
  TE-specific orchestration block that loads three model files, evaluates
  multiple harmonic components, and reconstructs the final TE compensation
  signal.
- `FB_Predict`
  Generic wrapper around Beckhoff `Tc3_MLL.FB_MllPrediction`.

This means the project does not load one monolithic end-to-end TE model. It
loads one amplitude-offset model plus shared multi-engine amplitude and phase
models, then rebuilds the TE waveform in Structured Text.

## Task And Scheduling Structure

- `Predict_ML` is assigned to `Plc_Task_MLPredictor`.
- The TwinCAT task file sets `CycleTime` to `500` microseconds.
- The user note that the main program is attached to a separate task is
  confirmed by the imported TwinCAT sources.

Operationally, this means the project already isolates ML prediction from the
rest of the experiment logic and keeps the TE prediction call in a dedicated
fast PLC task.

## File-Level Behavior

## `Predict_ML.TcPOU`

`Predict_ML` is a thin adapter program.

Its main responsibilities are:

- map external PLC I/O variables such as enable, input vector, position, model
  paths, reset request, and read trigger;
- call the `ML_Transmission_Error` block every task cycle;
- trigger model-file initialization when `Read_Done` becomes true.

The exposed input vector is:

- `Vector_Input[0]` -> speed
- `Vector_Input[1]` -> temperature
- `Vector_Input[2]` -> torque

The program also exposes three distinct file-path inputs:

- `Model_Ampl_0`
- `Model_Ampl`
- `Model_Phase`

This confirms that the TwinCAT side expects more than one deployed model asset.

## `FB_Predict.TcPOU`

`FB_Predict` is a reusable wrapper around Beckhoff `FB_MllPrediction`.

The wrapper performs three functions:

- configure and load a model file when `bLoadModel` is requested;
- execute prediction when `bEnable` is true and no error/reset is active;
- expose runtime status, reset completion, output value, and Beckhoff HRESULT.

Important implementation details:

- `stPredictionParameter.MlModelFilepath` is set to `sModelName`.
- The wrapper calls `Configure()` to load the model.
- After configuration it queries:
  - preferred I/O data types;
  - input dimension;
  - model name;
  - maximum concurrency.
- Prediction uses `PredictRef(...)` rather than `Predict(...)`.
- The engine reference string comes from `Model_input`.
- The wrapper uses `REAL` input/output and the Beckhoff enum
  `E_MLLDT_FP32_REAL`.
- Reset is delegated to `fbPredict.Reset()`.

The use of `PredictRef(...)` is central because it implies that the loaded
model file contains multiple named engines or parameter sets addressable by a
string reference.

## `ML_Transmission_Error.TcPOU`

`ML_Transmission_Error` is the TE-domain orchestration block.

It instantiates:

- one `FB_Predict` for amplitude engines;
- one `FB_Predict` for phase engines;
- one `FB_Predict` for the special zero-order amplitude model.

The block hardcodes the harmonic-component list:

- `0`
- `1`
- `39`
- `40`
- `3`
- `78`
- `81`
- `156`
- `162`
- `240`

Only the first `Component_used + 1` entries are evaluated. The current value is
`Component_used := 3`, so the active set is:

- `0`
- `1`
- `39`
- `40`

For each active component:

- component `0` uses the dedicated `Model_amplitude_0`;
- nonzero components use the shared amplitude and phase model files;
- the engine reference string is built as `engine_<component>`.

The TE output is then reconstructed as a Fourier-like sum:

- predicted amplitude per component;
- predicted phase per component;
- cosine evaluated at the current shaft angle.

The formula is implemented directly in ST and uses:

- current angle input;
- component index;
- `tau := 81`;
- input speed `Input_Vector[0]`.

The algebra simplifies substantially, so the practical phase argument is
effectively proportional to:

- harmonic component number;
- reducer angle;
- a fixed divisor of `6`.

The code keeps the expanded form rather than a simplified symbolic version.
This was likely done to preserve physical interpretability or match an earlier
derivation.

## End-To-End Runtime Flow

The runtime path extracted from the PLC code is:

1. The experiment or PLC client writes model paths, feature vector, angle, and
   enable/reset flags to the mapped variables consumed by `Predict_ML`.
2. `Predict_ML` calls `ML_Transmission_Error` every `500 us`.
3. When `Read_Done` is pulsed, `Initialization_Files()` sets `ReadModel := TRUE`
   so all predictor blocks reload their files.
4. Each `FB_Predict` instance configures the requested XML/BML model through
   Beckhoff `FB_MllPrediction`.
5. The zero-order amplitude model is queried with engine name `engine_0`.
6. The shared amplitude model is queried with engine names like `engine_1`,
   `engine_39`, `engine_40`.
7. The shared phase model is queried with the same engine names.
8. `ML_Transmission_Error` stores the outputs in amplitude and phase vectors.
9. The block reconstructs the instantaneous TE signal as a harmonic sum.
10. The resulting TE value is returned as `ML_Output`.

## How The Experiment Program Uses The Predictor

`P_Experiment_Cam_Correction_TE_ML.TcPOU` shows how the predictor is used in
the real TestRig experiment flow.

Key observations:

- the experiment state machine waits for CSV loading and ML model loading before
  starting the cam profile;
- temperature is frozen once at the start of the experiment as `Temp_start`,
  then reused as the predictor temperature input during the run;
- torque comes from the current CSV row and is negated before prediction;
- angle comes from the slow-shaft absolute encoder;
- speed is clamped or approximated:
  - if `VelBosch <= 150`, the predictor receives `150`;
  - otherwise it receives the speed stored in the CSV row;
- the predictor output `Res_ML` is treated as TE and guarded against NaN;
- the final position command is corrected by subtracting
  `TE * ReductionRatioMotorSide`, with an additional low-speed scaling branch.

This means the deployed PLC logic is not only a passive predictor. It is
embedded inside a larger compensation experiment that:

- performs warm-up;
- homes and zeroes the rig;
- applies torque control;
- streams cam positions;
- applies TE-based position correction online.

## Extracted Design Assumptions

- The online TE signal is represented as a small harmonic basis, not as a raw
  arbitrary waveform.
- A dedicated DC or zero-order amplitude model is separated from the harmonic
  amplitude and phase models.
- Multi-engine model files are important to the design because one file is
  reused for several harmonic components via `engine_<n>` references.
- The deployed predictor expects a fixed 3-feature tabular input:
  speed, temperature, torque.
- The experiment often uses a frozen initial oil temperature rather than a
  continuously updated temperature signal.
- The compensation path is explicitly PLC-friendly because the final runtime
  logic is only:
  model lookup -> harmonic reconstruction -> corrected position command.
- Runtime robustness matters:
  - there is explicit reset behavior;
  - error codes are checked;
  - missing model initialization is logged;
  - NaN TE outputs are forced to zero in the experiment code.

## Beckhoff Runtime Details Confirmed From The Imported Project

The imported TwinCAT project confirms that the current TestRig implementation is
based on the Beckhoff `Tc3_MLL` stack, not on the newer Machine Learning Server.

Confirmed project indicators:

- `PLC_project.plcproj` includes a placeholder reference to `Tc3_MLL`.
- `FB_Predict` uses `FB_MllPrediction`.
- `PLC_project.tmc` describes `ST_MllPredictionParameters.MlModelFilepath` as a
  path to `*.xml` or `*.bml`.
- the deployment section references `TcMachineLearningModel`.

This aligns with the older Beckhoff inference-engine workflow rather than the
newer server-based ONNX runtime workflow.

## Current Beckhoff Solution Status

The official Beckhoff documentation now shows two distinct deployment paths.

### Path A - Current TestRig Path

Product family:

- `TF38x0 | TwinCAT 3 ML/NN Inference Engine`

Confirmed current behavior from Beckhoff docs:

- ONNX must still be converted into Beckhoff-specific `XML` or `BML`.
- `FB_MllPrediction` reads Beckhoff proprietary description files, not raw
  ONNX.
- Beckhoff still documents CLI, API, and GUI converters for this workflow.

This means the historical path used by the TestRig code is still officially
supported and has not been replaced inside that product line.

### Path B - Newer Beckhoff Path

Product family:

- `TF3820 | TwinCAT 3 Machine Learning Server`
- `TF3830 | TwinCAT 3 Machine Learning Server Client`

Confirmed current behavior from Beckhoff docs:

- the Machine Learning Server loads AI models provided as `ONNX` files;
- the PLC client uses `FB_MlSvrPrediction`, not `FB_MllPrediction`;
- the TwinCAT Machine Learning Model Manager generates:
  - `JSON`
  - `PlcOpenXml`
- inference is asynchronous to the PLC task cycle;
- supported ONNX Opset for the server is documented as version `21`;
- dynamic input or output shapes are not supported except for a leading dynamic
  batch dimension.

This is a materially newer solution than the one described in the original
paper, because it avoids conversion into Beckhoff XML/BML for the execution
artifact itself.

## Practical Interpretation For This Repository

Two conclusions follow.

First, if the target is strict continuity with the existing TestRig PLC code,
the repository should still assume the legacy Beckhoff inference-engine path:

- export ONNX;
- convert to XML or BML;
- load through `FB_MllPrediction`;
- stay inside the subset of model classes and model structures that Beckhoff
  explicitly supports in the TF38x0 line.

Second, if the target can tolerate a Beckhoff-side architectural update, there
is now a newer route worth evaluating:

- export ONNX;
- prepare `JSON + PlcOpenXml`;
- execute through `FB_MlSvrPrediction` and Machine Learning Server.

That newer route is not a drop-in replacement for the current TestRig code,
because it changes:

- the PLC function block API;
- the model-preparation artifacts;
- execution semantics from in-runtime deterministic library calls to
  asynchronous server-backed inference;
- the likely suitability for hard real-time compensation loops.

## Recommended Engineering Reading

For future work in this repository, the most relevant question is not simply
"is there a newer Beckhoff solution?".

The real question is:

- do we need deterministic low-latency PLC-side compensation inside a tight
  control loop, or
- do we only need practical Beckhoff-side AI execution with looser timing?

If tight deterministic compensation remains the requirement, the existing
harmonic reconstruction strategy used in TestRig still looks well motivated.

If broader model freedom becomes more important than strict deterministic
timing, the Machine Learning Server path deserves a separate design study.

## Open Questions

- The current TwinCAT code still uses only four harmonic components even though
  ten candidates are listed in `Vector_Component`. It is unclear whether this is
  a final deployment choice or a temporary reduced configuration.
- The exact offline training/export pipeline that produced the multi-engine
  XML files is not yet present in this repository.
- The reason for the factorization and constants in the cosine argument should
  be cross-checked against the original derivation or future user-provided
  videos.
- The Beckhoff Machine Learning Server may still be unsuitable for this use case
  if the compensation loop cannot tolerate asynchronous jitter, even though it
  is more flexible for ONNX intake.

## Sources

- Beckhoff, [`TF38x0 | TwinCAT 3 ML/NN Inference Engine - Machine Learning Models and file formats`](https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8327534219.html?id=7232675525394384268)
- Beckhoff, [`TF38x0 | TwinCAT 3 ML/NN Inference Engine - Creation and conversion of ONNX`](https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8327536651.html)
- Beckhoff, [`TF38x0 | TwinCAT 3 ML/NN Inference Engine - Beckhoff ML XML`](https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8436762635.html)
- Beckhoff, [`TF38x0 | TwinCAT 3 ML/NN Inference Engine - Machine learning models supported`](https://infosys.beckhoff.com/content/1033/tf38x0_tc3_ml_nn_inference_engine/8353052299.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Overview`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17276122123.html?id=5681734396422319134)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Workflow`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17289311243.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Preparing ONNX for use with TwinCAT Machine Learning Server`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17289310091.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Configuring the server from the PLC client`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17289313547.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Execute AI model`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17311425547.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - ONNX Support`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17311427723.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - TwinCAT Machine Learning Model Manager`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17303110795.html?id=7999117522116304357)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Python interface`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17314850571.html)
- Beckhoff, [`TF3820 | TwinCAT 3 Machine Learning Server - Command Line Interface`](https://infosys.beckhoff.com/content/1033/tf3820_tc3_machine_learning_server/17314851723.html)
