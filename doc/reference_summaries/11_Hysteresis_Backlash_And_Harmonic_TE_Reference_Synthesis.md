# Hysteresis, Backlash, And Harmonic TE Reference Synthesis

## Scope

This synthesis covers the harmonic-drive, hysteresis, torsional-friction, and
offline joint-compensation sources in `reference/te_modeling/bibliography/`.
The goal is to extract model-development consequences without treating
mechanisms from harmonic drives, cycloidal drives, and complete robot joints as
interchangeable.

## Ghorbel, 2001

**Source:** *On the Kinematic Error in Harmonic Drive Gears*

The paper decomposes harmonic-drive kinematic error into a nominal kinematic
part and a contribution associated with torsional flexibility. The observed
error depends on the inertial load, assembly, and angular velocity. The model
captures speed dependence but does not close the load and friction problem.

Project consequences:

- periodic error can contain both geometric and elastodynamic contributions;
- velocity dependence is not proof of a purely empirical artifact;
- a harmonic residual should not assume constant amplitude and phase over all
  operating conditions;
- direct transfer to the RV reducer requires a geometry-specific audit.

## Iwasaki And Coauthors, 2009

**Source:** *Angular Transmission Error Modeling and Compensation for Harmonic
Drive Gearings*

The work separates:

- a synchronous periodic component, identified through Fourier analysis;
- a nonlinear elastic hysteresis component, described through a
  rolling-friction-based model.

The resulting feedforward compensation reduced the three-standard-deviation
settling error by approximately 40 percent in the reported setup.

Project consequences:

- periodic shape and hysteretic state should be modeled and evaluated
  separately;
- angle alone can describe the synchronous term, while direction and internal
  state are needed for the hysteretic term;
- curve reconstruction and closed-loop compensation success are distinct
  validation layers.

## Ruderman And Iwasaki, 2016

**Source:** *Sensorless Torsion Control of Elastic-Joint Robots With Hysteresis
and Friction*

The paper reconstructs joint torsion from motor torque and velocity and an
inverse torque-to-torsion hysteresis map, avoiding a load-side torsion sensor.
The method improves positioning, but it exposes three issues that are central
to a deployable physics-informed model:

- the hysteresis operator has an internal memory state;
- initialization and saturation of that state matter;
- robustness and friction compensation cannot be inferred from a static
  torque-angle law alone.

Project consequences:

- any hysteresis-aware pilot needs a causal state update and an explicit
  initialization policy;
- randomly shuffled samples are insufficient to validate a memory law;
- a time-windowed candidate is the natural reference for this branch.

## Mesmer And Coauthors, 2022

**Source:** *Modeling and Identification of Hysteresis in Robot Joints With
Cycloidal Drives*

The paper compares a white-box Bouc-Wen model with a nonlinear autoregressive
model with exogenous inputs. Both reproduce static hysteresis; the learned
model fits the observed behavior better and can be extended more easily, while
the authors retain a preference for the inspectability and industrial
acceptance of the white-box model.

Project consequences:

- Bouc-Wen is a plausible bounded differential residual only after torque,
  direction, time, and initialization conventions are reconstructed;
- fit superiority alone does not make a black-box hysteresis law physically
  identifiable;
- a white-box state law and a learned residual should be compared separately.

## Mesmer And Coauthors, 2023

**Source:** *Investigation and Compensation of Hysteresis in Robot Joints With
Cycloidal Drives*

The study reports that friction changes strongly with load and temperature,
that the investigated hysteresis is approximately rate-independent, and that
joint stiffness shows a smaller temperature-dependent increase. The
compensation uses an extended friction model and considers a temperature
observer as a practical alternative to direct sensing.

Project consequences:

- temperature affects more than the periodic Fourier coefficients;
- torque, temperature, and direction must remain explicit in hysteresis tests;
- a temperature observer is a separate causal-estimation component and must
  not use future TE;
- rate independence is source- and regime-specific and must be falsified on
  the local data.

## Olabi And Coauthors, 2012

**Source:** *Offline Compensation of Robot Joint Errors*

The paper separates joint compliance from kinematic error, identifies
axis-specific stiffness, and applies offline correction on a six-axis robot.

Project consequences:

- mean offset, elastic deflection, and angularly periodic error should not be
  forced into one undifferentiated target;
- direction-specific stiffness or compliance is a testable intermediate model;
- a complete robot correction map is not equivalent to a reducer governing
  law.

## Cross-Source Synthesis

The sources support the following minimal decomposition:

```text
TE(theta, operating state, history) =
    periodic synchronous component
  + quasi-static elastic or compliance component
  + hysteretic memory component
  + residual disturbance
```

This is a modeling decomposition, not yet a unique physical equation. It
suggests three bounded Wave 5.2 tests:

1. a direction-specific Polynomial-Fourier periodic component;
2. an independently evaluated compliance or offset component;
3. a causal hysteresis-state residual tested only on ordered trajectories.

The periodic candidate is immediately testable. The hysteresis candidate
requires a verified temporal ordering, torque convention, state initialization,
and enough reversal cycles. No source justifies collapsing forward and backward
surfaces into a single scalar-error objective.

## Deployment Implications

- Preserve explicit intermediate quantities: direction, angular phase,
  coefficient values, elastic contribution, and hysteresis state.
- Avoid target-derived states at inference time.
- Use bounded state variables and deterministic initialization for PLC
  deployment.
- Validate curve fidelity before claiming compensation benefit.
- Treat mechanism-specific harmonic orders as configuration, not universal
  constants.
