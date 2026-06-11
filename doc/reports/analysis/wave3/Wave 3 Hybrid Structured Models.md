# Wave 3 Hybrid Structured Models

## Purpose

`Wave 3` is the next architecture-design branch after the dispersion-aware
`Track 2H` probes. Its role is to test hybrid structured TE models that keep
the paper harmonic representation inspectable while adding learned correction
capacity where the current model families show offset, phase, amplitude, or
fragile-harmonic limitations.

This report is a design document only. It does not prepare runnable training
campaigns and does not modify the active `Track 2H` campaign.

## Reference Boundary

| Source | What It Supports | Wave 3 Consequence |
| --- | --- | --- |
| `MMT_TEModeling` summary | TE frequency components can be interpreted with respect to mechanical error sources, and analytical structure can guide features, losses, or constraints. | Keep the structured and learned parts separated so harmonic behavior remains interpretable. |
| `RCIM_ML_Compensation` summary | The practical ML workflow uses speed, torque, temperature, angular position, and direction-separated modeling. | Preserve causal inputs and report `global`, `Fw`, and `Bw` surfaces separately. |
| Recovered RCIM assets summary | The paper workflow is harmonic-wise and uses the recovered harmonic set `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`. | Use the paper harmonic set as the first structured basis before adding learned residuals. |
| `Track 2` h0 diagnostics | `h0` is the right mean-like channel, but large measured `h0` alone does not explain model failures. | Treat low-order offset terms as a structured channel, not as the sole cause of error. |
| Dispersion-aware roadmap | `h0`, some `h1`, and high harmonics such as `156`, `162`, and `240` are suspected fragile groups. | Let Wave 3 test grouped harmonic structure instead of one undifferentiated curve output. |

## Design Objective

The core question is whether a model that explicitly separates harmonic
structure from residual correction can outperform direct curve learners and
loss-only branches on the official `Track 2` promotion surface.

The model should be judged by:

- raw curve error;
- signed mean-offset error;
- centered-shape error;
- amplitude error;
- harmonic phase error;
- direction-stratified behavior on `global`, `Fw`, and `Bw`;
- visual overlays and collage reports when candidates are viable.

## Candidate Model Families

| Candidate | Structure | Main Test |
| --- | --- | --- |
| `wave3_harmonic_prior_residual` | Predict paper harmonic coefficients, reconstruct the base TE curve, then add a learned causal residual curve. | Tests whether a paper-style harmonic prior plus residual improves full-curve behavior. |
| `wave3_grouped_harmonic_heads` | Separate heads for low-order offset terms, stable middle harmonics, fragile high harmonics, and optional residual shape. | Tests whether different harmonic groups need different capacity or regularization. |
| `wave3_conditioned_residual_surface` | Start from a stable base predictor and learn condition-conditioned residual surfaces over speed, torque, temperature, and direction. | Tests whether structured operating-condition residuals remove mean-surface bias without damaging centered shape. |
| `wave3_basis_constrained_decoder` | Predict compact coefficients and decode the TE curve through fixed harmonic basis functions plus a constrained residual basis. | Tests whether curve decoding should be structurally constrained instead of fully free. |

## Harmonic Grouping

| Group | Harmonics | Initial Role |
| --- | --- | --- |
| Offset / low-order fragile group | `0`, `1` | Mean surface, preload-sensitive behavior, and low-frequency distortion. |
| Stable middle group | `3`, `39`, `40`, `78`, `81` | Main structured shape reference, unless future diagnostics show instability. |
| High-order fragile group | `156`, `162`, `240` | Candidate for stronger regularization, robust weighting, or separate residual handling. |

This grouping is a hypothesis. It must be tested against `Track 2` metrics and
must not be hard-coded as a final truth before campaign evidence exists.

## Architecture Principles

1. Preserve causal inputs: speed, torque, temperature, angular position,
   direction, and approved causal history features only.
2. Keep the harmonic reconstruction path explicit so the model can be audited
   by component.
3. Avoid using measured curve mean, future TE samples, or held-out target
   statistics during inference.
4. Keep direction-separated reporting mandatory for `global`, `Fw`, and `Bw`.
5. Compare every Wave 3 candidate against accepted Track 2 leaders and the
   completed `Track 2G`, `Track 2H`, `Wave 2B`, and `Wave 2C` branches.
6. Treat PLC-friendly export as a later constraint for this research stage,
   while avoiding architectures that are impossible to inspect.

## First Implementation Candidate

The first runnable Wave 3 candidate should be
`wave3_harmonic_prior_residual` because it gives the cleanest diagnostic split:

1. A structured harmonic branch predicts the recovered paper harmonic set.
2. A deterministic reconstruction layer builds the base TE curve from the
   predicted harmonics.
3. A small residual branch predicts a causal correction curve.
4. The final prediction is the sum of structured reconstruction and residual.

This candidate can answer whether the model needs more structure before it
needs a larger multi-head architecture.

## Comparison Plan

| Comparator | Why It Matters |
| --- | --- |
| Accepted Track 2 leaders | Defines the official promotion baseline. |
| `Track 2G` curve-aware candidates | Tests whether structure beats loss-only curve tuning. |
| `Track 2H` robust-loss candidates | Tests whether structure adds value beyond robust central-tendency fitting. |
| `Wave 2B` periodic sequence models | Tests whether harmonic structure beats temporal sequence capacity. |
| `Wave 2C` residual harmonic temporal models | Tests whether Wave 3 improves the existing harmonic-residual idea with cleaner grouping. |

## Decision Gates

Wave 3 should proceed to campaign preparation only if the next approval gate
accepts these design choices:

- use the recovered harmonic set as the first structured basis;
- start with `wave3_harmonic_prior_residual`;
- keep grouped harmonic heads as the second candidate, not the first;
- use official `Track 2` metrics rather than scalar validation loss as the
  promotion surface;
- wait for the running `Track 2H` campaign result before selecting final
  robust-loss or residual-loss defaults.

## Non-Goals

- Do not modify the active `Track 2H` campaign.
- Do not generate Wave 3 YAML packages or launchers in this design step.
- Do not claim that `h0` is the only physical cause of offset behavior.
- Do not merge Wave 3 with the final integrated multi-task / multi-head
  architecture before smaller Wave 3 candidates have been tested.
