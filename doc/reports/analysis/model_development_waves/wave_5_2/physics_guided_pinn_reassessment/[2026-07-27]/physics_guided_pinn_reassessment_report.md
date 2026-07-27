# Physics-Guided PINN Reassessment For Polished Setpoint Forward TE

## Executive Decision

Physics can still help the transmission-error predictor, and the completed
Wave 5.2 results do not demonstrate otherwise.

They demonstrate a narrower and more useful result: the specific oscillator,
periodic-closure, Bauer-anchor, and quasi-static compliance formulations tested
in Phases 2 and 3 did not pass the complete forward curve-first promotion gate.
Several constraints were mathematically valid and active during optimization,
but they either imposed behavior already present in the data, redistributed
error among harmonic orders, introduced an unstable anchor, or produced a
seed-dependent predictive benefit.

The correct next strategy is therefore neither to abandon physics nor to add
more unqualified loss terms. It is to treat physics as a hierarchy of
falsifiable inductive biases:

1. preserve exact structural facts through architecture where possible;
2. use the Polynomial-Fourier law as an inspectable analytical baseline;
3. assign the neural network only the discrepancy that the analytical model
   cannot explain;
4. supervise the error in curve, derivative, and complex harmonic spaces;
5. balance objectives dynamically and measure gradient conflict;
6. promote a physical ingredient only when it improves the accepted forward
   baseline on a stable, multi-index, held-out evaluation.

This report and its companion roadmap are restricted to:

- dataset: `polished_dataset`;
- input mode: `setpoints`;
- surface: `Fw`;
- operating coordinates: angle, speed setpoint, torque setpoint, and
  temperature setpoint;
- causal deployment target: explicit TwinCAT-compatible inference.

No `Bw`, global paired surface, actual-values input, simplified dataset, or
paper-faithful MMT experiment is part of this plan.

## What A PINN Can Mean In This Project

A physics-informed neural network is not required to contain a complete
first-principles model of the reducer. It must, however, contain a precise and
testable statement of domain knowledge that changes the learning problem.

### Five Levels Of Physics Guidance

| Level | Mechanism | Project example | Qualification |
| --- | --- | --- | --- |
| Structural representation | The architecture can only produce admissible forms | exact periodic basis in angle | strong inductive bias, not a governing law by itself |
| Weak physical prior | Penalize implausible signs, bounds, or roughness | positive bounded compliance | physics-guided if the bound has a source and an ablation |
| Compatibility equation | Enforce a relation among observable quantities | periodic value and slope closure | genuine constraint, but may be redundant |
| Analytical plus learned residual | Preserve a known model and learn its discrepancy | Bauer Polynomial-Fourier plus neural residual | grey-box physics-informed model |
| Governing residual | Penalize a differential or algebraic law | oscillator or compliance residual | full PINN when observable and identifiable |

This classification prevents two opposite errors:

- calling every Fourier feature a physical law;
- rejecting every incomplete physical model because it is not a complete
  contact solver.

### Incomplete Physics Can Be Useful

The most practical formulation is
`TE_prediction(theta, u) = TE_analytical(theta, u) +`
`residual_neural_network(theta, u)`, where
`u = [speed_setpoint, torque_setpoint, temperature_setpoint]`.

The analytical component supplies a low-complexity explanation of the dominant
periodic structure. The network compensates for missing interactions,
non-polynomial coefficient surfaces, local ripple, and systematic discrepancy.

This is exactly where a neural network can compensate for an incomplete model.
It does not make the analytical model true. It makes the model discrepancy
explicit, measurable, and separable.

The main risk is cancellation: an unconstrained residual can learn the negative
of the analytical component and turn the system into an opaque black box.
Every hybrid experiment must therefore report:

- analytical contribution magnitude;
- residual contribution magnitude;
- correlation between analytical and residual terms;
- residual energy inside and outside the analytical harmonic subspace;
- sensitivity to analytical-anchor corruption;
- performance when the anchor is frozen, partially trainable, or removed.

## What The Dataset Actually Supports

### Frozen Foundation

The completed Phase 0 audit established:

- `969` paired operating conditions;
- `966` Phase 1 eligible conditions after three metadata quarantines;
- `678 / 194 / 97` train, validation, and test conditions before exclusions;
- a stable split signature of
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- a full Cartesian grid of speed, torque, and temperature setpoints;
- one output-equivalent revolution per directional curve;
- causal angle, speed, signed torque, oil temperature, and direction;
- no held-out axis values absent from training;
- no out-of-domain extrapolation condition in the current split.

