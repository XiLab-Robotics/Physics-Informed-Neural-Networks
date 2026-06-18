# Track 2H Mixture Density Heads Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the next executable `Track 2H`
dispersion-aware package: mixture-density heads for locally dispersed TE
curves.

The completed robust-loss and quantile/probabilistic campaigns are verified
exploratory baselines, not promoted official winners. They still provide
evidence that the local dispersion problem should be modeled explicitly before
the project commits to a large integrated multi-task / multi-head architecture.
The mixture-density package tests whether a small set of plausible local TE
outcomes explains difficult regimes better than one robust curve, one median
curve, or one Gaussian distribution.

Training is not approved by this report. The executable campaign package must
be generated only after this plan and the paired technical document are
explicitly approved.

## Paired Technical Document

- [technical/2026-06/2026-06-13/2026-06-13-10-40-25_track2h_mixture_density_heads_package.md](../../technical/2026-06/2026-06-13/2026-06-13-10-40-25_track2h_mixture_density_heads_package.md)

## Baseline Interpretation

The accepted baseline before this campaign is:

| Evidence | Interpretation |
| --- | --- |
| `Track 2H` robust-loss campaign | Robust deterministic losses trained successfully and remain useful central-tendency controls. |
| `Track 2H` quantile/probabilistic campaign | Quantile and Gaussian heads improved some Track 2H results but did not displace the official leaders. |
| Official `Track 2H` probabilistic refresh | The probabilistic package is verified as exploratory and should feed later mixture, latent-state, and multi-head design. |
| Strongest probabilistic `global` | `track2h_gaussian_nll_global`, deterministic `mu` playback. |
| Strongest probabilistic `Fw` | `track2h_gaussian_nll_global` when evaluated on forward Track 2 metrics. |
| Strongest probabilistic `Bw` | `track2h_quantile_p10_p50_p90_Bw`, deterministic `p50` playback. |
| Current accepted official leaders | Direction-parallel and periodic sequence candidates remain the promotion baseline. |

The working hypothesis is that some local TE observations may come from
multiple nearby regimes caused by preload, elastic release, hidden protocol
state, or hysteresis-like history. A mixture head can represent this as several
candidate local means with learned probabilities instead of forcing the target
into one deterministic value or one symmetric Gaussian.

## Candidate Matrix

The first mixture-density package should remain narrow:

| Candidate Group | Surfaces | Deterministic Playback Curve | Training Objective |
| --- | --- | --- | --- |
| `mdn_k2` | `global`, `Fw`, `Bw` | mixture expectation | Two-component Gaussian mixture NLL. |
| `mdn_k3` | `global`, `Fw`, `Bw` | mixture expectation | Three-component Gaussian mixture NLL. |

This produces six queued runs:

1. `te_track2h_mdn_k2_global`
2. `te_track2h_mdn_k2_fw`
3. `te_track2h_mdn_k2_bw`
4. `te_track2h_mdn_k3_global`
5. `te_track2h_mdn_k3_fw`
6. `te_track2h_mdn_k3_bw`

The package intentionally excludes latent-state / hysteresis-aware candidates,
Wave 3 hybrid structured models, Wave 4 PINN losses, and the final integrated
multi-task / multi-head architecture. Those remain later branches.

## Model And Loss Requirements

Required behavior:

- keep the existing causal runtime input boundary;
- avoid measured target statistics at inference time;
- output mixture logits, component means, and guarded component log-scales;
- use stable log-sum-exp negative log likelihood;
- guard component scales with explicit minimum and maximum bounds;
- extract deterministic playback as the mixture expectation;
- fail fast when an MDN profile is used with an incompatible output size or
  target shape;
- preserve `global`, `Fw`, and `Bw` surfaces with separate registries.

Preferred implementation:

- extend the current Track 2H curve-aware harmonic residual-offset path if the
  existing output-size and loss-profile hooks can support MDN safely;
- otherwise add narrowly named MDN model/loss profile keys without changing
  completed robust-loss or quantile/probabilistic behavior.

## Evaluation Plan

Each run must still report deterministic TE metrics used in previous
campaigns. The deterministic comparison curve is the mixture expectation.

Required deterministic checks:

