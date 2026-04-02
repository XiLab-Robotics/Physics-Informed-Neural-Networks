# TwinCAT/TestRig Video Guide - Machine_Learning_2.mp4

Report type: `Technical Report (Engineering-Focused)`

---

## Source Reference

* Canonical source video: [machine_learning_2.mp4](../../../../reference/video_guides/source_bundle/machine_learning_2.mp4)
* Source bundle manifest: [source_manifest.json](../../../../reference/video_guides/source_bundle/source_manifest.json)

## Overview

The second machine-learning video is mainly about PLC-side orchestration rather
than offline model training. It explains how the TestRig experiment uses a
dedicated ML-related task, how the experiment reads CSV-driven trajectories,
and how state `100` preloads the slow shaft before the real experiment starts.

The strongest engineering value of this video is therefore:

1. the split between a fast task and a `500 us` ML-related task;
2. the practical delay budget introduced by task-begin I/O exchange;
3. the CSV contract used by the experiment path;
4. the preload logic used to start an already-loaded experiment condition.

## Why This Video Matters

* **Task-level realism**: shows that ML inference is not free-standing, but
  inserted into a multi-task PLC workflow with real communication delay.
* **Experiment contract clarity**: makes the CSV-fed experiment path more
  concrete than the imported code alone.
* **Deployment relevance**: reinforces that future TE models must be judged
  against TwinCAT task timing and experiment-state behavior, not only offline
  accuracy.

## Main Technical Findings

| Item | Detail |
| --- | --- |
| **Task structure** | The walkthrough repeatedly distinguishes a fast task from a dedicated ML-related task around `500 us`. The point is not just scheduling; it is that prediction and compensation live inside a controlled inter-task exchange. |
| **Communication delay budget** | The narration explicitly treats task-begin I/O exchange as a real delay source that must be considered when applying correction. The important takeaway is qualitative: correction timing must include handoff latency between tasks. |
| **Experiment CSV contract** | The video states that the experiment-side CSV uses four key columns: time, position, torque, and velocity. It also states the sign convention used for torque in the shown experiment path. |
| **State-100 preload logic** | State `100` reads the first torque value from the CSV. If that first target is nonzero, the slow shaft is preloaded to that target before the experiment continues. The narration also describes a stability window around the reached value before the next phase starts. |
| **Machine-learning orchestration** | The video is consistent with the imported code in showing that the ML path is embedded in `P_Experiment_Cam_Correction_TE_ML`-style logic rather than being a detached predictor service. |
| **Beckhoff runtime boundary** | This video is useful for tasking and orchestration, but it is not the right source to claim a raw ONNX-to-PLC runtime path. The imported TwinCAT code still confirms the Beckhoff XML/BML plus `FB_MllPrediction` path as the current deployed runtime. |

## TwinCAT And Deployment Implications

1. **Keep the task budget explicit**
   Future TE models must fit the practical ML-task budget and the associated
   handoff timing. The video makes it clear that communication delay is part of
   the runtime contract.

2. **Treat state logic as part of the deployment**
   A future exported model cannot assume a stateless "predict one row" runtime.
   The preload sequence in state `100` is part of the real experiment behavior.

3. **Preserve the CSV-side contract**
   Any future automation around replay or compensation should keep the
   experiment-side CSV schema and sign conventions explicit, not implicit.

4. **Do not collapse packaging layers**
   The imported code still points to Beckhoff-specific model artifacts and
   `FB_MllPrediction`. This video does not overturn that reading; it complements
   it by clarifying orchestration.

## Reference Snapshots

| Timestamp | Concept | Snapshot Description |
| --- | --- | --- |
| 00:01:15 | Task timing and inter-task communication | Project-tree view that anchors the discussion around task exchange and ML-related execution. |
| 00:06:11 | Fast task versus ML task | TwinCAT task view showing the fast task and the `500 us` ML-related task in the same runtime context. |
| 00:11:10 | Experiment orchestration | PLC-side experiment logic surrounding the ML path and correction flow. |
| 00:15:36 | CSV-fed experiment setup | View associated with the CSV-driven experiment path and its runtime triggers. |

## Open Questions Or Uncertain Points

1. **Exact delay value**
   The narration gives a timing figure, but the transcript quality is not strong
   enough to treat the exact numeric value as canonical. The important fact is
   the presence of a nonzero delay budget.

2. **Exact CSV-to-feature mapping inside the predictor**
   The video makes the experiment CSV contract clearer, but the final predictor
   feature vector should still be grounded primarily in the imported PLC code.

3. **Error handling on missing CSV data**
   The walkthrough focuses on the happy path and does not show explicit runtime
   recovery for missing or malformed experiment files.

4. **Scaling and normalization**
   The video does not clearly establish whether additional scaling occurs before
   the deployed predictor receives its final inputs.
