# Track 2H Dispersion-Aware Modeling Probe Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares `Track 2H`, the dispersion-aware
modeling probe stage for the `Track 2` TE curve-offset problem.

The goal is to test whether the remaining offset and fragile-harmonic failures
are better handled by robust central-tendency fitting, uncertainty modeling,
multi-modal local target modeling, or causal latent-state conditioning before
building the larger integrated multi-task / multi-head architecture.

Training is not approved by this report. The first executable campaign package
must be generated only after this plan and the paired technical document are
approved.

## Baseline Interpretation

The latest accepted evidence is:

| Evidence | Interpretation |
| --- | --- |
| `Track 2G` official refresh | Curve-aware losses are valid controls but did not promote a new accepted `Track 2` leader. |
| Measured h0 diagnostic | `h0` is the correct mean-like channel to inspect and remains the main offset suspect. |
| h0/error cross-check | Absolute measured `h0` magnitude alone does not explain model mean-offset failures. |
| Predicted-mean h0 surface diagnostic | Model-side mean-surface bias or compression is the actionable symptom. |
| Colleague repeatability feedback | Local experimental dispersion around `Component 0` may reach `6-8%`, but repository repeatability evidence still has to be quantified. |

The campaign should therefore compare deterministic point estimates against
dispersion-aware predictions rather than assuming that every training target is
a perfectly reproducible scalar value.

## Candidate Probe Matrix

The first `Track 2H` plan keeps `global`, `Fw`, and `Bw` surfaces separate.
Each probe group should produce all three surfaces unless implementation
evidence justifies a narrower smoke stage.

| Probe Group | Candidate Role | Initial Surfaces | Decision Value |
| --- | --- | --- | --- |
| `robust_loss` | Robust deterministic central estimate. | `global`, `Fw`, `Bw` | Tests whether reducing outlier sensitivity improves mean-surface and full-curve behavior. |
| `quantile_probabilistic` | Conditional interval or uncertainty estimate. | `global`, `Fw`, `Bw` | Tests whether the target should be evaluated as a distribution rather than one deterministic curve. |
| `mixture_density` | Multi-modal local target model. | `global`, `Fw`, `Bw` | Tests whether similar operating points contain multiple plausible preload or state-dependent offset modes. |
| `latent_state_hysteresis` | Causal state-conditioned predictor. | `global`, `Fw`, `Bw` | Tests whether short history or previous-condition summaries explain offset and fragile harmonic variation. |

The first implementation package may split these into smaller campaigns if the
blast radius is too large. The recommended order is:

1. `robust_loss`;
2. `quantile_probabilistic`;
3. `mixture_density`;
4. `latent_state_hysteresis`.

## Planned Probe Details

### Robust Loss Probe

Purpose:

- keep a deterministic prediction path;
- reduce sensitivity to outliers and local measurement dispersion;
- test whether the current failures are mostly caused by a small number of
  high-leverage curves.

Candidate losses:

- Huber-style loss;
- MAE or log-cosh control;
- Tukey or biweight-style robust loss if implemented safely;
- trimmed or winsorized loss if the batch grouping supports it without target
  leakage.

Promotion condition:

- lower raw curve error or mean-offset error without degrading centered-shape,
  amplitude, or phase diagnostics.

### Quantile Or Probabilistic Probe

Purpose:

- predict a median or interval instead of only a mean;
- expose uncertainty where the experimental target is locally dispersed;
- avoid treating non-repeatable offset as deterministic model failure.

Candidate outputs:

- quantile heads such as `p10`, `p50`, and `p90`;
- Gaussian-style `mu` and `sigma` heads;
- negative-log-likelihood or pinball-loss objectives.

Promotion condition:

- calibrated intervals around high-dispersion curves and improved median or
  mean-surface behavior in official `Track 2` playback.

### Mixture-Density Probe

Purpose:

- represent multiple plausible local target states for similar operating
  points;
- test the hypothesis that preload or elastic release creates multiple local
  offset modes.

Candidate outputs:

- mixture weights;
- mixture means for offset or low-order harmonic components;
- mixture variances with numerical guards.

Promotion condition:

- improved handling of offset outliers without unstable mode collapse or
  degraded direction-specific behavior.

### Latent-State / Hysteresis-Aware Probe

Purpose:

- test whether causal history explains part of the hidden mechanical state;
- model preload, elastic release, direction transition, or previous-condition
  influence without using future data.

Candidate inputs:

- previous operating-condition summaries;
- short causal TE or residual history only if already available at inference;
- direction-transition flags;
- monotonic counters or sequence-state summaries that do not include future
  curve information.

