# Wave 5.2R Stage 1 Extended Scientific Technique Discovery

## Executive Decision

Stage 1 is complete and passes its exit gate.

The search did not identify a previously missed, complete governing equation
that can be applied one-to-one to the current test-rig dataset. It did identify
a broad, scientifically grounded set of ways to help a neural model without
pretending that unavailable contact or internal-state variables are observed.

The candidate register is therefore frozen with:

- `30` documented techniques;
- `13` techniques in the active real-data roster;
- `11` techniques retained behind explicit diagnostic gates;
- `3` synthetic or offline oracle techniques;
- `3` excluded techniques;
- all `13` roadmap search families covered;
- zero target-derived runtime variables;
- zero missing variables in the active or conditional real-data roster.

The decision is not that physics is useless. The decision is that different
forms of knowledge must be used at different strengths:

1. exact construction for known periodic structure;
2. supervised spectral and derivative guidance for directly measurable curve
   properties;
3. bounded discrepancy learning around the Polynomial-Fourier anchor;
4. weak, falsifiable priors for incomplete mechanics;
5. synthetic or offline tests for mechanisms that are not identifiable from
   the current measurements.

This hierarchy lets the network compensate for an incomplete analytical model
while preventing the neural residual from hiding an invalid physical claim.

## Scope And Frozen Contract

Stage 1 inherits the immutable Stage 0 contract.

| Contract item | Frozen value |
| --- | --- |
| Dataset | `polished_dataset` |
| Input mode | setpoints |
| Surface | `Fw` only |
| Split signature | `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16` |
| Test conditions | `97` |
| Runtime variables | angle, speed setpoint, torque setpoint, temperature setpoint |
| Analytical anchor | `PF_A_LOCAL_QUADRATIC` |
| Neural references | accepted periodic harmonic MLP and accepted periodic GRU |

Training curves may supply measured TE, harmonic coefficients, angular
derivatives, PF-A residuals, and diagnostic statistics. Those quantities may
define training targets or losses, but they are not allowed as runtime inputs.

The following states are not available causally:

- contact force and contact location;
- mesh stiffness and internal load sharing;
- component-level manufacturing error groups;
- friction state and internal loss power;
- causal acceleration and identified inertia;
- repeated reversal and loop history;
- synchronized electrical current and motor sidebands;
- wear chronology and unit-specific geometry.

Any formulation requiring those quantities is excluded from real-data
training or retained only as a synthetic oracle.

## Evidence Method

The review combined three evidence layers.

### Repository-Primary Evidence

The ingested Bauer Polynomial-Fourier material, Fourier and polynomial notes,
the recovered Matlab implementations, RV reducer mechanics summaries, MMT
mapping, hysteresis and backlash synthesis, and dataset contract were read as
project-specific evidence.

Stage 0 was treated as the empirical baseline. It establishes that:

- the analytical PF-A anchor is reproducible;
- the accepted GRU is strongest on most raw and shape metrics;
- the harmonic MLP remains strong in harmonic diagnostics;
- no later candidate may claim improvement by changing the split or angular
  convention.

### External Primary Literature

Primary papers and official proceedings were searched for:

- model discrepancy and grey-box learning;
- variational and weak-form PINNs;
- loss balancing and gradient conflict;
- spectral bias and coordinate networks;
- derivative-aware objectives;
- symbolic and sparse discovery;
- uncertainty-aware weighting;
- curriculum and adaptive sampling;
- certification and neural operators;
- hybrid mechanical-system identification.

Review articles and secondary summaries were not used as the scientific basis
for candidate inclusion.

### Translation Rule

A paper result was not copied directly into the local plan. Each method was
translated through four questions:

1. Does the method address a failure that can exist in this TE task?
2. Are all required variables available causally or derivable from training
   data only?
3. Can the local hypothesis be compared with a matched control?
4. Is there a result that would falsify the local hypothesis?

Only techniques answering all four questions enter the real-data roster.

## What Counts As Physics Guidance Here

