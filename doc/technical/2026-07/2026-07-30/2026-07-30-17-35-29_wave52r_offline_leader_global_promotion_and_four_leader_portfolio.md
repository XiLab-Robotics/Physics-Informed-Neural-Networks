# Wave 5.2R Offline Leader Global Promotion And Four-Leader Portfolio

Approval and execution status: approved by the user on `2026-07-30`. The
local replay, causal, state, export-parity, and host-latency qualification gates
passed for both K01 and H08. The separate cross-surface campaign completed
`27 / 27` runs with zero failures on `2026-07-31`; official curve-first
promotion closed on `2026-07-31`: K01 passed as the cross-surface temporal
offline leader, while H08 remained a forward specialist and did not pass the
backward/global gate. Both non-PINN incumbents remain unchanged.

## Overview

This project will determine whether the two new Wave 5.2R forward offline
leaders can be promoted beyond diagnostic status while preserving the two
current non-PINN operational references:

- temporal Wave 5.2R leader: `wave52r_stage9_k01`;
- non-temporal Wave 5.2R leader: `wave52r_stage5_h08_seed_314159`;
- incumbent temporal reference: `periodic_gru_sequence`;
- incumbent non-temporal reference: `periodic_mlp_harmonic`.

No incumbent artifact, registry entry, or accepted decision will be deleted or
overwritten. If K01 and H08 pass all applicable gates, the intended outcome is
a four-leader portfolio: two Wave 5.2R physics-guided research leaders and two
established non-PINN operational leaders.

K01 and H08 are currently forward-only (`Fw`) checkpoints. Their existing
evidence cannot establish backward (`Bw`) or combined (`global`) leadership.
The work therefore separates forward deployment qualification from later
cross-surface promotion. A global claim is allowed only after matched global
and backward training, direction-separated curve verification, and deployment
acceptance.

This plan also records a near-term future TODO: investigate an integrated
empirical multi-component model that combines the strongest verified
ingredients from K01, H08, F01, S01, H04, Stage 10 R00, and Stage 10 S01. That
future branch must preserve causal inference, keep intermediate quantities
inspectable, and demonstrate that the combination reduces the known defects
instead of merely averaging incompatible predictors. It is not authorized for
implementation or training by this document.

## Technical Approach

### Gate A: Artifact And Contract Audit

Freeze checkpoint hashes, model definitions, parameter counts, training
configuration, split signature, angular grid, input normalization, causal
inputs, and saved prediction provenance for K01 and H08. Reconstruct the
forward test predictions from each checkpoint and compare them with the saved
`test_predictions.npz` payload.

K01 must retain deterministic hidden-state initialization, reset
reproducibility, causal prefix behavior, and declared chunk behavior. H08 must
retain its explicit harmonic-order list, coefficient reconstruction, bounded
correction behavior, and zero target-derived runtime inputs.

### Gate B: Forward Numerical And Causal Acceptance

Run both candidates on the frozen 97-curve forward test surface and exercise:

- checkpoint-to-payload replay parity;
- repeated-run determinism and finite-output checks;
- causal-prefix and no-future-information tests;
- reset, state carry, and chunk-boundary tests for K01;
- coefficient, harmonic reconstruction, closure, and saturation tests for H08;
- operating-band, tail, worst-condition, and invalid-input stress tests;
- raw error, centered shape, offset, closure, derivative, harmonic amplitude,
  harmonic phase, P95, and worst-curve metrics.

The accepted forward periodic GRU and periodic harmonic MLP remain mandatory
controls. F01, S01, H04, Stage 10 R00, and Stage 10 S01 remain diagnostic
specialists and are not silently removed from the evidence surface.

### Gate C: Export, Parity, Runtime, And PLC Preparation

Create standalone, immutable export packages for K01 and H08 only after their
Python replay contracts pass. Reuse the repository's Stage 15 H04 parity
discipline:

- compare Python checkpoint, portable export runtime, and independent
  PLC-reference computation on the same frozen payload;
- require no non-finite values and identical validity, envelope, saturation,
  and fallback flags;
- use the established reconstructed-TE tolerance of `2e-6 deg` unless a
  stricter model-specific threshold is practical;
- preserve explicit intermediate quantities where the model exposes them.

For H08, the preferred PLC-facing form is the inspectable coefficient network
plus explicit harmonic reconstruction. For K01, the first deliverable must
define a causal stateful streaming interface, including hidden-state reset,
state carry, sequence start, chunk boundaries, and output timing. A batch
full-curve export that depends on future samples does not satisfy the
deployment gate.

Benchmark Python and portable-runtime latency, memory, model size, and
worst-case execution distribution. These measurements are preparation
evidence, not TwinCAT runtime evidence. Actual deployment acceptance still
requires compilation and replay in the repository-owned TF3820 or documented
TestRig path, with the `500 us` ML-task context treated as a target rather than
an assumed pass.

Encoder zeroing, signed torque, speed, oil temperature, direction, angular
position, and `DataValid` semantics must remain explicit throughout replay and
PLC preparation.

### Gate D: Conditional Global And Backward Campaign

Only candidates that pass Gates A through C may enter a matched cross-surface
campaign. The campaign will train K01-family and H08-family variants on:

- `Fw`, as a reproducibility control;
- `Bw`, as a distinct directional surface;
- `global`, with direction retained explicitly.

The campaign must use multiple declared random seeds, immutable
`run_instance_id` directories, frozen train/validation/test splits, no
target-derived runtime inputs, and the same setpoint contract as the incumbent
comparison unless a separately approved sensitivity lane is added.

The existing periodic GRU and periodic harmonic MLP global and directional
artifacts remain frozen controls. Promotion requires a later official
direction-separated TE Curve Verification Pipeline refresh reporting `global`,
`Fw`, and `Bw` independently. A strong global aggregate may not hide a failed
direction.

### Gate E: Four-Leader Decision

The final decision will distinguish:

- offline curve leader;
- export-prepared candidate;
- runtime-qualified candidate;
- accepted deployable leader;
- accepted `Fw`, `Bw`, and `global` surface leader.

If K01 and H08 pass, they join rather than replace the incumbent periodic GRU
and periodic harmonic MLP. If either fails, its failure mode remains recorded
and the incumbents remain unchanged.

### Future Integrated-Model TODO

After the promotion work, prepare a separate technical roadmap for an
integrated empirical multi-task or mixture-of-experts design. The design study
must map each candidate to a specific reusable strength:

- K01: temporal context, raw error, and offset behavior;
- H08: balanced non-temporal harmonic and phase fidelity;
- F01: centered-shape fidelity and P95 robustness;
- S01: harmonic amplitude and phase specialization;
- H04: inspectable structured grey-box coefficient path;
- Stage 10 R00: low non-temporal raw error;
- Stage 10 S01: non-temporal tail robustness.

The study must also map and explicitly guard against each known weakness,
including temporal state complexity, single-seed fragility, worst-curve
behavior, harmonic collapse, phase degradation, and deployment cost. Candidate
architectures may include shared causal trunks, specialist heads, residual
composition, gated mixtures, constrained arbitration, or distillation, but no
architecture is preselected and no physics-integrated Wave 6 claim is made
without satisfying its existing entry rules.

## Involved Components

Current candidate evidence:

- `output/training_runs/temporal_analytical_residual_models/`
  `2026-07-29-19-21-15__stage9_k01/`;
- `output/training_runs/complex_harmonic_coefficient_residuals/`
  `2026-07-28-16-17-15__stage5_h08/`;
- `output/analysis/wave_5_2r/full_candidate_track2_analysis/`;
- the dated Wave 5.2R official Track 2 report and its curve-first diagnostics.

Expected implementation surfaces after approval:

- dedicated validation scripts under `scripts/analysis/wave_5_2r/`;
- export and PLC-reference tooling under `scripts/export/wave_5_2r/` and
  `scripts/deployment/`;
- immutable validation artifacts under
  `output/validation_checks/wave52r_offline_leader_promotion/`;
- a campaign manifest under `config/training/` if Gate D is reached;
- a dedicated local and `-Remote` PowerShell launcher under
  `scripts/campaigns/wave_5_2/`;
- a matching launcher note under `doc/scripts/campaigns/wave_5_2/`;
- a campaign-results Markdown/PDF bundle if cross-surface training occurs;
- a later operator-launched TE Curve Verification Pipeline package;
- synchronized backlog, master summary, closeout ledger, guide, and Sphinx
  portal entries after evidence changes.

The current active-campaign record is completed. Its protected Stage 13 files
will not be modified. No subagents are planned. Any later subagent proposal
must name the agent, reason, and exact scope and receive explicit user approval
before launch.

## Implementation Steps

1. Create and register this technical document and the preliminary campaign
   planning report.
2. Wait for explicit user approval of both documents.
3. Audit K01 and H08 checkpoint provenance, saved payloads, model contracts,
   split identity, causal inputs, and reproducibility.
4. Implement deterministic checkpoint replay and candidate-specific causal,
   reset, chunk, coefficient, harmonic, and invalid-input tests.
5. Run the complete forward Gate A and Gate B suite against both incumbents and
   preserve all specialist evidence.
6. If the Python gates pass, prepare standalone exports and frozen parity
   payloads for K01 and H08.
7. Run portable-runtime parity, latency, memory, model-size, and fallback
   tests; prepare but do not overclaim PLC evidence.
8. Produce a dated promotion-readiness report with an explicit pass, fail, or
   conditional result for each candidate.
9. If either candidate qualifies for cross-surface training, prepare the
   approved campaign YAML, local/remote launcher, launcher note, and active
   campaign state before execution.
10. Wait for the operator-launched campaign to complete, then perform normal
    campaign closeout with Markdown and validated PDF results.
11. Prepare a separate global/Fw/Bw TE Curve Verification Pipeline launcher,
    wait for operator completion, and evaluate each surface independently.
12. Decide whether K01 and H08 join the two incumbents in the four-leader
    portfolio; never delete or overwrite incumbent evidence automatically.
13. Synchronize the future-work roadmap with the integrated-model TODO and its
    ingredient/defect map.
14. Run Python, Markdown, PDF, Sphinx, path, launcher, package, and Git diff
    validation as applicable, then stop before any commit.

No implementation, test execution, training, registry promotion, or commit is
authorized until the user explicitly approves this document and the companion
campaign plan.
