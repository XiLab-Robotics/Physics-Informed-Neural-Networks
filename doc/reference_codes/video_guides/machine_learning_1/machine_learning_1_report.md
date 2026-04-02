# TwinCAT/TestRig Video Guide – Machine_Learning_1.mp4  

*Technical Report (Markdown)*

## Source Reference

- Canonical source video: [machine_learning_1.mp4](../../../../reference/video_guides/source_bundle/machine_learning_1.mp4)
- Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

---

## Overview  

The video **Machine_Learning_1.mp4** demonstrates the end‑to‑end workflow for integrating a machine‑learning (ML) model into a Beckhoff TwinCAT PLC environment using the TestRig framework. The key steps covered are:  

1. **Exporting an ML model** from the laboratory’s Python/Matlab pipeline to an XML file that can be consumed by the Beckhoff Model Manager.  
2. **Importing the XML** into TwinCAT via the *Model Manager* UI and converting it into a PLC‑ready format.  
3. **Instantiating the generated function blocks (FBs)** in the TestRig project, wiring them to the motor/torque sensors, and configuring input/output parameters.  
4. **Running the prediction loop** with a 500 µs task period and observing the real‑time output on the PLC side.  

The companion notes point to the folder where all simulation files are stored:  
`C:\Users\Alessio Tutarini\Unimore\XiLAB Robotics - DATA\02-Test Rig\Machine Learning`.  
All XML model files referenced in the video reside here.

---

## Why This Video Matters  

- **Bridging ML and PLC** – It shows a practical, reproducible method for moving a trained neural network from a research environment into an industrial controller.  
- **Real‑time constraints** – The 500 µs task period illustrates how to meet tight timing requirements while still executing complex inference logic.  
- **Modular design** – By using the TestRig’s function blocks, developers can swap models or update parameters without rewriting PLC code.  

---

## Main Technical Findings  

| Topic | Observation | Evidence |
|-------|-------------|----------|
| **Model Export Path** | Models are exported as XML files that include multiple references (`reference="ingen40"` etc.). | Transcript: “All’interno di un file XML è possibile inserire più modelli e riferirsi a ciascuno tramite il nome di reference assegnato.” |
| **Import UI Flow** | The user selects XML files, the Model Manager lists them, and the *Convert* button generates PLC‑compatible FBs. | Transcript: “Perciò si vanno a selezionare i file, ovviamente XML; una volta selezionati vengono visualizzati qui e si preme 'Conve'.” |
| **Function Block Structure** | Each model yields an FB with parameters such as `ModelName`, `ninputDim`, `bEnable`, and I/O arrays (`Vector_Input`). | OCR 00:21:06 – shows `49 sModelName T_MaxString P_Experiment_Cam ninputDim UDINT … Vector_Input ARRAY [0..2] OF REAL`. |
| **Task Timing** | The prediction task runs every 500 µs, slower than drive tasks but sufficient for the number of components. | OCR 00:29:49 – “Il task ha una durata di 500 µs; è più lento rispetto a quello realizzato per i drive perché…” |
| **Data Flow** | Inputs come from sensor FBs (`TEST_RIG_TORQUE_SEN`) and outputs are written to motor command variables. | OCR 00:16:07 – lists `TEST_RIG_MOTORS`, `FB_Predict_Amp`, etc. |
| **Error Handling** | A dedicated FB (`FB_ML_TE`) monitors transmission errors, exposing flags like `Busy` and `Enable_TE`. | OCR 00:30:21 – shows `FB_ML_TE ML_Transmission_Error 9 Busy BOOL FALSE Enable_TE BOOL FALS`. |

---

## TwinCAT And Deployment Implications  

1. **Model Manager Integration**  
   - The XML must follow the Beckhoff schema; otherwise the *Convert* step fails.  
   - Multiple models can coexist in one file, but each requires a unique `reference` name to be instantiated separately.

2. **Function Block Instantiation**  
   - Generated FBs are placed under `POUs`.  
   - Developers must manually wire input arrays (`Vector_Input`) and output variables (e.g., `Model_Ampl`, `Model_phase`).  

3. **Timing Constraints**  
   - A 500 µs task period is chosen to balance inference complexity with real‑time requirements.  
   - If the model size grows, consider increasing the task period or optimizing the FB code.

4. **Error Monitoring**  
   - The `FB_ML_TE` block should be connected to a watchdog or safety system; its `Busy` flag can trigger fallback logic if inference stalls.

5. **Deployment Packaging**  
   - After configuring the FBs, compile the project and download it to the target PLC.  
   - Verify that the XML path (`C:\Users\Admini...`) is accessible on the PLC host or adjust the path in the FB parameters.

---

## Reference Snapshots  

| Timestamp | Concept | Snapshot Description |
|-----------|---------|----------------------|
| 00:08:41 | Model Manager UI – *Open target folder* button | Shows the file explorer dialog where XML files are selected. |
| 00:16:07 | Function Block navigation – `TEST_RIG_MOTORS` and `FB_Predict_*` | Highlights the FBs that handle motor commands and predictions. |
| 00:21:06 | Parameter panel of a generated FB (`P_Experiment_Cam`) | Displays input dimension, enable flag, and reset request. |
| 00:30:21 | Task configuration – *ML Transmission Error* block | Illustrates the error monitoring logic tied to the prediction task. |

These snapshots conceptually represent the UI elements and code structures discussed in the video; they are not raw OCR dumps but rather summarized views of the relevant sections.

---

## Open Questions Or Uncertain Points  

1. **Model Size Limits** – The video does not specify how many layers or neurons can be accommodated before the 500 µs period becomes insufficient.  
2. **Memory Footprint** – No explicit data on RAM usage for the generated FBs; this could impact deployment on smaller PLCs.  
3. **Dynamic Model Reloading** – It is unclear whether the system supports hot‑reloading of a new XML without recompiling the entire project.  
4. **Safety Integration** – While `FB_ML_TE` monitors errors, the video does not show how these flags are integrated into a safety PLC or HMI.  

Addressing these points would strengthen confidence in deploying ML models at scale within TwinCAT TestRig environments.

---
