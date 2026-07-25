# RV Reducer Theoretical Mechanics Reference Synthesis

## Scope

This document distills the eight sources under
`reference/te_modeling/theoretical_mechanics/`. These papers contain the richest
first-principles material in the imported bundle, but most require geometry,
contact, stiffness, inertia, or wear variables that are not currently measured
in the repository dataset.

## Source-By-Source Findings

### Wang And Coauthors, 2024: Nonlinear Transmission Efficiency

The paper builds a force and loss analysis spanning the cycloidal drive, output
mechanism, and bearings. It distinguishes load-dependent and load-independent
losses and predicts nonlinear transient efficiency under multi-source errors.
At constant load, average efficiency decreases with increasing speed; at
constant speed, it increases with load.

Use for this project:

- auxiliary force, work, or energy consistency;
- regime checks at low speed, where multi-source errors have the strongest
  efficiency effect;
- not a direct TE residual without force, friction, and loss measurements.

### Xu And Coauthors, 2025: Dynamic TE Under Variable Speed

The work combines a dynamic contact model with geometric errors and compares
two acceleration and deceleration laws. It identifies angular acceleration and
load inertia as dominant TE drivers.

Reported examples include:

- without load inertia, variable-speed TE increases by about 6.3 and
  5.1 percent for the two drive laws;
- with inertia, the increase reaches about 494.3 and 599.9 percent;
- a 28.2 percent inertia increase raises TE from `8.208` to `10.732 arcmin`
  for one drive law and from `9.666` to `11.613 arcmin` for the other;
- an 81.8 percent acceleration increase raises TE from `3.221` to
  `4.347 arcmin` and from `3.833` to `5.241 arcmin`.

Use for this project:

- speed is not a sufficient dynamic input;
- acceleration, load inertia, and recent trajectory may be required for
  variable-speed tests;
- the current dataset must be audited for causal acceleration and inertia
  availability before a dynamic residual is proposed.

### Xu And Coauthors, 2025: Hysteresis, Rigidity, And Lost Motion

The paper constructs a dynamic contact model for hysteresis curves, torsional
rigidity, and lost motion. Support-bearing stiffness most strongly affects
torsional rigidity, while swivel-arm-bearing radial clearance strongly affects
lost motion. Geometric errors lower rigidity and increase lost motion.

The reported high-, moderate-, and low-precision examples give torsional
rigidity values of `131.98`, `125.55`, and `117.41 Nm/arcmin`, with lost motion
of `0.364`, `0.389`, and `0.412 arcmin`.

Use for this project:

- possible bidirectional stiffness and lost-motion constraints;
- evidence that loading smoothness and rate can affect the measured loop;
- blocked as a full contact residual until bearing stiffness, clearances,
  interface stiffness, and torque-loading history are available.

### E And Coauthors, 2026: Electromechanical Coupling And Fault Diagnosis

This source couples a PMSM model, translational and torsional RV dynamics, and
time-varying cycloid-pin stiffness. Fault signatures appear as current
sidebands around supply and mesh-related orders, spaced by crankshaft or
cycloidal-disc rotational components. The study includes test-rig and robot
validation.

Use for this project:

- health-state validation and frequency-sideband interpretation;
- possible future electromechanical consistency if motor current becomes an
  input;
- not a nominal TE residual with the current signal set.

### Wang And Coauthors, 2024: Bidirectional Drive TE

The paper derives forward and reverse TE and global lost motion using measured
multi-source errors and explicit pin-gear equivalence assumptions. It shows
that the output mechanism is not negligible and argues that forward TE,
reverse TE, and global lost motion must be assessed together.

The proposed model reports deviations of approximately `-6.8`, `-5.5`, and
`-5.7 percent` on its three principal comparison quantities, improving on the
alternative assumptions considered by the authors.

Use for this project:

- strongest source-backed reason to retain separate `Fw`, `Bw`, and global
  surfaces;
- candidate compatibility relation among directional TE and lost motion;
- paper-faithful evaluation is blocked by unavailable component-error
  measurements and geometry-specific equivalence parameters.

