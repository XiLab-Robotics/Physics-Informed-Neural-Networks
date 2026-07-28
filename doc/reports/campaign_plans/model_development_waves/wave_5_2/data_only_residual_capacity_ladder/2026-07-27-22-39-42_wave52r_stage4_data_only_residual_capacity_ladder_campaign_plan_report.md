# Wave 5.2R Stage 4 Data-Only Residual Capacity Ladder Campaign Plan

## Overview

This preliminary report defines the first training campaign in the Wave 5.2R
polished-setpoint forward reassessment.

The campaign asks one deliberately non-physics question:

**How much of the qualified PF-A analytical error can a data-only residual
network learn before any physics-guided loss is added?**

The automatically approved technical document is:

- `doc/technical/2026-07/2026-07-27/2026-07-27-22-37-41_wave52r_stage4_data_only_residual_capacity_ladder.md`

The plan does not reopen MMT, introduce a physical residual, or change the
accepted forward model. It establishes the capacity and cancellation controls
that every later physics-guided candidate must beat.

## Frozen Scope

- program stage: Wave 5.2R Stage 4;
- dataset: `polished_dataset`;
- input mode: setpoints;
- surface: `Fw`;
- schema: `polished_setpoint_curve_v1`;
- split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- training curves: `675`;
- validation curves: `194`;
- test curves: `97`;
- excluded metadata anomalies: the three Stage 0 quarantined conditions;
- analytical anchor: `PF_A_SETPOINT_QUADRATIC`;
- anchor source: training-only causal setpoint refit of the Stage 3 PF-A
  formulation;
- anchor deployment status: qualified only in `supported_core`;
- first-screen seed: `314159`;
- conditional stability seeds: `271828` and `161803`;
- official TE Curve Verification Pipeline: excluded from normal closeout.

No target-derived runtime input is permitted. The model receives only output
angle, setpoint speed, setpoint torque, and temperature through the existing
causal curve dataset.

## Analytical And Learned Decomposition

Every hybrid prediction must expose:

```text
predicted TE = frozen PF-A contribution + learned residual contribution
```

The direct controls expose:

```text
predicted TE = direct learned contribution
```

For coefficient and low-rank candidates, reconstruction remains explicit:

```text
predicted TE =
    corrected offset
  + sum over retained orders of
      corrected sine coefficient * sin(order * theta)
    + corrected cosine coefficient * cos(order * theta)
```

The PF-A offset and all nine sine/cosine pairs remain separately inspectable.

## Candidate Definitions

| ID | Candidate | Learned output |
| --- | --- | --- |
| `R0` | frozen PF-A | none |
| `R1` | direct parameter-matched MLP | pointwise TE |
| `R2` | frozen PF-A plus residual MLP | pointwise residual |
| `R3` | frozen PF-A plus bounded residual MLP | bounded pointwise residual |
| `R4` | frozen PF-A plus low-rank residual basis | basis coefficients |
| `R5` | frozen PF-A plus coefficient correction | offset and complex coefficient deltas |

`R0` is evaluated without training and does not consume a campaign queue slot.

### Bounded Residual

`R3` uses:

```text
residual = residual_bound * tanh(raw_residual)
```

The bound is selected from training-only PF-A residual statistics and frozen
before validation or test evaluation.

### Low-Rank Residual

`R4` predicts coefficients for a small fixed periodic basis. The basis is
chosen from training-only singular-value and harmonic evidence, and the
retained rank is declared in the queue YAML.

### Coefficient Correction

`R5` predicts corrections to:

- offset;
- sine coefficient for each of the nine PF-A orders;
- cosine coefficient for each of the nine PF-A orders.

The base PF-A coefficient surface remains explicit. Partial and full
unfreezing apply only to declared trainable correction or base-surface
parameters and never hide the original frozen coefficients.

## Screening Queue

The first campaign contains eighteen learned runs at seed `314159`.

### Parameter-Matched Direct Controls

| Queue ID | Role | Capacity |
| --- | --- | --- |
| `C01` | direct control for R2/R3 compact | compact |
| `C02` | direct control for R2/R3 deep | deep |
| `C03` | direct control for R4 compact | compact |
| `C04` | direct control for R4 deep | deep |
| `C05` | direct control for R5 compact | compact |
| `C06` | direct control for R5 deep | deep |

### Primary Hybrid Arms

| Queue ID | Candidate | Capacity | Anchor mode | Energy penalty |
| --- | --- | --- | --- | ---: |
| `H01` | R2 | compact | frozen | 0 |
| `H02` | R2 | deep | frozen | 0 |
| `H03` | R3 | compact | frozen | 0 |
| `H04` | R3 | deep | frozen | 0 |
| `H05` | R4 | compact | frozen | 0 |
| `H06` | R4 | deep | frozen | 0 |
| `H07` | R5 | compact | frozen | 0 |
| `H08` | R5 | deep | frozen | 0 |

