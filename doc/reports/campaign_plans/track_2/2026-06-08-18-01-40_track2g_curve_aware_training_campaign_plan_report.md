# Wave 3.3 Curve-Aware Training Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the proposed `Wave 3.3`
curve-aware training probe without launching training and without generating
the campaign package yet.

The completed Wave 3.1 and Wave 3.2 work showed that:

- a clean causal residual-offset branch is useful as a non-harmonic baseline;
- explicit harmonic structure improves the direction-specific `Fw` and `Bw`
  branches;
- the `global` branch still struggles to balance forward and backward offset,
  centered shape, amplitude, and phase;
- scalar pointwise `MAE` is not enough to decide whether a candidate is useful
  for continuous TE compensation over repeated motor revolutions.

Wave 3.3 should therefore test a curve-aware training objective while keeping
the runtime input contract unchanged. The model must still consume only the
current point-level state and, where the selected family supports it, a short
causal history of already observed samples. Complete curves are allowed for
training-loss aggregation, validation, diagnostics, and promotion decisions,
but not as future-looking runtime inputs.

Training must not start until this planning report and the already created
technical document are explicitly approved.

## Baseline And Verification Rule

TE Curve Verification Pipeline remains the official offline curve-first verification surface.
Wave 3.3 candidates must not be accepted from scalar training metrics alone.
Any promoted result must later refresh:

- the direction-aware curve-verification matrix;
- the official model verification report and PDF;
- the best-model collage report and PDF;
- the multi-model curve comparison report and PDF;
- relevant curve-first diagnostics when the result changes the decision;
- family and program registries;
- `Training Results Master Summary.md`.

The campaign keeps the repository direction rule:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

The campaign must maintain three branch decisions in parallel. It must not
collapse `global`, `Fw`, and `Bw` into one scalar winner.

## Candidate Matrix

The first Wave 3.3 package should isolate the effect of the curve-aware
objective before introducing a broader multi-head architecture. The proposed
campaign therefore uses one model family with four loss profiles across the
three required surfaces.

Model family:

- `curve_aware_harmonic_residual_offset_probe`

Direction surfaces:

- `global`;
- `Fw`;
- `Bw`.

Loss profiles:

| Loss Profile | Direction Surfaces | Candidate Count | Initial Role |
| --- | --- | ---: | --- |
| `pointwise_control` | `global`, `Fw`, `Bw` | 3 | same architecture with pointwise loss only |
| `raw_centered_shape` | `global`, `Fw`, `Bw` | 3 | pointwise loss plus centered curve-shape term |
| `raw_offset` | `global`, `Fw`, `Bw` | 3 | pointwise loss plus explicit curve-offset term |
| `full_curve_composite` | `global`, `Fw`, `Bw` | 3 | pointwise, centered-shape, offset, amplitude, and sparse harmonic terms |

The first package therefore contains `12` runnable training entries.

The explicit `multi_head_shape_offset_probe` remains planned but should not be
mixed into this first Wave 3.3 batch. If the loss-only branch improves raw
curve error but leaves branch behavior ambiguous, the multi-head branch should
become Wave 3.3-bis or the next approved campaign.

## Model And Objective Design

The candidate model should start from the Wave 3.2 harmonic residual-offset
structure because that branch already showed useful direction-specific
behavior:

```text
final_te_prediction =
  structured_harmonic_shape_prediction
  + causal_residual_offset_prediction
```

Wave 3.3 changes the objective more than the model. The planned composite loss
is:

```text
loss =
    w_point * pointwise_prediction_loss
  + w_centered * centered_curve_shape_loss
  + w_offset * curve_offset_loss
  + w_amplitude * curve_amplitude_loss
  + w_harmonic * sparse_harmonic_shape_loss
```

The loss terms should be logged separately for diagnostics:

- `pointwise_prediction_loss`: standard normalized prediction loss;
- `centered_curve_shape_loss`: curve error after subtracting prediction and
  truth means inside the training split;
- `curve_offset_loss`: absolute or squared difference between predicted and
  truth curve means;
- `curve_amplitude_loss`: peak-to-peak or amplitude mismatch on the training
  curve segment;
- `sparse_harmonic_shape_loss`: amplitude and optionally phase mismatch on
  the sparse RCIM-relevant harmonic basis, excluding the `DC` term.

The first implementation should keep the weighting grid narrow. The exact
weights must be materialized in YAML so each run is reproducible.

## Runtime Input Boundary

The campaign must preserve the practical deployment constraint:

- input features are current point-level operating state, supported short
  causal history, or causal derived features;
