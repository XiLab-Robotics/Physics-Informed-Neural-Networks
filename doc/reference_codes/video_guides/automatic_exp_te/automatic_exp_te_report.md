# Automatic_Exp_TE.mp4 Report

## Overview  

The video **Automatic_Exp_TE.mp4** demonstrates a laboratory experiment that varies the speed, temperature, and torque of a transmitter while monitoring its performance on a stable TestRig. The experiment is driven by an ADRC‑based control loop exported from TwinCAT ML. The companion transcript (see *Transcript file: Automatic_Exp_TE.mp4*) contains timestamps where key code fragments are visible in the OCR‑assisted snapshots, which we treat as **reference snapshots** for engineering analysis.

---

## Why This Video Matters  

- Provides a concrete example of how TwinCAT ML variables (`TE_Vel_Torque_Temp`) are exported and consumed by Beckhoff ADRC.  
- Highlights the integration points between TwinCAT’s ML export, the TestRig sensor interface (FB), and the PLC‑side task timing.  
- Reveals a persistent vector‑size error that must be addressed for reliable deployment.

---

## Main Technical Findings  

| Finding | Evidence (timestamp) | Engineering Implication |
|---------|----------------------|--------------------------|
| **Variable set** – speed, temperature, and torque are read from a matrix row. | 00:14:57‑00:16:32 (transcript) | The model assumes these three inputs; the video notes that four variables were used in practice but the code only assigns two directly. |
| **Vector‑size error** – always reported as “17”. | 00:09:57‑00:14:57 (transcript) | The ML export does not adapt to dynamic vector length; this must be resolved in TwinCAT configuration or code. |
| **ADRC task timing** – `Td_TE_Vel_Torque_Temp` is defined as a 4‑function timer. | 00:11:12 (OCR) | The PLC expects a specific inter‑task communication window; any deviation can cause missed updates. |
| **Control parameters** – Kp, Ti, Td are present in the ADRC controller block. | 00:06:14 (OCR) | These PID‑like coefficients are baked into the ML export and must be matched to the TestRig’s sensor bandwidth (`f_notch_filter_TE_Vel_Torque`). |
| **Sensor data flow** – `FB_TestRigSensorData` feeds `xCSV_and_Vectors`. | 00:15:21 (OCR) | The output vector is filtered through `f_notch_filter_TE_Vel_Torque_1` before being written to CSV. This defines the expected input shape for downstream PLC logic. |
| **Safety monitor** – “monitor della sicurez” is referenced but not observed. | 00:00:00‑00:05:00 (transcript) | The experiment proceeds despite an unconfirmed safety monitor; this may affect future deployments. |

---

## TwinCAT And Deployment Implications  

1. **ML Export Consistency** – The exported ML module must preserve the exact variable ordering (`TE_Vel_Torque_Temp`) and data types as shown in the reference snapshots. A mismatch will trigger the constant vector‑size error (value = 17).  
2. **PLC Integration** – TwinCAT’s `StartAutomaticTest_TE_Torq` task must be synchronized with Beckhoff ADRC’s `Td_TE_Vel_Torque_Temp`. The 4‑function timer (`TD`) is critical for timing the read of the matrix row and updating the PID loop.  
3. **Beckhoff Tooling** – The TestRig’s sensor interface (`FB_LightDevice`, `FB_TestRigSensorData`) must be declared in TwinCAT as a *sensor data source* that outputs a 4‑element vector, filtered by `f_notch_filter_TE_Vel_Torque_1`. This filter defines the bandwidth for the speed/torque channel.  
4. **Code Adaptation** – To avoid the persistent error, either:  
   - Redefine the ML module to accept a variable‑length vector (e.g., using `DynamicArray`), or  
   - Adjust the PLC task to ignore the extra 17th element and treat it as padding.  

---

## Reference Snapshots  

The OCR‑assisted snapshots serve as **reference points** for the engineering analysis:

- **00:01:15** – Shows `ADRC_controller a T_d_TE_Vel_Torque_Temp Fl ADRC_Grade_3 (FB) …` → confirms task definition and variable naming.  
- **00:11:12** – Displays the PID‑related constants (`K_p`, `T_i`, `T_v`, `T_d`) attached to the same variables.  
- **00:15:21** – Illustrates the data‑flow path: `xCSV_and_Vectors` → filtered vector → `FB_TestRigSensorData`.  

These snapshots are used conceptually to map TwinCAT’s ML export to Beckhoff ADRC and TestRig sensor interfaces.

---

## Open Questions Or Uncertain Points  

- **Why does the vector size error remain 17 despite code modifications?** The OCR notes “dimensione dei vettori lui comunque per sua dichiarazione l'errore è sempre 17.” This suggests a hard‑coded constant in the ML module that must be cleared.  
- **Is torque truly part of the optimal model, or is it a placeholder?** The transcript mentions four variables but only two are directly assigned; further validation is needed.  
- **What is the status of the safety monitor (“monitor della sicurez”)?** Its absence could affect compliance and future deployment.  

--- 

*Prepared from the transcript file *Automatic_Exp_TE.mp4* and the selected reference snapshots.*
