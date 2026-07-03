# Wave 5.2E Backlash Preload State PINN Design

## Purpose

`Wave 5.2E` targets the suspected preload, elastic-release, backlash, and hidden
state effects that may create local dispersion in `h0`, `h1`, and selected
high harmonics. It is the Wave 5.2 branch most directly connected to the
experimental-repeatability discussion.

## Physical Idea

Gear-dynamics literature commonly represents backlash and clearance with
piecewise nonlinear functions. In this repository, the practical equivalent is
not necessarily literal tooth separation. It may be an unobserved mechanical
state created by preload, prior motion, direction transition, or elastic
release.

## Design

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4e_backlash_preload_state_pinn` |
| State inputs | Direction, speed, torque, temperature, optional causal history, and direction-transition indicators. |
| Hidden state | Small latent preload or backlash-state variable. |
| Constraint type | Piecewise/dead-zone residual structure and state smoothness. |
| Main target | Low-order mean-surface dispersion and direction-dependent residual behavior. |

## Candidate Constraints

| Constraint | Purpose |
| --- | --- |
| Dead-zone residual | Allow different response inside and outside a learned clearance/preload band. |
| State persistence | Encourage latent state continuity across causal neighboring samples. |
| Direction transition | Permit different behavior after `Fw`/`Bw` transitions without forcing equality. |
| Offset uncertainty | Represent non-repeatable offset as interval or variance, not just a single deterministic value. |

## Implementation Outline

1. Start with diagnostic state features, not a complex recurrent model.
2. Add a small latent-state head or mixture/quantile offset head if Wave 4 series
   robust losses are insufficient.
3. Keep the model causal: no future curve samples or measured target means.
4. Evaluate whether low-order offset and high-harmonic residuals become more
   stable under direction and load stratification.

## Risks

- Latent state can become an uncontrolled memorization channel.
- Backlash-style equations may explain symptoms but not the actual rig
  mechanism.
- Without repeated measurements, variance estimates may be hard to validate.

## Decision Gate

Promote this branch if it improves offset robustness in repeated or
near-repeated operating conditions and does not degrade centered-shape
prediction.
