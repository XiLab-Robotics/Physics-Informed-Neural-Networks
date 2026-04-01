# Video_Errata_Corrige_ADRC.mkv Report

## Overview  

This video guide documents the correction of a simulation‑related error in **Video_Errata_Corrige_ADRC.mkv**. The primary issue concerns the variable used by TwinCAT’s *TE_Calc* function to perform the ADRC (Automatic Direction Control) calculation. Instead of relying on an external MATLAB‑derived value, the video demonstrates that the computation is performed directly within TwinCAT using the internal `position tot` signal.  

## Why This Video Matters  

Understanding this correction is critical for engineers who:  

* Export TwinCAT models to Beckhoff’s **ML (Model‑Level) framework** – the model must not depend on an external variable that does not exist in the PLC environment.  
* Integrate the simulation link into a **PLC‑based TestRig** – the simulated sum of two elements must be generated internally, avoiding mismatched data streams.  
* Use Beckhoff’s tooling (e.g., *TwinCAT Modeler*, *TestRig Designer*) to keep the model and hardware synchronized.  

## Main Technical Findings  

| Finding | Detail |
|---------|--------|
| **Variable source** | `TE_Calc` does not read a MATLAB‑generated variable; it uses the internal TwinCAT signal `position tot`. |
| **Simulation link expectation** | The simulation expects a summed value from two elements, which is now produced directly in TwinCAT. |
| **Model input/output assumptions** | The model’s I/O must reflect that the sum is generated internally, not imported from an external source. |
| **Beckhoff tooling impact** | No change to TestRig structure; only the internal calculation path needs adjustment. |

## TwinCAT And Deployment Implications  

* **ML Export:** When exporting a TwinCAT model to Beckhoff’s ML environment, the exported code will contain `TE_Calc` that references `position tot`. No external variable is required, simplifying downstream PLC integration.  
* **PLC Integration:** The simulated sum becomes a native output of the TwinCAT simulation block, which can be directly mapped to a physical output on the TestRig. This eliminates latency caused by waiting for MATLAB data.  
* **TestRig Structure:** The hardware configuration remains unchanged; only the internal logic (summation) is corrected.  

## Reference Snapshots  

The video includes a snapshot at **00:01:04** that visually confirms the *Axis Group (2)* properties, including its canvas color and title. This snapshot serves as a reference point for verifying that the simulation link’s configuration aligns with the intended model state before the correction is applied.

## Open Questions Or Uncertain Points  

* The exact name `position tot` has not been explicitly defined in the provided evidence; clarification on whether it maps to a specific PLC output or internal variable is needed.  
* How the summed value from TwinCAT should be routed to the TestRig’s input bus remains ambiguous—does it use a dedicated I/O tag, or is it handled via the simulation link?  

---  

*All conclusions are derived solely from the supplied video evidence and companion notes; no external OCR dump has been included.*
