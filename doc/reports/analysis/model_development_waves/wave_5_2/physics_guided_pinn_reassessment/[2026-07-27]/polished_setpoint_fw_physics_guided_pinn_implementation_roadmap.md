# Polished Setpoint Forward Physics-Guided PINN Implementation Roadmap

## Roadmap Decision

This roadmap defines `Wave 5.2R`, a new forward-only physics-guided
reassessment branch.

The branch is restricted to:

- `polished_dataset`;
- `setpoints`;
- `Fw`;
- the immutable Phase 0 condition split;
- causal, deployment-available inputs.

The goal is to implement and falsify every currently viable way of adding
physics or structured domain knowledge to the forward TE predictor. The goal
is not to force a winner, reopen paper-faithful MMT, or weaken the completed
Wave 5.2 closeout.

No training is authorized by this roadmap alone. Every training stage requires
an approved technical document, preliminary campaign plan, campaign YAML,
PowerShell launcher, launcher note, campaign state, and exact launch command.

## Success Definition

A physics-guided ingredient is promoted only when it:

1. improves or matches the accepted forward model on the complete
   multi-index curve-first gate;
2. remains stable across at least three seeds;
3. beats a parameter-matched black-box control;
4. uses no target-derived inference input;
5. preserves inspectable physics and residual contributions;
6. remains numerically bounded across the full forward operating domain;
7. has a credible TwinCAT execution path.

The accepted forward references at roadmap entry are:

- time-windowed: `polished_setpoints_periodic_gru_sequence_Fw`;
- non-windowed: `polished_setpoints_periodic_mlp_harmonic_Fw`;
- analytical: `PF_A_LOCAL_QUADRATIC`.

## Execution Status

| Stage | Status | Decision |
| --- | --- | --- |
| Stage 0: Evidence Freeze And Reproducibility Harness | completed | All eight exit-gate checks and all twelve reproduction comparisons pass. Stage 1 is authorized. |
| Stages 1 through 15 | planned | Continue in order; training stages retain their campaign approval gates. |

## Non-Negotiable Experimental Contract

### Data

- Use only eligible `Fw` curves from `polished_dataset`.
- Use setpoint speed, torque, and temperature as the primary operating inputs.
- Preserve the canonical split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
- Keep the three Phase 0 metadata anomalies quarantined.
- Fit scalers, harmonic targets, sparse libraries, and analytical corrections
  on training conditions only.

### Comparability

- Freeze one full-resolution evaluation harness before candidate training.
- Use identical held-out curves and angular grids.
- Report training-stride metrics separately from full-curve metrics.
- Use at least three fixed seeds for any candidate that passes its first
  bounded screen.
- Match parameter count and training budget for black-box controls.
- Store every loss weight, gradient diagnostic, checkpoint, and failure.

### Metrics

Every stage reports:

- raw MAE and RMSE;
- absolute offset error;
- centered MAE;
- peak-to-peak relative error;
- derivative MAE and derivative correlation;
- complex coefficient error per selected order;
- amplitude and phase error;
- P95 per-curve error;
- worst-cell regression;
- seed dispersion;
- inference time and numerical range.

Hybrid stages additionally report:

- analytical contribution energy;
- neural residual energy;
- residual-to-anchor ratio;
- residual projection onto analytical orders;
- analytical-residual correlation;
- anchor-corruption sensitivity.

## Stage 0: Evidence Freeze And Reproducibility Harness

### Objective

Create one immutable forward evaluation contract before changing any model.

### Implementation

1. Materialize the eligible train, validation, and test `Fw` condition
   manifests.
2. Verify byte-level or content-level source identity against Phase 0.
3. Reproduce the accepted GRU, accepted harmonic MLP, and `PF-A` predictions on
   the same `97` test conditions.
4. Recompute all required curve-first metrics from full-resolution curves.
5. Store a forward-only baseline registry and comparison table.
6. Add operating-cell and harmonic-band diagnostic exports.

### Exit Gate

- Every baseline reproduces within the declared tolerance.
- All metrics share one unit and angular convention.
- No test information enters preprocessing or fit state.

### Failure Action

Stop all model work and repair provenance.

## Stage 1: Extended Scientific Technique Discovery

### Objective

Perform a deeper, implementation-facing search before freezing the final
candidate roster.

### Search Families

- model-discrepancy PINNs and grey-box residual learning;
- weak-form, variational, and Petrov-Galerkin PINNs;
- adaptive loss weighting and augmented Lagrangian constraints;
- gradient conflict measurement and multi-objective optimization;
- spectral-bias mitigation, Fourier features, SIREN, and wavelet coordinate
  networks;
- Sobolev and derivative-aware training;
- sparse equation discovery and symbolic regression;
- uncertainty-aware physics weighting;
- curriculum, transfer, and synthetic-to-real learning;
- failure-informed sampling;
- certified residual bounds;
- reduced-order neural operators where the data contract justifies them;
- recent physics-guided mechanical-system identification.

