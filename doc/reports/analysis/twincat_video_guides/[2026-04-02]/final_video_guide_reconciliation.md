# Final Video Guide Reconciliation

## Scope

This note records the final reconciliation pass performed after rerunning the
canonical `reference/video_guides/source_bundle/` through the strongest
validated repository pipeline:

* remote `lan_ai_node_server.py`;
* remote `faster-whisper` with `large-v3`;
* remote `LM Studio`;
* remote `openai/gpt-oss-20b` for cleanup and report synthesis;
* local OCR fallback.

The goal of this pass was not to replace the promoted guide tree blindly, but
to decide whether the newer rerun was actually better than the canonical
artifacts already stored under `doc/reference_codes/video_guides/`.

## Outcome

The recheck rerun completed successfully for all `8` unique source videos in
`reference/video_guides/source_bundle/`.

However, the rerun outputs were **not promoted wholesale** into the canonical
guide tree.

The comparison showed a repeated pattern:

* the new rerun often preserved additional local detail in the raw cleaned
  transcript;
* the new rerun reports were generally more generic and less curated than the
  current canonical reports;
* some rerun outputs reintroduced duplication, weaker segmentation, or softer
  fact boundaries.

The correct repository action was therefore:

* keep the canonical promoted guide tree as the baseline;
* selectively merge confirmed corrections into the canonical notes;
* push newly confirmed implementation details into the TwinCAT/TestRig
  reference notes.

## Per-Video Reconciliation Judgment

| Slug | Recheck judgment | Canonical action |
| --- | --- | --- |
| `automatic_exp_te` | Recheck transcript confirms experiment-matrix details, operator monitoring, and the 1200 rpm resonance exclusion more clearly. Recheck report is too generic. | Keep canonical transcript and report structure. Merge the stronger experiment-matrix facts into the reference notes. |
| `controller_adrc` | Recheck transcript clarifies `omega close loop`, `b0`, `keso`, and the Simulink-to-`TC-COM` path. Recheck report overstates some export specifics. | Keep canonical guide set, but tighten the canonical report around `TC-COM` and parameter semantics. |
| `fb_adrc_and_pid` | Recheck output is close in meaning but does not materially improve the canonical report. | Keep canonical artifacts unchanged. |
| `machine_learning_1` | Recheck remains useful for Beckhoff Model Manager and XML/BML packaging, but the canonical version is already the better engineering summary. | Keep canonical artifacts unchanged. |
| `machine_learning_2` | Recheck transcript reinforces state-100 preload logic, task-begin communication delay, and the 4-column CSV experiment contract. Recheck report is less reliable than the canonical report. | Keep canonical artifacts, but correct the canonical report where it overreached into direct ONNX assumptions and oversimplified the CSV/input mapping. |
| `ml_simulation_and_generator_cam` | Recheck transcript is valuable for CSV semantics, cycle-time assumptions, and the GBR/SVR harmonic split. Recheck report again overstates direct ONNX/TwinCAT coupling. | Keep canonical artifacts, but tighten the canonical report around Beckhoff packaging, `TE_Calc`, and replay semantics. |
| `overview_test_rig` | Recheck does not outperform the canonical promoted version. | Keep canonical artifacts unchanged. |
| `video_errata_corrige_adrc` | Recheck stays aligned with the canonical errata understanding and does not justify a full replacement. | Keep canonical artifacts unchanged. |

## Canonical Corrections Applied

This reconciliation pass corrected the canonical bundle where the earlier
promoted reports were too speculative.

The main changes were:

* `machine_learning_2_report.md`
  * removed the direct "raw ONNX to PLC runtime" framing;
  * clarified that the video is mainly useful for task structure, state-100
    preload logic, CSV-fed orchestration, and delay budgeting;
  * aligned the deployment implications with the Beckhoff XML/BML plus
    `FB_MllPrediction` path already confirmed from imported code.
* `ml_simulation_and_generator_cam_report.md`
  * removed the direct ONNX/TwinCAT-runtime claim;
  * emphasized CSV replay semantics, harmonic model family split, and
    `TE_Calc` as a TwinCAT-side boundary variable.
* `controller_adrc_report.md`
  * replaced the unsupported `.tccode` export framing with the
    Simulink-to-`TC-COM` interpretation supported by the video;
  * clarified the meaning of `omega close loop`, `b0`, and `keso`.
* `automatic_exp_te_report.md`
  * reduced unsupported ADRC/ML-runtime specificity;
  * centered the guide on experiment-matrix construction, fixed vector shape,
    execution flagging, operator monitoring, and the skipped 1200 rpm case.

## Cross-Video Facts Strengthened By The Recheck

The recheck materially reinforced these implementation-facing conclusions:

* the machine-learning path is orchestrated by experiment logic rather than by
  a free-running predictor service;
* state `100` is used to preload the slow-shaft torque to the first CSV torque
  target before the experiment proper starts;
* the CSV-driven experiment path in `Machine_Learning_2` uses four key columns:
  time, position, torque, and velocity;
* torque in that CSV contract is expected with the sign convention shown in the
  video, namely negative torque for the positive-velocity case used there;
* inter-task communication delay is treated in the videos as a real correction
  budget and not as a zero-latency handoff;
* the automatic-experiment matrix uses fixed-width vectors plus an executed/not
  executed flag;
* the 1200 rpm case was intentionally excluded from one automated campaign
  because resonance had been observed previously;
* the ADRC workflow depends on three exposed tuning quantities:
  `omega close loop`, `b0`, and `keso`;
* the ADRC simulation path shown in the videos is tied to a local
  Simulink-to-`TC-COM` integration route, not to a generic drop-in PLC export;
* `TE_Calc` must remain a TwinCAT/TestRig-side semantic boundary and cannot be
  treated as a direct Matlab placeholder.

## Final Canonical Decision

The canonical guide tree under `doc/reference_codes/video_guides/` should stay
as the repository baseline.

The stronger recheck rerun was still worth doing, because it:

* confirmed that the current baseline is preferable to a naive re-promotion;
* exposed the specific reports that needed de-speculation;
* provided stronger evidence for implementation-facing TwinCAT/TestRig facts.

That combination is the right end state for repository use:

* canonical per-video guides remain readable and curated;
* reference notes absorb the deeper confirmed findings;
* temporary rerun artifacts can be discarded once the merge is complete.
