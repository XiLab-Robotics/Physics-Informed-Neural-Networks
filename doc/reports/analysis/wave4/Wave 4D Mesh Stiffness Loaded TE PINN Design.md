# Wave 4D Mesh Stiffness Loaded TE PINN Design

## Purpose

`Wave 4D` explores time-varying mesh stiffness and loaded static transmission
error (`LSTE`) as soft constraints. This branch is motivated by gear-dynamics
literature that links TE, mesh deformation, mesh stiffness, torque, and
dynamic response.

## Source Boundary

External references used for this candidate include NASA geared-system
dynamics work with backlash, periodic mesh stiffness, and static TE
excitation, plus recent mesh-stiffness and loaded-TE studies showing that
loaded transmission error and system compliance can drive mesh deformation and
dynamic TE. These are exploratory gear-system formulations, not validated
RV-reducer equations.

## Design

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4d_mesh_stiffness_loaded_te_pinn` |
| Physical state | Learned or parameterized mesh stiffness `k_mesh(theta, torque, temperature, direction)`. |
| TE state | Predicted unloaded/loaded TE decomposition or predicted curve plus load-sensitive residual. |
| Primary signal | Torque-stratified mean, amplitude, and high-harmonic behavior. |
| First constraint | Periodic stiffness or Fourier stiffness smoothness over angular position. |

## Candidate Constraints

| Constraint | Purpose |
| --- | --- |
| Periodic stiffness | Enforce repeating mesh-stiffness structure over the angular cycle. |
| Torque-sensitive loaded TE | Let torque affect loaded TE without using target means as inputs. |
| Deformation consistency | Penalize incompatible relationships between loaded TE residual and stiffness proxy. |
| Frequency-band consistency | Watch whether stiffness constraints affect `156`, `162`, and `240` without erasing them. |

## Implementation Outline

1. Start with a diagnostic Fourier stiffness proxy rather than a full FEM
   stiffness solver.
2. Fit or predict stiffness coefficients from causal operating variables.
3. Add weak loaded-TE residual consistency loss.
4. Compare against data-only and MMT-only candidates.
5. Promote only if torque/load stratification improves without hurting
   direction-separated Track 2 metrics.

## Risks

- Mesh stiffness is not measured directly in the repository dataset.
- Torque effects may be absorbed by the neural model without learning a real
  stiffness mechanism.
- A generic gear-pair formulation may not transfer cleanly to RV reducer
  cycloid-pin behavior.

## Decision Gate

Keep this branch only if it explains torque-linked residuals or fragile
high-harmonic behavior better than MMT-only and robust-loss baselines.