### Residual-Energy Ablations

| Queue ID | Candidate | Capacity | Penalty |
| --- | --- | --- | ---: |
| `A01` | R2 | compact | weak |
| `A02` | R2 | compact | moderate |

The exact weak and moderate weights will be derived from training-only scale
calibration and written into the immutable queue configs. The zero-penalty H01
arm is the matched reference.

### Anchor-Trainability Ablations

| Queue ID | Candidate | Capacity | Anchor mode |
| --- | --- | --- | --- |
| `A03` | R5 | compact | partial low-order unfreeze |
| `A04` | R5 | compact | full coefficient-surface unfreeze |

H07 is the frozen-anchor reference for these two arms.

## Capacity Contract

Two predeclared capacity levels are sufficient for the first width and depth
screen:

| Capacity | Intended structure |
| --- | --- |
| compact | two hidden layers near width 32 |
| deep | three hidden layers near widths 64, 64, and 32 |

Exact widths may be adjusted by the preparation script only to meet the
parameter-matching gate.

For each hybrid, its direct R1 control must:

- use the same causal inputs;
- use the same periodic input encoding when the hybrid uses it;
- have trainable parameter count within `5%`;
- use the same optimizer and epoch budget;
- use identical data loss and batching;
- differ only by the absence of PF-A and the residual decomposition.

Preparation fails if the parameter mismatch exceeds `5%`.

## Training Budget

Every screening arm uses:

- curve batch size: `4`;
- point stride: `8`;
- maximum points per curve: `4096`;
- workers: `2`;
- precision: float32;
- optimizer: AdamW;
- learning rate: `5e-4`;
- weight decay: `1e-5`;
- maximum epochs: `24`;
- minimum epochs: `4`;
- early-stopping patience: `5`;
- deterministic seed and DataLoader generator;
- identical checkpoint selection based on the predeclared validation
  objective.

The preparation script may lower batch size after one-batch validation if
memory requires it. It may not change split, stride, loss, capacity, seed, or
candidate identity without an updated plan.

## Loss Contract

Every learned arm shares the same normalized pointwise data objective:

```text
L_data = mean squared error of predicted normalized TE
```

The only permitted Stage 4 auxiliary objective is the declared
residual-energy penalty:

```text
L_total = L_data + lambda_energy * mean(residual^2)
```

The coefficient and low-rank arms may reconstruct through their explicit basis
but may not add coefficient-target, harmonic-target, derivative, periodic,
physics, or smoothness losses in Stage 4.

This restriction prevents Stage 5 or Stage 6 guidance from leaking into the
data-only capacity floor.

## Stage 2 Instrumentation

Every learned run records:

- raw and normalized data loss;
- residual-energy loss when enabled;
- loss exponential moving averages;
- per-loss shared-parameter gradient norms;
- pairwise gradient cosine when the energy penalty is active;
- update-to-parameter ratio;
- seed and dataloader fingerprint;
- parameter-freeze state;
- residual-bound state;
- checkpoint-selection objective.

Adaptive weighting and conflict projection are disabled. Stage 4 must first
establish fixed-objective behavior.

## Required Preflight

Before real training, the package must prove:

1. Stage 3 PF-A artifact and split hashes match, and its input contract is
   audited explicitly.
2. R0 reproduces the frozen causal setpoint-refit test metrics.
3. Zero-initialized residuals reproduce PF-A exactly.
4. Direct controls do not call the analytical-anchor path.
5. Bounded residuals never exceed their declared bound.
6. Low-rank and coefficient reconstruction are numerically exact.
7. Frozen anchor parameters receive no gradient and are absent from the
   optimizer.
8. Partial unfreeze touches only declared low-order coefficients.
9. Full unfreeze keeps the original coefficient surface separately
   serializable.
10. Every direct control is within `5%` of its matched hybrid parameter count.
11. Fixed seed and DataLoader construction reproduce the same batch
    fingerprint.
12. A different seed changes shuffled order.
13. All losses and gradients remain finite on one full batch.
14. All eighteen queue configs pass model-factory and one-batch validation.
15. Both local and `-Remote` launcher preflights pass.

## Evaluation Surface

All candidates are evaluated on identical full-resolution curves.

Required metrics are:

- raw MAE and RMSE;
- centered-shape MAE and RMSE;
- offset absolute error;
- peak-to-peak error;
- derivative MAE and correlation;
- retained-order complex coefficient error;
- amplitude and circular phase error;
- P95 and worst-curve error;
- inference time and numerical range;
- residual RMS and energy;
- residual-to-anchor energy ratio;
- residual projection by harmonic band;
- analytical-residual correlation;
- support-tier result for core, sparse/corner, and extrapolation populations.

The `supported_core` test population is the primary promotion surface.
Sparse/corner and extrapolation rows remain visible but cannot create a
promotion.

