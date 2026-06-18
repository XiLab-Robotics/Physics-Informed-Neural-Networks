# Wave 3 Harmonic Prior Residual Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the first real `Wave 3` campaign:
`wave3_harmonic_prior_residual` across `global`, `Fw`, and `Bw` surfaces.

The completed `Track 2H` dispersion-aware probes show that robust,
probabilistic, and MDN training pressures are useful exploratory evidence but
do not replace the accepted direction-parallel `Track 2` leaders. The next
question is whether explicit harmonic structure plus learned residual
correction improves curve fidelity more reliably than loss-only changes.

Training is not approved by this report. The executable campaign package must
be generated only after this plan and the paired technical document are
explicitly approved.

## Paired Technical Document

- [technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md](../../../technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md)

## Baseline Interpretation

| Evidence | Interpretation |
| --- | --- |
| `Track 2H` robust-loss campaign | Robust deterministic losses are useful central-tendency controls, especially for fragile dispersion regimes. |
| `Track 2H` quantile/probabilistic campaign | Quantile and Gaussian heads improved some exploratory branches but did not displace official leaders. |
| `Track 2H` MDN campaign and verification | MDN improved the backward dispersion-aware branch, but global/forward behavior and near-single-component usage argue against making MDN the first Wave 3 default. |
| `Wave 3` smoke-ready validation | `wave3_harmonic_prior_residual` already passed one-batch training-stack validation and is the cleanest first real Wave 3 candidate. |
| Accepted official leaders | Direction-parallel and periodic sequence candidates remain the promotion baseline. |

## Candidate Matrix

The first package should remain narrow enough to diagnose structure:

| Candidate Group | Surfaces | Main Loss Policy | Main Test |
| --- | --- | --- | --- |
| `harmonic_prior_residual_control` | `global`, `Fw`, `Bw` | deterministic curve control | Tests whether explicit harmonic reconstruction plus residual correction is already competitive. |
| `harmonic_prior_residual_robust` | `global`, `Fw`, `Bw` | robust or probabilistic pressure selected from Track 2H evidence | Tests whether Wave 3 structure benefits from dispersion-aware pressure without MDN as the default. |

The exact queue size should be finalized during package generation, but the
minimum campaign must include `global`, `Fw`, and `Bw`. If runtime budget is
tight, prefer one control and one robust/probabilistic profile per surface
over a broad sweep.

## Model And Loss Requirements

Required behavior:

- preserve causal inputs and direction-separated reporting;
- reconstruct the recovered paper harmonic set through an explicit structured
  branch;
- expose the learned residual curve separately from the final curve;
- keep deterministic playback as the standard campaign and official
  `Track 2` comparison curve;
- report low-order fragile channels, stable middle harmonics, and high-order
  fragile harmonics separately in diagnostics;
- avoid measured curve mean, future TE samples, or held-out target statistics
  during inference;
- fail fast when a campaign config is still marked as validation-only or
  `not_campaign_ready`.

Preferred first loss policy:

- include a deterministic control profile;
- include one robust or probabilistic profile selected from completed
  `Track 2H` evidence;
- do not use MDN as the first default unless a later explicit gate chooses it.

## Expected Campaign Package After Approval

After this planning gate is approved, the implementation step should prepare:

- a dedicated package root under
  `config/training/wave3_harmonic_prior_residual/campaigns/`;
- generated queue YAML files for `global`, `Fw`, and `Bw`;
- `scripts/campaigns/wave_3/prepare_wave3_harmonic_prior_residual_campaign.py`;
- `scripts/campaigns/wave_3/validate_wave3_harmonic_prior_residual_campaign.py`;
- `scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.ps1`;
- `doc/scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.md`;
- updated prepared campaign state in `doc/running/active_training_campaign.yaml`;
- exact local and `-Remote` launch commands.

The launcher must support:

- `-PreflightOnly`;
- `-EnqueueOnly`;
- `-Remote` through the repository-owned remote training infrastructure.

## Prepared Package Status

The `Wave 3` harmonic-prior residual campaign package has been prepared.

Prepared package:

- package root:
  `config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/`;
- queue entries: `6`;
- surfaces: `global`, `Fw`, and `Bw`;
- profiles: `pointwise_control` and `smooth_l1_structured`;
- deterministic playback: final structured plus residual TE curve;
- launcher:
  `scripts/campaigns/wave_3/run_wave3_harmonic_prior_residual_campaign.ps1`;
- validator:
  `scripts/campaigns/wave_3/validate_wave3_harmonic_prior_residual_campaign.py`;
- active campaign state: `prepared`.

Validated commands:

```powershell
conda run -n pinns_env python -B scripts/campaigns/wave_3/validate_wave3_harmonic_prior_residual_campaign.py --queue-root config/training/wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign/queue --require-prepared-state --run-one-batch
.\scripts\campaigns\wave_3\run_wave3_harmonic_prior_residual_campaign.ps1 -PreflightOnly
```

## Verification Plan

Before training launch:

- run Python compile checks on touched scripts and model modules;
- validate that generated YAML files are campaign-ready and not validation-only;
- validate model construction and finite one-batch loss for all surfaces;
- validate auxiliary harmonic, base-curve, residual, and final-curve outputs;
- run the dedicated launcher in `-PreflightOnly`;
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
| Planning approval | Authorize generation of the Wave 3 harmonic-prior residual package. |
| Package validation | Authorize local or remote campaign launch. |
| Campaign closeout | Decide whether explicit harmonic structure improves scalar and curve metrics beyond Track 2H loss-only probes. |
| Official `Track 2` refresh | Decide whether Wave 3 candidates should feed Wave 4, latent-state modeling, or the integrated multi-head design. |

## Non-Goals

- No latent-state or hysteresis-aware branch in this first Wave 3 package.
- No Wave 4 PINN loss or MMT feature integration.
- No integrated multi-task / multi-head architecture.
- No MDN default unless a later explicit gate changes the loss policy.
- No PLC-friendly export optimization in this package.
