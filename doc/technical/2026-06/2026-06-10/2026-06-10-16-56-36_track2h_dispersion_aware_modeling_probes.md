# Track 2H Dispersion-Aware Modeling Probes

## Overview

This technical document plans the next `Track 2` modeling branch after the
completed `Track 2G` official verification refresh and the h0/component-offset
diagnostics.

`Track 2G` showed that curve-aware losses are useful experimental controls,
especially on the `Fw` and `global` surfaces, but loss-only tuning did not
promote a new accepted `Track 2` leader. The h0 diagnostics also showed that
`h0` is the right mean-like channel to inspect, while large absolute measured
`h0` alone does not explain where models fail. The next branch should
therefore test whether the problem is better handled as locally dispersed,
partially non-deterministic target behavior rather than as a purely
deterministic regression error.

`Track 2H` is the dispersion-aware probe stage. It should test robust,
probabilistic, mixture, and latent-state approaches separately before the
project commits to a larger integrated multi-task / multi-head architecture.

## Technical Approach

The campaign should keep the existing causal input boundary and the
direction-separated `Track 2` promotion surface:

- `global`: bidirectional training, evaluated by direction and combined;
- `Fw`: forward-only training and forward-only evaluation;
- `Bw`: backward-only training and backward-only evaluation.

The first `Track 2H` implementation should use a conservative two-level
design:

1. Start from a known stable curve-capable base branch, preferably the
   `Track 2G` curve-aware harmonic residual-offset probe family.
2. Add one dispersion-aware mechanism at a time so each result can be
   interpreted against `Track 2G`, `Track 2F-bis`, `Wave 2B`, and the accepted
   `Track 2` leaders.

The planned probe groups are:

- robust regression losses for local outlier resistance;
- quantile or probabilistic heads for conditional uncertainty;
- mixture-density heads for multi-modal local target states;
- latent-state or hysteresis-aware causal features for preload or mechanical
  state effects.

The first package should not enforce PLC-friendly export constraints. This is
a Python research branch. The retained hard boundary is causal input
discipline: no future TE values, future angular positions, full held-out curve
normalization, or truth-curve means may enter inference.

## Involved Components

Expected documentation and planning components:

- this technical document;
- `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- `doc/README.md`.

Expected implementation components after approval:

- one or more narrow model/loss extensions in the existing TE training stack;
- campaign preparation script under `scripts/campaigns/track2/`;
- package validation script under `scripts/campaigns/track2/`;
- local and `-Remote` PowerShell launcher under `scripts/campaigns/track2/`;
- launcher note under `doc/scripts/campaigns/track2/`;
- campaign YAML package under `config/training/track2h_dispersion_aware_modeling/`;
- prepared campaign state in `doc/running/active_training_campaign.yaml`.

Prepared first implementation package:

- robust-loss probe group only;
- `9` queue entries: `mae_robust`, `smooth_l1_robust`, and
  `log_cosh_robust` across `global`, `Fw`, and `Bw`;
- package root:
  `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/`;
- launcher:
  `scripts/campaigns/track2/run_track2h_dispersion_aware_modeling_campaign.ps1`;
- validator:
  `scripts/campaigns/track2/validate_track2h_dispersion_aware_modeling_package.py`;
- active campaign state: `prepared`.

Expected evaluation components after training:

- campaign results Markdown and PDF;
- family and program registry updates;
- optional operator-launched official `Track 2` verification refresh;
- refreshed visual overlays and collage reports if the campaign produces
  viable candidates.

## Implementation Steps

1. Create and approve this technical document.
2. Create the preliminary `Track 2H` campaign planning report.
3. Implement the smallest runnable robust-regression probe first, using the
   current `Track 2G` pointwise-control candidates as the MSE control branch.
4. Add quantile/probabilistic, mixture-density, and latent-state probes as
   separate named candidate groups, not as one opaque combined model.
5. Generate campaign YAMLs, launcher, launcher note, validator, active campaign
   state, and local / `-Remote` commands only after implementation approval.
6. Validate the package with compile checks, YAML resolution, one-batch checks,
   and preflight launcher validation.
7. Wait for explicit user approval before launching training.
8. After training, close out the campaign normally before proposing the
   optional official `Track 2` refresh.

## Approval Gate

This document and the paired campaign plan define the next modeling branch.
They do not approve training execution. Because `Track 2H` introduces new
losses and heads that are not yet materialized as validated runnable campaign
entries, the YAML package and launcher should be generated only after this
planning gate is approved.
