# Wave 1 Periodic MLP Explicit Harmonic Tracking Campaign Plan Report

## Overview

This preliminary plan defines a controlled `Wave 1` follow-up campaign for the
existing `periodic_mlp` family after the approved explicit harmonic-basis
extension. The campaign mirrors the harmonic-bank comparison pattern used by
the completed high-order harmonic tracking campaign, but keeps the scope to
the periodic-feature neural model only.

The approved technical document is:
`doc/technical/2026-05/2026-05-20/2026-05-20-22-34-11_periodic_mlp_explicit_harmonic_basis.md`.

No training should be launched from this plan until this planning report is
explicitly approved.

## Motivation

The completed harmonic tracking campaign showed that explicit harmonic banks
are useful for probing whether direct models can recover high-frequency TE
curve content. The `periodic_mlp` family is the natural next test because its
architecture already uses fixed sine/cosine angle features before a standard
feedforward backbone.

This campaign tests whether selected and dense harmonic dictionaries improve
`periodic_mlp` curve fidelity without turning the model into a separate future
`Fourier-Feature MLP` family. The pure `feedforward` baseline remains unchanged
and should be used only as an existing comparison point.

## Candidate Harmonic Banks

| Bank | Harmonic indices | Purpose |
| --- | --- | --- |
| Existing baseline | Current best `periodic_mlp` runs | Comparison baseline; no rerun required in this first package. |
| RCIM sparse | `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | Paper-aligned sparse periodic-feature dictionary. |
| Dense 240 | `0..240` | Paper-maximum dense periodic-feature stress test. |
| Dense 360 | `0..360` | Extended dense periodic-feature stress test beyond the paper maximum. |

The RCIM sparse bank is the safest first candidate because it keeps feature
count low and matches known physically meaningful harmonics. Dense banks are
kept in the package to match the harmonic campaign comparison surface, but
promotion decisions must consider overfitting and curve-level behavior.

## Proposed Scope

The prepared campaign should contain `9` runs:

| Model family | Direction scopes | Harmonic banks | Run count |
| --- | --- | --- | --- |
| `periodic_mlp` | `global`, `fw`, `bw` | `rcim_sparse`, `dense240`, `dense360` | `9` |

Configuration rules:

- Use the current `Wave 1` directional best-hyperparameter source configs for
  `periodic_mlp`, `periodic_mlp_fw`, and `periodic_mlp_bw`.
- Change only the harmonic bank fields unless a later approved addendum opens
  broader neural hyperparameter tuning.
- Preserve `hidden_size`, activation, dropout, layer norm, learning rate,
  dataset stride, batch size, and training schedule from the source configs.
- Keep `include_raw_angle_feature` unchanged from the source configs.
- Write outputs under `output/training_runs/<model_family>/` through immutable
  timestamped `run_instance_id` folders.

## Expected Campaign Package

After approval, preparation should create:

- `config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/`
- `9` queue YAML files under that campaign root.
- A dedicated launcher:
  `scripts/campaigns/wave1/run_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.ps1`.
- A launcher note:
  `doc/scripts/campaigns/run_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.md`.
- Prepared campaign state in `doc/running/active_training_campaign.yaml`.
- A campaign output root under
  `output/training_campaigns/wave1/periodic_mlp_explicit_harmonic_tracking/`.

## Evaluation Criteria

Campaign closeout must evaluate both scalar and curve-level behavior:

- Validation and test `MAE`, `RMSE`, and available repository metrics.
- Direction-specific comparison against the existing `periodic_mlp` best runs.
- `Track 2` curve overlays for representative held-out curves.
- Visual inspection for recovered TE oscillations versus noisy ringing.
- Parameter count and deployment impact, especially for dense `0..240` and
  `0..360` periodic-feature inputs.

## Risks And Controls

- Dense periodic-feature banks can overfit angular noise. Control this by
  reviewing held-out curve overlays before promotion.
- Very large expanded inputs can make the first layer dominate model capacity.
  Control this by preserving the current neural architecture and changing only
  the harmonic dictionary in this campaign.
- Scalar metrics can hide curve smoothing or ringing. Control this by requiring
  Track 2 visual review during closeout.
- The future `Fourier-Feature MLP` family could become conceptually blurred.
  Control this by recording this campaign as a fixed engineered-feature
  `periodic_mlp` extension only.

## Required Artifacts After Approval

After this planning report is approved, campaign preparation should create:

- Campaign YAML files under `config/training/`.
- A dedicated PowerShell launcher under `scripts/campaigns/`.
- A launcher usage note under `doc/scripts/campaigns/`.
- Persistent campaign state in `doc/running/active_training_campaign.yaml`.
- Exact launch commands for the prepared queue.

## Approval Gate

This report is ready for user review. Training execution and campaign package
generation are blocked until both the technical document and this campaign
planning report have explicit user approval.
