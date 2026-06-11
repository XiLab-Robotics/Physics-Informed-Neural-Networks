# Wave 4 PINN Formulation And First PINN

## Purpose

`Wave 4` defines the first physics-informed neural-network branch for TE curve
prediction. Its purpose is to test whether physically motivated soft
constraints improve the same failure modes seen in `Track 2`: mean-surface
bias, centered-shape error, amplitude error, phase error, and fragile harmonic
behavior.

This report is a design document only. It does not prepare runnable training
campaigns and does not modify the active `Track 2H` campaign.

## Reference Boundary

| Source | What It Supports | Wave 4 Consequence |
| --- | --- | --- |
| `MMT_TEModeling` summary | TE is structured by RV reducer kinematics, and frequency components can be interpreted with respect to physical error sources. | Use physics-informed constraints as soft regularizers, not as a black-box replacement for data fit. |
| `RCIM_ML_Compensation` summary | The practical ML model depends on speed, torque, oil temperature, angular position, and direction-separated behavior. | Preserve causal operating variables and report `global`, `Fw`, and `Bw` separately. |
| Recovered RCIM harmonic workflow | The recovered paper workflow predicts selected harmonic amplitude and phase components. | Include harmonic-consistency constraints around the recovered harmonic set. |
| `Track 2` h0 diagnostics | `h0` is the correct mean-like channel, but measured `h0` magnitude alone does not explain model failures. | Include offset/mean-surface diagnostics, but do not encode `h0` as the only physical cause. |
| Wave 3 design | Hybrid structured models separate harmonic structure and learned residual correction. | Let the first PINN reuse the same inspectable harmonic and residual split where useful. |

## PINN Scope

The first Wave 4 PINN should be a soft-constraint TE model, not a complete
analytical RV reducer simulator. The repository does not yet expose a full
differentiable analytical model that maps every physical component error to
the measured TE curve. Therefore, the first PINN should use constraints that
can be validated from the available TE representation:

- periodic curve closure over the angular cycle;
- smoothness of TE as a function of angular position;
- harmonic reconstruction consistency;
- operating-condition smoothness over speed, torque, and temperature;
- direction-separated behavior;
- optional residual regularization when combined with a structured harmonic
  branch.

## Candidate Loss Terms

| Loss Term | Purpose | Boundary |
| --- | --- | --- |
| Data-fit loss | Preserve direct agreement with measured TE curves. | This remains the primary loss because physics constraints are incomplete. |
| Periodicity loss | Enforce curve closure and derivative consistency at angular wraparound. | Valid only for curve segments that represent a full compatible angular period. |
| Smoothness loss | Penalize unrealistic local oscillation in angular TE prediction. | Must not erase legitimate high-order harmonics such as `156`, `162`, and `240`. |
| Harmonic-consistency loss | Keep predicted curves consistent with selected harmonic amplitudes and phases. | The recovered harmonic set is a structured basis, not proof that all error lives there. |
| Condition-surface smoothness | Encourage nearby speed, torque, and temperature conditions to have compatible mean and shape behavior. | Must avoid leaking held-out target statistics or memorizing full operating-condition cells. |
| Direction-consistency diagnostic | Compare `Fw` and `Bw` behavior under the same formulation without forcing equality. | Directional models remain separate because the paper and repository treat them separately. |
| Residual regularization | Keep learned residuals small or smooth when a harmonic prior branch is present. | The residual must still be allowed to correct real non-harmonic or unmodeled behavior. |

## First PINN Candidate

The first runnable Wave 4 candidate should be
`wave4_soft_constraint_harmonic_pinn`:

1. Use a causal neural predictor for TE curve or harmonic-plus-residual output.
2. Compute the ordinary curve data-fit loss.
3. Add periodicity and angular smoothness penalties on the predicted curve.
4. Add harmonic-consistency penalties on the recovered harmonic set:
   `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`.
5. Add optional condition-surface smoothness only when the split design proves
   it does not leak held-out target information.
6. Evaluate by official `Track 2` raw, offset, centered-shape, amplitude,
   phase, and visual diagnostics.

This candidate is intentionally narrow. It tests whether soft physics helps
before adding a full physics model or combining PINN losses with the final
multi-task / multi-head architecture.

## Relationship To Wave 3

| Wave 3 Concept | Wave 4 Extension |
| --- | --- |
| Harmonic prior residual | Add periodicity, smoothness, and harmonic-consistency losses to the structured reconstruction path. |
| Grouped harmonic heads | Apply stronger or different regularization to low-order offset terms, stable middle harmonics, and fragile high harmonics. |
| Conditioned residual surface | Add condition-surface smoothness or residual regularization without assuming exact repeatability. |
| Basis-constrained decoder | Treat fixed harmonic basis functions as an inspectable constraint surface for PINN penalties. |

## Evaluation Plan

Wave 4 candidates should be compared against:

- accepted `Track 2` leaders;
- completed `Track 2G` curve-aware candidates;
- completed `Track 2H` robust-loss candidates;
- approved Wave 3 hybrid structured candidates;
- `Wave 2B` and `Wave 2C` sequence/harmonic baselines.

Promotion must use the official `Track 2` curve-facing diagnostics rather than
scalar validation loss alone.

## Decision Gates

Wave 4 should proceed to campaign preparation only if a later approval gate
accepts these choices:

- start with `wave4_soft_constraint_harmonic_pinn`;
- treat physics terms as soft regularizers, not hard truth constraints;
- keep the ordinary data-fit loss primary;
- avoid condition-surface smoothness unless leakage checks are explicit;
- wait for `Track 2H` and Wave 3 evidence before selecting final loss weights
  for a larger integrated architecture.

## Non-Goals

- Do not modify the active `Track 2H` campaign.
- Do not generate Wave 4 YAML packages or launchers in this design step.
- Do not claim that a full analytical RV reducer PINN has been implemented.
- Do not enforce equality between `Fw` and `Bw` behavior.
- Do not use measured curve means, future TE samples, or held-out target
  statistics at inference time.