### Jin And Coauthors, 2025: Tolerance Virtual Prototype

The paper builds a SolidWorks, RecurDyn, and Adams virtual prototype and reports
agreement within five percent across five physical prototypes. It combines
single-factor sensitivity with an L16 orthogonal tolerance experiment.

Important tolerances include crank eccentricity, moved and equidistant
modification, pinwheel runout, and pin radius. The proposed optimization
tightens crank eccentricity and equidistant modification tolerances from
`0.006` to `0.004 mm`.

Use for this project:

- manufacturing priors and parameter-sensitivity ranking;
- synthetic geometry perturbation and uncertainty tests;
- not an inference-time residual unless the unit-specific tolerances are known.

### Chen And Coauthors, 2026: Geometric Errors And Wear

The source combines Archard wear, a 20-degree-of-freedom quasi-static
mass-spring model, tooth and load contact analysis, Hertz contact, and iterative
geometry updates. It considers eleven error sources.

The cycloidal-stage and cam-eccentricity effects dominate precision, while
planetary-stage errors are smaller in the reported setup. Wear progression
correlates with TE degradation. The reported maximum relative bearing-force
error is about 8.89 percent, the maximum TE precision error is about
6.31 percent, and theoretical versus measured TE is `23.32` versus
`25.5 arcsec`.

Use for this project:

- a latent wear or health state for long-horizon monitoring;
- contact-load and non-penetration oracle tests;
- blocked as an operational PINN residual by missing geometry, contact, force,
  lubrication, and wear-state observations.

### Wang And Coauthors, 2026: Ensemble TE Prediction And Optimization

The paper combines finite-element simulations, Latin hypercube sampling, and
orthogonal and variance analysis across eight error variables. A stacked
surrogate uses SVR, XGBoost, random forest, and K-nearest neighbors with an
XGBoost meta-learner.

The reported model improves `R2` by 14.3 percent and reduces RMSE by
27.4 percent relative to the best single learner. Differential-evolution
optimization reduces peak-to-peak TE by 52.48 percent. The study excludes
clearance, dynamic load, friction, and thermal effects.

Use for this project:

- synthetic oracle generation and sensitivity screening;
- comparison of physics simulators and learned surrogates;
- not a full PINN solely because the training labels originate from FEA.

## Cross-Source Physics Map

| Phenomenon | Required state beyond current basic inputs | Near-term role |
| --- | --- | --- |
| Angular periodicity | Angular coordinate and reducer geometry | Directly testable |
| Bidirectional lost motion | Direction, loading path, component errors | Partial compatibility test |
| Elastic compliance | Torque, stiffness, temperature, direction | Bounded intermediate model |
| Dynamic TE | Acceleration, load inertia, trajectory | Dataset observability audit |
| Contact and load sharing | Clearances, stiffness, forces, geometry | Synthetic oracle or future instrumentation |
| Efficiency and friction | Force, speed, loss, temperature | Auxiliary consistency only |
| Wear progression | Geometry history, load cycles, wear state | Future latent-state program |
| Electromechanical faults | Motor current and drive state | Future health-monitoring branch |

## Full-PINN Consequences

The sources do not support one monolithic residual with all mechanisms. They
support a staged program:

1. establish the explicit direction-specific periodic baseline;
2. audit a simple compliance or bidirectional compatibility law;
3. test whether acceleration and history add causal value;
4. use detailed contact and wear models as synthetic oracles until their
   variables become observable;
5. introduce one physical law per bounded pilot.

The first implementation should not fit unobserved stiffness, friction,
clearance, wear, and component-error parameters simultaneously. Such a model
would be weakly identifiable even if it achieved low TE error.

## TwinCAT Implications

- Prefer algebraic periodic and compliance terms for the first deployment
  candidate.
- Make direction and state-transition logic explicit.
- Bound any learned physical parameters to meaningful ranges.
- Expose acceleration or history only if it is available causally and robustly.
- Keep detailed contact solvers offline unless a reduced-order formulation is
  validated.
- Retain inspectable intermediate values for every physical contribution.