- direction, speed, torque, oil temperature, angular position, and known
  harmonic functions of angular position may be used when available at
  runtime;
- future TE values, future angular positions, full-curve truth means,
  complete-curve normalization, and future-looking smoothing are forbidden as
  model inputs;
- full curves are allowed only inside the training split for loss aggregation
  and after inference for validation, diagnostics, and promotion decisions.

This means Wave 3.3 may group training samples by curve identity to compute
loss terms, but the deployed forward pass must remain point or short-history
causal.

## Prepared Configuration Surface

After this planning report is approved, the implementation should prepare a
new campaign root:

```text
config/training/track2g_curve_aware_training/
```

Expected campaign profile:

- `campaign_profile=track2g_curve_aware_training`

Expected model type:

- `model_type=curve_aware_harmonic_residual_offset_probe`

Expected loss profiles:

- `loss_profile=pointwise_control`;
- `loss_profile=raw_centered_shape`;
- `loss_profile=raw_offset`;
- `loss_profile=full_curve_composite`.

Expected direction selections:

- `direction=global`;
- `direction=fw`;
- `direction=bw`.

The implementation should reuse existing sequence dataset profiles where
possible. Any new dataset wrapper or batch sampler must expose only causal
inputs to the model and must keep curve grouping as training/evaluation
metadata, not as future inference information.

## Execution Gate

Before launch, the approved campaign package must contain:

- materialized queue YAML files for all `12` candidates;
- any required direction-specific dataset variant YAML files;
- a dedicated PowerShell launcher under `scripts/campaigns/track_2/`;
- a launcher note under `doc/scripts/campaigns/track_2/`;
- an updated `doc/running/active_training_campaign.yaml`;
- both local and `-Remote` launch commands;
- package validation output proving all queue files resolve.

The expected local launch command after approved preparation is:

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1
```

The expected remote launch command after approved preparation is:

```powershell
.\scripts\campaigns\track_2\run_track2g_curve_aware_training_campaign.ps1 -Remote
```

No training execution is approved by this report alone.

## Verification Plan

Before campaign execution:

- confirm the campaign state is `prepared`;
- validate all materialized YAML files;
- run Python compile checks for touched model, loss, training, and campaign
  scripts;
- run focused one-batch validation for each loss profile;
- run a fast-dev smoke check for at least one `global` entry;
- run Markdown QA on touched authored documentation;
- provide the exact local and remote launcher commands.

After campaign execution:

- inspect `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- preserve separate `global`, `Fw`, and `Bw` branch candidates;
- close out the campaign with Markdown and validated PDF deliverables;
- apply the standard styled-PDF repair pass after PDF generation;
- update family-level and program-level registries only through the
  established workflow;
- refresh `Training Results Master Summary.md`;
- propose the optional heavy TE Curve Verification refresh as a separate operator-launched
  step.

## Decision Criteria

The probe is successful only if it clarifies whether curve-aware training is
worth carrying forward.

Carry forward a Wave 3.3 branch if:

- it improves TE Curve Verification Pipeline raw curve error on the matching `global`, `Fw`, or `Bw`
  surface;
- centered-shape, offset, amplitude, and harmonic diagnostics do not reveal a
  hidden regression;
- the gain is visible in curve-first reports, not only in scalar training
  `test_mae`;
- the result remains compatible with point or short-history causal runtime
  inference.

Prefer `raw_centered_shape` if:

- shape improves materially but offset remains manageable;
- Wave 3.2 harmonic already handles offset well enough on that surface.

Prefer `raw_offset` if:

- offset drops materially without damaging mean-centered shape or harmonic
  phase;
- the branch improves the clean Wave 3.1 baseline and the Wave 3.2
  harmonic baseline.

Prefer `full_curve_composite` if:

- it is the only profile that balances raw error, offset, centered shape,
  amplitude, and harmonic diagnostics;
- it improves the direction-specific branch without making `global` less
  stable.

Do not promote Wave 3.3 if:

- it only improves pointwise scalar metrics;
- it uses any future curve information at inference time;
- the gain depends on collapsing `Fw`, `Bw`, and `global` into one pooled
  scalar result;
- it worsens visual curve tracking versus Wave 2.2, Wave 3.1, or Wave 3.2
  baselines.

## Approval Gate

This planning report is the second workflow gate. After explicit approval, the
next step is campaign package preparation: YAMLs, launcher, launcher note,
active campaign state, validation script updates, and smoke checks. Training
must still wait for the final launch approval and should be operator-run
through the generated PowerShell launcher.
