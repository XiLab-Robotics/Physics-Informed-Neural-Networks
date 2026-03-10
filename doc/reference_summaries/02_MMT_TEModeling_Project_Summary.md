# MMT TE Modeling - Project Summary

## Source

- Reference PDF: `reference/MMT_TEModeling.pdf`

## Work Objective

The paper develops an analytical model for the Rotational Transmission Error of an RV reducer. The core idea is to convert the over-constrained kinematic structure of the reducer into an equivalent multi-loop mechanism, so that explicit equations can link the original component errors to the final Transmission Error.

## Main Theoretical Concepts

- Rotational Transmission Error is the main accuracy indicator of the reducer.
- The RV structure is reduced to an equivalent kinematic mechanism by replacing higher pairs with lower pairs.
- The model is developed through a loop incremental approach.
- Manufacturing and assembly errors are represented as equivalent linkage-length errors in the mechanism.
- The model makes the contribution of both the high-speed and low-speed stages explicit in the final TE.

## Considered Errors

- Crankshaft eccentricity.
- Geometric errors in the involute gear train.
- Cycloidal profile errors.
- Pin radius and pitch circle errors.
- Accumulated pitch errors.
- Assembly errors on the output disc and other coupled parts.

## Results Relevant To The Project

- Low-speed stage errors have a particularly strong impact on TE.
- TE frequency components can be interpreted directly with respect to physical error sources.
- The analytical model can be used as a physics basis for constraints, feature engineering, or a physics-informed loss.

## Implications For This Repository

- The project should treat TE as a quantity structured by reducer kinematics, not as a pure black-box regression target.
- A future physics-informed loss should incorporate relationships among kinematic variables, stage coupling, and transmission-ratio consistency.
- The characteristic TE frequencies should not be treated only as empirical features, but as manifestations of specific mechanical errors.

## Translation Into Software Requirements

- Keep data-driven and physics-based model components clearly separated.
- Keep relevant mechanical parameters explicit in configuration files.
- Favor functions that preserve traceability between error source, expected harmonics, and model output.

## Recommended Direction

- Use the analytical model as a reference for:
  - ML result validation;
  - physically meaningful feature design;
  - composite or physics-informed loss construction;
  - interpretation of compensated harmonics.
