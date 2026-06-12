# Wave 3 Grouped Harmonic Heads Skeleton

## Overview

This technical document defines the next non-campaign `Wave 3` parallel-work
step: prepare an implementation skeleton for `wave3_grouped_harmonic_heads`.

The current `wave3_harmonic_prior_residual` skeleton is already
training-smoke-ready, but it remains not campaign-ready while the separate
`Track 2H` quantile / probabilistic campaign runs on another workstation.
This step advances the second `Wave 3` architecture candidate without
launching training, creating queue YAMLs, mutating
`doc/running/active_training_campaign.yaml`, or selecting final loss defaults.

The skeleton should answer only whether the grouped-head interface can be
constructed, configured, and forward-smoked with point and sequence batches.

## Technical Approach

The grouped-head skeleton should keep the recovered paper harmonic set
inspectable while separating capacity by harmonic role:

- low-order offset / fragile terms: `0`, `1`;
- stable middle harmonics: `3`, `39`, `40`, `78`, `81`;
- high-order fragile harmonics: `156`, `162`, `240`;
- optional residual shape correction.

The first implementation pass should:

- create a separate `Wave3GroupedHarmonicHeadsNetwork` model class;
- reuse existing feedforward and harmonic-basis patterns where possible;
- expose auxiliary tensors for each harmonic group and residual branch;
- support rank-2 point batches and rank-3 sequence batches through the same
  readout conventions used by the existing `Wave 3` skeleton;
- add a dry-run config template and validator;
- keep the skeleton explicitly `implementation_ready` and
  `not_campaign_ready`;
- avoid any real training campaign package, registry update, or active-campaign
  state mutation.

Because the implementation touches PyTorch-facing model code, Context7 must be
used before coding. Final loss choices, branch weights, regularization policy,
queue surfaces, and launch mode must wait for `Track 2H` closeout and a later
approved campaign plan.

## Involved Components

Expected source components:

- `doc/reports/analysis/wave3/Wave 3 Hybrid Structured Models.md`;
- `scripts/models/wave3_harmonic_prior_residual_network.py`;
- `scripts/models/harmonic_regression.py`;
- `scripts/models/feedforward_network.py`;
- `scripts/models/model_factory.py`;
- `scripts/campaigns/wave3/validate_wave3_embryonic_skeleton_package.py`;
- `config/training/wave3_embryonic_skeleton/wave3_harmonic_prior_residual_template.yaml`;
- `doc/reference_summaries/06_Programming_Style_Guide.md`.

Expected new or updated implementation components after approval:

- `scripts/models/wave3_grouped_harmonic_heads_network.py`;
- `scripts/models/model_factory.py`;
- `scripts/campaigns/wave3/validate_wave3_grouped_harmonic_heads_package.py`;
- `scripts/campaigns/wave3/run_wave3_grouped_harmonic_heads_checks.ps1`;
- `config/training/wave3_embryonic_skeleton/wave3_grouped_harmonic_heads_template.yaml`;
- `doc/scripts/campaigns/wave3/wave3_grouped_harmonic_heads_checks.md`;
- `doc/reports/analysis/wave3/Wave 3 Hybrid Structured Models.md`;
- optional Sphinx model API entries if the new model is exposed in the portal.

Expected output components after approval:

- dry-run validation artifacts under
  `output/validation_checks/wave3_grouped_harmonic_heads/`;
- no training campaign output and no registry changes.

No subagent is planned. If a subagent becomes useful later, its proposed name,
task boundary, and approval requirement must be recorded before launch.

## Implementation Steps

1. Create and approve this technical document.
2. Create and approve the paired preliminary non-campaign plan report.
3. Use Context7 for PyTorch-facing model implementation details.
4. Inspect the existing `Wave 3` skeleton, harmonic regression model, model
   factory, and dry-run validators.
5. Implement `Wave3GroupedHarmonicHeadsNetwork` with explicit low, middle,
   high, residual, and combined outputs.
6. Register the model factory key for construction smoke checks only.
7. Add a dry-run template that records `implementation_ready`,
   `not_campaign_ready`, and `blocked_on_track2h_results`.
8. Add a validator that checks metadata, factory construction, point forward,
   sequence forward, and auxiliary output keys.
9. Add a PowerShell dry-run wrapper and launcher note that clearly state that
   no training campaign is launched.
10. Update the Wave 3 design report, documentation indexes, and Sphinx API
    entries if the model becomes user-facing.
11. Verify Python compilation, validator execution, dry-run launcher
    execution, scoped Markdown QA, Sphinx `-W` if portal scope changes, and
    `git diff --check`.
12. Stop for explicit user approval before any commit.
