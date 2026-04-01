# Controller_ADRC.mkv Report

## Overview  

The video **Controller_ADRC.mkv** demonstrates a closed‑loop tuning workflow that couples a Simulink model (exported as TwinCAT ML) to the Beckhoff TestRig hardware. The core of the system is a discrete gain observer (`Gain_observer_discrete.m`) that implements a *diarrecci* coefficient – effectively the multiplier for the ω<sub>c</sub> closed‑loop bandwidth. The model’s input and output are defined as **“Ris Discreto”** (discrete reference) and **“Ris Discreto Stimata”** (estimated response), respectively, with a linear transfer function expressed via `num(z)` / `den(z)`.  

The workflow is visualised in the selected reference snapshots:  
* 00:21:02 – shows the Test Rig’s I/O mapping (`num den(z) … Ris Discreto Stimata`).  
* 00:36:22 – displays TwinCAT scope auto‑save configuration (no auto‑delete, custom mask `{SCOPE}`).  

---

## Why This Video Matters  

- **Practical integration** of Beckhoff TestRig with TwinCAT ML export.  
- Provides a concrete example of how the *diarrecci* coefficient is derived from the closed‑loop bandwidth (ω<sub>c</sub>) and used as a multiplier in the discrete observer.  
- Highlights the **code‑adaptation** needed to translate Simulink’s MATLAB function into TwinCAT’s `ule` I/O model, which is essential for reliable PLC integration.  

---

## Main Technical Findings  

| # | Finding | Engineering Detail |
|---|----------|--------------------|
| 1 | **Model definition** – The Test Rig supplies a discrete transfer function (`TF`) that maps the reference (`Ris Discreto`) to the estimated output (`Ris Discreto Stimata`). | `num(z)` / `den(z)` are used; the TF is stored in the Simulink model and exported as part of the TwinCAT ML target file. |
| 2 | **Gain observer implementation** – The MATLAB function `Gain_observer_discrete.m` computes a *diarrecci* coefficient (ω<sub>c</sub> multiplier) that scales the closed‑loop response. | Coefficient is stored in the ML export (`target file, Twink Uplink tip.lc`). |
| 3 | **TwinCAT ML export** – The exported model contains a `ule` input (`u`) and output (`y`) block that correspond to the Test Rig’s I/O names. | Input = “Ris Discreto”, Output = “Ris Discreto Stimata”. |
| 4 | **Beckhoff tooling integration** – TwinCAT reads the ML file via TICOM, invoking `ule` functions defined in `Gain_observer_discrete.m`. No direct Simulink‑TwinCAT bridge is used. | The observer runs inside TwinCAT’s PLC environment; any change to the coefficient must be re‑exported and re‑loaded into TwinCAT. |
| 5 | **Auto‑save configuration** – Scope auto‑save is disabled (`AutoSaveMode None`) with a custom mask `{SCOPE}` to avoid cluttering the workspace. | Data persistence is manual; this aligns with Beckhoff’s recommendation for production runs where only critical snapshots are retained. |
| 6 | **Simulation vs. hardware** – The video distinguishes between Simulink‑based simulation (used for tuning) and the actual Test Rig hardware that provides the discrete I/O. | The model’s input/output assumptions must match the physical test rig; otherwise, the closed‑loop gain will be incorrect. |

---

## TwinCAT And Deployment Implications  

- **Export format** – The ML file (`tip.lc`) is a standard TwinCAT ML export that can be loaded into any Beckhoff PLC (e.g., TIA Portal). No custom code generation beyond `ule` functions is required.  
- **Parameter handling** – The *diarrecci* coefficient is a scalar stored in the ML file; it can be updated by editing the MATLAB function and re‑exporting, which triggers a TwinCAT reload.  
- **I/O mapping** – The test rig’s discrete I/O (`Ris Discreto`, `Ris Discreto Stimata`) must be declared as `ule` variables in the ML file; mismatched names cause runtime errors.  
- **Closed‑loop stability** – Because the observer uses a *discrete* TF, the closed‑loop bandwidth (ω<sub>c</sub>) directly influences the gain multiplier. A mis‑calculated ω<sub>c</sub> can degrade performance or cause oscillation.  
- **Deployment checklist** – 1) Verify `Gain_observer_discrete.m` is compiled and exported; 2) Confirm TwinCAT’s TICOM reads the correct ML file; 3) Validate that the scope auto‑save mask `{SCOPE}` does not delete required snapshots during a run.  

---

## Reference Snapshots (Conceptual)

| Timestamp | Snapshot Content | Relevance |
|-----------|------------------|-----------|
| **00:21:02** | `num den(z) Test Rig SOLO1’ Ris Discreto TF TestRig Stimata 1°fraq Ris Test Rig SOLO1’ Ris Discreto Stimata` | Shows the exact I/O mapping of the discrete transfer function used in the model. |
| **00:36:22** | `Properties ~ x Scope Project1 … AutoSavePath $ScopeProject$\AutoSave AutoSaveMode None Delete more than 0 Filename Mask {SCOPE} AutoSave_{HH_m` | Illustrates TwinCAT’s scope auto‑save settings; confirms that only the `{SCOPE}` mask is retained, matching the video’s “no clutter” approach. |

---

## Open Questions Or Uncertain Points  

1. **What is the exact value of the *diarrecci* coefficient?** The transcript mentions it as a multiplier for ω<sub>c</sub>, but no numeric value is displayed in the video or snapshot.  
2. **Why does the scope auto‑save mode use `AutoSaveMode None`?** Is this intentional to prevent loss of critical snapshots, or is there a risk of data being overwritten?  
3. **How does the discrete TF (`num(z)/den(z)`) affect closed‑loop stability?** The video assumes linear behavior; any non‑linearities in the Test Rig could invalidate the observer’s gain calculation.  
4. **Is the `Gain_observer_discrete.m` function fully compatible with future TwinCAT ML revisions?** If Beckhoff updates the export schema, will this MATLAB function need modification?  

--- 

*Prepared from the transcript of **Controller_ADRC.mkv** and the selected reference snapshots (00:21:02 & 00:36:22). All technical conclusions are derived solely from the supplied evidence.*
