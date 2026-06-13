# Track 2H Mixture Density Heads Package

## Overview

This technical note prepares the next `Track 2H` dispersion-aware package:
mixture-density heads for locally dispersed TE curves. The completed robust
losses and quantile/probabilistic packages showed that dispersion-aware
training is useful as evidence, but it has not displaced the current official
`Track 2` leaders. The next question is whether the measured curve is better
represented as a small mixture of plausible local TE outcomes rather than as a
single robust central estimate or a single Gaussian distribution.

This document is a planning gate only. No training configuration, launcher,
model code, or active campaign state should be modified until this document
and the matching campaign plan are explicitly approved.

## Technical Approach

The package will reuse the causal curve-aware Track 2H backbone, the
direction-separated `global` / `Fw` / `Bw` surfaces, and the dataset split
discipline used by the robust-loss and quantile/probabilistic campaigns. The
main change is the output interpretation: each point prediction will expose a
small Gaussian mixture over the TE target, while retaining one deterministic
curve for standard campaign metrics and later official `Track 2` verification.

The first package scope should remain deliberately narrow:

- `mdn_k2` predicts two mixture components per TE point;
- `mdn_k3` predicts three mixture components per TE point;
- each profile is prepared for `global`, `Fw`, and `Bw`, producing six queued
  runs;
- each point head emits mixture logits, component means, and guarded component
  log-scales;
- the deterministic playback curve is the mixture expectation, not the best
  component selected with target information;
- training uses negative log likelihood with numerically stable log-sum-exp
  aggregation and guarded scale bounds;
- evaluation keeps deterministic TE metrics plus mixture-specific diagnostics:
  NLL, effective component usage, mean component scale, entropy of mixture
  weights, and high-dispersion harmonic summaries.

The implementation should inspect the current
`curve_aware_harmonic_residual_offset_probe` stack and the existing
quantile/Gaussian loss extension points before choosing the concrete code
shape. Prefer a minimal configuration-driven extension if the current training
module can support MDN output channels cleanly. If deterministic playback or
loss routing would become ambiguous, introduce explicit narrowly named
Track 2H model-family or loss-profile keys for mixture-density candidates.

The package remains offline Python research work. PLC-friendly compression,
export simplification, integrated multi-task / multi-head design, and
latent-state / hysteresis-aware modeling remain later branches.

## Involved Components

- `doc/technical/2026-06/2026-06-13/2026-06-13-10-40-25_track2h_mixture_density_heads_package.md`
  records this technical gate.
- `doc/README.md` registers the new technical document.
- `doc/reports/campaign_plans/track2/2026-06-13-10-40-25_track2h_mixture_density_heads_campaign_plan_report.md`
  records the matching campaign plan.
- `scripts/campaigns/track2/prepare_track2h_quantile_probabilistic_campaign.py`
  and `config/training/track2h_quantile_probabilistic_modeling/` provide the
  closest package structure to reuse.
- `scripts/models/model_factory.py`,
  `scripts/models/harmonic_residual_offset_network.py`, and the current
  training module/loss routing provide the likely extension points.
- A new campaign-preparation script should generate the MDN queue and campaign
  state after approval.
- A new validation script should check YAML schema, output shape, finite MDN
  loss, deterministic expectation extraction, and one-batch execution.
- A dedicated PowerShell launcher and launcher note should expose local and
  `-Remote` execution paths.
- `doc/running/active_training_campaign.yaml` should be updated only after
  package generation is approved.

No subagent is planned for this work.

## Implementation Steps

1. Create this technical document and register it in `doc/README.md`.
2. Create the paired campaign plan under `doc/reports/campaign_plans/track2/`.
3. Stop for explicit user approval before implementation changes.
4. After approval, inspect the existing Track 2H probabilistic implementation
   and choose whether MDN support is a configuration extension or a narrow new
   model/loss profile.
5. Implement stable MDN output parsing, negative log likelihood, scale
   guarding, deterministic mixture-expectation playback, and diagnostics.
6. Generate six queue entries: `mdn_k2` and `mdn_k3` for `global`, `Fw`, and
   `Bw`.
7. Add package validation with YAML checks, output-shape checks, finite-loss
   checks, and one-batch execution.
8. Add the local/remote PowerShell launcher and repository launcher note.
9. Update `doc/running/active_training_campaign.yaml` to prepared state with
   exact local and `-Remote` launch commands.
10. Run compile checks, package validation, Markdown QA, and Sphinx QA.
11. Stop before training execution and wait for explicit operator launch.
12. After operator completion, close the campaign through the standard
    campaign-results report, real PDF validation, registry synchronization,
    active-state cleanup, and optional separate official `Track 2` refresh.
