# Remote High-Quality TwinCAT Video Campaign Sum-Up

## Scope

This report summarizes the repository-owned remote-strong rerun that processed
the full current TwinCAT/TestRig media bundle with:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` using `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for transcript cleanup and report synthesis;
- local OCR fallback for snapshot evidence.

The rerun is the current strongest validated campaign for turning the TestRig
video bundle into canonical repository knowledge.

A later repository-owned comparison pass against the canonical source bundle is
recorded in:

- `doc/reports/analysis/twincat_video_guides/[2026-04-02]/final_video_guide_reconciliation.md`

## Campaign Outcome

The tracked campaign completed successfully for all `11` source videos listed in
`doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/remote_high_quality_video_rerun_status.json`.

Validated per-video stages completed for every video:

- transcript extraction;
- transcript cleanup;
- snapshot selection;
- OCR-backed evidence capture;
- transcript Markdown export;
- report Markdown export;
- Markdown validation.

The campaign outputs were first written into the tracked temporary roots and
then promoted into the canonical tree under
`doc/reference_codes/video_guides/`.

## Output Quality Assessment

### Overall Judgment

The remote-strong campaign is materially better than the earlier local-light
pass.

The main reasons are:

- `large-v3` handles spoken Italian technical terminology more robustly than the
  lighter local transcript path;
- `openai/gpt-oss-20b` produces more stable technical cleanup and better
  engineering summaries than the smaller local LM Studio models used for
  validation;
- per-video snapshots and OCR support keep TwinCAT/TestRig UI details anchored
  to real screen evidence instead of transcript-only inference.

### Transcript Quality

The strongest transcript value is concentrated in the videos that explain:

- ML export and Beckhoff Model Manager import;
- TwinCAT task structure and inter-task timing;
- CSV/vector preparation for simulation and experiment replay;
- TestRig startup, reset, homing, and driver-side configuration;
- ADRC export and correction workflow.

The cleaned transcripts are not perfect verbatim replacements for the original
Italian narration, but they are strong enough to extract implementation-facing
facts and to cross-check code assumptions.

### Snapshot And OCR Quality

The snapshot set is especially useful for:

- TwinCAT project tree views;
- function-block parameter panes;
- task configuration panels;
- TestRig variable/property sheets;
- model-manager or prediction-block setup screens.

OCR remains secondary evidence rather than a canonical source of truth. Its
main value is to recover labels, variable names, timestamps, and configuration
anchors from the selected frames.

### Report Quality

The English per-video reports are suitable as engineering reference notes,
provided they are read with explicit source boundaries:

- direct transcript evidence;
- OCR/snapshot evidence;
- repository inference.

They should not be treated as proof for details that are still better grounded
in the imported TwinCAT code.

## Per-Video Engineering Value

| Video Slug | Main Value For Implementation | Quality Judgment |
| --- | --- | --- |
| `machine_learning_1` | Beckhoff Model Manager import, XML multi-model concept, generated function-block shape, task timing | High |
| `machine_learning_2` | state-100 orchestration, CSV-fed inference flow, fast-task vs ML-task split, prediction-block runtime use | High |
| `testrig___machine_learning_1` | GVL/task coupling, `FB_Predict_*` structure, enable/reset/runtime flags | High |
| `testrig___machine_learning_2` | prediction block assumptions, task timing, compensation trigger logic, file-driven runtime flow | High |
| `overview_test_rig` | physical rig context, IndraDrive/TwinCAT setup, reset behavior, homing/zero patterns | High |
| `testrig___overview` | rig architecture, mode switching, driver synchronization, PLC startup context | High |
| `ml_simulation_and_generator_cam` | simulation-table semantics, `TE_Calc` caveat, replay/generator workflow, PLC-side post-processing hints | High |
| `video_errata_corrige_adrc` | correction of the `TE_Calc` misunderstanding, variable-mapping discipline, TestRig wiring caveat | High |
| `controller_adrc` | MATLAB to TwinCAT/TestRig export path for ADRC controllers and parameter persistence | Medium |
| `fb_adrc_and_pid` | ADRC/PID FB semantics, reset logic, deployment interpretation | Medium |
| `automatic_exp_te` | automated experiment matrix, fixed vector-size convention, completion-flag semantics | Medium |

