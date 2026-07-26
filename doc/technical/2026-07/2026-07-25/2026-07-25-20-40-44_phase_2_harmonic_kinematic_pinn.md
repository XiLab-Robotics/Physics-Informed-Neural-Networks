# Phase 2 Harmonic And Kinematic Constraint PINN

## Overview

This project implements Phase 2 of the sixteen-phase Wave 5.2 full-PINN
theory-validation roadmap. Phase 0 established the data, coordinate,
observability, causality, and leakage contracts. Phase 1 selected
`PF_A_LOCAL_QUADRATIC` as the direction-specific analytical reference and
`PF_E_REDUCED_QUADRATIC` as the alternative comparator.

Phase 2 will test whether an explicit angular governing residual improves
held-out harmonic fidelity beyond a Fourier-feature or Fourier-head model.
The physical statement under test is that a synchronous component associated
with output order `k` obeys the angular oscillator equation

```text
d2 h_k(theta) / d theta2 + k^2 h_k(theta) = 0
```

over one output revolution. The test is intentionally limited to periodic
harmonic and kinematic structure. It does not introduce compliance,
hysteresis, contact, wear, MMT parameter estimation, or electromechanical
mechanisms.

This technical document is automatically approved under the user's standing
instruction for the sixteen-phase implementation. That approval does not
authorize training. The preliminary campaign plan remains subject to explicit
approval before any training-related experiment runs.

## Technical Approach

### Source-Backed Physics Contract

The implementation will preserve the following conclusions from Ghorbel,
Iwasaki, Bauer, the MMT harmonic mapping, and the completed repository
evidence:

- TE contains a synchronous angularly periodic component;
- amplitude and phase may vary with torque, speed, temperature, and direction;
- mechanism-specific orders are configuration, not universal constants;
- periodic shape must remain separate from offset and future hysteretic state;
- a Fourier input feature or harmonic metric alone is not a full PINN;
- the paper-faithful MMT branch remains deferred, while its order mapping may
  be used as a non-identifying harmonic diagnostic.

The primary admissible order set is the locally validated Phase 1 set:
`1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`.

### Model Variants

The bounded campaign will prepare four model roles for both `Fw` and `Bw`:

1. `PINN-H0`, a parameter-matched Fourier-head control with no physics
   residual;
2. `PINN-H1`, an implicit mechanism-grouped harmonic-head network trained with
   angular oscillator residuals;
3. `PINN-H2`, the same PINN with periodic value and first-derivative boundary
   residuals;
4. `PINN-H3`, the periodic PINN with a soft coefficient-surface anchor to the
   frozen `PF_A_LOCAL_QUADRATIC` analytical reference.

The offset head is independent of angle. Every implicit harmonic head receives
the causal operating-condition representation and angle, exposes its own
component curve, and remains differentiable with respect to the angular input.
There is no unconstrained free residual head in the first bounded campaign,
because such a path could bypass the physics residual.

`PINN-H0` is not called a full PINN. `PINN-H1` through `PINN-H3` qualify as
full-PINN candidates only if the training loss contains the explicit
differentiable angular governing residual and the persisted artifacts prove
that it was evaluated.

### Autodifferentiation Contract

Second angular derivatives will be computed with current PyTorch higher-order
autograd behavior:

- the angular input tensor requires gradients;
- the first derivative is built with `create_graph=True`;
- the second derivative is taken from the first derivative;
- `grad_outputs` matches the differentiated component tensor;
- unused gradients are treated as implementation errors, not silently
  materialized zeros;
- the residual is normalized per order to prevent high orders from dominating
  solely through the `k^2` scale.

Deterministic synthetic tests will prove the residual is near zero for exact
sine and cosine components, nonzero for an inadmissible component, stable
under phase wrapping, and differentiable back to model parameters.

### Campaign Design

The first campaign will remain bounded:

- separate `Fw` and `Bw` runs;
- no `global` run, because Phase 0 and Phase 1 establish direction-specific
  surfaces and a combined model would confound the first physics test;
- common 675 / 194 / 97 eligible paired-condition split;
- identical causal inputs and curve sampling across control and PINN arms;
- point stride `8`, which retains at least `1,350` angular samples on the
  Phase 0 minimum audited curve of `10,799` rows and therefore remains more
  than `2.8` times above the `480`-sample Nyquist minimum for output order
  `240`;
- runtime-bounded curve batches of `4`, with a distributed cap of `4,096`
  angular samples per curve and `64` physics collocation points per batch;
- at least `10,800` physics collocation evaluations per training epoch across
  the `675`-curve training split;