The word physics covers several distinct kinds of structure. Keeping them
separate is essential.

### Exact Observable Structure

The angular curve is periodic and has a measurable harmonic decomposition.
These are directly testable properties of the output. They can be imposed
through:

- periodic features;
- exact periodic output construction;
- complex harmonic targets;
- spectral losses;
- zero-mean centered-shape construction.

These constraints are strong because they do not require unobserved internal
states.

### Semi-Analytical Mechanistic Structure

PF-A predicts Fourier coefficients as low-order functions of operating
conditions. It is an effective analytical anchor, but it is not a complete
governing law for every reducer mechanism.

The appropriate hybrid is
`y_hat(theta, z) = PF_A(theta, z) + bounded_residual(theta, z)`.

where `z` contains the three setpoints. The residual is allowed to repair
misspecification, but it must beat a parameter-matched data-only control and
remain bounded under anchor corruption.

### Weak Mechanical Priors

Quasi-static compliance, torque sensitivity, smooth coefficient surfaces, and
bounded response are physically motivated but incompletely specified. They
may be tested as weak sign or interval priors only after training-data
bootstrap analysis supports them.

They are hypotheses, not laws. If the weak prior reduces its own loss without
improving held-out curves, it is rejected.

### Unobservable Governing Mechanisms

Contact, load sharing, friction energy, dynamic inertia, MMT component errors,
and backlash memory are valid mechanical topics. They cannot be evaluated
honestly from the current forward setpoint contract.

The network cannot make a missing state observable merely because a loss
equation contains that state. Replacing the missing state with target TE would
create leakage and circular reasoning.

## Frozen Technique Roster

### Active Real-Data Roster

These techniques are directly testable with the frozen contract.

| ID | Technique | Priority | Stage | Main test |
| --- | --- | --- | ---: | --- |
| `T01` | Bounded PF-A discrepancy residual | high | 3 | Anchor plus residual versus matched residual control |
| `T02` | Complex harmonic-coefficient residual | high | 5 | Joint amplitude and phase fidelity |
| `T03` | Mean and centered-shape heads | high | 7 | Offset and shape improve jointly |
| `T04` | Fourier-feature coordinate residual | high | 4 | High-order fidelity without spectral artifacts |
| `T05` | SIREN coordinate residual | medium | 4 | Derivative and harmonic gain versus tanh |
| `T07` | Complex spectral supervision | high | 6 | Harmonic gain without raw-error regression |
| `T08` | Angular Sobolev supervision | high | 6 | Derivative gain robust to estimator choice |
| `T09` | Local Fourier-moment weak residual | medium | 13 | Integrated moments improve held-out curves |
| `T11` | Gradient-statistics annealing | high | 2 | Reduced loss-gradient imbalance |
| `T12` | ReLoBRaLo balancing | high | 2 | Stable weights and better repeatability |
| `T16` | Staged guidance curriculum | high | 2 | Better final result at equal update budget |
| `T22` | Temporal PF-A plus GRU residual | high | 9 | Beat the accepted GRU, not only PF-A |
| `T23` | Exact periodic output construction | high | 4 | Closure by construction without lost capacity |

### Conditional Real-Data Roster

These techniques remain testable, but only after their trigger is observed.

| ID | Technique | Trigger | Priority |
| --- | --- | --- | --- |
| `T06` | Wavelet coordinate network | Stable localized multiscale residual remains after Fourier and SIREN tests | low |
| `T10` | Weak compliance sign or bound | Training bootstrap establishes a stable derivative sign or interval | medium |
| `T13` | Main-loss-preserving PCGrad | Persistent negative gradient cosine is measured | medium |
| `T14` | CAGrad | Multi-objective conflict remains after simpler adapters | low |
| `T15` | Augmented Lagrangian | A simple soft prior first shows incremental signal | low |
| `T17` | Failure-informed sampling | Cross-fitted localized failure regions are stable | medium |
| `T18` | Self-adaptive point weights | Effective-sample-size and noise checks prevent collapse | low |
| `T19` | Ensemble anchor-trust calibration | Error localization is useful enough to justify inference cost | medium |
| `T20` | Sparse harmonic-condition discovery | Terms are stable across bootstrap resamples | medium |
| `T21` | Constrained symbolic residual search | Sparse-library limits are demonstrated | low |
| `T24` | Residual certification | A supported tournament candidate and meaningful residual exist | low |

