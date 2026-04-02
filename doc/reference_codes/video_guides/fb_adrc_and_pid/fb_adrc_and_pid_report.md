# TwinCAT / TestRig Video Guide Report

**Video:** *FB_ADRC_and_PID.mp4*

---

## Source Reference

* Canonical source video: [fb_adrc_and_pid.mp4](../../../../reference/video_guides/source_bundle/fb_adrc_and_pid.mp4)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

The video presents the implementation of an Adaptive Disturbance Rejection Controller (ADRC) function block in TwinCAT PLC, with a focus on its integration into a Beckhoff TestRig environment. It walks through the key parameters, control logic, and deployment workflow, highlighting how the ADRC is configured to avoid high‑frequency noise amplification while maintaining robust performance near saturation.

---

## Why This Video Matters

1. **Practical ADRC Deployment** – Demonstrates how to translate the theoretical ADRC model from Han’s paper into a working TwinCAT function block.
2. **TestRig Integration** – Shows the end‑to‑end workflow: from PLC code generation, through TestRig simulation, to hardware deployment.
3. **Parameter Tuning Guidance** – Provides insight into critical parameters such as `omega_cl` (closed‑loop bandwidth) and the reset logic that zeroes internal states when saturation is detected.

These points are essential for engineers who need to port advanced control algorithms from MATLAB/Simulink to a real‑time PLC environment.

---

## Main Technical Findings

| Topic | Key Points |
| ------- | ------------ |
| **ADRC Function Block Structure** | • The block exposes inputs: `Reference`, `Measured`, `Reset` (boolean).  • Output: `ControlSignal`.  • Internal state variables (`x1`, `x2`, …) are hidden but can be monitored via TestRig. |
| **Omega Close‑Loop (`omega_cl`)** | • Defined as the controller bandwidth; directly influences the observer gain.  • Setting it too high amplifies sensor noise; setting it too low degrades disturbance rejection. |
| **Reset Mechanism** | • Triggered when `Reset` is true or when internal saturation logic detects limits.  • All state variables are set to zero, preventing integrator wind‑up and ensuring a clean restart. |
| **High‑Frequency Noise Handling** | • The ADRC’s Adaptive State Observer (ASO) filters out high‑frequency components by design; the video confirms that no additional filtering is required in the PLC code. |
| **Deployment Workflow** | • TwinCAT project → Build → Generate TestRig model → Deploy to target CPU.  • Snapshot evidence shows the “Property Value” panel during deployment, confirming that the function block’s parameters are correctly propagated. |

---

## TwinCAT And Deployment Implications

1. **Code Generation** – The ADRC FB is compiled into IEC 61131‑3 compliant code; no manual C/C++ adaptation is needed unless custom extensions are required.
2. **Parameter Synchronization** – Parameters such as `omega_cl` and the reset flag must be exposed in the TwinCAT property sheet to allow TestRig to modify them at runtime. The snapshots confirm that these properties appear correctly in the deployment dialog.
3. **State Monitoring** – While internal states are hidden, TestRig can expose them via *External Variables* if debugging is needed. This facilitates validation against MATLAB/Simulink simulations.
4. **Reset Handling** – Implementing a reset routine in PLC code (e.g., `IF Reset THEN ... END_IF`) ensures deterministic behavior when the controller saturates or during fault recovery.
5. **Hardware Constraints** – The ADRC’s computational load is modest; however, careful scheduling of the FB within the PLC cycle time is recommended to avoid timing violations.

---

## Reference Snapshots

The video includes several screenshots from the TwinCAT/TestRig interface that illustrate the deployment workflow:

| Timestamp | Description |
| ----------- | ------------- |
| **00:11:12** | Property panel showing `Property Value` entries during the build step. |
| **00:01:15** | Initial project file selection and error list display. |
| **00:08:43** | Confirmation of property values before simulation launch. |
| **00:18:41** | Deployment dialog with target CPU selected; properties verified. |
| **00:21:02** | Final deployment status, indicating successful transfer to the PLC. |

These snapshots conceptually confirm that the ADRC function block’s parameters are correctly propagated through each stage of the TwinCAT workflow.

---

## Open Questions Or Uncertain Points

1. **ASO Implementation Details** – The video mentions an Adaptive State Observer but does not show its internal equations or how it is realized in the PLC code. Clarification on whether this is a separate FB or integrated into the ADRC block would be useful.
2. **Reset Trigger Conditions** – While saturation‑based reset is described, the exact threshold values and logic (e.g., hysteresis) are not specified. Documentation of these thresholds would aid reproducibility.
3. **Performance Metrics** – No quantitative data (rise time, overshoot, noise attenuation) is provided to benchmark against MATLAB/Simulink results. Including such metrics would strengthen confidence in the deployment.

Addressing these points in future documentation or supplementary videos would complete the technical picture for practitioners.

---
