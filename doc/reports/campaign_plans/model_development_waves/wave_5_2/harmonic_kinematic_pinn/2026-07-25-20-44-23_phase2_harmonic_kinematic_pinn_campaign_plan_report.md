# Phase 2 Harmonic And Kinematic PINN Campaign Plan

## Overview

This preliminary report defines the first real full-PINN campaign in the
Wave 5.2 sixteen-phase theory-validation program. It follows the automatically
approved technical document:

- `doc/technical/2026-07/2026-07-25/2026-07-25-20-40-44_phase_2_harmonic_kinematic_pinn.md`

The campaign tests one bounded physical proposition: whether explicit angular
oscillator and periodic-boundary residuals improve unseen-condition harmonic
fidelity over a parameter-matched Fourier-head control.

The user's time-bounded standing approval covered preparation, preflight,
training, closeout, and the phase commit. The canonical campaign subsequently
completed `8 / 8` runs.

## Scope

- program phase: Wave 5.2 Phase 2;
- dataset: `polished_dataset`;
- input mode: causal operating setpoints plus output angle;
- dataset schema: `polished_setpoint_curve_v1`;
- eligible paired conditions: `966`;
- common split: `675` train, `194` validation, `97` test;
- surfaces: separate `Fw` and `Bw`;
- global surface: deliberately excluded from the first causal physics test;
- planned run count: `8`;
- point stride: uniform `8` across every canonical restart arm; the Phase 0
  minimum audited curve of `10,799` rows retains at least `1,350` samples,
  more than `2.8` times the `480`-sample Nyquist minimum for order `240`;
- runtime-bounded batching: `4` curves per batch, a distributed cap of `4,096`
  points per curve, and `64` physics collocation points per batch;
- collocation coverage: at least `10,800` physics evaluations per epoch over
  the `675` training curves;
- optimization ceiling: `24` epochs with patience `5` and best-checkpoint
  reevaluation;
- execution: repository-owned local or `-Remote` launcher;
- official TE Curve Verification Pipeline: deferred until normal closeout.

The three Phase 0 metadata anomalies remain quarantined. Phase 2 must reuse the
Phase 1 split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.

The initial exact-split PINN arm required `144` seconds for one epoch while
using only about `38%` of the local GPU. That runtime audit is diagnostic only.
The canonical restart applies the bounded batching contract above uniformly to
all eight arms; it does not change the eligible conditions, causal inputs,
harmonic basis, loss weights, or acceptance rule.

## Physical Residual

For every configured output order `k`, the implicit component head
`h_k(theta, u)` is tested against

```text
R_k = (1 / k^2) * d2 h_k / d theta2 + h_k
```

where `u` contains only causal operating inputs. The normalized form prevents
high orders from dominating solely through derivative scale.

Optional boundary terms are:

```text
R_value = y(0, u) - y(2 pi, u)
R_slope = dy/dtheta(0, u) - dy/dtheta(2 pi, u)
```

`PINN-H3` also compares its condition-dependent harmonic coefficients with the
frozen Phase 1 local-order quadratic surface. That analytical anchor is a soft
ablation and cannot replace the oscillator residual when claiming a full PINN.

## Planned Arms

The queue will contain the same four roles for `Fw` and `Bw`.

| Role | Physics Terms | Purpose |
| --- | --- | --- |
| `PINN-H0` | none | parameter-matched Fourier-head control; explicitly not a full PINN |
| `PINN-H1` | normalized oscillator, low weight | test isolated governing-residual value |
| `PINN-H2` | oscillator plus value and slope closure | test stronger periodic kinematic consistency |
| `PINN-H3` | H2 plus frozen PF-A coefficient anchor | test analytical-plus-PINN guidance |

The primary harmonic order set is `1`, `3`, `39`, `40`, `78`, `81`, `156`,
`162`, and `240`. Deterministic preflight will also run one order-drop and one
inadmissible-order test without expanding the eight-run campaign.

## Fair-Comparison Controls

All arms will share:

- the same eligible-condition manifest;
- the same direction-specific split;
- the same angular collocation grid;
- the same causal operating features;
- comparable condition-trunk and head capacity;
- the same optimizer, epoch ceiling, early-stopping policy, and random seeds;
- identical scalar and curve-first evaluation code.

