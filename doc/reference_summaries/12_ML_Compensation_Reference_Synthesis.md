# Machine Learning Compensation Reference Synthesis

## Scope

This document synthesizes two state-dependent transmission-error compensation
studies for rack-and-pinion drives. They do not model the same reducer as the
repository, but they provide useful architectural and validation patterns for
hybrid analytical and learned compensation.

## Steinle And Coauthors, 2024

**Source:** *State-Dependent Transmission Error Compensation Using Machine
Learning for Rack-and-Pinion Drives*

The study separates the error into:

- repeatable geometric commissioning errors;
- state-dependent elastic deformation;
- localized deviations not captured by the broad elasticity model.

The implementation uses a two-stage learned model:

1. a neural network for general elasticity;
2. a tree ensemble for localized deviations.

It also addresses backlash and introduces a correction velocity for practical
control integration. The reported average path-error reduction is 66 percent.

## Steinle And Coauthors, 2025

**Source:** *Transmission Error Compensation for Electrically Preloaded
Rack-and-Pinion Drives*

The system uses two electrically preloaded drives. The paper derives how the
two TE sources combine and how compensation interacts with both the path and
preload control loops. The training data include preload-torque variation, and
the compensation is fed forward into position and preload control. The
reported average path-error reduction is 57.8 percent.

## Relevance To The TE Program

The transferable lessons are architectural:

- split broad, interpretable deformation from localized learned residuals;
- include the actual control state, such as preload or direction, when it
  changes the load path;
- preserve the superposition law when multiple actuators or error sources are
  physically coupled;
- distinguish offline prediction accuracy from closed-loop path improvement;
- design compensation outputs for their real control-loop insertion point.

The rack-and-pinion equations and reported percentages are not direct evidence
for an RV-reducer PINN. The mechanism, preload arrangement, and controller are
different.

## Candidate Use In Wave 5.2

These sources support a hybrid implementation pattern:

```text
TE prediction =
    interpretable global or elastic component
  + localized learned residual
```

For this repository, the first term could be a verified Polynomial-Fourier,
compliance, or bidirectional compatibility component. The second term must be
bounded and evaluated for incremental value. This architecture only qualifies
as physics-informed when the first component or an additional loss contains a
stated physical equation or compatibility law.

## Deployment Consequences

- Keep analytical and learned contributions separately inspectable.
- Expose the state variables that select load path or direction.
- Confirm that every input is causally available to TwinCAT.
- Evaluate the compensation command in addition to the predicted TE.
- Do not claim closed-loop benefit until a controller-level experiment exists.