- a bounded ceiling of `24` epochs with patience `5`, retaining best-checkpoint
  validation and test evaluation;
- physics-weight sweep bounded to zero, low, and moderate pressure;
- order-drop and order-add ablations performed without changing held-out
  conditions;
- accepted periodic GRU and periodic harmonic MLP retained as external
  time-windowed and non-windowed references.

The original stride-`2` local attempt is retained as runtime-diagnostic
evidence. It completed `PINN-H0` on `Bw`, then showed that one implicit PINN
epoch required approximately 160 seconds. The clean campaign restart uses the
same conditions, order set, model definitions, losses, and acceptance policy
with stride `8` for all eight valid arms. No completed stride-`2` arm is mixed
into the restart leaderboard.

The campaign package will include local and `-Remote` execution, persistent
campaign state, immutable run-instance outputs, winner artifacts, and exact
post-run synchronization.

### Evaluation And Exit Gate

Selection will not use scalar MAE alone. The campaign report and later
TE Curve Verification Pipeline package will separate:

- raw MAE and RMSE;
- mean-centered shape fidelity;
- offset behavior;
- dominant-order amplitude and circular phase error;
- spurious-harmonic energy;
- periodic value and derivative closure;
- direction-specific continuity;
- physics residual magnitude;
- data-versus-physics gradient cosine similarity;
- compute, memory, ONNX, and TwinCAT implications.

Phase 2 passes only if at least one genuine physics-residual arm improves
held-out harmonic fidelity over `PINN-H0` without materially degrading raw
error, offset behavior, or continuity. If no arm passes, Phase 2 records a
negative result and later phases proceed without promoting this constraint.

## Involved Components

Planned code and configuration surfaces:

- `scripts/models/harmonic_kinematic_pinn_network.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/`
- `config/training/harmonic_kinematic_pinn/`
- `scripts/campaigns/wave_5_2/`
- `doc/scripts/campaigns/wave_5_2/`
- `doc/reports/campaign_plans/model_development_waves/wave_5_2/`
- `doc/reports/campaign_results/model_development_waves/wave_5_2/`
- `output/training_campaigns/`
- `output/training_runs/`
- `output/validation_checks/`

Canonical evidence inputs:

- Phase 0 foundation audit and eligible-condition contract;
- Phase 1 coefficient surfaces, per-curve metrics, and selected models;
- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`;
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`;
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`;
- `doc/reference_summaries/14_MMT_Linkage_Matlab_Project_Summary.md`;
- Waves 3.1 through 3.3 and Wave 5.1 results.

Protected campaign files will be checked again immediately before preparation.
No subagent is planned.

## Implementation Steps

1. Register this automatically approved technical document.
2. Create the preliminary campaign planning report and stop at its explicit
   training-approval gate.
3. Implement the parameter-matched control and implicit harmonic-head PINN.
4. Add normalized oscillator, periodic-value, periodic-derivative, and
   analytical-anchor loss terms with explicit logging.
5. Add deterministic synthetic residual, phase, gradient, and boundary tests.
6. Add model-factory, configuration, dataset, and serialization support.
7. Prepare the direction-separated campaign YAML queue and persistent state.
8. Create the dedicated local and `-Remote` PowerShell launcher and launcher
   note.
9. Run preflight and smoke validation without starting the real campaign.
10. After explicit campaign-plan approval, execute or hand off the real
    campaign.
11. Inspect winner artifacts and produce Markdown and validated PDF results.
12. Synchronize registries, backlog, ledger, master summary, guide, and portal.
13. Offer the TE Curve Verification Pipeline as a separate post-closeout step.
14. Commit the completed and verified Phase 2 scope.

## Verification Plan

- current PyTorch higher-order-autograd contract checked through Context7;
- exact synthetic oscillator residual below numerical tolerance;
- deliberately inadmissible-order residual above the pass threshold;
- finite first and second derivatives on CPU and available accelerator;
- nonzero parameter gradients from each enabled physics term;
- no target-derived inference input;
- common-split and quarantined-condition preservation;
- model-factory, one-batch, checkpoint, and export smoke tests;
- campaign preflight locally and through `-Remote` synchronization preflight;
- Markdown zero-warning checks;
- `git diff --check`;
- warning-free Sphinx build;
- file-size and staged-pack preflight before the phase commit.

## Completion Outcome

Phase 2 completed `8 / 8` canonical runs and a bounded common-split
curve-payload diagnostic. No physical residual arm passed the joint exit gate.
The oscillator, periodic-boundary, and Bauer-anchor weights are not promoted;
the implementation and falsification evidence remain reusable for later
phases. Phase 3 is the next active roadmap step.