## Cross-Video TwinCAT/TestRig Knowledge

### 1. Current ML Runtime Shape

Across the machine-learning videos and the imported PLC code, the same runtime
pattern appears consistently:

- a dedicated ML-related task around `500 us`;
- a faster task responsible for lower-level or drive-facing behavior;
- inter-task exchange through shared variables or data blocks;
- explicit enable/reset/load orchestration rather than opaque background
  inference.

This supports the repository assumption that future TE models must be judged not
only for offline accuracy, but also for cycle-level schedulability and
communication delay.

### 2. Feature And Simulation Semantics

The videos strengthen the practical meaning of the feature path around:

- speed;
- torque;
- temperature.

They also add simulation-side columns and replay semantics around:

- TE;
- absolute slow-shaft position;
- cumulative slow-shaft position;
- cumulative fast-shaft position.

This is important because future exported models must not ignore the fact that
TwinCAT/TestRig surrounding logic already performs part of the signal
preparation and reconstruction work.

### 3. Multi-Artifact Beckhoff Model Story

The video bundle reinforces the code-level conclusion that the deployed path is
not a generic “load one monolithic ONNX and run it” story.

Instead, the practical runtime involves:

- XML/BML-oriented Beckhoff model artifacts;
- model-manager conversion or loading steps;
- generated prediction function blocks;
- task and GVL wiring;
- experiment-side orchestration and harmonic or structured post-processing.

This strongly favors structured, inspectable model exports over opaque end-to-end
black-box deployment claims.

### 4. Experiment Orchestration Matters

The videos repeatedly show that the PLC-side experiment does more than simple
inference:

- CSV reading and first-row initialization;
- state-machine transitions such as state `100`;
- homing and zeroing;
- reset and error clearing;
- torque or position compensation branches;
- use of frozen or staged operating variables at experiment start.

This means a future model export must be designed against the experiment
contract, not only against a generic offline predictor signature.

### 5. `TE_Calc` Must Stay Explicit

The errata and simulation videos are especially important because they correct a
bad simplification:

- `TE_Calc` should not be treated as “the Matlab variable imported as-is”.

The video evidence instead supports the repository view that TwinCAT/TestRig
already owns part of the TE calculation or reconstruction path. That boundary is
critical for future code changes and model export decisions.

## Implementation Consequences For Future Models

The current campaign strengthens five repository-level implementation rules.

1. Prefer structured TE models that preserve explicit operating variables and
   inspectable intermediate quantities.
2. Treat TwinCAT export as a system-integration problem, not as pure model-file
   conversion.
3. Preserve compatibility with task-level timing and shared-variable
   communication constraints.
4. Keep the distinction explicit between:
   - offline TE prediction;
   - PLC-side harmonic or compensation reconstruction;
   - TestRig experiment orchestration.
5. Assume that future non-paper model families may require TwinCAT-side logic
   changes, not only a new exported artifact.

## Recommended Baseline

For future video-guided TwinCAT/TestRig knowledge extraction, the repository
should treat the remote-strong path as the current default baseline.

Recommended baseline:

- transcript: remote `large-v3`;
- cleanup: remote `openai/gpt-oss-20b`;
- report synthesis: remote `openai/gpt-oss-20b`;
- OCR: local fallback;
- execution mode: tracked one-video-at-a-time rerun launcher.

The local-only path remains useful for smoke tests and development validation,
but it should not be treated as the canonical knowledge-refresh path when the
remote workstation is available.

## Remaining Gaps

The campaign improved the repository’s practical understanding, but some gaps
remain:

- the exact offline pipeline that generated the Beckhoff XML/BML artifacts is
  still not fully reconstructed end-to-end from repository code alone;
- some per-video reports still contain engineering inference that should be
  confirmed against TwinCAT source when the detail becomes implementation
  critical;
- the exact variable mappings behind some simulation or ADRC screens remain
  partially implicit in the videos.

These are now narrower gaps than before the remote-strong campaign.