Promotion condition:

- reduced offset and fragile-harmonic error on repeated or nearby operating
  regimes without weakening strict causal deployment discipline.

## Harmonic Focus

The planned diagnostics should report at least these harmonic groups:

| Group | Role |
| --- | --- |
| `h0` | Primary mean-surface and offset-dispersion channel. |
| `h1` | Secondary low-order fragile component. |
| Middle harmonic band | Shape-reference band expected to be more stable. |
| `h156`, `h162`, `h240` | High-order fragile components requiring separate robust or structured treatment. |

The campaign must not conclude that `h0` is the sole cause unless the
component-level error, repeatability, and model-side surface evidence support
that claim.

## Runtime Input Boundary

Allowed inference inputs:

- current point-level operating state;
- direction, speed, torque, oil temperature, and angular position when known at
  runtime;
- causal history that would exist before the current prediction time;
- causal derived features computed only from available past or current state.

Forbidden inference inputs:

- future TE values;
- future angular positions;
- full held-out truth-curve statistics;
- mean-centering based on the target curve;
- complete-curve normalization unavailable during prediction.

Full curves may be used for training-loss aggregation, validation, diagnostics,
and promotion after inference, but not as future information supplied to the
model.

## Expected Campaign Package After Approval

After this planning gate is approved, the implementation step should prepare:

- `config/training/track2h_dispersion_aware_modeling/`;
- queue YAML files for the selected probe set;
- a package preparation script under `scripts/campaigns/track2/`;
- a package validation script under `scripts/campaigns/track2/`;
- `scripts/campaigns/track2/run_track2h_dispersion_aware_modeling_campaign.ps1`;
- `doc/scripts/campaigns/track2/run_track2h_dispersion_aware_modeling_campaign.md`;
- updated prepared campaign state in `doc/running/active_training_campaign.yaml`;
- local and `-Remote` launch commands.

The launcher must support:

- `-PreflightOnly`;
- `-EnqueueOnly` for local verification;
- `-Remote` through the repository-owned remote training infrastructure.

## Prepared Package Status

The first `Track 2H` package has been prepared for the robust-loss probe group.
It intentionally does not yet include the later quantile/probabilistic,
mixture-density, or latent-state / hysteresis-aware packages.

Prepared package:

- package root:
  `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/`;
- queue entries: `9`;
- surfaces: `global`, `Fw`, and `Bw`;
- robust pointwise losses: `mae`, `smooth_l1`, and `log_cosh`;
- launcher:
  `scripts/campaigns/track2/run_track2h_dispersion_aware_modeling_campaign.ps1`;
- validator:
  `scripts/campaigns/track2/validate_track2h_dispersion_aware_modeling_package.py`;
- active campaign state: `prepared`.

Validated commands:

```powershell
conda run -n pinns_env python -B scripts/campaigns/track2/validate_track2h_dispersion_aware_modeling_package.py --queue-root config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue --require-prepared-state
.\scripts\campaigns\track2\run_track2h_dispersion_aware_modeling_campaign.ps1 -PreflightOnly
```

The `mae_robust_global`, `smooth_l1_robust_global`, and
`log_cosh_robust_global` entries also passed one-batch validation. The
`smooth_l1_robust_global` entry passed a one-batch Lightning fast-dev smoke
test.

## Verification Plan

Before training launch:

- run Python compile checks on touched implementation and campaign scripts;
- validate all generated YAML files resolve;
- run one-batch checks for every implemented probe group;
- run at least one fast-dev smoke check for a `global` entry;
- run Markdown QA on touched documentation;
- confirm `doc/running/active_training_campaign.yaml` is in `prepared` state;
- provide exact local and `-Remote` commands.

After training completion:

- close out the campaign with Markdown and PDF results;
- export and visually validate the real PDF;
- update family and program registries;
- clean active campaign state;
- update the live backlog and training master summary;
- propose official `Track 2` refresh as a separate operator-launched step.

## Decision Gates

| Gate | Decision |
| --- | --- |
| Planning approval | Authorize implementation of the selected `Track 2H` probe subset. |
| Package validation | Authorize local or remote campaign launch. |
| Campaign closeout | Decide which probe group deserves official `Track 2` refresh. |
| Official `Track 2` refresh | Decide whether the probe should feed `Wave 3`, `Wave 4`, or the later integrated multi-head architecture. |

## Non-Goals

- No PLC-friendly export optimization in this stage.
- No direct integrated multi-head campaign before `Track 2H` evidence.
- No claim that `h0` is the sole confirmed cause of the offset symptom.
- No future-looking smoothing or target-curve statistics at inference time.
