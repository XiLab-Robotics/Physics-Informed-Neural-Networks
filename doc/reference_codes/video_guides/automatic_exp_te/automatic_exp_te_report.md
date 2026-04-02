# TwinCAT/TestRig Video Guide – *Automatic_Exp_TE.mp4*

## Source Reference

* Canonical source video: [automatic_exp_te.mp4](../../../../reference/video_guides/source_bundle/automatic_exp_te.mp4)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

The video demonstrates an automated experiment designed to evaluate transmission error (TE) across a range of operating conditions: speed, torque, and temperature. The workflow is fully integrated into the Beckhoff TwinCAT ecosystem, leveraging TestRig for data acquisition, a custom ADRC controller, and a machine‑learning module that predicts TE from sensor inputs.

Key points covered in the video:

| Time | Content |
| ------ | --------- |
| 00:00–00:05 | Introduction to the experiment’s purpose and automation rationale. |
| 00:05–00:10 | Discussion of vector sizing (fixed at 17 elements) and how changes to input parameters do not alter internal array dimensions. |
| 00:10–00:15 | Explanation of the boolean flag column that indicates whether an experiment run has been completed. |
| 00:15–00:16 | Automatic assignment of the first three columns (speed, torque, temperature) from the data matrix to the TestRig variables. |

The accompanying transcript file (`Automatic_Exp_TE.txt`) contains the full spoken commentary and is referenced throughout this report.

## Why This Video Matters

* **Automation Insight** – Shows how a complex multi‑parameter test can be scripted in TwinCAT without manual intervention, reducing human error and increasing repeatability.
* **Data Pipeline Clarity** – Illustrates the flow from raw sensor data → TestRig variables → ADRC controller → ML predictor → TE reconstruction.
* **Engineering Discipline** – Highlights the importance of maintaining consistent vector sizes (17 elements) for downstream algorithms that expect fixed‑length inputs.

## Main Technical Findings

1. **Vector Dimension Consistency**
   * The experiment matrix is always 17 elements long, regardless of how many parameters are varied. This design choice simplifies indexing in the ADRC controller and ML model but requires careful handling when adding new variables.

2. **Boolean Completion Flag**
   * An extra column (`0`/`1`) indicates whether a particular experimental run has been executed. The TestRig uses this flag to filter out incomplete data before feeding it into the ML predictor.

3. **Automatic Variable Mapping**
   * The first three columns of the matrix are automatically mapped to `TE_Vel_Torque_Temp`, `K_p_TE_Vel_Torque_Temp`, etc., as shown in the OCR‑extracted code snippets (e.g., `FB_TestRigSensorData`). This eliminates manual assignment and ensures synchronization between the data table and TestRig variables.

4. **ADRC Controller Integration**
   * The ADRC controller (`ADRC_controller a`) is configured with parameters such as `T_d_TE_Vel_Torque_Temp`, `bandwidth_TE_Vel_Torque_Temp`, and `f_notch_filter_TE_Vel_Torque_Temp`. These are exposed in the TestRig workspace (see OCR at 00:01:15) and are tuned per experiment.

5. **Machine‑Learning Module**
   * The ML predictor (`FB_Predict`) receives processed sensor data and outputs a TE estimate. The model expects inputs of type `LREAL` with specific timing parameters (`T_i_TE_Vel_Torque_Temp`, `T_v_TE_Vel_Torque_Temp`). These are defined in the TestRig workspace (OCR at 00:15:20).

6. **Task Timing & Inter‑Task Communication**
   * The video emphasizes that task scheduling is critical; the ADRC controller and ML predictor run on separate tasks with carefully set priorities to avoid data races. OCR evidence at 00:11:14 confirms the presence of `FB_TestRigSensorData` and timing variables.

## TwinCAT And Deployment Implications

| Aspect | Implication |
| -------- | ------------- |
| **Fixed Vector Size** | When deploying to a new hardware platform, ensure that the PLC memory allocation can accommodate 17 elements per experiment. |
| **Boolean Flag Handling** | In production code, guard ML inference calls with a check on the completion flag to avoid processing incomplete data. |
| **ADRC Parameter Exposure** | Expose controller parameters as TwinCAT variables so they can be tuned via HMI or OPC UA without recompiling. |
| **Task Priorities** | Maintain the same task priority scheme used in the video (e.g., ADRC on high‑priority task, ML on medium) to preserve real‑time performance. |
| **ML Model Deployment** | The predictor is implemented as a function block (`FB_Predict`). When porting to another TwinCAT version, verify that the underlying library (e.g., MathWorks or custom DLL) remains compatible. |

## Reference Snapshots

The report conceptually references three key snapshots captured during the video:

1. **Snapshot 00:01:15** – Shows the TestRig workspace with ADRC controller parameters (`T_d_TE_Vel_Torque_Temp`, `bandwidth_TE_Vel_Torque_Temp`) and the ML predictor block.
2. **Snapshot 00:11:14** – Highlights the task timing configuration, including the `FB_TestRigSensorData` function block that feeds sensor data into the system.
3. **Snapshot 00:15:20** – Displays the prepared values for the ML model (`K_p_TE_Vel_Torque_Temp`, `T_i_TE_Vel_Torque_Temp`, etc.) and their data types.

These snapshots are referenced in the transcript file as visual anchors for each technical section discussed above.

## Open Questions Or Uncertain Points

1. **Vector Size Rationale** – The video states that vector size remains 17, but does not explain why this specific number was chosen or how it maps to the underlying sensor array.
2. **Boolean Flag Implementation** – It is unclear whether the flag column is updated automatically by TestRig or manually set in the matrix before execution.
3. **ML Model Training Data** – The source and preprocessing steps for the data used to train `FB_Predict` are not shown; understanding this would aid in assessing model generalizability.
4. **Error Handling** – No explicit mention of how the system reacts if a sensor fails or returns out‑of‑range values during an experiment.

Addressing these points would strengthen confidence in deploying the automated TE testing framework across different hardware configurations and production environments.
