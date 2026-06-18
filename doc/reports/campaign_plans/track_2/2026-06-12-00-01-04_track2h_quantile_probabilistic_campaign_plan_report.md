# Track 2H Quantile Probabilistic Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the second executable `Track 2H`
dispersion-aware package: quantile and Gaussian probabilistic regression for
locally dispersed TE curves.

The completed robust-loss `Track 2H` campaign is now a verified exploratory
baseline. It showed that robust deterministic fitting is useful, but not
sufficient to beat the current `Track 2` direction-parallel leaders. The next
campaign should therefore test whether the target should be modeled as an
interval or distribution in regimes where preload, elastic release, or hidden
experimental state may perturb the measured curve.

Training is not approved by this report. The executable campaign package must
be generated only after this plan and the paired technical document are
explicitly approved.

## Paired Technical Document

- [technical/2026-06/2026-06-11/2026-06-11-23-49-15_track2h_quantile_probabilistic_package.md](../../technical/2026-06/2026-06-11/2026-06-11-23-49-15_track2h_quantile_probabilistic_package.md)

## Baseline Interpretation

The accepted baseline before this campaign is:

| Evidence | Interpretation |
| --- | --- |
| `Track 2H` robust-loss campaign | Robust deterministic losses were trained successfully across `global`, `Fw`, and `Bw`. |
| `Track 2H` official verification refresh | Robust-loss candidates were verified as exploratory baselines but not promoted. |
| Best robust `Fw` candidate | `track2h_mae_robust_Fw`, official `Track 2` MAE `0.003134`. |
| Best robust `Bw` candidate | `track2h_smooth_l1_robust_Bw`, official `Track 2` MAE `0.003078`. |
| Best robust `global` candidate | `track2h_mae_robust_global`, official `Track 2` MAE `0.003401`. |
| Current accepted `Fw` leader | `rcim_retuned_GBM19_Fw`, official `Track 2` MAE `0.001089`. |
| Current accepted `Bw` leader | `periodic_gru_sequence_Bw`, official `Track 2` MAE `0.002392`. |
| Current accepted `global` leader | `periodic_gru_sequence_global`, official `Track 2` MAE `0.002704`. |

The working hypothesis is that a deterministic central estimate may be the
wrong sole training target for locally dispersed measurements. The quantile and
probabilistic package must test this without weakening the deterministic
playback path required by official `Track 2` verification.

## Candidate Matrix

The first quantile/probabilistic package should remain deliberately narrow:

| Candidate Group | Surfaces | Deterministic Playback Curve | Training Objective |
| --- | --- | --- | --- |
| `quantile_p10_p50_p90` | `global`, `Fw`, `Bw` | `p50` | Pinball loss over `p10`, `p50`, and `p90`. |
| `gaussian_nll` | `global`, `Fw`, `Bw` | `mu` | Gaussian negative log likelihood with guarded dispersion. |

This produces six queued runs:

1. `te_track2h_quantile_p10_p50_p90_global`
2. `te_track2h_quantile_p10_p50_p90_fw`
3. `te_track2h_quantile_p10_p50_p90_bw`
4. `te_track2h_gaussian_nll_global`
5. `te_track2h_gaussian_nll_fw`
6. `te_track2h_gaussian_nll_bw`

The package intentionally excludes mixture-density and latent-state /
hysteresis-aware candidates. Those remain later `Track 2H` packages so this
campaign can answer one question cleanly: whether explicit uncertainty-aware
heads improve the robust-loss result or expose useful calibrated intervals.

## Model And Loss Requirements

The implementation should inspect the existing causal sequence model and
training objective stack before choosing the concrete code shape.

Required behavior:

- keep the existing causal runtime input boundary;
- avoid target-curve statistics at inference time;
- support deterministic extraction of `p50` or `mu` for standard curve metrics;
- keep output dimensions and loss aggregation explicit in generated YAML;
- guard dispersion outputs against zero variance, overflow, and non-finite
  values;
- fail fast when a configured probabilistic head is used with an incompatible
  loss or target shape.

Preferred implementation:

- extend the current curve-aware harmonic residual-offset path with an explicit
  head or objective option if the training stack supports it cleanly;
- otherwise add narrowly named `Track 2H` model-family keys for quantile and
  Gaussian heads, without disturbing the completed robust-loss package.

## Evaluation Plan

Each run must still report the normal deterministic TE metrics used in previous
campaigns. In addition, the package should emit uncertainty-specific summaries.

Required deterministic checks:

- validation and test MAE;
- full-curve playback metrics;
- direction-specific comparison for `global`, `Fw`, and `Bw`;
- later official `Track 2` comparison using `p50` or `mu` only.

Required probabilistic checks:

- quantile pinball loss for quantile candidates;
- negative log likelihood for Gaussian candidates;
- empirical interval coverage;
- interval width;
- coverage versus width tradeoff on high-error candidates;
- focused diagnostics for `h0`, `h1`, the stable middle band, and high-order
  fragile harmonics such as `h156`, `h162`, and `h240`.

The campaign should not promote a candidate only because it has wider
intervals. A useful candidate must either improve deterministic playback, expose
well-calibrated uncertainty around difficult regimes, or provide evidence that
later mixture-density or latent-state packages are needed.

## Expected Campaign Package After Approval

After this planning gate is approved, the implementation step should prepare:

- a dedicated package root under
  `config/training/track2h_quantile_probabilistic_modeling/`;
- generated queue YAML files for the six primary candidates;
- `scripts/campaigns/track_2/prepare_track2h_quantile_probabilistic_campaign.py`;
- `scripts/campaigns/track_2/validate_track2h_quantile_probabilistic_package.py`;
- `scripts/campaigns/track_2/run_track2h_quantile_probabilistic_campaign.ps1`;
- `doc/scripts/campaigns/track_2/run_track2h_quantile_probabilistic_campaign.md`;
- updated prepared campaign state in `doc/running/active_training_campaign.yaml`;
- exact local and `-Remote` launch commands.

The launcher must support:

- `-PreflightOnly`;
- `-EnqueueOnly`;
- `-Remote` through the repository-owned remote training infrastructure.

## Prepared Package Status

The `Track 2H` quantile/probabilistic package has been prepared.

Prepared package:

- package root:
  `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/`;
- queue entries: `6`;
- surfaces: `global`, `Fw`, and `Bw`;
- probabilistic profiles: `quantile_p10_p50_p90` and `gaussian_nll`;
- deterministic playback: `p50` for quantile runs and `mu` for Gaussian runs;
- launcher:
  `scripts/campaigns/track_2/run_track2h_quantile_probabilistic_campaign.ps1`;
- validator:
  `scripts/campaigns/track_2/validate_track2h_quantile_probabilistic_package.py`;
- active campaign state: `prepared`.

Validated commands:

```powershell
conda run -n pinns_env python -B scripts/campaigns/track_2/validate_track2h_quantile_probabilistic_package.py --queue-root config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign/queue --require-prepared-state --run-one-batch
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_campaign.ps1 -PreflightOnly
```

## Verification Plan

Before training launch:

- run Python compile checks on touched scripts and model modules;
- validate that all generated YAML files resolve;
- validate that quantile and Gaussian heads produce the expected output shapes;
- run one-batch checks for at least one `global`, one `Fw`, and one `Bw`
  candidate;
- run at least one fast-dev Lightning smoke check when the implementation path
  changes training-module behavior;
- run Markdown QA on touched documentation;
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
| Planning approval | Authorize generation of the quantile/probabilistic package. |
| Package validation | Authorize local or remote campaign launch. |
| Campaign closeout | Decide whether uncertainty-aware heads outperform robust-loss baselines or only improve calibration. |
| Official `Track 2` refresh | Decide whether the best candidate should influence mixture, latent-state, `Wave 3`, or multi-head design. |

## Non-Goals

- No mixture-density candidates in this package.
- No latent-state or hysteresis-aware features in this package.
- No integrated multi-task / multi-head architecture in this package.
- No PLC-friendly export optimization in this package.
- No future-looking smoothing or target-curve statistics at inference time.