For this forward-only plan, the split is preserved but only the eligible `Fw`
surface is consumed.

### Strong Forward Harmonic Evidence

The Phase 0 forward prevalence ranking begins with orders `1, 39, 3, 40, 78,
240, 81, 159, 2, 156, 162, 80, 120, 237, 42`.

Order `1` has mean truth amplitude close to `0.0172 deg`. Orders `39`, `78`,
`40`, and `3` form the next strongest forward group in the Phase 2 analysis.

This proves three things:

1. the output is strongly periodic in the angular coordinate;
2. a small set of orders contains substantial repeatable information;
3. the amplitude and phase of those orders remain prediction targets whose
   condition dependence must be learned.

It does not prove that every prevalent order maps uniquely to one physical
component. Mechanism attribution remains a hypothesis unless the reducer
geometry and excitation path support it.

### Unsupported Forward-Only Claims

The current scope cannot identify:

- directional lost motion from an `Fw/Bw` difference;
- a backlash gap from forward curves alone;
- a hysteresis state without repeated loops and reset evidence;
- acceleration and inertia effects from nearly steady directional windows;
- contact force, load sharing, clearance, or mesh stiffness;
- input power, internal loss, or efficiency balance;
- wear progression without unit identity and longitudinal history;
- electromechanical sidebands without synchronized motor current;
- MMT equivalent-error groups without condition-varying causal measurements.

These mechanisms remain scientifically relevant. They cannot be inserted as
identified forward residuals under the present data contract.

## What Was Demonstrated Before This Reassessment

### Polynomial-Fourier Analytical Baseline

The Bauer-style law represents TE as a sum of harmonics whose offset,
amplitude, and phase vary with operating condition:
`TE_PF(theta, u) = a0(u) +`
`sum_k A_k(u) * sin(k * theta + phi_k(u))`.

Each coefficient surface can be a complete quadratic polynomial of the three
operating variables. In Phase 1, the selected
`PF_A_LOCAL_QUADRATIC` forward model achieved:

| Metric | `PF_A_LOCAL_QUADRATIC` `Fw` |
| --- | ---: |
| Mean raw MAE | `0.001807 deg` |
| Mean centered MAE | `0.001385 deg` |
| Mean offset error | `0.000965 deg` |

The reduced `PF_E_REDUCED_QUADRATIC` model was slightly weaker. The recovered
ONNX coefficient path achieved `0.003047 deg` mean raw MAE on the common
forward test surface. The recovered PLC degree-10 polynomial was numerically
unsafe across the broader forward torque domain. The direct per-curve Fourier
oracle reached approximately `0.00031 deg`, proving representational capacity
while remaining target-leaking and non-deployable.

The key gap is visible: the deployable quadratic Polynomial-Fourier law leaves
substantial distance to the direct Fourier ceiling. This is a rational place
for a learned residual.

### Harmonic And Kinematic PINN Screen

Phase 2 compared:

- `H0`: explicit Fourier data-driven control;
- `H1`: implicit harmonic heads with normalized oscillator residual;
- `H2`: oscillator residual plus periodic value and slope closure;
- `H3`: the same constraints plus a frozen Bauer anchor.

The normalized oscillator residual for each order was
`R_k = (1 / k^2) * d2(h_k) / d(theta)^2 + h_k`.

The validator proved that the residual was correct, differentiable, finite,
and active in optimization. Nevertheless, the forward scalar MAE was:

| Candidate | Forward test MAE |
| --- | ---: |
| `H0` Fourier control | `0.001646 deg` |
| `H2` oscillator plus periodic closure | `0.001784 deg` |
| `H1` oscillator | `0.001951 deg` |
| `H3` oscillator, closure, and Bauer | `0.002389 deg` |

On the full held-out forward curves, both accepted references remained
stronger:

| Candidate | Raw MAE | Amp. error | Phase error |
| --- | ---: | ---: | ---: |
| accepted periodic GRU | `0.001618` | `19.237%` | `12.167 deg` |
| accepted periodic harmonic MLP | `0.001694` | `15.380%` | `13.592 deg` |
| Phase 2 `H0` | `0.001998` | `39.328%` | `21.029 deg` |
| Phase 2 `H1` | `0.002232` | `43.016%` | `19.899 deg` |
| Phase 2 `H2` | `0.002102` | `49.491%` | `20.335 deg` |
| Phase 2 `H3` | `0.002651` | `69.329%` | `27.110 deg` |

