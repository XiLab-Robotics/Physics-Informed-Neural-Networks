# Wave 4C MMT Soft Constraint PINN Design

## Purpose

`Wave 4C` is the first true MMT-informed PINN candidate. It adds weak MMT
equation residuals to a curve or harmonic-plus-residual neural model while
keeping ordinary data fit as the primary objective.

## Physical Idea

The neural model should not be forced to exactly satisfy the MMT equation
chain because equivalent-error inputs and contact geometry are not fully
observed for every repository curve. Instead, the MMT chain should act as a
soft regularizer that discourages physically implausible offset, harmonic, and
subsystem-contribution behavior.

## Candidate

| Element | Design Choice |
| --- | --- |
| Candidate name | `wave4c_mmt_soft_constraint_pinn` |
| Base model | Curve predictor or Wave 3 harmonic-prior residual predictor. |
| Physics layer | Batch-callable MMT reconstruction using calibrated or predicted equivalent-error channels. |
| Primary loss | Data-fit curve loss. |
| Physics losses | MMT `RTE` residual, subsystem contribution regularization, harmonic consistency, and optional residual smoothness. |
| Promotion surface | Official Track 2 raw, offset, centered-shape, amplitude, phase, and visual diagnostics. |

## Loss Structure

| Loss | Initial Role |
| --- | --- |
| `L_data` | Primary pointwise or curve-aware fit to measured TE. |
| `L_mmt_rte` | Weak penalty between predicted TE and MMT reconstructed `RTE`. |
| `L_mmt_subsystem` | Optional bound or smoothness penalty on `f1`, `f2i`, `f3`, and `f4i`. |
| `L_harmonic` | Consistency on recovered harmonic set. |
| `L_residual` | Keeps learned residual correction interpretable but not zero. |

## Implementation Outline

1. Convert the MMT reproduction into a batch-callable module or differentiable
   approximation.
2. Start from the `Wave 4A` parameter inventory and fixed calibrated
   equivalent-error parameters from `Wave 4B`.
3. Add an optional head that predicts a small equivalent-error vector.
4. Sweep weak physics weights and compare against data-only control.
5. Reject the branch if MMT losses reduce validation loss but worsen Track 2
   curve diagnostics.

`Wave 4C` should not be implemented as the next branch until `Wave 4B` proves
that at least one MMT feature or calibrated equivalent-error group explains
held-out offset or fragile-harmonic behavior without target leakage.

## Scaling Risks

- MMT terms may have units or magnitudes far from TE curve loss.
- Strong physics weights can force wrong geometry assumptions into the model.
- Predicting equivalent errors can become a hidden memorization channel if the
  split is not condition-safe.

## Decision Gate

Continue only if weak MMT penalties improve Track 2 offset or harmonic
diagnostics while preserving or improving centered-shape metrics.
