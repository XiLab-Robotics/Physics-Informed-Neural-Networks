# TwinCAT / TestRig Video Guide – Machine_Learning_2.mp4  

*(Technical Report – Engineering‑Focused)*  

---

## Source Reference

- Canonical source video: [machine_learning_2.mp4](../../../../reference/video_guides/source_bundle/machine_learning_2.mp4)
- Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

The second video in the “Machine Learning” series demonstrates how a pre‑trained ML model is exported from Python, imported into TwinCAT, and orchestrated by a PLC‑side TestRig. The workflow covers:

1. **Export of the trained model** (ONNX/ML.NET format) from the Python environment.  
2. **Import into TwinCAT’s Machine Learning framework** via the *Predict_ML.req_re* block.  
3. **Integration with existing FBs** (`FB_BoschMotor`, `P_Experiment_CanGi`, `FB_LightDevice`) and the TestRig’s state machine (state 100).  
4. **Real‑time communication** between the Fast Task (250 µs) and the ML task (500 µs).  

The video also explains how to configure input vectors from CSV files located in  
`C:\Users\Alessio Tutarini\Unimore\XiLAB Robotics - DATA\02-Test Rig\Machine Learning`.

---

## Why This Video Matters

- **Bridging the gap** between data‑science and real‑time control: shows a concrete pipeline for deploying ML models on Beckhoff hardware.  
- **Timing insights**: highlights the 1.325 µs communication latency between tasks, which is critical when tuning closed‑loop compensation.  
- **State‑machine integration**: demonstrates how to trigger model inference only in specific states (e.g., state 100) and how to handle first‑row CSV values for torque initialization.  

---

## Main Technical Findings

| Item | Detail |
|------|--------|
| **Model Export Format** | The video references a *Predict_ML.req_re* block that expects an ONNX file (`*.onnx`). The block is configured with `Db xCSV_and_Vectors` and `Filtering Type BOOL`. |
| **Input Vector Construction** | Three input vectors are assembled from the CSV: torque, velocity, and position. These are fed into the ML block via the *Task_500us_ML* group. |
| **Timing Architecture** | - Fast Task (250 µs) handles low‑level motor commands.<br>- ML Task (500 µs) performs inference and updates feed‑forward terms (`bEnableFF_TE`).<br>- Communication latency measured at ~1.325 µs, suggesting negligible overhead for the chosen sampling rates. |
| **State Machine Logic** | In state 100, the system reads the first torque value from the CSV. If this value differs from a threshold, it toggles forward/backward motor flags for three cycles to stabilize the initial condition. |
| **PLC‑Side Orchestration** | The `P_Experiment_Cam_Correction_TE_ML` program (`PRG`) controls when the ML block is activated (`startEx_TE`). It also sets `needToReadCSV_` to ensure fresh data each cycle. |
| **Error Handling** | No explicit error handling shown, but the video implies that if CSV reading fails, the system falls back to a default torque value. |

---

## TwinCAT And Deployment Implications

1. **Model Compatibility** – Ensure the ONNX model uses only operators supported by TwinCAT’s ML runtime (e.g., `MatMul`, `Add`, `Relu`).  
2. **Memory Footprint** – The 500 µs task must fit within the PLC’s RAM budget; monitor the size of the *Predict_ML.req_re* block and associated DBs (`xCSV_and_Vectors`).  
3. **Task Prioritization** – Keep the ML task at a lower priority than the Fast Task to avoid starving motor control loops.  
4. **File System Access** – The CSV file path must be accessible from the PLC’s file system (e.g., via `C:\Users\...`). Consider using a network share or local flash for production deployments.  
5. **Code Adaptation** – When porting to other machines, adjust the state machine logic: replace hard‑coded state 100 with a configurable parameter (`stateTrigger`).  

---

## Reference Snapshots

| Timestamp | Concept | Snapshot Description |
|-----------|---------|----------------------|
| 00:01:15 | Task timing & inter‑task communication | Left navigation shows `Predict_ML.req_re` block linked to `Task_500us_ML`. |
| 00:06:11 | Fast Task configuration | Right properties panel displays “Fast Task (250 µs)” and low‑correction position application. |
| 00:11:10 | ML orchestration in PLC | Left navigation lists POUs (`P_Experiment_Cam_Correction_TE_ML`, `startEx_TE`) and flags (`bEnableFF_TE`). |
| 00:15:36 | CSV read trigger | Same block list, highlighting `needToReadCSV_` flag. |

These snapshots illustrate the key configuration points that must be replicated when setting up a new TestRig.

---

## Open Questions Or Uncertain Points

1. **Model Precision** – The video does not specify whether the ONNX model uses FP32 or INT8 quantization; this affects inference speed and memory usage.  
2. **Error Recovery** – How does the system behave if the CSV file is missing or corrupted? Is there a watchdog mechanism?  
3. **Scalability** – Can multiple ML models run concurrently on the same PLC, or must each be isolated in its own task group?  
4. **Security** – The path to the CSV file uses a user directory; for production environments, should we use a dedicated data folder with restricted access?  

Addressing these points will ensure robust deployment of TwinCAT‑based ML solutions in industrial settings.

---
