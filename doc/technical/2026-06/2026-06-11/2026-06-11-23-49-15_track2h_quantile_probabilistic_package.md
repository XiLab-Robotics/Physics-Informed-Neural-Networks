# Track 2H Quantile Probabilistic Package

## Overview

This technical note prepares the second `Track 2H` dispersion-aware package:
quantile and probabilistic regression candidates for locally dispersed TE
curves. The completed robust-loss package showed that outlier-resistant losses
are useful exploratory baselines, but they did not displace the current
direction-parallel `Track 2` leaders. The next package must test whether
explicit uncertainty modeling can separate reproducible curve shape from the
experiment-dependent dispersion that appears to affect `h0`, `h1`, and selected
higher harmonics.

This document is a planning gate only. No training configuration, launcher,
model code, or campaign state should be modified until this document and the
matching campaign plan are explicitly approved.

## Technical Approach

The package will reuse the causal sequence framing, dataset split discipline,
and `global` / `Fw` / `Bw` decision surfaces already used by the robust-loss
`Track 2H` campaign. The main change is the prediction target interpretation:
instead of fitting a single deterministic curve with a robust point loss, each
candidate will expose either calibrated quantiles or a distribution parameter
head while preserving a deterministic curve for official `Track 2` scoring.

The first package scope should remain narrow enough to close cleanly:

- Quantile candidates predict lower, median, and upper TE curves, initially
  using `p10`, `p50`, and `p90` pinball losses. The `p50` curve is the
  deterministic candidate submitted to the standard `Track 2` comparison.
- Gaussian probabilistic candidates predict `mu` and a numerically guarded
  dispersion term. The `mu` curve is the deterministic candidate submitted to
  the standard `Track 2` comparison.
- Each candidate family is prepared for `global`, `Fw`, and `Bw`, producing six
  primary queued runs before any mixture-density or latent-state branch is
  attempted.
- Candidate evaluation must include the normal deterministic curve metrics plus
  interval-specific diagnostics: quantile pinball loss, coverage, interval
  width, negative log likelihood where applicable, and focused summaries on
  high-dispersion harmonic regions.

The implementation should inspect the current model and training-loss extension
points before choosing the concrete code shape. If the existing
`curve_aware_harmonic_residual_offset_probe` stack can support output-head and
loss variants cleanly, prefer a minimal configuration-driven extension. If that
would make the deterministic path ambiguous, introduce explicit `Track 2H`
model-family keys for quantile and Gaussian heads.

This package does not change the later roadmap order. Mixture density networks,
causal latent-state / hysteresis-aware candidates, `Wave 3` hybrid structured
models, and `Wave 4` PINN branches remain separate follow-up stages. The
probabilistic package should instead provide evidence about whether uncertainty
aware training is worth carrying into the later multi-task / multi-head branch.

## Involved Components

- `doc/technical/2026-06/2026-06-11/2026-06-11-23-49-15_track2h_quantile_probabilistic_package.md`
  records this technical gate.
- `doc/README.md` registers the new technical document.
- `doc/reports/campaign_plans/track_2/` will receive the matching preliminary
  campaign plan after this technical document is approved.
- `scripts/campaigns/track_2/prepare_track2h_dispersion_aware_modeling_campaign.py`
  provides the reference robust-loss package structure.
- A new Track 2 campaign-preparation script will generate the quantile and
  probabilistic YAML queue without modifying the completed robust-loss package.
- A new Track 2 validation script will check generated YAML files, campaign
  state, model/loss availability, deterministic output selection, and one-batch
  execution where feasible.
- A new dedicated PowerShell launcher will expose local and `-Remote` execution
  paths.
- `doc/scripts/campaigns/track_2/` will receive the matching launcher note.
- `doc/running/active_training_campaign.yaml` will be updated only after the
  package is approved and generated.

No subagent is planned for this work.

## Implementation Steps

1. Create this technical document and register it in `doc/README.md`.
2. After approval, create the campaign plan for the quantile/probabilistic
   package under `doc/reports/campaign_plans/track_2/`.
3. Inspect the existing causal sequence model, training objective, registry,
   and candidate-generation code paths to choose the least invasive output-head
   implementation.
4. Implement or configure quantile pinball and Gaussian negative-log-likelihood
   training support with deterministic `p50` or `mu` selection for standard
   curve scoring.
5. Generate the six primary campaign queue entries:
   `quantile_p10_p50_p90` and `gaussian_nll` for `global`, `Fw`, and `Bw`.
6. Add a validation entry point that checks YAML schema, file references,
   output dimensions, finite losses, deterministic prediction selection, and
   local launcher prerequisites.
7. Add the dedicated local/remote PowerShell launcher and its repository
   documentation note.
8. Update `doc/running/active_training_campaign.yaml` to the prepared campaign
   state with exact local and `-Remote` launch commands.
9. Stop before training execution and wait for explicit operator launch.
10. After operator completion, close the campaign through the normal result
    report, PDF validation, registry synchronization, and optional separate
    official `Track 2` verification refresh.
