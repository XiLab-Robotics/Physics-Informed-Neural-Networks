# Wave 4F Cycloid Contact Force PINN Design

## Purpose

`Wave 4F` explores cycloid-pin contact-force, profile-modification, and loaded
transmission-error relations as soft constraints for the RV reducer TE
problem.

## Source Boundary

External cycloid-drive studies show that cycloid tooth-profile modification,
contact force, return error, and loaded transmission error can be analyzed
together. These studies are relevant because the MMT paper also emphasizes
low-speed cycloid-pin stage errors, but their exact equations and geometry
must be validated before being treated as repository truth.

## Design

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4f_cycloid_contact_force_pinn` |
| Physical focus | Cycloid-pin contact, profile modification, contact force, loaded TE, and low-speed-stage error. |
| Required assumptions | Cycloid geometry, pin radius, pin position, contact interval, and load distribution proxy. |
| Main targets | High-order fragile harmonics, torque-sensitive residuals, and low-speed-stage attribution. |
| First constraint | Contact-force or loaded-TE proxy smoothness over angular position and torque. |

## Candidate Constraints

| Constraint | Purpose |
| --- | --- |
| Contact interval consistency | Penalize contact-force proxy outside plausible engagement regions. |
| Contact-force smoothness | Avoid unrealistic angular spikes unless supported by measured harmonics. |
| Loaded TE proxy | Link torque-sensitive TE residual to cycloid contact/load proxy. |
| High-order harmonic watch | Test whether `156`, `162`, and `240` respond to cycloid-contact constraints. |

## Implementation Outline

1. Start from MMT low-speed terms and add a simple cycloid contact proxy.
2. Use torque as a causal load proxy.
3. Compare high-order harmonic residuals before and after contact constraints.
4. Avoid full contact-force claims until geometry and contact assumptions are
   explicitly validated.

## Risks

- Contact force is not directly measured.
- Incorrect contact intervals can bias the model toward a wrong harmonic
  explanation.
- Cycloid profile-modification equations may not match the tested reducer.

## Decision Gate

Keep this branch if it improves high-order harmonic diagnostics or
torque-sensitive loaded-TE behavior without damaging the low-order offset
channel.