### Required Output Per Technique

| Field | Requirement |
| --- | --- |
| Scientific source | primary paper or official implementation |
| Claimed benefit | exact problem the technique addresses |
| Required variables | mapped to local causal availability |
| Proposed local formulation | equation, loss, or architecture |
| Control | matched model without the technique |
| Falsification | predeclared failure criterion |
| Deployment impact | operations, state, memory, and precision |
| Priority | high, medium, low, or excluded |

### Exit Gate

Freeze a candidate register with no untestable mechanism in the real-data
training roster.

## Stage 2: Evaluation And Optimization Instrumentation

### Objective

Make loss interaction observable before testing more physics.

### Implementation

1. Add named loss components with normalized units.
2. Record per-component loss values and exponential moving averages.
3. Record gradient norm per loss on shared parameters.
4. Record pairwise gradient cosine similarity.
5. Record update-to-parameter ratios.
6. Add fixed-weight, gradient-statistics, ReLoBRaLo-style, and conflict-aware
   optimizer adapters.
7. Add staged loss activation and freeze-unfreeze schedules.
8. Add deterministic seed and dataloader checks.

### Required Controls

- fixed equal weights;
- manually normalized fixed weights;
- adaptive weighting without physics;
- physics model with identical fixed weights.

### Exit Gate

All diagnostics reproduce on a one-batch test and a short smoke run. Adaptive
weighting must not produce non-finite weights or disable the data objective.

## Stage 3: Analytical Anchor Reproduction And Stress Tests

### Objective

Qualify `PF-A` as a forward analytical component rather than assuming that its
Phase 1 aggregate score is sufficient.

### Implementation

1. Refit the complete-quadratic coefficient surfaces on the frozen training
   split.
2. Preserve offset and complex harmonic coefficients explicitly.
3. Report condition-number and coefficient-stability diagnostics.
4. Compare local, reduced, paper-derived, recovered ONNX, and safe PLC-order
   subsets on `Fw`.
5. Create torque, speed, temperature, and corner holdouts.
6. Add analytical-anchor corruption tests:
   - coefficient scale perturbation;
   - phase perturbation;
   - order omission;
   - operating-input shift.
7. Define the deployable validity envelope.

### Exit Gate

`PF-A` must reproduce Phase 1 and remain finite across every valid forward
condition. Unstable anchor variants remain comparators only.

## Stage 4: Data-Only Residual Capacity Ladder

### Objective

Determine whether an explicit learned residual closes the analytical gap
before adding a physical loss.

### Candidate Ladder

| ID | Candidate |
| --- | --- |
| `R0` | pure `PF-A` |
| `R1` | residual MLP without analytical anchor |
| `R2` | frozen `PF-A` plus residual MLP |
| `R3` | `PF-A` plus bounded residual amplitude |
| `R4` | `PF-A` plus low-rank residual basis |
| `R5` | trainable coefficient correction with frozen base coefficients |

### Required Ablations

- matched total parameter count;
- identical data loss;
- identical optimizer and budget;
- residual width and depth sweep;
- residual-energy penalty sweep;
- freeze, partial-unfreeze, and full-unfreeze comparison.

### Exit Gate

A hybrid advances only if it beats both `PF-A` and its parameter-matched
black-box control without opaque analytical cancellation.

## Stage 5: Complex Harmonic Coefficient Residuals

### Objective

Learn corrections in the smallest interpretable output space.

### Implementation

1. Represent every selected order with sine and cosine coefficients.
2. Predict:
   - offset;
   - base coefficient;
   - learned coefficient correction.
3. Reconstruct the curve exactly from the coefficients.
4. Group orders into:
   - order `1`;
   - low orders;
   - reducer-related middle orders;
   - high-order ripple;
   - exploratory residual orders.
5. Compare fixed local orders, data-selected orders, and nested order sets.
6. Add coefficient smoothness across neighboring operating conditions.

### Losses

```text
L = L_curve
  + lambda_complex * L_complex_coefficients
  + lambda_band * L_band_balance
  + lambda_surface * L_condition_surface_smoothness
```

### Exit Gate

The candidate must improve curve metrics and not merely reduce coefficient
loss. Phase-wrap artifacts must be absent because training uses sine and cosine
coefficients.

## Stage 6: Spectral And Sobolev Guidance

### Objective

Directly address derivative and fragile-harmonic failures.

### Candidate Arms

- pointwise curve loss only;
- curve plus derivative loss;
- curve plus complex spectral loss;
- curve plus derivative and spectral losses;
- frequency-band curriculum;
- failure-informed angular or condition sampling;
- Fourier-feature residual MLP;
- SIREN residual branch;
- weak-form harmonic residual.