- validation and test MAE;
- full-curve playback metrics;
- direction-specific summaries for `global`, `Fw`, and `Bw`;
- later official `Track 2` comparison using mixture expectation only.

Required mixture-specific checks:

- negative log likelihood;
- effective component usage;
- mixture-weight entropy;
- average and percentile component scale;
- component-mean separation;
- high-dispersion summaries for `h0`, `h1`, the stable middle band, and
  fragile higher harmonics such as `h156`, `h162`, and `h240`;
- comparison against Gaussian NLL to see whether multimodality adds value over
  single-distribution uncertainty.

The campaign should not promote a candidate only because it uses more
components. A useful candidate must improve deterministic playback, improve
distributional fit without collapsing components, or provide evidence that
latent-state / hysteresis-aware models are the correct next step.

## Expected Campaign Package After Approval

After this planning gate is approved, the implementation step should prepare:

- a dedicated package root under
  `config/training/track2h_mixture_density_heads/campaigns/`;
- generated queue YAML files for the six primary candidates;
- `scripts/campaigns/track_2/prepare_track2h_mixture_density_heads_campaign.py`;
- `scripts/campaigns/track_2/validate_track2h_mixture_density_heads_package.py`;
- `scripts/campaigns/track_2/run_track2h_mixture_density_heads_campaign.ps1`;
- `doc/scripts/campaigns/track_2/run_track2h_mixture_density_heads_campaign.md`;
- updated prepared campaign state in `doc/running/active_training_campaign.yaml`;
- exact local and `-Remote` launch commands.

The launcher must support:

- `-PreflightOnly`;
- `-EnqueueOnly`;
- `-Remote` through the repository-owned remote training infrastructure.

## Prepared Package Status

The `Track 2H` mixture-density heads package has been prepared.

Prepared package:

- package root:
  `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/`;
- queue entries: `6`;
- surfaces: `global`, `Fw`, and `Bw`;
- mixture profiles: `mdn_k2` and `mdn_k3`;
- deterministic playback: mixture expectation;
- launcher:
  `scripts/campaigns/track_2/run_track2h_mixture_density_heads_campaign.ps1`;
- validator:
  `scripts/campaigns/track_2/validate_track2h_mixture_density_heads_package.py`;
- active campaign state: `prepared`.

Validated commands:

```powershell
conda run -n pinns_env python -B scripts/campaigns/track_2/validate_track2h_mixture_density_heads_package.py --queue-root config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue --require-prepared-state --run-one-batch
.\scripts\campaigns\track_2\run_track2h_mixture_density_heads_campaign.ps1 -PreflightOnly
```

## Verification Plan

Before training launch:

- run Python compile checks on touched scripts and model modules;
- validate that all generated YAML files resolve;
- validate MDN output shape for `k=2` and `k=3`;
- validate finite MDN NLL and deterministic expectation extraction;
- run one-batch checks for at least one `global`, one `Fw`, and one `Bw`
  candidate;
- run fast-dev Lightning smoke checks if the training module changes;
- run Markdown QA on touched documentation;
- run Sphinx QA when documentation indices change;
- confirm `doc/running/active_training_campaign.yaml` is in `prepared` state;
- provide exact local and `-Remote` commands.

After training completion:

- close out the campaign with Markdown and PDF results;
- export and validate the real PDF deliverable;
- update family and program registries;
- clean active campaign state;
- update the live backlog and training master summary;
- propose official `Track 2` refresh as a separate operator-launched step.

## Decision Gates

| Gate | Decision |
| --- | --- |
| Planning approval | Authorize generation of the mixture-density package. |
| Package validation | Authorize local or remote campaign launch. |
| Campaign closeout | Decide whether mixture heads improve over Gaussian/quantile Track 2H baselines. |
| Official `Track 2` refresh | Decide whether mixture behavior should feed latent-state, Wave 3, or multi-head design. |

## Non-Goals

- No latent-state or hysteresis-aware features in this package.
- No Wave 3 hybrid structured model changes in this package.
- No Wave 4 PINN loss or feature-generator changes in this package.
- No integrated multi-task / multi-head architecture in this package.
- No PLC-friendly export optimization in this package.
- No future-looking smoothing or target-curve statistics at inference time.