### Oracle-Only And Excluded Roster

| ID | Technique | Decision | Reason |
| --- | --- | --- | --- |
| `T27` | Misspecified-anchor synthetic curriculum | oracle only | Useful for recovery power, not proof of real mechanics |
| `T28` | Paper-faithful MMT oracle | oracle only | Component errors and geometry are not causally observed |
| `T29` | Contact, friction, and energy residuals | oracle only | Internal force, stiffness, sharing, and loss states are absent |
| `T25` | Physics-informed neural operator | excluded | No function-valued excitation or governing PDE operator |
| `T26` | Universal differential-equation residual | excluded | No identified dynamic state, acceleration, or initial-state contract |
| `T30` | Hysteresis and backlash memory | excluded | Forward-only curves do not contain repeated reversal loops or reset state |

## Detailed Formulations

### Analytical Discrepancy Learning

Model-discrepancy PINNs explicitly distinguish an assumed model from a learned
correction. That is the closest scientific analogue to the local problem:
PF-A explains a large part of the signal, while a network represents what the
polynomial coefficient surface omits.

The primary candidate is:

- inputs:
  `z = [speed_setpoint, torque_setpoint, temperature_setpoint]`;
- hybrid:
  `y_hat = PF_A(theta, z) + b(z) tanh(r(theta, z) / b(z))`.

The envelope `b(z)` must be estimated from training residuals only. The
unbounded version is retained as an ablation, not as the default.

Required controls are:

- PF-A alone;
- a parameter-matched data-only residual network;
- the same hybrid with a corrupted or omitted anchor;
- the accepted harmonic MLP and accepted GRU.

The hybrid is falsified if additional capacity, rather than the analytical
anchor, explains the gain. It is also falsified if the residual becomes an
unbounded replacement for PF-A.

### Complex Harmonic Coefficients

For harmonic order `k`, represent the coefficient as
`C_k = A_k exp(j phi_k) = Re(C_k) + j Im(C_k)`.

Optimize `L_complex = sum_k w_k |C_hat_k - C_k|^2`.

This avoids the discontinuity between phases near `-pi` and `pi`. The weights
are fitted or normalized on training data and frozen before held-out
evaluation.

Two related candidates are kept separate:

- `T02` predicts corrections to complex coefficients directly;
- `T07` applies a training-only complex spectral loss to a curve predictor.

The separation determines whether any gain comes from the representation or
from the objective.

### Mean And Centered Shape

The multi-head construction is:

- centered shape:
  `s_centered(theta,z) = s_raw(theta,z) - mean_theta(s_raw(theta,z))`;
- reconstructed curve:
  `y_hat(theta,z) = mu_hat(z) + s_centered(theta,z)`.

The zero-mean constraint is architectural and exact on the sampled angular
grid. It prevents the shape head from silently carrying the offset.

The matched single-head control must have comparable parameter count. A result
is accepted only when offset and centered-shape metrics improve jointly.

### Fourier Features And Exact Periodicity

For a predeclared set of angular orders `K`, the coordinate map is
`gamma(theta) = [sin(k theta), cos(k theta) for k in K]`.

This directly exposes the periodic basis and guarantees identical features at
`theta` and `theta + 2*pi`. It is preferable to learned arbitrary frequencies
as the first test because the reducer harmonics are already measurable.

The experiment must compare:

- fixed physically motivated orders;
- a raw-angle MLP;
- learned or random Fourier frequencies at the same parameter budget;
- exact periodic construction versus a soft closure penalty.

### SIREN And Wavelets

