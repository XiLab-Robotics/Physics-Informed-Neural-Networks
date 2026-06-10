# Track 2 Dispersion-Aware Wave Roadmap

## Purpose

This roadmap fixes the next modeling order for the `Track 2` TE curve-offset
problem after the completed h0/component-offset diagnostics.

## Evidence Boundary

| Evidence | Current Conclusion | Boundary |
| --- | --- | --- |
| Measured component-offset diagnostic | Harmonic zero / `h0` is the largest average measured component and the correct mean-like channel to inspect. | This does not prove that `h0` is the only cause of model offset failures. |
| `Track 2D` h0/error cross-check | Large absolute measured `h0` does not reliably identify the cases where models have the largest mean-offset errors. | The problem is not solved by filtering high-`h0` curves alone. |
| Predicted-mean h0 surface diagnostic | The actionable failure is model-side mean-surface bias or compression against measured `h0`. | The diagnostic identifies the symptom but not the best model intervention. |
| Colleague repeatability feedback | A `6-8%` Component 0 variation is plausible under repeated experiments and may be linked to preload, elastic release, protocol state, or hysteresis-like internal state. | This is external evidence until repository repeat measurements are explicitly joined and quantified. |
| Harmonic fragility pattern | The highest concern is around `h0`, some `h1`, and selected high harmonics such as `156`, `162`, and `240`; a middle-frequency band appears more stable. | The grouping must be tested numerically before it becomes a fixed architecture rule. |

## Modeling Implication

The next training branch should not assume that the target curve mean is a
perfectly reproducible deterministic value. The working hypothesis is that the
dataset may contain local dispersion caused by experiment-dependent preload or
internal mechanical state. The model plan must therefore test whether better
results come from robust central-tendency fitting, uncertainty modeling,
multi-modal target modeling, latent-state conditioning, or structured physics
constraints.

PLC-friendly execution is not a constraint for this research stage. The only
hard boundary retained now is causal input discipline: the model may use point
state, direction, operating condition, causal history, and causal derived
features, but it must not use future curve information or measured target
statistics unavailable at prediction time.

## Planned Modeling Order

| Stage | Scope | Decision Value |
| --- | --- | --- |
| `Track 2H` dispersion-aware probes | Robust losses, quantile or probabilistic regression, mixture-density heads, and latent-state or hysteresis-aware features. | Identify which noise/dispersion treatment actually reduces mean-surface and full-curve errors. |
| `Wave 3` hybrid structured models | Combine harmonic structure, condition-conditioned residual learning, and explicit grouped treatment of stable and fragile harmonic bands. | Test whether structure improves extrapolation and reduces fragile-harmonic overfitting. |
| `Wave 4` PINN formulation and first PINN | Add soft physics, periodicity, smoothness, harmonic-consistency, and operating-condition constraints in a first narrow PINN branch. | Test whether physics-informed regularization helps the same offset and high-harmonic failure modes. |
| Integrated multi-task / multi-head stage | Combine the best proven elements into shared-trunk heads for offset, low-frequency terms, centered shape, uncertainty or mixture parameters, and optional structured residuals. | Avoid committing to a large architecture before smaller probes show which mechanisms are worth integrating. |

## Track 2H Probe Set

| Probe | What It Tests | Candidate Methods |
| --- | --- | --- |
| Robust regression | Whether the model should fit a robust center instead of chasing local outliers. | Huber loss, Tukey biweight, trimmed or winsorized loss, MAE, log-cosh, robust sample weighting. |
| Quantile / probabilistic regression | Whether the offset target is better represented as an interval or distribution. | Quantile heads such as `p10`, `p50`, and `p90`; Gaussian `mu/sigma`; negative log-likelihood. |
| Mixture-density heads | Whether repeated or similar operating points contain multiple plausible local states. | Mixture weights, means, and variances for offset or low-order harmonic heads. |
| Latent-state / hysteresis-aware models | Whether preload, elastic release, or prior motion history acts like a hidden state. | Causal history windows, previous-condition summaries, direction-transition features, sequence encoders. |

## Harmonic Grouping Hypothesis

| Group | Initial Treatment |
| --- | --- |
| `h0` and low-order offset terms | Treat as the primary mean-surface and dispersion diagnostic channel. |
| `h1` | Monitor as a secondary low-order fragile component. |
| Middle harmonics | Use as a comparatively stable shape-reference band unless diagnostics show otherwise. |
| `h156`, `h162`, and `h240` | Treat as high-order fragile components that may need robust weighting, structured regularization, or separate heads. |

## Decision Gates

1. Do not claim that `h0` is the sole cause unless component-level error,
   repeatability, and model-side surface diagnostics support that conclusion.
2. Start with `Track 2H` probes before opening the integrated multi-head
   campaign.
3. Run `Wave 3` and `Wave 4` as separate evidence-generating branches before
   deciding which mechanisms belong in the final integrated architecture.
4. Keep official `Track 2` verification, visual overlays, offset metrics,
   centered-shape metrics, amplitude, and phase diagnostics as the promotion
   surface for every branch.
