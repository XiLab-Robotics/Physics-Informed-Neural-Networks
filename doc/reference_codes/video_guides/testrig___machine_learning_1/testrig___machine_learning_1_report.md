# TwinCAT/TestRig Video Guide – Machine Learning 1

**Video:** *TestRig - Machine_Learning 1.mp4*  
**Transcript source:** `Machine_Learning_1.txt` (extracted from the video)  
**Reference snapshots:** Conceptually referenced in the report; actual image files are stored under  
`C:\Users\Alessio Tutarini\Unimore\XiLAB Robotics - DATA\02-Test Rig\Machine Learning`

---

## Overview

The video demonstrates how a Beckhoff TwinCAT PLC can be used to orchestrate machine‑learning (ML) predictions for a TestRig experiment. It covers:

1. **Importing an exported ML model** from the *Beckhoff Model Manager* into the PLC project.
2. **Configuring the prediction function block** (`FB_Predict_*`) with input dimensions, enable flags, and reset signals.
3. **Running predictions in real‑time** while monitoring task timing and inter‑task communication through global variables.

The companion notes point to the folder where all simulation files (XML, model exports, snapshots) are located, providing a clear directory structure for reproducibility.

---

## Why This Video Matters

- **Bridging ML and PLC:** It shows a concrete workflow that connects an externally trained ML model (e.g., from Python or MATLAB) with a real‑time PLC control loop.
- **Deployment Insight:** Demonstrates how to package the model as XML, load it via the Model Manager, and expose its parameters through TwinCAT’s POUs.
- **Performance Awareness:** Highlights task timing considerations when predictions are performed in a slower task than drive updates, which is critical for safety‑critical robotics.

---

## Main Technical Findings

| Topic | Key Points |
|-------|------------|
| **Model Export** | The model is exported as an XML file from the ML environment and placed in the *Machine Learning* folder. The video shows selecting this file in the Model Manager, then clicking “Convert Files”. |
| **Function Block Configuration** | `FB_Predict_*` blocks expose properties such as: <br>• `nInputDim` (UDINT) – number of input features.<br>• `bEnable` (BOOL) – start prediction when true.<br>• `req_reset` (BOOL) – reset internal state.<br>• `bLoadModed` (BOOL) – load the model into memory. |
| **Global Variables** | A set of GVLs (`Global_Variables`) holds flags like `Busy`, `Enable_TE`, and vectors for input/output (`Vector_Input`). These are shared between tasks to coordinate prediction requests. |
| **Task Timing** | The prediction task runs at a lower frequency than the drive control task, causing observable delays in the experiment. This is intentional to accommodate the computational load of ML inference. |
| **Inter‑Task Communication** | Inputs from sensors (`P_Experiment_Cam`, `P_Experiment_Torque_Sen`) are fed into the prediction block via POUs (`FB_Predict_Amp`, `FB_Predict_Phase`). Outputs are routed back to actuator commands after optional filtering or compensation routines. |

---

## TwinCAT And Deployment Implications

1. **Model Manager Integration**  
   - The Model Manager must be configured to recognize the XML format used by the exported ML model.  
   - After conversion, the generated POUs can be added to the PLC project and linked to the appropriate tasks.

2. **Memory Footprint**  
   - Loading large models (`bLoadModed = TRUE`) consumes RAM; ensure the target CPU has sufficient memory or consider quantized/compact models.

3. **Task Scheduling**  
   - Place the prediction block in a dedicated task with a period that balances latency and computational load (e.g., 10 ms vs. 1 ms for drive updates).  
   - Use `Busy` flags to prevent overlapping predictions.

4. **Safety & Redundancy**  
   - The `req_reset` signal allows the system to recover from erroneous states without rebooting the PLC.  
   - Implement watchdog checks on prediction outputs before applying them to actuators.

5. **Code Adaptation**  
   - When porting this setup to another experiment, adjust `nInputDim`, input vector names, and output handling accordingly.  
   - Ensure that any new POUs follow the same property naming convention for consistency.

---

## Reference Snapshots

The video references several snapshots of the TwinCAT IDE:

- **Navigation Pane** – shows the hierarchy: *Gig TEST_RIG_MOTORS*, *FB_Predict_* blocks, and global variables.  
- **Properties Window** – displays key parameters (`nInputDim`, `bEnable`, etc.) for each function block.  
- **Model Manager Dialog** – illustrates the “Open target folder” button used to locate the XML file.

These snapshots are stored in the *Machine Learning* directory and can be reviewed to verify the exact configuration shown in the video.

---

## Open Questions Or Uncertain Points

| Question | Context |
|----------|---------|
| **Model Format** | The exact schema of the exported XML (e.g., whether it includes quantization tables) is not detailed. |
| **Prediction Latency** | Precise timing measurements for the prediction task are not provided; only qualitative statements about delays. |
| **Error Handling** | How the system reacts to model loading failures or malformed input vectors remains unspecified. |
| **Scalability** | No discussion on scaling to multiple simultaneous predictions or higher‑frequency tasks. |

Addressing these points would strengthen confidence in deploying this workflow in production environments.

---