SIREN is retained because periodic activations can represent fine detail and
derivatives. Its initialization is part of the method and cannot be replaced
with an arbitrary sinusoidal MLP initialization.

Wavelets are lower priority. The current TE signal already has a strong global
harmonic representation. A wavelet network is justified only if Stage 2 and
Stage 6 show stable, localized multiscale residuals that Fourier features and
SIREN cannot resolve.

### Sobolev Guidance

The first-order angular objective is
`L_d1 = mean((d y_hat / d theta - d y_train / d theta)^2)`.

A second-order term is allowed only after:

- the derivative estimator is selected on training data;
- smoothing sensitivity is reported;
- gains reproduce under at least two reasonable derivative estimators;
- the model does not amplify unsupported high-frequency noise.

Derivative loss is training-only. Runtime inference still requires only angle
and setpoints.

### Weak-Form Harmonic Moments

For residual `r(theta,z)`, fixed test functions `psi_m(theta)` define:

- weak moment: `R_m(z) = integral r(theta,z) psi_m(theta) d theta`;
- weak loss: `L_weak = sum_m |R_m(z)|^2`.

The initial test set uses sine, cosine, and compact angular functions. The
pointwise PF-A residual is the matched control.

A small weak residual is not sufficient evidence. The method advances only if
the integrated constraint improves held-out curve metrics and remains robust
to a second predeclared test-function bank.

### Weak Compliance

The theoretical mechanics support torque-dependent deformation, but the
current data do not identify internal contact stiffness.

The only admissible real-data test is therefore a weak prior on a measurable
response derivative, such as `d mu_hat(z) / d torque`.

The sign or interval must first be stable across training-only bootstrap
resamples. A shuffled-torque prior is required as a negative control. No
parameter may be labelled physical stiffness without independent mechanical
identification.

### Temporal Analytical Residual

The strongest temporal candidate combines PF-A with a recurrent residual:
`y_hat_1:N = PF_A_1:N + bounded_GRU_residual_1:N`.

The hidden state must have deterministic initialization and reset semantics.
The candidate must beat:

- PF-A;
- the accepted GRU;
- a parameter-matched GRU without PF-A.

Beating only the analytical anchor is not enough.

## Optimization And Sampling Findings

### Instrument Before Intervention

The literature consistently shows that composite objectives can fail because
their gradients differ in scale or direction. Stage 2 must therefore record:

- each named loss;
- gradient norm per loss;
- pairwise gradient cosine;
- update-to-parameter ratios;
- adaptive weights and their effective range.

No gradient method is authorized merely because it is fashionable.

### Fixed And Adaptive Weighting

The mandatory ordering is:

1. equal weights;
2. manually normalized fixed weights;
3. gradient-statistics annealing;
4. ReLoBRaLo relative-progress balancing;
5. conflict-aware methods only after conflict is measured.

Every adaptive method must preserve a minimum contribution from the primary
data objective. Non-finite weights or data-loss collapse are immediate
failures.

### Gradient Conflict

PCGrad is modified locally so the data gradient is never projected. Only a
secondary guidance gradient may be removed from a direction that conflicts
with the primary objective.

CAGrad is a later, heavier comparator. It is not part of the first
instrumentation implementation because its additional complexity is
unjustified until multi-objective conflict is observed.

### Augmented Lagrangian

An augmented Lagrangian cannot make a wrong equation informative. It may be
used only after a weak or exact constraint shows incremental held-out signal
under a simple soft formulation.

Improving constraint feasibility while prediction worsens is a failed result,
not a successful PINN.

### Curriculum

The retained schedule is:

1. learn the data-only curve;
2. activate the analytical residual;
3. activate spectral or derivative guidance;
4. test freeze and unfreeze variants.

The control receives the same total number of updates with all losses active
from the start.

### Adaptive Sampling

Failure-informed and retain-resample-release methods can be translated to:

- angular locations;
- operating-condition cells;
- harmonic-band failures.