### Rules

- Target derivatives must be derived through a documented training-only
  filtering process.
- No derivative target may use future samples at runtime.
- Spectral targets are training labels, not inference inputs.
- Every high-frequency gain must be checked for noise amplification.

### Exit Gate

The candidate must improve selected harmonic fidelity, derivative behavior,
and P95 robustness without degrading raw error or offset.

## Stage 7: Mean And Centered-Shape Multi-Head Model

### Objective

Separate operating-condition offset from angular shape.

### Architecture

```text
shared_condition_encoder(u)
    -> mean_head(u)
    -> coefficient_or_shape_head(theta, u)
    -> optional uncertainty_head(u)

TE_hat = mean_head + zero_mean_shape
```

### Structural Constraints

- centered shape has exact zero cycle mean;
- periodicity is exact by basis or circular coordinate encoding;
- mean and shape outputs remain separately inspectable;
- the uncertainty head cannot alter the mean prediction during evaluation.

### Candidate Arms

- shared trunk;
- partially shared trunk;
- independent mean and shape networks;
- gradient-conflict-aware shared trunk;
- analytical mean plus learned shape;
- learned mean plus analytical-shape correction.

### Exit Gate

Multi-head sharing must beat independent heads or demonstrate a clear
parameter-efficiency advantage. Negative gradient cosine between mean and
shape must be reported, not hidden.

## Stage 8: Weak Forward Compliance Priors

### Objective

Revisit the strongest partially positive Phase 3 signal with less brittle
constraints.

### Candidate Sequence

1. compliance diagnostic head with no training penalty;
2. sign-only monotonicity penalty;
3. broad bounded stiffness interval;
4. confidence-weighted stiffness penalty;
5. temperature-conditioned broad interval;
6. adaptive or curriculum-activated compliance penalty;
7. hard compliance equation as a negative control.

### Safeguards

- do not interpret forward compliance as backlash;
- report predictive and parameter stability separately;
- measure whether the compliance gradient conflicts with offset and shape;
- stop escalation if the sign-only prior fails.

### Exit Gate

At least three of three seeds must pass raw, offset, centered-shape, harmonic,
and P95 gates. Stable stiffness alone is insufficient.

## Stage 9: Temporal Analytical-Residual Models

### Objective

Test whether causal history explains residual structure beyond static
conditions.

### Candidate Arms

- accepted periodic GRU;
- parameter-matched residual GRU without `PF-A`;
- frozen `PF-A` plus residual GRU;
- coefficient-residual GRU;
- mean-static plus shape-temporal model;
- curriculum sequence-length residual model.

### Runtime Contract

Only causal angle, setpoints, and documented history are allowed. No measured
TE, future value, centered target, or offline harmonic coefficient can become
an inference input.

### Exit Gate

The hybrid must beat the accepted GRU, not only the analytical or MLP
references. It must expose deterministic hidden-state initialization and
bounded behavior.

## Stage 10: Sparse And Symbolic Formulation Discovery

### Objective

Search for parsimonious condition-harmonic interactions that the complete
quadratic law misses.

### Implementation

1. Build a predeclared dictionary of polynomial, harmonic, and interaction
   terms.
2. Fit sparse models on training conditions only.
3. Use stability selection across bootstrap resamples.
4. Reject terms whose sign or magnitude is unstable.
5. Compare discovered terms with source-backed mechanism orders.
6. Convert stable terms into explicit ablation candidates.

### Interpretation Rule

Discovered terms are empirical structure until independently connected to a
mechanism. They may improve an interpretable predictor without being called a
new physical law.

### Exit Gate

Only stable, low-complexity terms with held-out gain advance.

## Stage 11: Uncertainty And Physics-Trust Calibration

### Objective

Estimate when the analytical anchor or learned residual is unreliable.

### Candidate Methods

- deep ensemble;
- heteroscedastic residual head;
- Bayesian last layer;
- condition-distance uncertainty;
- anchor-discrepancy confidence;
- physics-loss uncertainty weighting.

### Required Tests

- calibration by torque, speed, and temperature band;
- high-error capture rate;
- uncertainty-error rank correlation;
- boundary-holdout behavior;
- ensemble inference cost.

### Exit Gate

Uncertainty must be calibrated and actionable. A wider interval without error
localization is not sufficient.

## Stage 12: Advanced Constraint Optimization

### Objective

Apply heavier PINN optimization only to ingredients that survived simpler
tests.

### Candidate Methods

- gradient-statistics annealing;
- ReLoBRaLo-style relative balancing;
- self-adaptive sample weights;
- PCGrad or main-loss-preserving gradient projection;
- augmented Lagrangian constraints;
- curriculum regularization;
- failure-informed resampling;
- second-order refinement where numerically justified.

### Ordering Rule

