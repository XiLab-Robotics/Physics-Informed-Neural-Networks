# Shape-Gate Loss Pilot And Full-Surface Campaign Strategy

## Overview

This document records the next training strategy after the calibrated
shape-gated `TE Curve Verification Pipeline` reranker. The primary pilot
surface is `polished_dataset` with `setpoints` inputs and forward-only
training, because the latest reduced reranker exposes a concrete forward
shape target there while keeping the pilot small enough to fail quickly.

The full promotion rule remains stricter than the pilot scope. Any new model
family or materially changed loss profile must eventually be trained and
reported across all currently supported dataset/input-mode targets:

- `simplified_dataset` with `setpoints`;
- `polished_dataset` with `setpoints`;
- `polished_dataset` with `actual_values`.

For each target, the full campaign must preserve all three surfaces:

- `global`;
- `Fw`;
- `Bw`.

The `original_dataset` root remains a raw/reference lineage source, not the
direct third model-development training target for this campaign family unless
a separate technical document and campaign plan explicitly add that support.

## Technical Approach

Use the calibrated shape-gate metrics as training evidence in two stages.

Stage 1 is a local or short-cluster pilot on `polished_dataset` `setpoints`
`Fw` only. It should test whether shape-aware pressure improves the actual
curve-following behavior without hiding a scalar-error regression. The pilot
must compare against the current `periodic_gru_sequence` and
`wave4_1_mae_robust_loss` evidence, with the calibrated reranker as the
acceptance screen.

Stage 2 is the full Aries campaign only if Stage 1 produces credible evidence.
The full package must materialize one queue entry per dataset/input-mode target
and surface, for a minimum of nine runs per model/loss profile. Full promotion
requires dataset/input-mode-specific artifacts plus `global`, `Fw`, and `Bw`
results; a forward-only pilot is not promotable by itself.

The existing `TransmissionErrorRegressionModule` already supports pointwise,
centered-shape, offset, amplitude, and sparse harmonic loss terms. The first
implementation should therefore reuse or extend that mechanism instead of
creating an unrelated training path. Any new derivative or shape-gate-derived
loss term must be normalized, logged separately, and disabled by default unless
the approved pilot profile enables it.

## Involved Components

- `scripts/training/transmission_error_regression_module.py`
  Existing loss implementation and likely location for any new derivative or
  calibrated shape-gate monitor term.
- `config/training/`
  Source YAML configurations for pilot and full campaign queue entries.
- `scripts/campaigns/cross_wave/prepare_dataset_input_mode_retraining_campaign.py`
  Existing dataset/input-mode campaign materialization pattern for
  `simplified_setpoints`, `polished_setpoints`, and `polished_actual_values`.
- `scripts/campaigns/aries/`
  Aries launcher surface for Slurm-bound full campaigns.
- `doc/reports/campaign_plans/`
  Required planning report location before any training campaign or experiment
  execution.
- `doc/running/active_training_campaign.yaml`
  Persistent campaign state file that must be updated only after the campaign
  package is approved.
- `output/training_runs/`, `output/training_campaigns/`,
  `output/validation_checks/`, and `output/registries/`
  Required artifact destinations for runs, campaign state, validation checks,
  and registry updates.

## Implementation Steps

1. Create a campaign planning report for the Stage 1 pilot before any training
   or experiment execution.
2. Define the pilot profile on `polished_dataset` `setpoints` `Fw`, starting
   from the strongest compatible temporal baseline and the existing
   curve-aware loss support.
3. Add only the minimum required implementation for normalized derivative or
   calibrated shape-gate monitor terms, if the existing loss components are
   insufficient.
4. Validate the pilot config with compile and one-batch setup checks before
   launching any training.
5. Run the pilot as an operator-approved experiment and evaluate it with the
   calibrated shape-gated reranker.
6. If the pilot passes, prepare a full Aries campaign package with
   `simplified_setpoints`, `polished_setpoints`, and `polished_actual_values`
   targets, each across `global`, `Fw`, and `Bw`.
7. Keep the full campaign operator-launched on Aries and do not run the heavy
   `TE Curve Verification Pipeline` matrix as part of normal campaign closeout.
8. After closeout, decide separately whether to prepare an official
   `TE Curve Verification Pipeline` refresh launcher for the accepted full
   campaign artifacts.
