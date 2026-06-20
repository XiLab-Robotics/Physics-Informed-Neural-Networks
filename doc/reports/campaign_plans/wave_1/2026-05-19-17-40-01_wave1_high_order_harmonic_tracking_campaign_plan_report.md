# Wave 1 High-Order Harmonic Tracking Campaign Plan Report

## Overview

This preliminary plan defines a controlled `Wave 1` follow-up campaign for
direct transmission-error models that currently smooth multi-frequency TE
curves in `TE Curve Verification Pipeline` plot review. The campaign focuses on the two model families
that can immediately benefit from richer angular bases:
`harmonic_regression` and `residual_harmonic_mlp`.

The approved technical document is:
`doc/technical/2026-05/2026-05-19/2026-05-19-17-32-08_wave1_high_order_harmonic_tracking.md`.

No training should be launched from this plan until this planning report is
explicitly approved.

## Motivation

The observed gap is not only an aggregate metric issue. The `TE Curve Verification Pipeline` curves
show that direct `Wave 1` models tend to average out high-frequency and
mixed-amplitude oscillations. In contrast, the paper-faithful `RCIM Model-Bank Reproduction` model
banks benefit from harmonic-wise decomposition and therefore preserve more of
the visible TE structure.

This campaign tests whether increasing the direct-model harmonic basis can
recover curve detail before adding more complex temporal models.

## Candidate Harmonic Banks

| Bank | Harmonic indices | Purpose |
| --- | --- | --- |
| Baseline | Current best `harmonic_order` values | Reproduce current behavior for comparison. |
| RCIM sparse | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | Paper-aligned sparse bank from recovered RCIM assets. |
| Dense 240 | `0..240` | Paper-maximum dense Fourier-style basis stress test. |
| Dense 360 | `0..360` | Extended dense basis stress test beyond the paper maximum. |

The RCIM sparse bank is the most important candidate because it matches the
known paper harmonic set while keeping the feature count low. Dense banks are
secondary because they carry higher overfitting and sampling-risk exposure.

## Proposed Scope

The initial campaign should stay narrow:

- Model families: `harmonic_regression` and `residual_harmonic_mlp`.
- Direction scopes: `global`, `fw`, and `bw`, matching the current `Wave 1`
  directional split.
- Coefficient mode for harmonic regression: start from the latest winning
  `linear_conditioned` configuration.
- Residual branch: start from the current best exported
  `residual_harmonic_mlp` configuration, changing only the harmonic bank unless
  a later approved addendum opens residual-width tuning.
- Dataset stride: reuse the current best stride settings from the latest
  directional best-hyperparameter closeout so the first comparison isolates the
  harmonic-basis change.

## Evaluation Criteria

Campaign closeout must evaluate both scalar and curve-level behavior:

- Validation and test `MAE`, `RMSE`, and available repository metrics.
- `TE Curve Verification Pipeline` curve overlays for representative held-out curves.
- Visual review of whether high-frequency TE oscillations are recovered or only
  reintroduced as noisy ringing.
- Direction-specific behavior for `fw` and `bw`.
- Parameter count and deployment impact, especially for dense `0..240` and
  `0..360` banks.

## Risks And Controls

- Dense harmonic banks can overfit angular noise. Control this by comparing
  against held-out full curves and not promoting models from scalar metrics
  alone.
- Very high harmonic orders can be sensitive to angular sampling density.
  Control this by preserving stride provenance in every run name and report.
- The residual branch can hide whether the structured branch actually improved.
  Control this by inspecting branch-level auxiliary outputs where available.
- Dense configurations increase coefficient count. Control this by keeping the
  first campaign to a small matrix before opening any larger tuning sweep.

## Required Artifacts After Approval

After this planning report is approved, campaign preparation should create:

- Campaign YAML files under `config/training/`.
- A dedicated PowerShell launcher under `scripts/campaigns/`.
- A launcher usage note under `doc/scripts/campaigns/`.
- Persistent campaign state in `doc/running/active_training_campaign.yaml`.
- Exact launch commands for the prepared queue.

## Approval Gate

This report is ready for user review. Training execution is blocked until both
the technical document and this campaign planning report have explicit user
approval.