No advanced optimizer may rescue an uninformative physical equation.
Optimization methods are tested after the equation or prior shows incremental
signal in a simpler setting.

### Exit Gate

The method must improve repeatability or curve-first accuracy relative to the
same candidate with the standard optimizer.

## Stage 13: Synthetic And Weak-Form Oracle Lane

### Objective

Test formulations that are mathematically meaningful but not fully
identifiable from current real data.

### Permitted Work

- synthetic coefficient-surface perturbations;
- controlled harmonic injection and omission;
- synthetic compliance nonlinearities;
- misspecified-anchor recovery;
- weak-form versus pointwise residual comparison;
- synthetic noise and sampling-density stress;
- analytical residual certification experiments.

### Boundary

Synthetic success does not authorize a real-data physical claim. It can:

- validate code;
- determine observability requirements;
- tune detection power;
- define future instrumentation.

## Stage 14: Cross-Formulation Forward Tournament

### Entry Requirements

A candidate enters only if it has:

- passed its isolated gate;
- completed three-seed evaluation;
- beaten its matched control;
- passed leakage and causality checks;
- complete full-curve payloads;
- an inspectable inference path.

### Tournament Categories

- best raw error;
- best centered shape;
- best offset;
- best harmonic fidelity;
- best robustness;
- best interpretability;
- best TwinCAT readiness;
- recommended balanced candidate.

### Decision

No scalar-only winner is allowed. The tournament may end with no promotion.

## Stage 15: Official Forward Verification And Deployment Preparation

### Objective

Move only a tournament-qualified candidate into official acceptance.

### Work

1. Prepare a separate `TE Curve Verification Pipeline` launcher.
2. Run the forward-only candidate and accepted references on the official
   common surface.
3. Generate overlays, collages, and multi-index reports.
4. Update family and program registries only after acceptance.
5. Define a TwinCAT inference graph with:
   - input normalization;
   - analytical coefficients;
   - learned corrections;
   - harmonic reconstruction;
   - residual bounds;
   - state initialization where applicable;
   - output saturation and diagnostics.
6. Compare ONNX, Python, and PLC numerical parity.

### Exit Gate

The candidate must pass official curve-first verification and deployment
parity. Otherwise, it remains exploratory.

## Candidate Priority Matrix

| Priority | Candidate family | Reason |
| --- | --- | --- |
| 1 | `PF-A` plus bounded residual MLP | strongest observable grey-box test |
| 2 | complex coefficient residual model | compact, exact-periodic, inspectable |
| 3 | spectral and Sobolev loss | directly addresses harmonic redistribution |
| 4 | mean plus centered-shape heads | separates offset and periodic structure |
| 5 | adaptive loss and gradient diagnostics | addresses demonstrated optimization risk |
| 6 | temporal `PF-A` residual GRU | challenges the accepted forward GRU directly |
| 7 | weak forward compliance | promising but previously seed-unstable |
| 8 | sparse condition-harmonic discovery | interpretable formulation discovery |
| 9 | Fourier-feature or SIREN residual | representation ablation |
| 10 | weak-form harmonic residual | derivative-noise and redundancy ablation |
| 11 | uncertainty calibration | needed after predictive candidates emerge |
| 12 | neural operator | low priority under the current input contract |

## Explicit Stop Rules

Stop a branch when:

- the physical loss improves only itself;
- a matched black-box control is equally good or better;
- the analytical component is cancelled by the residual;
- one of three seeds fails the predeclared promotion gate;
- harmonic gains are offset by raw, offset, or P95 regressions;
- the formulation requires an unavailable runtime input;
- a physical parameter is non-identifiable or unstable;
- deployment cost is unjustified by predictive gain.

Stopping one branch does not stop the roadmap. It prevents weak evidence from
contaminating later compositions.

## Future Data Recommendations

The following data would enable branches excluded from the current scope:

- repeated forward and backward load-unload loops;
- deterministic warm-up and state-reset protocols;
- continuous reversal trajectories;
- unit-specific geometry and clearance metrology;
- load inertia and commanded acceleration profiles;
- synchronized motor current, voltage, and torque;
- input and output power;
- reducer identity and longitudinal load-cycle history.

These recommendations remain outside the `Wave 5.2R` training scope.

## Governance And Execution Order

The immediate approved documentation sequence ends with this roadmap.

The next executable project should be:

```text
Stage 0:
Forward Evidence Freeze And Reproducibility Harness
```

After Stage 0 closes, Stage 1 technique discovery is refreshed and the first
training package should combine Stages 2 through 4 only:

```text
Instrumentation
+ analytical anchor stress
+ data-only residual capacity ladder
```

Physics-loss campaigns begin only after that ladder establishes whether the
analytical residual architecture adds value.

This ordering prevents an improvement from being attributed to physics when
it is actually caused by extra parameters or a better residual architecture.