The periodic-slope term reduced its own residual by several orders of
magnitude. The original curves already had approximately `0.0009 deg` closure
mismatch, so optimizing closure added little useful information.

This is a textbook case of a valid constraint being redundant rather than
wrong.

### Quasi-Static Compliance PINN Screen

Phase 3 tested learned-mean controls, soft compliance derivatives,
temperature-conditioned stiffness, nonlinear compliance, hard elastic
equations, and shared-stiffness compatibility.

The best forward candidate, `C1`, used
`d(mean_TE) / d(tau_signed) = 1 / k_forward`.

with positive bounded stiffness. On the forward full-curve screen:

| Candidate | Raw MAE | Offset | Centered MAE | Amp. error | Phase |
| --- | ---: | ---: | ---: | ---: | ---: |
| accepted periodic GRU | `0.001618` | `0.000690` | `0.001382` | `19.237%` | `12.167 deg` |
| accepted periodic MLP | `0.001694` | `0.000825` | `0.001390` | `15.380%` | `13.592 deg` |
| `C1` | `0.001843` | `0.000932` | `0.001481` | `34.128%` | `21.434 deg` |
| `C0` control | `0.001953` | `0.000989` | `0.001608` | `40.930%` | `22.373 deg` |

`C1` improved every listed metric except peak-to-peak error relative to its
matched `C0` control. Its fitted stiffness was also stable:

- mean: `28,164.36 Nm/deg`;
- population coefficient of variation: `2.48%`.

However, only two of three initializations passed the predeclared joint gate.
The physical parameter was stable while the predictive gain was not.

This is important positive information. Compliance is not disproved. The
tested joint optimization is not yet reliable enough to become a default
ingredient.

## Why Valid Physics Did Not Automatically Improve Prediction

### Redundant Information

If the architecture already uses exact Fourier heads, an oscillator residual
may merely restate the definition of those heads. If the measured curve is
already nearly periodic, a stronger closure loss spends gradient budget on an
almost-solved objective.

The next experiments must quantify the incremental information in each
constraint before training.

### Loss-Scale And Gradient Conflict

PINNs are multi-objective optimizers. A small reported residual does not imply
that the residual helped the data objective. Different terms can have:

- incompatible gradient directions;
- orders-of-magnitude gradient differences;
- different convergence rates;
- different noise sensitivities;
- incompatible optima under model misspecification.

The new roadmap therefore requires per-loss gradient norms, cosine
similarities, and weight trajectories. Fixed physics weights will be controls,
not the only strategy.

### Model Misspecification

The Bauer law is semi-analytical and incomplete. Compliance is only one
component of mean TE. Harmonic orders may be correct while their coefficient
surfaces are too rigid.

A hard or strongly weighted imperfect model can bias the network away from the
measured surface. The solution is not to hide the mismatch; it is to model it
explicitly through a bounded discrepancy branch.

### Identifiability

Low prediction error does not prove that a learned stiffness, phase law, or
latent state is physically correct. Multiple decompositions can reconstruct
the same curve.

The roadmap separates:

- predictive promotion;
- parameter stability;
- mechanism identification;
- deployment usefulness.

A model may be accepted for prediction without claiming that every latent
quantity is a uniquely identified physical parameter.

### Spectral Competition

The Phase 2 results showed improvement in some harmonic orders and regression
in others. Aggregate pointwise loss can hide this redistribution.

The new loss design must distinguish:

- low-order shape;
- reducer-related middle orders;
- fragile high-order ripple;
- offset;
- complex amplitude and phase;
- residual energy outside the selected basis.

## Candidate Physics-Guided Formulations

### A. Polynomial-Fourier Plus Bounded Residual

The proposed prediction law is
`TE_hat = TE_PF_A + alpha(u) * r_theta(theta, u)`.

where `alpha(u)` is bounded and the residual network is capacity-limited.

Required ablations:

- pure `PF-A`;
- identical residual network without `PF-A`;
- frozen `PF-A` plus residual;
- partially trainable coefficient correction;
- corrupted `PF-A` anchor plus residual;
- residual with and without analytical-subspace exclusion.

This is the highest-priority family because every inference quantity is
available and the analytical baseline is already reproduced.

### B. Coefficient-Residual Model

