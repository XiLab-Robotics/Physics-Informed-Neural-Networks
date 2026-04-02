# TwinCAT/TestRig Video Guide - Automatic_Exp_TE.mp4

## Source Reference

* Canonical source video: [automatic_exp_te.mp4](../../../../reference/video_guides/source_bundle/automatic_exp_te.mp4)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

This video explains how the TestRig automates a transmission-error experiment
across multiple operating conditions. The emphasis is on orchestration:

* building the experiment matrix;
* mapping matrix columns into the experiment variables;
* keeping a fixed vector width;
* tracking which runs have already been executed;
* excluding operating points that are known to excite resonance.

It is therefore most useful as an experiment-automation reference, not as a
standalone proof of the internal ML-runtime implementation.

## Why This Video Matters

* **Automation discipline**: shows how a large TE experiment campaign is turned
  into a repeatable TwinCAT/TestRig procedure.
* **Coverage interpretation**: clarifies that experiment selection is shaped by
  stability constraints, not only by the ideal Cartesian product of variables.
* **Safety realism**: the narration explicitly states that the rig still
  requires human monitoring even in the automated mode.

## Main Technical Findings

| Topic | Detail |
| --- | --- |
| **Automatic experiment matrix** | The first columns of the matrix are described as speed, torque, and temperature. The matrix is then assigned row by row to the experiment variables. |
| **Fixed-width structure** | The narration describes the experiment vectors as staying at a fixed width even when the user changes how many parameters are actively varied. |
| **Executed/not-executed flag** | An additional boolean-like column is used to record whether a run has already been executed. |
| **1200 rpm exclusion** | The walkthrough states that the 1200 rpm case was excluded because resonance had been observed previously in that operating condition. |
| **Operator supervision** | The system is automated, but not considered self-supervising from a safety standpoint; the user is expected to remain nearby and listen for anomalies. |

## TwinCAT And Deployment Implications

1. **Experiment coverage must respect stability boundaries**
   A future campaign generator should preserve the ability to exclude unstable
   operating points explicitly, rather than assuming every point in the grid is
   safe to execute.

2. **Keep the matrix semantics explicit**
   When new variables are added, the column mapping and fixed-width convention
   should be updated intentionally instead of relying on informal assumptions.

3. **Treat completion flags as first-class orchestration state**
   The executed/not-executed marker is part of the experiment contract and
   should stay inspectable in any future automation refresh.

4. **Do not confuse automation with safety autonomy**
   The video explicitly separates automatic sequencing from true safety
   monitoring. That distinction should remain visible in future tooling.

## Reference Snapshots

| Time | Concept | Snapshot Description |
| --- | --- | --- |
| 00:01:15 | Experiment variables and matrix-driven setup | View associated with the operating-variable assignment used by the automatic run logic. |
| 00:11:14 | Runtime orchestration context | TwinCAT/TestRig screen used to anchor the orchestration discussion. |
| 00:15:20 | Variable preparation and run status | View associated with the prepared values and executed-run bookkeeping. |

## Open Questions Or Uncertain Points

1. **Exact final column count rationale**
   The narration reinforces the fixed-width convention, but does not fully
   justify the chosen final vector size.

2. **Flag update ownership**
   The video makes the executed/not-executed flag visible, but does not fully
   prove whether it is written automatically by the experiment code or updated
   by a surrounding layer.

3. **Detailed safety interlocks**
   The operator-monitoring requirement is clear, but the full safety-interlock
   implementation is not explained in this walkthrough.
