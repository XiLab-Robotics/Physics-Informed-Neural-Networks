# Wave 4G Planetary Mesh Force LSTE PINN Design

## Purpose

`Wave 4G` explores planetary-style mesh-force, load-sharing, and
loaded-static-transmission-error (`LSTE`) formulations as diagnostic or soft
constraint candidates. It is exploratory because the RV reducer is not a
simple planetary gearbox, but the test rig may still show support, load, and
branch-interaction effects that resemble planetary load-sharing behavior.

## Source Boundary

Planetary gear literature links mesh stiffness, load sharing, planet phasing,
support flexibility, loaded static TE, and dynamic mesh force. These ideas can
suggest useful diagnostics, but they must not be copied directly into the RV
model without validation.

## Design

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4g_planetary_mesh_force_lste_pinn` |
| Physical focus | Branch load sharing, support compliance, mesh force, and loaded static TE. |
| Required assumptions | Equivalent branches, load-sharing proxy, support-compliance proxy, and direction-separated behavior. |
| Main targets | Condition-regime residuals, torque effects, and harmonics linked to branch interaction. |
| First constraint | Load-sharing or branch-balance diagnostic, not a hard equality. |

## Candidate Constraints

| Constraint | Purpose |
| --- | --- |
| Branch-balance proxy | Penalize implausible unequal branch contribution unless supported by residuals. |
| LSTE torque consistency | Encourage loaded TE changes to follow torque/load regime smoothly. |
| Support-compliance proxy | Allow support flexibility to affect low-frequency and condition-regime residuals. |
| Phasing diagnostic | Check whether multi-branch phasing can explain selected harmonic groups. |

## Implementation Outline

1. Define a minimal equivalent-branch abstraction rather than a full planetary
   gearbox model.
2. Compute branch-balance and LSTE proxy diagnostics from causal operating
   variables.
3. Test whether proxies explain residuals that MMT and cycloid-contact
   branches do not.
4. Keep this branch behind MMT and cycloid-contact branches unless Track 2
   residuals show clear branch/load-sharing signatures.

## Risks

- RV reducer topology differs from planetary gear models.
- Branch/load-sharing proxies may become arbitrary latent features.
- This branch is likely less direct than MMT and cycloid-contact modeling.

## Decision Gate

Promote only if it explains residual structure that remains after MMT,
mesh-stiffness, backlash/preload, and cycloid-contact candidates have been
tested.
