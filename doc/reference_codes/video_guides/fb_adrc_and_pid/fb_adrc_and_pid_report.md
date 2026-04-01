# FB_ADRC_and_PID.mp4 Report

## Overview  

The video **FB_ADRC_and_PID.mp4** demonstrates the use of a TwinCAT ML‑generated function block (GRC) that implements an ADRC/PID controller. The block is part of a degree‑3 PLC system and is exported from TwinCAT as executable code. It is then integrated into Beckhoff’s **TestRig** environment, where it receives input variables defined as *reference* types (`PG`) and produces output values stored in storage registers of type `G`. The workflow is visualised through a series of screen captures (snapshot 00:11:00, 00:01:13, 00:08:36, 00:20:43) that show the deployment process and a recurring “Property Value A Search Error List Project File Line” message.  

---

## Why This Video Matters  

Understanding this video is essential for anyone tasked with exporting TwinCAT ML functions to Beckhoff TestRig, because it reveals:

* The **ML‑exported GRC block** structure (degree 3, linear filter, closed‑loop omega).  
* How **reference variables (`PG`)** are used as model input/output assumptions.  
* Where the **deployment pipeline** fails – a property‑value search error that points to missing project‑file lines.  

These insights directly affect code adaptation and integration testing.

---

## Main Technical Findings  

| Finding | Evidence |
|---------|----------|
| The GRC block is a degree‑3 function block with an internal linear filter and a closed‑loop omega variable. | Transcript: “la function block della GRC ha una function block realizzata per effettuare un controllo … è stato utilizzato una diari lineare, per cui non è comu” |
| A Boolean flag (`omega`) disables the lock; when false it only returns the response value. | Transcript: “Se è falsa, vuoi dire che il sistema è disabilitato? Per l'asse che registra solo valori di true …” |
| Two storage registers of type **G** store the reference values (PG). | Transcript: “Ci vedete che si chiamano i due memorizzatori, quindi i tipi G e gli stessi, questo perché perchè prima e tutto ci sono quali PG …” |
| The model assumes `PG` variables as inputs and outputs; any deviation triggers a property‑value search error. | Snapshot OCR (00:11:00, 00:01:13, etc.): “Property Value A Search Error List Project File Line”. |

---

## TwinCAT And Deployment Implications  

* **TwinCAT ML Export** – The GRC block is compiled as a native executable that must be placed in the TwinCAT project file. Missing lines cause the “Property Value A Search Error” shown in TestRig screenshots.  
* **Beckhoff Tooling Integration** – TestRig expects inputs of type `PG` and outputs stored in `G`. The code‑adaptation step is to map these types correctly; otherwise the block will not be instantiated.  
* **Closed‑loop omega handling** – When `omega = false`, the controller bypasses lock logic, returning only a raw value. This must be reflected in test scripts that interpret the output.  

---

## Reference Snapshots  

The following screen captures are used as reference points for the deployment workflow:  

* **00:11:00** – Shows the GRC block within the TwinCAT project tree.  
* **00:01:13** – Displays a property‑value search dialog (error line).  
* **00:08:36** – Highlights the storage registers (`G` type) in TestRig.  
* **00:20:43** – Indicates the “Property Value A Search Error List Project File Line” message again, confirming a missing project‑file entry.  

These snapshots are conceptually linked to the transcript timestamps and illustrate where the ML export meets the TestRig environment.

---

## Open Questions Or Uncertain Points  

1. **Disabling behavior** – Is the GRC block truly disabled when `omega = false`, or does it merely return a value? The transcript is ambiguous.  
2. **Linear filter role** – Does the linear filter belong to the ML‑generated code, or is it an external configuration? Clarifying this will affect how the export is validated.  
3. **Project‑file line source** – The repeated “Property Value A Search Error List Project File Line” suggests a missing line; however, the transcript does not specify which line number or property is required.  

Addressing these points will ensure robust TwinCAT ML → TestRig integration and prevent future deployment failures.
