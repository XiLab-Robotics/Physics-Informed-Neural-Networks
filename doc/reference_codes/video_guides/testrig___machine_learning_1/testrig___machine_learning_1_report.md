# Overview  

The video **TestRig - Machine_Learning 1.mp4** demonstrates the end‑to‑end flow of exporting a TwinCAT ML model from Beckhoff’s Model Manager, importing it into TwinCAT 15 via code, and using the resulting prediction blocks on the PLC side. The companion transcript file is located at  

```
C:\Users\Alessio Tutarini\Unimore\XiLAB Robotics - DATA\02-Test Rig\Machine Learning
```  

The selected reference snapshots (e.g., 00:30:17 – “Task timing and inter‑task communication”, 00:11:10 – “Model export or Beckhoff model‑manager workflow”) illustrate the key points of this flow without reproducing raw OCR text.

---

## Why This Video Matters  

Understanding how TwinCAT ML models are exported, packaged in an XML file with multiple references, and then instantiated as prediction blocks is critical for any integration that relies on Beckhoff’s **TwinCAT** toolchain. The video clarifies the data‑flow assumptions (input arrays, output strings), the role of `Global_Variables` for model loading, and the impact of timing delays on downstream tasks such as motor control.

---

## Main Technical Findings  

| Finding | Evidence Reference |
|---------|--------------------|
| **Model export** is performed through Beckhoff’s Model Manager; the exported file is an XML that contains several models linked by a common name (`Raffronz`). | Snapshot 00:11:10 – “Open target folder”. |
| **Import via code** uses `LoadModel_ins` and writes the model to a local path, then creates prediction blocks (`FB_Predict_Amp`, `FB_Predict`). The import must succeed; otherwise an error is raised. | Snapshot 00:30:17 – “Task timing and inter‑task communication”. |
| **Prediction block configuration** includes: <br>• `sModelName` (string) <br>• `P_Experiment_Cam` (UDINT, input dimension) <br>• `FB_Predict_Amp` (BOOL) <br>• `FB_Predict` (BOOL) <br>• `FB_MilPredic` (STRING(255)) | Snapshot 00:16:07 – “TwinCAT prediction blocks and PLC‑side ML orchestration”. |
| **Input array** is defined as `%I* %I*` (real values) with a size of `[0..2]`. The model expects two real inputs per call. | Snapshot 00:16:07 – “Vector_Input ARRAY [0..2] OF REAL”. |
| **Output string** is limited to 255 characters (`Model_Ampl STRING(255)`). | Same snapshot as above. |
| **Timing delay** observed when the model is loaded from disk (≈ 49 s) due to file‑system constraints, which can affect real‑time performance. | Snapshot 00:30:17 – “Task timing and inter‑task communication”. |
| **Two deficiencies** are noted in the test rig: <br>1. `FB_Predict_Amp` never becomes TRUE (busy flag FALSE). <br>2. `ML_Transmission_Error` remains FALSE despite a non‑zero error condition. | Transcript 00:04:58 – “deficiencies un bloc fb predicto e l’intransmission error”. |

---

## TwinCAT And Deployment Implications  

1. **File location & naming** – The XML must be placed in the folder referenced by `Open target folder`. All models share the identifier **Raffronz**; any change to this name breaks downstream code that references it.  
2. **Prediction block wiring** – The PLC side uses `Global_Variables` (index 4) to pass model‑specific parameters (`FB_Predict_Amp`, `FB_Predict`). Ensure these variables are correctly populated before invoking the block.  
3. **Input/output assumptions** – The model expects a 2‑element real array (`%I* %I*`) and returns a string ≤ 255 characters. Mismatched dimensions or length will cause silent failures (e.g., `FB_Predict_Amp` stays FALSE).  
4. **Code‑adaptation impact** – Because the model is loaded via code, any change to the XML (new models, renamed identifiers) requires a rebuild of the TwinCAT project and recompilation of the PLC program that calls `LoadModel_ins`. This adds a non‑trivial deployment step.  
5. **Timing considerations** – The 49 s load time is a bottleneck for real‑time loops; consider pre‑loading models into memory or using faster storage (e.g., SSD) to meet the 500 µs task window.

---

## Reference Snapshots  

- **Snapshot 00:30:17** – Illustrates *Task timing and inter‑task communication*. It shows that the model’s execution is part of a larger workflow where delays (e.g., file I/O) propagate to subsequent tasks such as motor control. This snapshot confirms the need for low‑latency data paths.  
- **Snapshot 00:11:10** – Shows *Model export or Beckhoff model‑manager workflow*. The screenshot highlights the “Open target folder” step, confirming that the XML file containing multiple models linked by `Raffronz` is the source of truth for TwinCAT ML integration.

---

## Open Questions Or Uncertain Points  

1. **Exact path** – The transcript mentions a local folder but does not specify whether the model must be copied to a specific sub‑folder (e.g., `Model_Export`). Clarify if the path is absolute or relative to the TwinCAT project root.  
2. **Identifier consistency** – All models reference the name *Raffronz*. Is this a hard‑coded constant in the PLC code, or does it come from an external configuration file? A mismatch could cause `FB_Predict_Amp` to remain FALSE.  
3. **Error handling** – The video notes “intransmission error” but the screenshot shows `ML_Transmission_Error = FALSE`. How is this flag supposed to be set, and why does it stay clear in practice?  
4. **Performance bottleneck** – The 49 s load time is far longer than the 500 µs task window. Is there a possibility of pre‑loading models into memory at startup, or must each call trigger a reload?  

These points remain open for further investigation to ensure reliable TwinCAT ML deployment on the TestRig.