The accepted `periodic_gru_sequence` and `periodic_mlp_harmonic` candidates
remain external time-windowed and non-windowed references. They are not
retrained in this campaign.

## Training And Resource Bounds

The preparation will target:

- curve batch size chosen by one-batch memory validation;
- angular collocation subsampling that preserves every configured order;
- maximum `60` epochs;
- early stopping on a multi-index validation objective;
- physics weights limited to zero, low, and moderate pressure;
- float32 training unless second-derivative stability requires a documented
  precision change;
- deterministic seeds for the bounded comparison;
- explicit per-run compute-time and peak-memory artifacts.

The campaign may be reduced before launch if one-batch validation proves that
order `240` cannot be resolved under the proposed collocation or memory
contract. Such a reduction requires an updated plan and explicit approval.

## Required Preflight Evidence

Before real training, preparation must prove:

- exact sine and cosine heads give near-zero oscillator residual;
- an inadmissible order gives a nonzero residual;
- periodic value and derivative closure are numerically stable;
- first and second angular derivatives are finite;
- enabled physics terms backpropagate nonzero parameter gradients;
- `PINN-H0` has zero physics weight and is never labeled a full PINN;
- no target TE value enters the inference input or analytical anchor input;
- Fw and Bw conditions remain paired but direction-specific;
- all eight queue configs pass model-factory and one-batch validation;
- both local and `-Remote` launch paths pass preflight.

## Selection Policy

The scalar campaign leaderboard is diagnostic only. The Phase 2 exit decision
will combine:

- raw MAE and RMSE;
- centered-shape MAE;
- offset error;
- dominant-order amplitude error;
- circular phase error;
- spurious-harmonic energy;
- value and derivative closure;
- physics residual magnitude;
- data-versus-physics gradient cosine similarity;
- inference cost and deployment readiness.

A PINN arm may advance only if it improves held-out harmonic fidelity over
`PINN-H0` without a material regression in raw error, offset, or continuity.
If no arm passes, the campaign closes as a valid negative result and no
harmonic constraint is promoted.

## Planned Execution Package

After plan approval, preparation will create:

- campaign manifest under
  `config/training/harmonic_kinematic_pinn/campaigns/`;
- eight immutable queue-source YAML files;
- persistent queue and campaign state;
- dedicated launcher
  `scripts/campaigns/wave_5_2/run_phase2_harmonic_kinematic_pinn_campaign.ps1`;
- launcher note under `doc/scripts/campaigns/wave_5_2/`;
- local, local one-batch, remote preflight, and remote run commands;
- validation-check artifacts for every queue arm.

The launcher will reuse the repository remote-training infrastructure and
synchronize source, configuration, technical and planning documentation before
launch. It will synchronize campaign outputs, per-run artifacts, queue end
state, registries, and status artifacts after completion.

## Closeout Requirements

Normal closeout must produce:

- `campaign_leaderboard.yaml`;
- `campaign_best_run.yaml`;
- `campaign_best_run.md`;
- family and program registry updates where applicable;
- Markdown and validated PDF campaign-results report;
- synchronized active-campaign state;
- synchronized live backlog, master summary, and closeout ledger;
- explicit Phase 2 pass or negative-result decision.

## Runtime Restart Record

The initial local stride-`2` attempt is diagnostic only. It completed the
backward Fourier control and established that an implicit PINN epoch required
about 160 seconds. The attempt was stopped during the first implicit-PINN
epoch, without accepting that partial run.

The canonical campaign is
`phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26`. It reran
every control and PINN arm with uniform stride `8`; no earlier result is
eligible for its leaderboard or Phase 2 decision. The spectral sampling
margin and all causal, directional, loss, and split contracts remained
unchanged.

The user's time-bounded approval covers this restart from
`2026-07-26T12:37:56+02:00` through `2026-07-26T22:37:56+02:00`.

The heavy TE Curve Verification Pipeline is a separate optional step after
normal closeout. It must not run automatically with the campaign.

## Approval Gate

**Approved and completed.**

The campaign completed `8 / 8` runs with no failures. The bounded common-split
curve-payload closeout promoted no physical constraint and advanced the
roadmap to Phase 3.