Instead of correcting the curve pointwise, predict corrections to offset and
complex harmonic coefficients:
`c_k(u) = c_k_PF(u) + delta_c_k(u)`, with
`c_k = a_k - i * b_k`.

Using sine and cosine or complex coefficients avoids phase-wrap discontinuity.
Amplitude and phase can be derived for reporting.

Advantages:

- exact periodic reconstruction;
- lower-dimensional learned output;
- inspectable condition dependence;
- direct harmonic-band regularization;
- straightforward PLC realization.

Risks:

- retained orders may omit local structure;
- coefficient errors can interact nonlinearly in amplitude and phase;
- a direct coefficient target must be computed from training curves only.

### C. Mean Plus Centered-Shape Decomposition

The prediction is
`TE_hat(theta, u) = mean_head(u) + centered_shape_head(theta, u)`, with
`integral(centered_shape_head dtheta) = 0`.

The zero-mean property should be imposed by construction, not by a large loss.
This separates offset learning from angular shape learning.

Candidate auxiliary outputs:

- mean TE;
- peak-to-peak TE;
- selected complex harmonic coefficients;
- derivative or curvature summaries;
- bounded compliance slope as a diagnostic head.

### D. Weak Compliance Guidance

Compliance should return as a weak, staged prior rather than an immediate hard
equation. The proposed loss is
`L_compliance = penalty_negative(d mean_TE / d tau) +`
`penalty_outside_source_bound(k_effective)`.

The exact derivative target should not be forced uniformly across all
conditions unless supported by the data. The candidate can use:

- sign-only monotonicity;
- broad stiffness interval;
- temperature-stratified interval;
- confidence-weighted penalty;
- warm-started activation after data convergence.

### E. Spectral And Sobolev Objectives

For each held-out or training curve:

- `L_complex_k = abs(c_k_prediction - c_k_truth)^2`;
- `L_slope = mean(abs(dTE_prediction/dtheta - dTE_truth/dtheta))`;
- `L_band = sum_k w_k * L_complex_k`.

This is supervised shape guidance, not a governing physical law. It is
nevertheless valuable because it targets the exact failure mode observed in
Phase 2.

The physically informed element comes from the selection and grouping of
orders, the analytical basis, and any source-backed coefficient constraints.

### F. Temporal Residual Model

The accepted forward GRU remains the strongest time-windowed reference.
A temporal hybrid can use
`TE_hat_t = TE_PF(theta_t, u_t) + GRU_residual(history_t)`.

This is appropriate only if the history inputs remain causal and no
target-derived state is used at inference. It should be compared against:

- the accepted GRU;
- a parameter-matched residual GRU without analytical anchor;
- a non-windowed residual MLP.

### G. Conditional Periodic Implicit Representation

Fourier-feature MLP and SIREN-style variants can represent high-frequency
coordinate functions and their derivatives. They are candidates for the
centered-shape or residual branch, not physical laws.

They should be tested only after the explicit harmonic models because:

- explicit orders are more inspectable;
- periodic activations can create unwanted frequencies;
- initialization and bandwidth are critical;
- deployment cost may exceed a compact coefficient model.

### H. Weak-Form Harmonic Residual

A variational residual integrates the equation against test functions instead
of enforcing high-order derivatives pointwise:
`R_j = integral(R(theta, u) * v_j(theta) dtheta)`.

For the TE problem, test functions can be localized Fourier or polynomial
windows. This may reduce derivative noise and reveal where a pointwise
oscillator constraint is redundant.

It should be evaluated as an ablation against direct complex-coefficient loss.
If both encode the same information, the simpler coefficient loss wins.

### I. Sparse Residual Discovery

Sparse identification can screen a controlled dictionary of condition and
harmonic interactions. The initial library contains `1`, `tau`, `speed`,
`temperature`, their squares and pairwise products, `sin(k*theta)`,
`cos(k*theta)`, and condition-harmonic interaction terms.

The goal is not to declare a newly discovered physical law from one dataset.
It is to find parsimonious candidate terms for a later interpretable model.

Selection must occur on training conditions only and be validated on held-out
conditions.

## Deep Technique Discovery

The following external techniques were reviewed for project relevance.

