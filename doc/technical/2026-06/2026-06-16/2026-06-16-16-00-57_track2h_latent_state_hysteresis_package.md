# Wave 4.4 Latent-State Hysteresis Package

## Overview

This technical note aligns the repository status after the completed `Wave 5.1`
official `TE Curve Verification Pipeline` verification refresh and prepares the next targeted
`Wave 4.4` probe: latent-state / hysteresis-aware modeling for the observed
offset, preload, and fragile-harmonic behavior.

The immediate status correction is that `Wave 5.1` harmonic-prior residual has
now completed both normal campaign closeout and official `TE Curve Verification Pipeline`
verification. It is a verified exploratory baseline and is not promoted over
the accepted direction-parallel leaders.

The next modeling question is whether a causal hidden state, estimated from
past operating conditions and direction transitions, explains residual offset
or fragile-harmonic errors better than robust losses, probabilistic heads,
mixture-density heads, or the first `Wave 5.1` structured branch.

This document and its campaign plan are planning gates only. No model code,
campaign YAMLs, launcher scripts, or active campaign state should be modified
until the user explicitly approves this package.

## Technical Approach

The `Wave 4.4` package should remain narrow and diagnostic. It should test
latent-state / hysteresis-aware candidates that use only deployment-valid
causal information:

- current operating point: angular position, speed, torque, temperature, and
  direction;
- short history of previous operating states already observed at runtime;
- direction-transition or previous-condition summaries derived without future
  target information;
- no measured TE, curve mean, full held-out curve statistic, future sample, or
  post-prediction centering as an input.

The first candidate package should compare at least:

- a compact causal latent-state encoder, such as a small GRU or temporal
  convolution over recent operating states;
- an offset/low-order head focused on `h0`-like mean behavior and `h1`;
- a residual curve head for remaining shape correction;
- deterministic playback curves for scalar and official `TE Curve Verification Pipeline` evaluation.

The package must keep `global`, `Fw`, and `Bw` as separate surfaces. It should
compare directly against:

- completed `Wave 4.1` robust-loss candidates;
- completed `Wave 4.2` quantile/probabilistic candidates;
- completed `Wave 4.3` MDN candidates, especially the strong `Bw` branch;
- completed `Wave 5.1` harmonic-prior residual candidates;
- accepted direction-parallel `TE Curve Verification Pipeline` leaders.

The physics-informed / PINN-style branch remains `Wave 5.2`, not `Wave 4.4`.
`Wave 4.4` should answer whether the missing signal is a causal hidden state
or protocol-history effect before the project spends effort on heavier
physics-informed losses.

Because this package will touch PyTorch-facing model code after approval,
Context7 must be consulted before implementation.

## Involved Components

- `doc/technical/2026-06/2026-06-16/2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md`
  records this technical gate.
- `doc/reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md`
  records the matching preliminary campaign plan.
- `doc/running/te_model_live_backlog.md` records the post-`Wave 5.1` status
  alignment and the new active next gate.
- `doc/running/active_training_campaign.yaml` records the completed `Wave 5.1`
  campaign and its completed official `TE Curve Verification Pipeline` verification status.
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md` records the
  high-level program snapshot.
- `doc/README.md` registers the new technical note and campaign plan.
- Existing model references for later implementation include:
  - `scripts/models/temporal_sequence_network.py`;
  - `scripts/models/periodic_temporal_sequence_network.py`;
  - `scripts/models/sequential_residual_offset_network.py`;
  - `scripts/models/harmonic_residual_offset_network.py`;
  - `scripts/models/wave3_harmonic_prior_residual_network.py`;
  - `scripts/training/transmission_error_regression_module.py`;
  - `scripts/models/model_factory.py`.
- Existing campaign-package precedents include:
  - `scripts/campaigns/track_2/prepare_track2h_mixture_density_heads_campaign.py`;
  - `scripts/campaigns/track_2/validate_track2h_mixture_density_heads_package.py`;
  - `scripts/campaigns/track_2/run_track2h_mixture_density_heads_campaign.ps1`.

No subagent is planned.

## Implementation Steps

1. Create this technical document and register it from `doc/README.md`.
2. Create the paired campaign plan under `doc/reports/campaign_plans/track_2/`.
3. Align status documents so `Wave 5.1` official `TE Curve Verification Pipeline` verification is no
   longer described as pending.
4. Stop for explicit user approval before implementation changes.
5. After approval, use Context7 for PyTorch implementation details.
6. Inspect existing temporal, offset, harmonic-residual, and Wave 5.1 model
   classes before choosing whether `Wave 4.4` is a new narrow model type or
   a configuration-driven extension.
7. Implement a causal latent-state encoder with explicit input-history
   boundaries and no target leakage.
8. Add auxiliary outputs for latent state, offset/low-order prediction, and
   residual curve prediction.
9. Generate a narrow `global`, `Fw`, and `Bw` campaign package.
10. Add package validation for queue schema, causal input metadata, model
    construction, finite one-batch loss, and auxiliary outputs.
11. Add a PowerShell launcher with local and `-Remote` support plus a launcher
    note.
12. Update `doc/running/active_training_campaign.yaml` only after package
    generation is approved.
13. Run compile checks, package validation, Markdown QA, and Sphinx QA when
    portal scope changes.
14. Stop before training execution and provide exact local and `-Remote`
    launch commands.
