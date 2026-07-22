# Causal Offset Mean Calibration Pilot

## Overview

This technical document defines the next approved-candidate branch after the
post-shape-loss `Wave 5.2` decision gate.

The recent shape-gate, shape-objective, and shape-first distillation pilots
showed that threshold-like Track 2 shape pressure is useful for model
selection, but not sufficient as direct training pressure. The repeated failure
mode was not a complete loss of curve shape. It was a combined degradation in
raw error, curve offset / mean behavior, centered-shape error, harmonic
amplitude behavior, and robustness.

The next branch should therefore test a narrow causal offset / mean
calibration mechanism anchored to the accepted
`polished_setpoints_periodic_gru_sequence_Fw` baseline. The non-windowed
`polished_setpoints_periodic_mlp_harmonic_Fw` path must remain visible as the
required comparator.

This document is not a campaign plan and does not authorize training. After
approval, the next implementation step is to prepare the campaign planning
report, model/report updates, YAML files, launcher, launcher note, active
campaign state, one-batch validation path, and exact launch commands.

No subagent is planned. If later review help is useful, the proposed subagent
name, reason, and delegated scope will be declared before asking for approval.

## Technical Approach

The pilot should test whether a causal calibration term can reduce offset and
mean-surface error without harming the already strong periodic GRU curve-shape
behavior.

The first implementation should stay bounded:

- dataset: `polished_dataset`;
- input mode: `setpoints`;
- first surface: `Fw`;
- primary road: time-windowed GRU-compatible offset / mean calibration;
- required comparator: non-windowed `periodic_mlp_harmonic`;
- promotion gate: bounded Track 2 screen before any expansion.

The pilot should compare a small set of controlled arms:

| Arm | Purpose |
| --- | --- |
| Baseline replay | Re-evaluate the accepted GRU baseline under the same campaign/reporting gate. |
| Offset-head GRU | Add a train-time offset / mean auxiliary head while preserving pointwise TE loss. |
| Offset-residual calibrator | Learn a small causal residual over the GRU path or GRU-compatible sequence features. |
| Non-windowed harmonic comparator | Keep the `periodic_mlp_harmonic` road visible under the same evidence gate. |

The offset / mean target must be train-only. Runtime inference may use the
model's predicted offset or residual term, but it must not use held-out target
curve means, future samples, or offline polishing statistics.

The loss and selection policy should keep these axes separate:

- pointwise TE error;
- causal offset / mean auxiliary error;
- centered-shape error;
- harmonic amplitude error or diagnostic consistency;
- P95 mean percentage error;
- shape-gated reranker composite score;
- measured-versus-predicted Track 2 visual evidence.

The pilot should not be promoted if it improves scalar test MAE while
worsening the accepted GRU baseline on offset, centered-shape, harmonic, or
robustness metrics.

## Involved Components

Expected read-only inputs:

- `doc/running/active_training_campaign.yaml`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/model_development_waves/wave_5_2/post_shape_loss_decision_gate/[2026-07-22]/wave52_post_shape_loss_decision_gate.md`;
- `output/validation_checks/wave52_post_shape_loss_decision_gate/2026-07-22-16-27-19__wave52_post_shape_loss_decision_gate/`;
- `scripts/models/periodic_temporal_sequence_network.py`;
- `scripts/models/sequential_residual_offset_network.py`;
- `scripts/models/wave52b_offset_harmonic_guided_network.py`;
- `scripts/training/transmission_error_regression_module.py`;
- `scripts/training/shared_training_infrastructure.py`;
- `scripts/training/train_feedforward_network.py`;
- `output/registries/families/periodic_gru_sequence_fw/latest_family_best.yaml`;
- `models/polished_dataset/setpoints/periodic_gru_sequence/forward/reference_inventory.yaml`;
- `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/reference_inventory.yaml`.

Expected outputs after approval and implementation:

- a model explanation report under
  `doc/reports/analysis/model_development_waves/wave_5_2/`;
- a campaign planning report under
  `doc/reports/campaign_plans/cross_wave/causal_offset_mean_calibration/`;
- training configs under
  `config/training/causal_offset_mean_calibration/`;
- a local and `-Remote` launcher under
  `scripts/campaigns/cross_wave/`;
- a launcher note under
  `doc/scripts/campaigns/cross_wave/`;
- prepared active campaign state in
  `doc/running/active_training_campaign.yaml`;
- validation artifacts under
  `output/validation_checks/causal_offset_mean_calibration/`;
- campaign artifacts under
  `output/training_campaigns/<run_instance_id>_causal_offset_mean_calibration_pilot_2026_07_22/`;
- future bounded Track 2 screen artifacts only after normal campaign closeout.

Deferred components:

- official full `TE Curve Verification Pipeline` refresh;
- global or backward expansion;
- dirty-to-clean `Wave 5.2C` transfer;
- full PINN / MMT soft loss;
- Wave 6 integrated multi-head architecture;
- registry promotion.

## Implementation Steps

1. Inspect the existing periodic GRU, sequential residual offset, and
   `Wave 5.2B` offset/harmonic-guided model code to choose the smallest
   implementation path that preserves causal inputs and existing training
   infrastructure.
2. Draft a model explanation report defining the offset / mean calibration
   mechanism, runtime boundary, expected tensors, loss terms, and rejection
   criteria.
3. Create a campaign planning report with the bounded arm list, dataset/input
   scope, selection policy, expected outputs, local command, and `-Remote`
   command.
4. Implement only the minimum model or configuration changes required by the
   approved plan.
5. Create aligned training YAML files, a dedicated PowerShell launcher with
   local and `-Remote` support, and a matching launcher note.
6. Update `doc/running/active_training_campaign.yaml` to the prepared state
   with protected files, local launch commands, and remote launch commands.
7. Run one-batch validation and launcher preflight without launching training.
8. Run Python compile checks for changed Python files, YAML parse checks for
   generated configs, Markdown QA for touched authored Markdown, Sphinx build
   if portal-covered docs change, and `git diff --check`.
9. Stop before training execution and provide the exact local and remote launch
   commands for approval.