## Opaque-Cancellation Gate

A hybrid is rejected as opaque cancellation when any of these conditions
holds:

- the residual-to-anchor RMS ratio exceeds `0.50`;
- combined error improves while centered shape or offset materially regresses;
- improvement is confined to sparse/corner or extrapolation conditions;
- the analytical contribution cannot be reconstructed independently;
- the residual contains non-finite values or violates its declared bound;
- the hybrid does not beat its parameter-matched direct control.

Per-curve analytical-residual correlation and harmonic projection remain
diagnostics. They are not used alone to reject a valid offset correction.

## First-Screen Exit Rule

A hybrid reaches stability testing only if it:

1. beats frozen PF-A on supported-core raw MAE;
2. beats its parameter-matched direct control on supported-core raw MAE;
3. has no material centered-shape, offset, P95, derivative, amplitude, or phase
   regression;
4. remains finite across all `966` eligible forward conditions;
5. passes the opaque-cancellation gate;
6. preserves separately inspectable analytical and learned contributions.

If no arm passes, Stage 4 closes as a valid negative result and Stage 5 must
not claim that a residual architecture has already been validated.

## Conditional Stability Continuation

If one hybrid passes the first screen:

- repeat that hybrid at seeds `271828` and `161803`;
- repeat its matched direct control at the same seeds;
- combine the initial and repeat evidence into a three-seed decision;
- require the hybrid-versus-anchor and hybrid-versus-control advantage to
  remain directionally consistent.

This continuation adds four runs, for a maximum Stage 4 total of twenty-two
learned runs.

If multiple hybrids pass, select the simplest passing hybrid before the repeat
campaign. Complexity cannot be chosen solely from scalar validation MAE.

## Planned Execution Package

After explicit approval of this campaign plan, preparation will create:

- model implementation and model-factory registration;
- training-module integration;
- model explanatory report;
- campaign manifest and eighteen immutable queue-source YAML files;
- preparation and validation scripts;
- dedicated PowerShell launcher supporting local and `-Remote`;
- launcher note documenting both paths;
- persistent active-campaign state;
- one-batch and smoke-test artifacts;
- exact operator commands.

The remote path will reuse
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`. It will
synchronize source, configuration, technical and planning documentation before
launch and synchronize queue state, campaign outputs, run artifacts,
registries, and status evidence afterward.

## Closeout Requirements

Normal closeout must produce:

- `campaign_leaderboard.yaml`;
- `campaign_best_run.yaml`;
- `campaign_best_run.md`;
- explicit R0 and parameter-matched control comparisons;
- full-curve and support-tier diagnostics;
- family and program registry synchronization where justified;
- Stage 4 Markdown campaign-results report;
- visually validated PDF companion;
- active-campaign cleanup;
- roadmap, backlog, master-summary, and ledger synchronization;
- explicit positive or negative Stage 4 decision;
- dedicated Stage 4 commit.

The heavy TE Curve Verification Pipeline is not part of normal closeout.

## Preparation Causality Erratum

The executable preflight found a material provenance mismatch before training:
the exact Stage 3/Phase 1 PF-A reproduction constructed its operating features
from measured curve averages, although the Stage 3 report and the Wave 5.2R
roadmap declare setpoint-only inference.

Stage 4 does not pass those measured values to the network and does not conceal
the mismatch inside a learned residual. The preparation script instead:

1. preserves the legacy Stage 3 surface unchanged as comparison evidence;
2. refits the same nine-order complete-quadratic PF-A formulation using only
   forward nominal torque, speed, and temperature setpoints from the `675`
   training curves;
3. freezes that causal surface before validation and test access;
4. records legacy measured-input, legacy surface-on-setpoints, and causal
   setpoint-refit metrics in
   `stage4_training_only_calibration.yaml`.

The corrected causal anchor reaches test MAE `0.001808977 deg`, versus
`0.001807084 deg` for the legacy measured-input replay. The `0.000001893 deg`
difference is small numerically but decisive for the leakage contract.

The preparation also recomputed the validity envelope in setpoint space rather
than inheriting the legacy measured-input tiers. It contains `96`
`supported_core` and `1` `supported_sparse_or_corner` test conditions, with no
setpoint-axis extrapolation in the test split. All `966` eligible forward
conditions remain finite.

## Approval Gate

**Approved.**

The user approved all current and future project documents for the next
twenty-four hours:

- approval start: `2026-07-27T23:57:23+02:00`;
- approval expiry: `2026-07-28T23:57:23+02:00`;
- approved scope: technical documents, campaign plans, model reports,
  launcher notes, preparatory reports, campaign execution, closeout reports,
  and the required per-stage commits within the Wave 5.2R roadmap.

Training and protected campaign-state changes are authorized inside this
window when they remain within the approved Stage 4 plan.
