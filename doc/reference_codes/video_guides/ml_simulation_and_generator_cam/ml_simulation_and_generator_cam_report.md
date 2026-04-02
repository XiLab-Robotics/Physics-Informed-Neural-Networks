# TwinCAT/TestRig Video Guide Report

**Video:** *ML_Simulation_and_Generator_Cam.mkv*

---

## Source Reference

* Canonical source video: [ml_simulation_and_generator_cam.mkv](../../../../reference/video_guides/source_bundle/ml_simulation_and_generator_cam.mkv)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

The video demonstrates how a machine‑learning (ML) model, trained in MATLAB and exported as an ONNX file, is integrated into a Beckhoff TwinCAT PLC using the TestRig framework. It covers data preparation, model import, PLC‑side inference, and post‑processing of the transmission error (`TE`) signal. The companion notes point out a critical variable naming issue: `TE_Calc` in the PLC is **not** the MATLAB‑derived variable but rather a value computed directly inside TwinCAT from the total position.

---

## Why This Video Matters

1. **Bridging MATLAB and TwinCAT:** It shows a concrete workflow for moving an ML model from MATLAB to a real‑time PLC environment, which is essential for practitioners looking to deploy predictive maintenance or fault detection algorithms on industrial hardware.
2. **TestRig Utilization:** The video highlights how TestRig can be used to validate the model’s behavior before flashing it onto the target controller, reducing deployment risk.
3. **Variable Management Insight:** The error noted in the notes underscores the importance of consistent variable naming across MATLAB, ONNX export, and PLC code—an often overlooked but critical detail.

---

## Main Technical Findings

| Item | Detail |
| ------ | -------- |
| **Data Columns** | 1) Speed (RPM), 2) Slow‑shaft torque, 3) Temperature, 4) Transmission error. The transcript confirms the first three columns are speed, torque, temperature; the fourth is TE. |
| **Model Import** | GBR models were imported for phase and amplitude at non‑zero frequencies; a separate model handles zero‑frequency amplitude. These are loaded into `Machine_Learning.Untitied1.Cam` (OCR evidence 00:11:12). |
| **PLC Prediction Block** | The PLC contains a `Cam_Corection_ML_1_Vel_Cost_250_500` block that receives speed, torque, and temperature as inputs and outputs a predicted TE. OCR at 00:01:15 shows the block’s variable list (`Enab`, `Mis delay`, etc.). |
| **TE Calculation** | The PLC calculates an intermediate `TE_Calc` from the total position (not from MATLAB). This is highlighted in the notes; it implies that the ML output may be post‑processed or combined with a deterministic model. |
| **TestRig Structure** | TestRig projects are organized under `Experiments > TrasmissioneAllacciata > Experiment_ML`. The script `ForSim_And_Exp.m` (OCR 00:16:09) drives the simulation, feeding recorded data into the PLC and capturing outputs for analysis. |
| **Timing & Communication** | OCR evidence at 00:07:29 and 00:16:09 shows task timing windows and inter‑task communication via `Machine_Learning.Untitied1.Cam`. The PLC uses cyclic tasks to fetch inputs, run inference, and write outputs within the same cycle. |
| **Post‑Processing** | After inference, the TE signal is likely filtered or scaled before being used in higher‑level control logic (implied by the mention of “acceleration” and “velocity” calculations in the transcript). |

---

## TwinCAT And Deployment Implications

1. **Variable Consistency:** The discrepancy between `TE_Calc` and the MATLAB variable means that any deployment must explicitly map PLC variables to the ONNX inputs/outputs; otherwise, the model will receive wrong data.
2. **Real‑Time Constraints:** The inference block must fit within the PLC cycle time (typically 1 ms or less). TestRig allows profiling of execution time before flashing to hardware.
3. **Memory Footprint:** GBR models are relatively lightweight, but the ONNX runtime in TwinCAT consumes RAM; ensure sufficient memory on the target CPU.
4. **Safety Considerations:** The video references “Safety Project CRCs Display” (OCR 00:07:29). Any ML‑based TE prediction that influences safety‑critical actuators must be validated against safety standards (e.g., IEC 61508).
5. **Code Adaptation:** When porting the PLC code to a different controller, rename `TE_Calc` to match the MATLAB variable name or adjust the inference block’s input mapping accordingly.

---

## Reference Snapshots

| Time | Concept | Snapshot Description |
| ------ | --------- | ----------------------- |
| 00:07:29 | Task Timing & CRCs | Screenshot of the TwinCAT IDE showing task timing and safety CRC display. |
| 00:11:12 | ML Prediction Block | Center workspace view with `Cam_Corection_ML_1_Vel_Cost_250_500` block highlighted, including input/output ports. |
| 00:16:09 | TestRig Execution | Breakpoints window showing the `ForSim_And_Exp.m` script running within the `Experiment_ML` folder. |
| 00:25:20 | Data Pre‑Processing | File explorer view of the `Test_30deg_Torque_PreProcessing` folder, indicating raw data files used for simulation. |

These snapshots illustrate key stages: setting up tasks, configuring ML blocks, executing simulations, and preparing input data.

---

## Open Questions Or Uncertain Points

1. **Exact Mapping of Variables:** The notes mention an error with `TE_Calc`. It is unclear whether the PLC code was later corrected or if the model still uses the wrong variable during deployment.
2. **Post‑Processing Steps:** The transcript hints at acceleration and velocity calculations but does not detail how TE predictions are combined with deterministic models.
3. **Safety Validation Procedure:** While CRCs are displayed, the specific safety validation steps (e.g., SIL level, fault tolerance) are not shown in the video.
4. **ONNX Runtime Version:** The exact version of the ONNX runtime used inside TwinCAT is not specified; this could affect compatibility with newer MATLAB export formats.

Addressing these points would provide a more complete understanding of the deployment pipeline and its robustness for industrial use.