Scores must be cross-fitted on training data. Uniform-coverage samples remain
in every batch so the sampler cannot erase easy regions and create blind
spots.

## Sparse And Symbolic Discovery

Sparse discovery is retained as an interpretation and candidate-generation
tool, not as automatic discovery of a physical law.

The initial dictionary contains:

- polynomial speed, torque, and temperature terms;
- selected cross terms;
- fixed harmonic orders;
- condition-by-harmonic interactions;
- PF-A coefficient residuals.

Terms must pass bootstrap stability selection. Stable empirical terms can
become explicit Stage 10 ablations.

Symbolic regression follows only after this restricted library establishes
the limits of the simpler approach. Expressions must be:

- complexity bounded;
- unit safe;
- stable across resamples;
- evaluated on nested held-out conditions;
- compared with a parameter-matched MLP.

An interpretable expression is still empirical until independently connected
to a reducer mechanism.

## Uncertainty And Trust

Uncertainty is useful only if it locates error.

The retained tests are:

- deep-ensemble spread;
- condition-distance uncertainty;
- PF-A discrepancy magnitude;
- calibration by speed, torque, and temperature band;
- high-error capture rate;
- uncertainty-error rank correlation.

A uniformly wide interval fails the gate. Ensemble deployment cost is high, so
a full ensemble can advance only if its error localization is materially
useful. A distilled trust head would then need its own calibration and parity
test.

## Certification

Post-training certification is retained as a late-stage option. It cannot
certify that PF-A is the true governing physics. It may bound a selected
network residual over a normalized input domain if:

- the architecture is supported by the verifier;
- the residual has a meaningful local interpretation;
- the bound is non-vacuous;
- empirical TE error is evaluated separately.

Dense adversarial gridding is the matched control.

## Why Neural Operators Are Excluded

PINO and related neural operators learn mappings from functions to functions
over families of parametric PDEs. The current task maps four finite-dimensional
causal inputs to a periodic curve and does not expose:

- a function-valued excitation;
- a governing PDE;
- boundary-condition fields;
- multiple spatial resolutions of the same operator solution.

Using a neural operator here would add complexity without matching the local
mathematical problem. It can be reconsidered only if the instrumentation and
data contract change.

## Why Full Dynamic, MMT, Contact, And Backlash Losses Stay Out

### Universal Differential Equations

Universal differential equations require a partially known differential
system and observable state trajectory. The polished forward setpoint lane
does not identify acceleration, inertia, damping state, or initial-state
semantics.

### MMT

The MMT mapping remains scientifically valuable as a synthetic oracle.
Paper-faithful real-data calibration is still deferred because the five
equivalent-error groups and unit geometry are not independently observed.

### Contact And Energy

Contact, load sharing, friction, and energy equations are valid. The dataset
does not contain their internal forces, stiffnesses, losses, or geometry. A
network output cannot be called those quantities without independent labels or
an identifiable balance.

### Backlash And Hysteresis

Backlash is direction and history dependent. Forward-only curves do not expose
repeated reversals, minor loops, warm-up state, or deterministic reset
semantics. A backlash loss would therefore encode an assumed hidden state that
cannot be falsified in this lane.

## Controls And Falsification Contract

Every later candidate inherits these requirements.

### Mandatory Controls

- accepted GRU;
- accepted harmonic MLP;
- PF-A;
- parameter-matched data-only architecture;
- identical architecture without the proposed guidance;
- shuffled or corrupted prior when meaningful;
- equal total training budget.

### Mandatory Metrics

- raw MAE and RMSE;
- absolute offset error;
- centered-shape error;
- peak-to-peak error;
- harmonic amplitude error;
- circular harmonic phase error;
- derivative and smoothness diagnostics;
- closure mismatch;
- robustness by operating-condition cell;
- seed stability;
- inference cost and deployment feasibility.

### General Rejection Rules

A technique is rejected if:

- its own loss improves but held-out curve metrics do not;
- it beats PF-A but not its matched neural control;
- it uses a target-derived runtime quantity;
- it depends on a missing state;
- gains disappear across fixed seeds;
- improvement comes from extra parameters or training steps;
- the inference graph cannot be made inspectable;
- the result requires post-hoc test-set tuning.

## Deployment Assessment

The most deployment-friendly retained mechanisms are:

- fixed Fourier features;
- complex coefficient heads;
- mean plus centered-shape decomposition;
- sparse explicit coefficient laws;
- bounded feedforward PF-A residuals.

Moderate-risk mechanisms are:

- SIREN activations, pending ONNX and Beckhoff support;
- PF-A plus feedforward residual composition.

High-risk mechanisms are:

- recurrent analytical residuals with reset state;
- full ensembles;
- wavelet networks;
- any future dynamic or contact-state formulation.

Training-only losses and optimizers have no direct inference cost, but they
still require Python, ONNX, and PLC parity for the selected model.

## Stage Routing

The register maps techniques to the remaining roadmap.

| Next stage | Frozen work |
| --- | --- |
| Stage 2 | Gradient diagnostics, normalized weights, ReLoBRaLo, curriculum |
| Stage 3 | PF-A reproduction and corruption stress |
| Stage 4 | Data-only ladder, Fourier features, SIREN, exact periodic construction |
| Stage 5 | Complex harmonic coefficient residuals |
| Stage 6 | Spectral, Sobolev, and conditional wavelet guidance |
| Stage 7 | Mean and centered-shape heads |
| Stage 8 | Weak compliance only if bootstrap support exists |
| Stage 9 | Temporal PF-A plus bounded GRU residual |
| Stage 10 | Sparse and symbolic residual discovery |
| Stage 11 | Uncertainty and anchor-trust calibration |
| Stage 12 | Conditional PCGrad, CAGrad, augmented Lagrangian, and adaptive sampling |
| Stage 13 | Weak-form, certification, synthetic corruption, MMT, and contact oracles |
| Stage 14 | Only isolated candidates that pass matched controls |
| Stage 15 | Official verification and deployment parity |

The immediate next implementation remains Stage 2. Physics candidates are not
trained before the instrumentation can show whether the objectives cooperate
or conflict.

## Machine-Readable Evidence

The canonical Stage 1 evidence is stored under:

`output/analysis/wave_5_2r/stage1_extended_scientific_technique_discovery/`

Authored inputs:

- `stage1_source_register.yaml`;
- `stage1_technique_register.yaml`.

Generated outputs:

- `stage1_candidate_register.csv`;
- `stage1_exit_gate_summary.json`.

The validator enforces source identity, field completeness, search-family
coverage, causal-variable allowlists, missing-variable exclusion, and the
absence of target-derived runtime quantities.

Validation result:

| Result field | Value |
| --- | ---: |
| Status | `WAVE52R_STAGE1_VALIDATION_OK` |
| Techniques | `30` |
| Real-data techniques | `24` |
| Oracle-only techniques | `3` |
| Excluded techniques | `3` |
| Search families | `13` |

The `24` real-data count contains `13` active and `11` conditional techniques.

## Exit-Gate Audit

| Gate | Result | Evidence |
| --- | --- | --- |
| All required search families covered | pass | `13 / 13` |
| Every technique has a source | pass | `30 / 30` |
| Every technique has a local formulation | pass | `30 / 30` |
| Every technique has a matched control | pass | `30 / 30` |
| Every technique has a falsification rule | pass | `30 / 30` |
| Every technique has deployment assessment | pass | `30 / 30` |
| Real-data roster has no missing variables | pass | `0` violations |
| Target-derived runtime variables | pass | `0` |
| Unobservable mechanisms excluded or oracle-only | pass | explicit roster |
| Candidate register frozen | pass | content-hashed YAML and JSON summary |

**Decision:** freeze the Stage 1 candidate register and authorize Stage 2,
Evaluation And Optimization Instrumentation.

