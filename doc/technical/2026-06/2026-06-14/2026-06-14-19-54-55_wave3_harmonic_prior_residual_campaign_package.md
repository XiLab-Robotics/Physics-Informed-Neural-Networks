# Wave 5.1 Harmonic Prior Residual Campaign Package

## Overview

This technical note prepares the first real `Wave 5.1` campaign package after
the completed `Wave 4.1` robust-loss, quantile/probabilistic, and
mixture-density probes.

The next campaign should test whether an explicit paper-harmonic prior plus a
learned residual curve improves full TE prediction more reliably than
dispersion-aware loss changes alone. This document is a planning gate only.
No campaign YAMLs, launcher scripts, model code, or active campaign state
should be modified until this document and the matching campaign plan are
explicitly approved.

## Technical Approach

The first campaign-ready `Wave 5.1` branch should start from the existing
training-smoke-ready `wave3_harmonic_prior_residual` scaffold. The model
predicts the recovered paper harmonic set, reconstructs a structured base TE
curve, and adds a learned causal residual curve.

The campaign package should preserve these decisions:

- train and report direction-separated `global`, `Fw`, and `Bw` surfaces;
- use the generated smoke-ready config only as a template source, not as a
  queue file;
- compare against the accepted `TE Curve Verification Pipeline` direction-parallel leaders and the
  completed `Wave 4.1` robust, probabilistic, and MDN exploratory baselines;
- keep `h0` and `h1` as fragile low-order channels without claiming that
  `h0` alone is the confirmed offset cause;
- keep high harmonics such as `h156`, `h162`, and `h240` visible in diagnostics;
- use deterministic playback curves for scalar and official `TE Curve Verification Pipeline`
  comparison.

The `Wave 4 series` outcome should guide but not dominate the first `Wave 5.1`
package. Robust and probabilistic losses are useful controls. MDN helped the
backward branch, but its effective component counts were near `1.0`, so it
should not be the default `Wave 5.1` loss. The first campaign should start with
a conservative deterministic or robust/probabilistic loss policy and preserve
MDN as comparison evidence for later multi-head design.

Latent-state / hysteresis-aware modeling remains a valid alternate next probe
if explicitly prioritized, but it is not part of this first `Wave 5.1` package.
`Wave 5.2` PINN work and the integrated multi-task / multi-head architecture
remain downstream evidence-integration stages.

## Involved Components

- `doc/technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md`
  records this technical gate.
- `doc/reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md`
  records the matching campaign plan.
- `doc/README.md` registers the new technical document and campaign plan.
- `doc/running/te_model_live_backlog.md` records the current next-step
  alignment after completed `Wave 4.3` MDN verification.
- `doc/reports/analysis/model_development_waves/wave_3/Wave 3 Hybrid Structured Models.md` remains the
  design source for `Wave 5.1` architecture boundaries.
- `scripts/models/wave3_harmonic_prior_residual_network.py` contains the first
  `Wave 5.1` model candidate.
- `scripts/campaigns/wave_3/validate_wave3_training_smoke_ready.py` and
  `scripts/campaigns/wave_3/run_wave3_training_smoke_ready_checks.ps1` provide
  the existing one-batch validation precedent.
- `output/validation_checks/wave3_training_smoke_ready/generated_configs/`
  provides the validation-only template source for later campaign YAMLs.
- `doc/running/active_training_campaign.yaml` must remain unchanged until an
  approved campaign package is generated.

No subagent is planned for this work.

## Implementation Steps

1. Create this technical document and register it in `doc/README.md`.
2. Create the paired campaign plan under `doc/reports/campaign_plans/`.
3. Align the live backlog so the current next step no longer points to
   already completed `Wave 4.3` MDN refresh work.
4. Stop for explicit user approval before generating campaign YAMLs,
   launchers, launcher notes, validators, or active campaign state.
5. After approval, inspect the existing smoke-ready config and prepare real
   `global`, `Fw`, and `Bw` queue entries for
   `wave3_harmonic_prior_residual`.
6. Select a narrow first loss matrix using `Wave 4 series` evidence: deterministic
   control plus robust or probabilistic pressure before any MDN default.
7. Add a package validator that checks metadata, queue resolution, output
   directories, model construction, finite one-batch loss, and required
   auxiliary harmonic/residual outputs.
8. Add a dedicated PowerShell launcher under `scripts/campaigns/wave_3/` with
   local execution and `-Remote` support.
9. Add the matching launcher note under `doc/scripts/campaigns/wave_3/`.
10. Update `doc/running/active_training_campaign.yaml` to prepared state only
    after package generation is approved.
11. Run compile checks, package validation, Markdown QA, and Sphinx QA when
    portal scope changes.
12. Stop before training execution and provide the exact local and `-Remote`
    launch commands.
