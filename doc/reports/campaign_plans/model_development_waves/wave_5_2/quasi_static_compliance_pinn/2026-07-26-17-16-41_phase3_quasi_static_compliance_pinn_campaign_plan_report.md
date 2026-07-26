# Phase 3 Quasi-Static Compliance PINN Campaign Plan

## Overview

This preliminary report defines the bounded Wave 5.2 Phase 3 campaign for
quasi-static compliance and elastic-offset PINNs. It follows the automatically
approved technical document:

- `doc/technical/2026-07/2026-07-26/2026-07-26-17-14-40_phase_3_quasi_static_compliance_pinn.md`

The campaign tests whether a positive, bounded, inspectable stiffness law can
improve held-out curve offset and raw error beyond an otherwise equivalent
periodic-plus-offset control. It does not inherit nonzero Phase 2 physics
weights.

The user's standing approval covers this plan, preparation, preflight,
training, closeout, and the Phase 3 commit through
`2026-07-26T22:37:56+02:00`.

## Scope

- program phase: Wave 5.2 Phase 3;
- dataset: `polished_dataset`;
- input mode: causal operating setpoints plus output angle and direction where
  required;
- dataset schema: `polished_setpoint_curve_v1`;
- eligible paired conditions: `966`;
- exact split: `675` train, `194` validation, `97` test per direction;
- directional surfaces: separate `Fw` and `Bw`;
- joint surface: one paired `global` control and one paired `global`
  shared-stiffness arm;
- planned run count: `12`;
- point stride: uniform `8`;
- curve batch size: `4`;
- maximum retained points per curve: `4,096`;
- synthetic compliance collocation points per batch: `64`;
- optimization ceiling: initially `20` epochs with patience `5`;
- execution: repository-owned local or `-Remote` launcher;
- heavy official TE Curve Verification Pipeline: excluded from normal
  closeout.

The three Phase 0 metadata anomalies remain quarantined. All directional arms
must reuse the exact common split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
The joint arms must prove that the same condition IDs are used for both
directions without cross-split leakage.

## Entry Audit

Real training is blocked until a persisted Phase 3 audit establishes:

- torque sign and magnitude support by direction and split;
- oil-temperature support and torque-temperature correlation;
- curve-mean and harmonic-zero surfaces;
- low- or zero-torque availability;
- repeated-condition support;
- load-unload and reversal observability;
- parameter identifiability for each proposed stiffness law;
- a leakage-safe paired-direction loader for joint arms.

The audit may mark load-unload consistency as unobservable. It may not invent
ordered trajectories or derive a runtime input from held-out TE targets.

## Physical Formulations

For signed torque `tau`, oil temperature `T`, direction `d`, and positive
effective stiffness `k`, the primary physical relation is:

```text
e_elastic(tau, T, d) = tau / k(T, d)
```

The campaign will test:

| Role | Formulation | Surface |
| --- | --- | --- |
| `PINN-C0` | learned periodic-plus-offset control; no compliance equation | `Fw`, `Bw`, `global` |
| `PINN-C1` | bounded positive linear direction-specific stiffness | `Fw`, `Bw` |
| `PINN-C2` | bounded positive temperature-conditioned stiffness | `Fw`, `Bw` |
| `PINN-C3` | positive linear compliance plus bounded odd nonlinear response | `Fw`, `Bw` |
| `PINN-C4` | hard elastic offset plus learned zero-mean periodic residual | `Fw`, `Bw` |
| `PINN-C5` | shared positive stiffness plus explicit direction intercepts | `global` |

`PINN-C0` is not a full PINN. `PINN-C1` through `PINN-C5` qualify as
physics-informed candidates only when their explicit law or target-free
physical constraints are active and persisted in the run artifacts.

## Physics And Boundary Tests

Deterministic preflight must prove:

- every stiffness parameter remains finite, positive, and within configured
  bounds;
- linear compliance is exactly odd in signed torque when its intercept is
  disabled;
- zero torque produces zero elastic deflection for `C1` through `C4`;
- `C3` remains monotonic throughout the audited torque range;
- `C2` remains positive throughout the audited temperature range;
- `C4` periodic residual has numerically zero curve mean;
- `C5` shares stiffness while exposing separate direction intercepts;
- enabled physics terms backpropagate finite nonzero gradients;
- target TE is absent from inference and collocation inputs.

## Fair-Comparison Controls

All comparable arms will share:

- exact eligible-condition manifests;
- causal inputs and normalization;
- point sampling, batching, optimizer, epoch ceiling, and checkpoint policy;
- matched condition-trunk and periodic-head capacity;
- deterministic seeds;
- raw and curve-first evaluation code.

The accepted periodic MLP and GRU remain external non-windowed and
time-windowed references. Phase 2 candidates remain historical evidence and
are not promoted into this phase.

## Training And Resource Bounds

The first pass will use:

- float32 training;
- one seed per arm for the screening campaign;
- low physical pressure for `C1` through `C5`;
- checkpoint selection on validation raw/offset behavior without using test
  curves;
- at most `20` epochs and patience `5`;
- persisted runtime and trainable-parameter counts.

Repeat seeds are authorized only for an arm that passes the initial
multi-index gate and shows potentially stable stiffness. No blind weight grid
is permitted before that gate.

## Selection Policy

Scalar leaderboard rank is diagnostic only. The phase decision requires:

- raw MAE and RMSE;
- signed and absolute curve-mean error;
- centered-shape MAE;
- peak-to-peak, harmonic-amplitude, and circular-phase fidelity;
- positive-stiffness and monotonicity pass rates;
- parameter range and initialization sensitivity;
- temperature-held-out and condition-held-out transfer;
- direction-specific and global behavior;
- compute and TwinCAT inspectability.

A formulation advances only if it improves held-out offset behavior and raw
error without a material centered-shape or harmonic regression, while its
stiffness-like parameters remain positive, bounded, stable, and predictive
outside fitting conditions.

## Planned Execution Package

Preparation will create:

- Phase 3 audit script, artifacts, report, and validator;
- model and deterministic equation validator;
- model report;
- campaign manifest and twelve queue-source YAML files;
- persistent queue and active-campaign state;
- dedicated PowerShell launcher with local, `-Remote`, and preflight modes;
- launcher note with exact commands;
- per-arm validation-check artifacts.

The remote path will reuse
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` and will
synchronize source, configuration, technical and planning documentation before
execution. It will synchronize campaign outputs, per-run artifacts, queue end
state, registries, and status artifacts after completion.

## Closeout Requirements

Normal closeout must produce:

- `campaign_leaderboard.yaml`;
- `campaign_best_run.yaml`;
- `campaign_best_run.md`;
- family and program registry updates;
- a Markdown and validated styled PDF campaign-results report;
- a bounded common-split curve-first comparison;
- synchronized active-campaign state, backlog, master summary, and ledger;
- an explicit Phase 3 pass or negative-result decision.

The official heavy TE Curve Verification Pipeline remains a separate optional
post-closeout step.

## Approval Gate

**Automatically approved.**

The technical document and this campaign plan are approved under the user's
standing ten-hour authorization. Training remains conditionally gated by the
persisted Phase 3 entry audit and queue-item preflights.
