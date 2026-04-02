# TwinCAT/TestRig Video Guide – Technical Report

**Video:** `Video_Errata_Corrige_ADRC.mkv`

---

## Source Reference

* Canonical source video: [video_errata_corrige_adrc.mkv](../../../../reference/video_guides/source_bundle/video_errata_corrige_adrc.mkv)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

The video demonstrates the correction of a simulation error in a TwinCAT TestRig environment that was originally caused by an incorrect variable reference (`TE_Calc`). The presenter shows how to properly link the MATLAB‑generated model with the TwinCAT PLC, ensuring that the calculated control signal is correctly passed into the simulation. Key elements covered include:

* Identification and correction of the erroneous variable.
* Integration of the MATLAB‑derived model (ML export) into a TwinCAT TestRig project.
* Configuration of input/output channels for the PLC program.
* Verification of simulation results against expected behavior.

The accompanying transcript and snapshot evidence confirm that the presenter explicitly acknowledges the mistake, explains the fix, and demonstrates the corrected workflow.

---

## Why This Video Matters

1. **Error Rectification** – Highlights a common pitfall when importing MATLAB models into TwinCAT: mis‑matching variable names between the generated code and the PLC program.
2. **Best‑Practice Workflow** – Provides a step‑by‑step method for linking MATLAB outputs to TestRig inputs, ensuring reproducibility in future projects.
3. **Toolchain Insight** – Offers practical insight into how Beckhoff’s tooling (TwinCAT 3, TestRig) interprets and executes the exported ML code.
4. **Educational Value** – Serves as a concise reference for engineers transitioning from MATLAB/Simulink to real‑time PLC simulation.

---

## Main Technical Findings

| Item | Observation | Implication |
| ------ | ------------- | ------------- |
| **Variable Mis‑reference** | The video states: *“TE_Calc in TwinCAT non è la variabile calcolata tramite Matlab”* (the `TE_Calc` variable is not the one computed by MATLAB). | Direct calculation must be performed inside TwinCAT or the correct exported variable must be mapped. |
| **Corrected Workflow** | The presenter connects “componenti correttamente” and shows a simulation that now uses the proper input channel. | Demonstrates how to adjust the PLC program to read from the correct TestRig input (e.g., `v1` channel). |
| **Snapshot Evidence** | At 00:03:15, the right‑hand properties panel displays *“Name v1 Time Shift [ps] 0”* and other visual settings. | Confirms that the variable `v1` is being used as an input to the simulation; this is likely the correct MATLAB output channel. |
| **Simulation Output** | The video shows a corrected graph (line color orange) matching expected behavior. | Validates that the updated PLC code correctly processes the MATLAB‑derived signal. |

---

## TwinCAT And Deployment Implications

1. **ML Export Compatibility**
   * When exporting from Simulink to TwinCAT, ensure that variable names in the generated C/C++ code match those referenced in the PLC program.
   * Use the *“Export Variable Names”* option in the MATLAB export wizard and verify them against the TestRig input channel list.

2. **PLC Program Structure**
   * The PLC should contain a dedicated block (e.g., `ADRC_Controller`) that receives the input from the TestRig (`v1`) and outputs the control signal to the plant model.
   * Avoid hard‑coding variable names; instead, use configuration tables or parameter blocks that can be updated without recompiling.

3. **TestRig Configuration**
   * The snapshot shows properties such as *“Visible True”* and *“Line Color 255, 165, 0”*, indicating that the TestRig is set to plot the `v1` channel in orange.
   * Ensure that the same channel names are used consistently across the PLC, TestRig, and any monitoring tools.

4. **Code‑Adaptation Implications**
   * When adapting code from MATLAB to TwinCAT, remember that MATLAB’s vectorized operations may need to be translated into iterative PLC logic or use of Beckhoff’s `FOR` loops.
   * The error highlighted in the video underscores the importance of validating each variable mapping after export.

---

## Reference Snapshots

| Time | Snapshot Description | Key Elements |
| ------ | --------------------- | -------------- |
| 00:03:15 | Right‑hand properties panel | *Name v1*, *Time Shift [ps] 0*, *Line Color 255,165,0* (orange), *Visible True* |
| 00:04:20 | Initial apology and correction statement | Text: “Mi scuso per l’errore nella presentazione precedente…” |

These snapshots conceptually illustrate the correct input channel configuration (`v1`) and its visual representation in TestRig. They serve as a reference for verifying that the PLC program is correctly wired to the simulation.

---

## Open Questions Or Uncertain Points

| Question | Context | Why it matters |
| ---------- | --------- | ---------------- |
| **Exact mapping of MATLAB output variables** | The transcript mentions `TE_Calc` being incorrect, but does not specify which exported variable replaces it. | Knowing the exact name is essential for automated code generation and debugging. |
| **Parameter values used in the corrected simulation** | No explicit values are shown for gains or time constants. | These parameters influence controller performance; without them, reproducing the results may be difficult. |
| **Version of TwinCAT/TestRig** | The video does not state which version was used. | Different versions may have subtle differences in variable handling and UI layout. |
| **Integration with external plant model** | The video focuses on the controller side but does not detail how the plant is modeled or connected. | Full system understanding requires knowledge of both sides. |

---

### Conclusion

This video provides a concise, engineering‑oriented walkthrough of correcting a TwinCAT TestRig simulation error caused by an incorrect variable reference. By focusing on proper variable mapping, PLC program structure, and TestRig configuration, the guide offers actionable insights for practitioners transitioning between MATLAB/Simulink and Beckhoff’s real‑time environment.
