# Wave 5.2R Stage 8 Weak Forward Compliance Priors

## Overview

Stage 8 tests whether the positive but seed-unstable Phase 3 compliance signal
can become useful when it is introduced progressively above the qualified
Stage 5 H04 component.

The scope remains fixed to:

- `polished_dataset`;
- setpoint-only causal inputs;
- forward (`Fw`) curves;
- the Stage 0 split signature;
- the canonical `2048`-point uniform angular representation;
- frozen PF-A and H04 evidence;
- no backlash, hysteresis, contact-state, or lost-motion claim.

The direct mechanical reference supports torsional rigidity as the slope of a
cyclic torque-deformation curve, but its identification requires ordered
loading and unloading, synchronous torque and torsional angle, contact
stiffness, clearances, and working-position control. Those quantities are not
available in the current static setpoint contract. Stage 8 therefore tests a
weak observable response prior on predicted mean TE, not an identified
component stiffness law.

## Technical Approach

### Evidence Boundary

The earlier Phase 3 screen established:

- positive training-only torque-to-mean slopes;
- fitted forward stiffness near `28.2 kNm/deg`;
- only `2 / 3` C1 initializations passing the full-curve gate;
- stable fitted stiffness with unstable predictive benefit;
- hard elastic equations underfitting the measured surface.

Stage 8 will preserve that evidence but reduce model misspecification and
optimization pressure. The tested response derivative is:

```text
compliance_response =
    d predicted_curve_mean / d signed_forward_torque
```

The derivative remains an effective response quantity. It must not be called
unit-specific contact stiffness without independent mechanical
identification.

### Training-Only Bootstrap Gate

Before model training, the campaign will bootstrap the train-condition
relationship between measured curve mean and signed forward torque while
stratifying or controlling for speed and temperature. It will persist:

- derivative-sign support;
- central and broad quantile intervals;
- effective-stiffness transforms where the derivative is positive;
- speed- and temperature-band support;
- shuffled-torque negative-control distributions;
- extrapolation and low-support masks.

Weak compliance losses are enabled only where the training bootstrap supports
their sign or interval. Validation and test targets remain evaluation-only.

### Candidate Sequence

| ID | Formulation | Training role |
| --- | --- | --- |
| `D00` | frozen H04 diagnostic | measure derivative, bounds, and support without optimization |
| `C00` | H04 bounded data-only fine-tune | matched optimization control |
| `S01` | sign-only monotonicity | penalize only unsupported negative derivative |
| `B01` | broad bootstrap interval | penalize derivative outside conservative train-only bounds |
| `W01` | confidence-weighted interval | down-weight low-support condition regions |
| `T01` | temperature-stratified interval | permit broad temperature-dependent response |
| `A01` | delayed compliance activation | warm-start data fitting before enabling the weak prior |
| `R01` | adaptive compliance weight | use Stage 2 gradient statistics within a bounded range |
| `N01` | shuffled-torque sign prior | negative control for prior specificity |
| `H01` | hard compliance equation | deliberately strong negative control |

The first screen uses seed `314159`. Only candidates passing every declared
gate continue with seeds `271828` and `161803`.

### Losses And Diagnostics

Every trainable candidate records:

- raw full-curve loss;
- curve-mean loss;
- centered-shape loss;
- compliance sign or interval loss;
- compliance-to-raw, compliance-to-mean, and compliance-to-shape gradient
  cosines;
- gradient norms and effective loss weights;
- derivative-bound activation fraction;
- condition-support confidence;
- raw, offset, centered-shape, derivative, harmonic, closure, and P95 metrics.

The hard-equation negative control may not be promoted even if it fits one
scalar metric; its purpose is to quantify misspecification pressure.

### Exit Gates

A compliance candidate advances only when all three seeds:

1. improve raw MAE relative to frozen H04 and matched C00;
2. improve absolute curve-mean error;
3. preserve or improve centered-shape MAE;
4. preserve derivative, harmonic amplitude, harmonic phase, closure, and P95;
5. outperform the shuffled-torque negative control;
6. retain the training-supported derivative sign without saturating the
   interval penalty;
7. expose bounded, finite, causal intermediate quantities;
8. show no target-derived runtime input.

Stable effective stiffness alone is insufficient. The campaign may close with
no promotion.

## Involved Components

- `reference/te_modeling/theoretical_mechanics/dynamics_hysteresis_and_efficiency/2025_xu_hysteresis_torsional_rigidity_lost_motion_rv_reducer.pdf`;
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`;
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`;
- Phase 3 compliance model, identifiability audit, campaign closeout, and
  stability artifacts;
- Stage 2 optimization instrumentation;
- Stage 5 H04 checkpoint, coefficient representation, and dataset builder;
- Stage 7 explicit mean and centered-shape diagnostics;
- a new Stage 8 model and campaign implementation;
- a dedicated local and `-Remote` PowerShell launcher;
- immutable run, campaign, preflight, and closeout artifacts;
- Markdown and validated styled-PDF results;
- backlog, roadmap, status, usage-guide, and Sphinx synchronization.

No subagent is planned. If delegation becomes useful, its exact boundary will
be documented and separately approved before launch.

## Implementation Steps

1. Freeze the Stage 8 evidence and runtime contract.
2. Build a deterministic train-only compliance bootstrap and shuffled-torque
   negative control.
3. Define broad sign, interval, confidence, and temperature support masks.
4. Implement an H04-compatible weak-compliance model with inspectable mean and
   derivative outputs.
5. Add sign-only, bounded, confidence-weighted, delayed, adaptive, shuffled,
   and hard-equation candidate losses.
6. Record named losses, gradient norms, pairwise cosines, activation
   fractions, and effective weights.
7. Generate the campaign YAML, queue, launcher, launcher note, state, and
   exact local and remote commands.
8. Run deterministic model, derivative, leakage, split, and launcher
   preflight checks.
9. Execute the first screen and conditional three-seed continuation.
10. Evaluate the complete multi-index forward surface against frozen H04,
    matched C00, and the negative controls.
11. Publish the campaign-results Markdown and styled PDF, inspect every
    rendered page, and validate the final PDF.
12. Synchronize the roadmap, backlog, ledger, master summaries, usage guide,
    and Sphinx portal.
13. Run Python, PowerShell, Markdown, PDF, Sphinx, Git, file-size, and staged
    pack preflight checks before the approval-covered commit.
