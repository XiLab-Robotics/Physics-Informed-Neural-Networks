# TestRig - Machine_Learning 2.mp4 Report

## Overview  

The video *“TestRig – Machine_Learning 2.mp4”* continues the discussion from the first TwinCAT‑ML test rig demonstration, addressing issues that were not fully resolved earlier (e.g., communication latency, model loading conditions). The companion transcript is stored at  

```
C:\Users\Alessio Tutarini\Unimore\XiLAB Robotics - DATA\02-Test Rig\Machine Learning
```  

and the selected reference snapshots are conceptually linked to the video timestamps (e.g., 00:06:11, 00:11:07, 00:15:34). The report focuses on how TwinCAT’s ML export integrates with Beckhoff PLC tooling, the structure of the TestRig hardware, and the assumptions that govern model input/output handling.

---

## Why This Video Matters  

- **Timing clarification:** The video quantifies the inter‑module communication delay (≈ 1.300 ms) and states that a correction is acceptable if it stays below 500 µs, which is useful for timing‑critical PLC integration.  
- **Model loading condition:** It defines a concrete trigger – the first QP value must be zero – before the TwinCAT ML block can start processing. This eliminates ambiguous “wait until system ready” logic that appeared in the first video.  
- **Reference to transcript & snapshots:** The transcript file is referenced implicitly; the three reference snapshots provide visual evidence of task timing, communication flow, and the ML orchestration configuration.

---

## Main Technical Findings  

| Finding | Evidence (conceptual) |
|---------|-----------------------|
| **Communication latency** – 1.300 ms between TwinCAT prediction blocks and PLC side is within acceptable range (< 500 µs). | Transcript: “1,300, 25.3 microsecondi … se desidera 500.000, sentendo sul ritardo di comunicazione tra le tasche”. |
| **Model input assumption** – The first row of the QP vector must be zero to start ML processing; otherwise the system remains in a “load‑system” state. | Transcript: “se questo è diverso da 0, andare a caricare il sistema. Finché non sia il giunto di tale valore”. |
| **Input vectors** – Three forward models are defined (forward 1, 2, 3) that feed the ML block. | OCR‑assisted evidence (00:06:11): “QP Aggiornamento presenta V 7 … Modello di forward”. |
| **ML orchestration** – TwinCAT prediction blocks are linked to a Beckhoff PLC via a TEFF file; the configuration repeats at 00:11:07 and 00:15:34. | OCR‑assisted evidence (00:11:07, 00:15:34): “ae targetVelocity_TE 4 … P_Experiment_Cam_with_TECompens”. |
| **Task timing** – Two Fast Task blocks are present (250 s vs 2501 s) with a low‑correction flag; this indicates the system can tolerate minor jitter. | OCR‑assisted evidence (00:06:11): “Task Fast Task Fast (250s) (2501s) Invio Pos con low correzione”. |

---

## TwinCAT And Deployment Implications  

- **Export from TwinCAT:** The ML model is exported as a prediction block that expects three forward‑model inputs. Any change to the number of vectors or their ordering will break the PLC integration.  
- **Beckhoff tooling:** The TEFF file (`P_Experiment_Cam_with_TECompens`) supplies calibration data for `targetVelocity_TE 4`. The PLC must be configured to read this file at startup; otherwise the ML block receives stale parameters.  
- **Integration point:** TwinCAT’s prediction block is linked to a Beckhoff FB (e.g., `FB_BoschMotor`). The output of the ML block (`P_Experiment_Cam_correction_TE_ML`) drives the motor feed‑forward, but only after the QP zero condition is met.  
- **Deployment checklist:**  
  1. Verify that the first QP value is zero (or handle non‑zero gracefully).  
  2. Confirm TEFF file path and `targetVelocity_TE` value are correct in the PLC configuration.  
  3. Ensure the three forward models match the TwinCAT export; otherwise the ML block will raise an error.  

---

## Reference Snapshots  

- **00:06:11** – Shows task timing and inter‑task communication (Fast Task Fast, low correction).  
- **00:11:07** – Displays TwinCAT prediction blocks linked to Beckhoff PLC via TEFF file (`P_Experiment_Cam_with_TECompens`).  
- **00:15:34** – Repeats the same ML orchestration configuration, confirming consistency across timestamps.  

These snapshots are not raw OCR dumps; they serve as conceptual anchors for the engineering analysis above.

---

## Open Questions Or Uncertain Points  

1. **TEFF file path:** The video mentions `TEFF_File = P_Experiment_Cam_wi` but does not specify the exact location on disk. Is this a relative path or an absolute one?  
2. **Correction threshold:** The 500 µs limit is mentioned as a “desidera” value; can it be tuned via Beckhoff configuration, or is it fixed in TwinCAT?  
3. **Non‑zero QP handling:** If the first QP row deviates from zero, what fallback strategy does the PLC implement (e.g., hold motor, log error)? The transcript only says “caricare il sistema”; no explicit fallback is described.  

These points remain open for further engineering validation before full deployment.