This authorization is for non-training Stage 2 implementation and validation.
Any later training campaign retains the repository campaign-plan and explicit
training-approval gates.

## Primary References

1. Bauer et al., Modeling Load-, Velocity-, and Temperature-Dependent
   Transmission Errors of Cycloidal Drives for Industrial Robots Using Fourier
   Series, IEEE ICIT 2025, repository copy at
   `reference/te_modeling/bibliography/polynomial_fourier/2025_bauer_load_velocity_temperature_dependent_cycloidal_te_fourier_model.pdf`.
2. Zou, Meng, and Karniadakis, Correcting model misspecification in PINNs,
   arXiv `2310.10776`.
3. Kharazmi, Zhang, and Karniadakis, Variational Physics-Informed Neural
   Networks, arXiv `1912.00873`.
4. Wang, Teng, and Perdikaris, Understanding and mitigating gradient
   pathologies in PINNs, arXiv `2001.04536`.
5. Bischof and Kraus, Multi-Objective Loss Balancing for Physics-Informed
   Deep Learning, DOI `10.1016/j.cma.2025.117914`.
6. Yu et al., Gradient Surgery for Multi-Task Learning, NeurIPS 2020.
7. Liu et al., Conflict-Averse Gradient Descent, NeurIPS 2021.
8. Rahaman et al., On the Spectral Bias of Neural Networks, ICML 2019.
9. Tancik et al., Fourier Features Let Networks Learn High Frequency
   Functions, NeurIPS 2020.
10. Sitzmann et al., Implicit Neural Representations with Periodic Activation
    Functions, NeurIPS 2020.
11. Son et al., Sobolev Training for Physics Informed Neural Networks,
    arXiv `2101.08932`.
12. Brunton, Proctor, and Kutz, Sparse identification of nonlinear dynamical
    systems, DOI `10.1073/pnas.1517384113`.
13. Udrescu and Tegmark, AI Feynman, DOI `10.1126/sciadv.aay2631`.
14. Perez et al., Adaptive weighting of Bayesian PINNs, DOI
    `10.1016/j.jcp.2023.112342`.
15. Krishnapriyan et al., Characterizing possible PINN failure modes,
    NeurIPS 2021.
16. Gao, Yan, and Zhou, Failure-informed adaptive sampling for PINNs, arXiv
    `2210.00279`.
17. McClenny and Braga-Neto, Self-Adaptive PINNs, arXiv `2009.04544`.
18. Lu et al., Augmented-Lagrangian PINNs, arXiv `2205.01059`.
19. Eiras et al., Efficient Error Certification for PINNs, arXiv
    `2305.10157`.
20. Li et al., Physics-Informed Neural Operator, arXiv `2111.03794`.
21. Uddin et al., Wavelet-based PINNs, DOI
    `10.1038/s41598-023-29806-3`.
22. Rackauckas et al., Universal Differential Equations, arXiv
    `2001.04385`.
23. Sukumar and Srivastava, Exact imposition of constraints with distance
    functions, arXiv `2104.08426`.
24. Daw et al., Retain-Resample-Release sampling, ICML 2023.
25. Hybrid modelling and identification of mechanical systems using
    Physics-Enhanced Machine Learning, DOI
    `10.1016/j.engappai.2025.111762`.

Direct source URLs and retained claims are preserved in
`stage1_source_register.yaml`.

## Conclusion

Stage 1 expands the PINN program without weakening scientific discipline.

The most promising direction is not a monolithic full-PINN with every theory
inserted as a loss. It is a controlled sequence of hybrids:

- exact periodic representation;
- strong Polynomial-Fourier anchor;
- bounded learned discrepancy;
- direct complex harmonic and derivative supervision;
- explicit mean and shape decomposition;
- weak mechanics only where the data support the prior;
- optimization methods activated only after their failure mode is measured.

The network can compensate for missing analytical detail. It cannot make
unmeasured mechanical states identifiable. The frozen roster preserves both
facts and provides a falsifiable path through Stages 2 through 15.
