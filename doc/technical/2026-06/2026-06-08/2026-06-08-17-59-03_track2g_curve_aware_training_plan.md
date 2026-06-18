# Track 2G Curve-Aware Training Plan

## Overview

This technical document plans the next Track 2 modeling branch after the
completed Track 2F and Track 2F-bis offset-aware probes.

Track 2F proved that a causal residual-offset branch can be trained as a clean
non-harmonic baseline, but its offline curve playback can lose waveform shape.
Track 2F-bis showed that adding harmonic structure improves the direction
specific `Fw` and `Bw` branches, while the `global` surface still struggles to
balance forward and backward offset, centered shape, amplitude, and phase in a
single model.

Track 2G therefore shifts the next experiment from a pure architecture probe
to a curve-aware training objective. The objective is not to change the
runtime input contract. The deployed predictor must still consume only the
current point-level state and, when supported by the selected family, a short
causal history of already observed samples. Complete future curves, future TE
samples, future angular positions, and truth-curve mean subtraction remain
offline-only diagnostic tools.

The project will continue to maintain three parallel decision surfaces:

- `Fw`: forward-only model branch and forward Track 2 evaluation;
- `Bw`: backward-only model branch and backward Track 2 evaluation;
- `global`: bidirectional model branch evaluated on both directions.

The next campaign must not collapse these surfaces into one scalar winner.
Each branch needs its own best candidate and its own Track 2 interpretation.

## Technical Approach

Track 2G should test whether training can directly reduce the failure modes
identified by the Track 2 mean-centered, Track 2D, Track 2E, Track 2F, and
Track 2F-bis work:

- raw curve error;
- curve-level mean offset / `DC` bias;
- mean-centered waveform-shape error;
- amplitude and peak-to-peak mismatch;
- harmonic amplitude and phase mismatch on the sparse RCIM-relevant basis;
- direction imbalance between forward and backward conditions.

The first Track 2G branch should be conservative and inspectable:

1. Keep pointwise prediction causal.
2. Build curve-aware training batches or loss aggregation only from samples
   already present in the training split.
3. Preserve the current feature schema and dataset origin.
4. Avoid future-looking normalization or full-curve truth information at
   inference time.
5. Report all losses and auxiliary terms separately, so a model cannot look
   better only because one term hides another.

The proposed training loss is a composite objective:

```text
loss =
    w_point * pointwise_prediction_loss
  + w_centered * centered_curve_shape_loss
  + w_offset * curve_offset_loss
  + w_amplitude * curve_amplitude_loss
  + w_harmonic * sparse_harmonic_shape_loss
```

The exact weights should be campaign parameters, not hard-coded constants. The
first campaign should test a narrow grid, not a broad sweep, because the goal
is to validate whether curve-aware training improves Track 2 behavior before
large-scale HPO.

Two model forms should be considered in parallel:

- `curve_aware_harmonic_residual_offset`: a minimal extension of the
  Track 2F-bis harmonic residual-offset branch with the composite curve-aware
  loss;
- `multi_head_shape_offset_probe`: an explicit multi-head model where one head
  predicts centered shape, one head predicts curve offset / low-frequency
  correction, and the final TE prediction is reconstructed from those
  components.

The first implementation can start with the loss-only extension if that keeps
the blast radius smaller. The multi-head branch should remain in the same plan
because it is the natural follow-up if the loss-only extension improves raw
error but still leaves ambiguous branch behavior.

Track 2F and Track 2F-bis remain mandatory baselines:

- Track 2F clean non-harmonic residual offset isolates the effect of causal
  short-history offset learning without forced harmonic shape.
- Track 2F-bis harmonic residual offset isolates the effect of explicit
  harmonic structure without curve-aware loss.
- Track 2G must prove that the new objective or multi-head decomposition adds
  value beyond both.

No subagent is planned for this implementation. If a later step proposes a
subagent for independent metric review or campaign validation, its name,
delegated scope, and approval requirement must be documented before launch.

## Involved Components

Expected documentation and planning components:

- this technical document;
- a future campaign planning report under `doc/reports/campaign_plans/track_2/`;
- `doc/running/active_training_campaign.yaml`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- a future Track 2G explanatory model report under
  `doc/reports/analysis/wave2/` or a dedicated Track 2 model-report folder.

Expected implementation components after approval:

- training loss support in the existing regression module or a narrow helper
  owned by the TE training stack;
- candidate model registration in the existing model factory if the multi-head
  branch is implemented;
- campaign preparation script under `scripts/campaigns/track_2/`;
- local and `-Remote` PowerShell launcher under `scripts/campaigns/track_2/`;
- launcher note under `doc/scripts/campaigns/track_2/`;
- queue YAMLs under `config/training/track2g_curve_aware/`;
- validation or preflight script for the generated campaign package.

Expected evaluation components after training:

- normal campaign closeout report and PDF;
- family-level and program-level registry synchronization;
- optional operator-launched Track 2 verification refresh;
- official Track 2 decision report with `Fw`, `Bw`, and `global` interpreted
  separately;
- regenerated collage and overlay PDFs with the standard post-export layout
  corrections and real-PDF validation.

## Implementation Steps

1. Create and approve this technical document.
2. Create the Track 2G campaign planning report before any training execution.
3. Define the candidate matrix with three parallel surfaces:
   `global`, `Fw`, and `Bw`.
4. Define the first narrow loss-weight grid:
   pointwise-only control, raw plus centered-shape, raw plus offset, and full
   composite loss.
5. Decide whether the first campaign implements only the loss extension or
   also includes the explicit multi-head shape/offset branch.
6. Generate campaign YAMLs, campaign launcher, launcher note, active campaign
   state, and package validation output.
7. Wait for explicit user approval before launching any training.
8. After user-run training completion, perform normal campaign closeout:
   results Markdown, PDF export, PDF QA, registry updates, active campaign
   cleanup, and master-summary synchronization.
9. Propose the Track 2 verification refresh as a separate operator-launched
   step.
10. After Track 2 refresh completion, decide separately for `Fw`, `Bw`, and
    `global` whether Track 2G improves over Track 2F, Track 2F-bis, Wave 2B,
    and the accepted Track 2 reference baselines.

## Approval Gate

This document is the first workflow gate only. No implementation code, campaign
YAMLs, launcher scripts, or training execution should be created until this
technical plan is explicitly approved.