| Technique | Main idea | Forward TE relevance | Priority |
| --- | --- | --- | --- |
| Gradient-statistics annealing | balance composite loss gradients | directly addresses Phase 2 and 3 objective imbalance | high |
| ReLoBRaLo or related adaptive weighting | weight objectives by relative learning progress | useful for curve, spectral, and weak-physics losses | high |
| Gradient conflict diagnostics or PCGrad | detect or project conflicting task gradients | useful before accepting any multi-head benefit | high |
| Curriculum regularization | activate difficult physics progressively | avoids early domination by imperfect residuals | high |
| Model-discrepancy PINNs | learn an explicit correction to misspecified physics | direct match to Bauer plus residual | high |
| Fourier features | increase learnable angular bandwidth | useful residual or centered-shape ablation | medium-high |
| SIREN | periodic activations with accurate derivatives | useful coordinate-network ablation | medium |
| Sobolev training | supervise derivatives as well as values | matches slope and ripple fidelity objectives | high |
| VPINN or weak form | enforce integrated residuals with lower derivative order | useful oscillator and local-band ablation | medium |
| Failure-informed sampling | focus collocation on high-residual regions | useful only if angular or condition errors are localized | medium |
| Augmented Lagrangian constraints | separate constraint satisfaction from fixed penalties | useful for exact closure or bounds if soft loss fails | medium |
| Universal differential equations | replace missing terms in a known differential model | strong future pattern; current steady `Fw` law is limited | medium-low |
| Sparse equation discovery | select parsimonious interaction terms | useful offline formulation discovery | medium |
| Bayesian or ensemble discrepancy | quantify trust in physics and residual branches | useful near domain boundaries and for deployment | medium |
| Neural operators | learn maps between function spaces | possible only with a richer curve-to-curve input contract | low now |
| Formal residual certification | bound worst-case continuous residual | valuable after a candidate exists, not an initial model | later |

### Research Interpretation

The literature reinforces five lessons.

1. Composite PINN losses commonly suffer from gradient imbalance.
2. Harder physics does not guarantee better optimization.
3. High-frequency behavior requires architectural and loss-level attention.
4. Imperfect physics should be paired with an explicit discrepancy model.
5. Residual satisfaction and predictive accuracy must be validated separately.

These lessons align closely with the local Wave 5.2 evidence.

## Techniques Deliberately Excluded From The Active Forward Plan

| Technique or mechanism | Reason for exclusion |
| --- | --- |
| Directional backlash gap | requires bidirectional or loop evidence |
| Bouc-Wen or rolling-friction state | no repeated forward loops or reset contract |
| Dynamic inertia residual | current forward windows are nearly steady and inertia is unavailable |
| Contact and mesh-force PINN | contact state, stiffness, clearance, and force are unavailable |
| Energy-balance PINN | input power and internal losses are unavailable |
| MMT paper-faithful residual | condition-varying equivalent-error inputs are unavailable |
| Wear or degradation state | no longitudinal reducer identity or load-cycle history |
| Electromechanical residual | no synchronized motor current or sideband evidence |
| Forward neural operator | no function-valued causal input justifying the additional complexity |

Exclusion means “not identifiable in this data contract,” not “physically
invalid.”

## Revised Experimental Logic

### Separate Representation From Physics

Every candidate must declare which improvement is being tested:

- representation capacity;
- analytical prior;
- weak physical constraint;
- optimization strategy;
- temporal information;
- uncertainty model.

No experiment may change all of them simultaneously.

### Use A Ladder Of Controls

For every hybrid:

1. accepted periodic GRU;
2. accepted periodic harmonic MLP;
3. pure analytical `PF-A`;
4. parameter-matched black-box;
5. analytical plus residual without physics loss;
6. analytical plus residual with one physics ingredient.

This ladder tells us whether a gain comes from physics, extra parameters, or a
better representation.

### Require Stable Evidence

Every promotable training configuration requires:

- at least three fixed seeds;
- identical condition split and angular evaluation;
- no target-derived inference input;
- complete checkpoint and loss-weight provenance;
- no unreported failed run;
- parameter and gradient diagnostics;
- full-resolution forward curve replay.

### Measure More Than MAE

Required forward metrics:

- raw MAE and RMSE;
- absolute mean-offset error;
- mean-centered MAE;
- peak-to-peak relative error;
- derivative MAE and correlation;
- complex coefficient error by selected order;
- amplitude and phase error;
- P95 per-curve error;
- worst operating-cell degradation;
- residual-to-anchor energy ratio;
- seed dispersion;
- inference cost and numerical range.

### Add Boundary Tests

The current held-out split is interpolation over supported axis values.
Additional evaluation should create training-only boundary holdouts such as:

- maximum and minimum torque bands;
- maximum and minimum speed bands;
- temperature-level holdout;
- corner-cell holdouts;
- harmonic-amplitude extremes.

These are experimental splits, not replacements for the canonical split.

## Answer To The Central Question

Yes: the neural network can compensate for missing parts of an incomplete
physical model.

It will help only when the physical component contributes information that is
useful, correctly scaled, observable, and not already encoded by the network.
The network must then have enough freedom to model the discrepancy without
being allowed to erase the analytical structure invisibly.

The completed tests were valuable because they exposed exactly where naive
physics insertion fails:

- mathematically true but redundant constraints;
- correct local effects that do not improve the complete curve;
- unstable optimization across seeds;
- physical parameters that are stable without sufficient predictive gain;
- mechanisms that are real but unobservable in the available data.

The next full-PINN effort should therefore begin with the strongest observable
physics: angular periodic structure, condition-dependent harmonic
coefficients, an explicit Polynomial-Fourier anchor, and carefully bounded
forward compliance. It should combine them with discrepancy learning,
frequency-resolved supervision, and modern multi-objective optimization.

## Program Decision

The previous sixteen-phase Wave 5.2 evidence closeout remains valid. This
report does not retroactively promote a rejected residual.

It creates the new forward-only `Wave 5.2R: Physics-Guided Forward
Reassessment` branch for `polished_dataset / setpoints / Fw`.

Wave 5.2R is currently a documented roadmap, not an authorized training
campaign. Each bounded implementation or campaign stage requires its own
technical document, campaign plan where applicable, explicit approval, and
curve-first closeout.

## Local Evidence

- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`
- `doc/reference_summaries/11_Hysteresis_Backlash_And_Harmonic_TE_Reference_Synthesis.md`
- `doc/reference_summaries/12_ML_Compensation_Reference_Synthesis.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/phase0_pinn_program_foundations_report.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/polynomial_fourier_benchmark/[2026-07-25]/phase1_polynomial_fourier_analytical_benchmark_report.md`
- `doc/reports/campaign_results/wave_5_2/2026-07-26-16-53-50_phase2_harmonic_kinematic_pinn_campaign_results_report.md`
- `doc/reports/campaign_results/wave_5_2/2026-07-26-20-13-18_phase3_quasi_static_compliance_pinn_campaign_results_report.md`

## External Scientific References

- Rackauckas et al., Universal Differential Equations for Scientific Machine
  Learning, arXiv:2001.04385.
- Wang, Teng, and Perdikaris, Understanding and Mitigating Gradient
  Pathologies in Physics-Informed Neural Networks,
  arXiv:2001.04536.
- Kharazmi, Zhang, and Karniadakis, Variational Physics-Informed Neural
  Networks for Solving Partial Differential Equations,
  arXiv:1912.00873.
- McClenny and Braga-Neto, Self-Adaptive Physics-Informed Neural Networks
  Using a Soft Attention Mechanism,
  arXiv:2009.04544.
- Bischof and Kraus, Multi-Objective Loss Balancing for Physics-Informed Deep
  Learning, arXiv:2110.09813.
- Krishnapriyan et al., Characterizing Possible Failure Modes in
  Physics-Informed Neural Networks,
  arXiv:2109.01050.
- Zou, Meng, and Karniadakis, Correcting Model Misspecification in
  Physics-Informed Neural Networks,
  arXiv:2310.10776.
- Tancik et al., Fourier Features Let Networks Learn High Frequency Functions
  in Low Dimensional Domains,
  arXiv:2006.10739.
- Sitzmann et al., Implicit Neural Representations with Periodic Activation
  Functions, arXiv:2006.09661.
- Czarnecki et al., Sobolev Training for Neural Networks,
  arXiv:1706.04859.
- Son et al., Sobolev Training for Physics-Informed Neural Networks,
  arXiv:2101.08932.
- Gao, Yan, and Zhou, Failure-Informed Adaptive Sampling for PINNs,
  arXiv:2210.00279.
- Brunton, Proctor, and Kutz, Discovering Governing Equations from Data:
  Sparse Identification of Nonlinear Dynamical Systems,
  arXiv:1509.03580.
- Yu et al., Gradient Surgery for Multi-Task Learning,
  arXiv:2001.06782.
- Eiras et al., Efficient Error Certification for Physics-Informed Neural
  Networks, arXiv:2305.10157.
