# Wave 5.2B And Wave 5.2C Model Design Gate

## Overview

This report translates the completed `Wave 5.2A` full paired-dataset matrix
into the next implementable model-design gate. It is not a training result,
not a training-campaign plan, and not a `TE Curve Verification Pipeline`
promotion.

The externally running full-wave `polished_dataset` retraining campaign
remains out of scope. Final polished-branch promotion decisions must wait for
that campaign to finish, be synchronized, closed out, and optionally evaluated
through the official `TE Curve Verification Pipeline`.

## Input Evidence

The design gate uses the full paired matrix in:

- `doc/reports/analysis/model_development_waves/wave_5_2/paired_dataset_diagnostics/[2026-07-01]/wave52a_paired_dataset_diagnostics.md`
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/`

The paired diagnostic evaluated all `1938` paired directional records between
`simplified_dataset` and `polished_dataset`.

| Signal | Value |
| --- | ---: |
| Evaluated paired directional records | 1938 |
| Mean absolute offset delta [deg] | 0.003216838 |
| Mean absolute peak-to-peak delta [deg] | 0.000000134 |
| Mean absolute smoothness delta [deg] | 0.000000003 |
| Mean maximum nonzero-harmonic delta [deg] | 0.001749405 |
| Offset-shifted pairs | 901 |
| Nonzero-harmonic changed pairs | 944 |
| Nearly identical pairs | 65 |
| Sampling anomalies | 27 |
| Smoothness-changed pairs | 1 |
| Shape-changed pairs | 0 |

The practical interpretation is narrow but important: the paired datasets are
well aligned enough for model-design work, but the dominant differences are
not broad curve-shape or smoothness changes. The observed differences are
mainly offset / mean shifts and nonzero-harmonic amplitude changes.

## Prior Wave Lessons

The next branch must not repeat older work blindly.

| Evidence Source | Relevant Lesson |
| --- | --- |
| `CVP 1.4` and `CVP 1.5` | Offset is real and partly condition-linked, but offset-only correction is not enough; centered shape, amplitude, and phase still matter. |
| `Wave 3.3` | Curve-aware objectives are useful but did not automatically promote over accepted leaders. |
| `Wave 4.1`-`Wave 4.4` | Robust, probabilistic, mixture-density, and latent-state branches are integration evidence, not current promoted solutions. |
| `Wave 5.1` | Compact harmonic-prior residual structure is architecturally useful, but its verified candidates were exploratory and not promoted. |
| `Wave 5.2A` | The next model should target offset / mean and nonzero-harmonic differences before attempting a heavy full-physics PINN. |

## Design Decision

Do not start with a complete PINN or full physical surrogate.

The next model-design gate should prepare two bounded candidates:

| Candidate | Decision |
| --- | --- |
| `Wave 5.2B` offset and harmonic guided model | Primary next implementation candidate after design approval. |
| `Wave 5.2C` dirty-to-clean transfer model | Secondary candidate, only if its paired supervision is kept leakage-safe and diagnostic first. |

`Wave 6` remains deferred. It should integrate only mechanisms that survive
the `Wave 5.2B` and `Wave 5.2C` checks plus the synchronized full-wave
`polished_dataset` evidence.

## Wave 5.2B Candidate Specification

`Wave 5.2B` should be a lightweight offset and harmonic guided model on the
clean `polished_dataset` branch.

### Objective

Test whether explicit offset / mean supervision and harmonic consistency
improve curve-first readiness without degrading raw TE prediction, centered
shape, or direction balance.

### Candidate Structure

| Component | Specification |
| --- | --- |
| Backbone | Reuse the strongest causal periodic sequence or compact harmonic-residual family once full-wave polished evidence is synchronized. Until then, design against a generic causal trunk. |
| Primary head | Pointwise TE prediction. |
| Offset / mean head | Predict condition-linked curve mean / low-frequency offset using causal operating inputs only. |
| Centered-shape path | Evaluate or train on prediction residual after batch-local or curve-local diagnostic centering only where it is train-time safe. |
| Harmonic consistency term | Penalize or report nonzero-harmonic amplitude mismatch on diagnostic curve windows. |
| Sampling mask | Exclude or downweight the `27` sampling-anomaly paired conditions in paired-dataset supervision. |
| Direction handling | Keep `global`, `forward`, and `backward` reporting surfaces separate. |

### Loss Sketch

The first candidate loss should remain simple and auditable:

| Term | Purpose | Deployment Boundary |
| --- | --- | --- |
| Pointwise TE loss | Preserve raw TE accuracy. | Runtime-safe. |
| Offset / mean auxiliary loss | Learn condition-linked curve mean behavior. | Runtime-safe if target is train-only and inference uses predicted head output. |
| Centered-shape loss | Prevent offset terms from hiding shape errors. | Train-time diagnostic only unless reformulated causally. |
| Nonzero-harmonic amplitude loss or metric | Track the `Wave 5.2A` harmonic-change signal. | Train-time or validation diagnostic; no future curve information at runtime. |
| Smoothness penalty | Keep derivative behavior stable without over-smoothing. | Runtime-safe if computed on predicted causal sequence windows. |

### Acceptance Criteria

`Wave 5.2B` is worth campaign preparation only if the design can define:

- causal inputs only;
- explicit `global`, `forward`, and `backward` surfaces;
- no use of target curve means or future samples at inference;
- separate raw error, centered-shape, offset, harmonic, smoothness, and
  direction-balance metrics;
- a small ablation matrix that proves which term helps.

## Wave 5.2C Candidate Specification

`Wave 5.2C` should remain a dirty-to-clean or transfer design, not the first
training branch.

### Objective

Test whether the paired `simplified_dataset` surface can improve robustness or
pretraining without importing polishing leakage into runtime inference.

### Allowed Paired-Data Uses

| Use | Status |
| --- | --- |
| Pretrain on `simplified_dataset`, fine-tune on `polished_dataset` | Allowed design candidate. |
| Auxiliary dirty-to-clean offset target | Allowed if target is train-only and not used as measured input at inference. |
| Dirty-to-clean harmonic correction target | Allowed as diagnostic or auxiliary train-time target. |
| Sampling-anomaly mask | Required for paired supervision. |
| Full-curve target mean at runtime | Forbidden. |
| Offline polishing operations inside inference | Forbidden. |

### Rejection Criteria

`Wave 5.2C` should be rejected or deferred if:

- paired supervision requires target-only information at inference;
- the simplified branch improves scalar metrics but worsens curve-first
  shape, offset, or harmonic diagnostics;
- transfer only helps the `global` surface while degrading `forward` or
  `backward`;
- reduced-point tests show the learned correction depends on dense full-curve
  sampling.

## Deferred To Wave 6

The following mechanisms remain integration candidates, not immediate
implementation requirements:

- uncertainty heads;
- mixture-density heads;
- latent-state / hysteresis heads;
- integrated multi-task trunk with all auxiliary heads active;
- reduced-point backbone adaptation;
- final deployable model packaging;
- official `TE Curve Verification Pipeline` promotion.

## Next Action

The next actionable implementation should be a `Wave 5.2B` model and campaign
preparation plan only after a new explicit approval. That future step must
create a campaign planning report, model explanation report, training configs,
launcher, launcher note, active-campaign state, and exact launch commands
before any training is run.

Until then, this design gate should be treated as the current decision surface:
start from lightweight offset / mean and nonzero-harmonic guidance, keep
dirty-to-clean transfer secondary, and defer full PINN and integrated
multi-head work.
