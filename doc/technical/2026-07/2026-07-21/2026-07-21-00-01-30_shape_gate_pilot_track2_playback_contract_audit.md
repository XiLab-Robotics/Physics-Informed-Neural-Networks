# Shape-Gate Pilot Track 2 Playback Contract Audit

## Overview

This technical document scopes the follow-up audit for the completed
`shape_gate_loss_pilot_periodic_gru_sequence_Fw` checkpoint. The pilot closed
with acceptable scalar training metrics for a one-run experiment, but the
forward-only `TE Curve Verification Pipeline` playback produced a severe
offset-dominated failure and a `shape_gate_failed` decision.

The goal is to identify whether the failure comes from the trained checkpoint
itself or from a mismatch between training/test-loader inference and Track 2
full-curve playback.

## Technical Approach

The audit will compare the same checkpoint across the smallest reproducible
paths:

- training-run metric artifacts and queue configuration;
- the family registry entry used by Track 2;
- Track 2 candidate loading and feature construction;
- GRU sequence-window reconstruction and padding behavior;
- input feature order, normalization, direction flag, and torque sign;
- target scaling, mean/offset handling, and angular-position indexing.

The first pass is diagnostic only. It must not retrain the model, promote a
candidate, or apply an offline correction to inference. If a concrete contract
bug is found, a separate implementation decision can patch the responsible
loader or report generator and rerun the same forward-only gate.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/`
- `output/registries/families/shape_gate_loss_pilot_periodic_gru_sequence_fw/latest_family_best.yaml`
- `config/training/shape_gate_loss_pilot/`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/reports/analysis/build_track2_candidate_curve_plots.py`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `data/polished_dataset`

No subagent is planned for this pass. If a subagent becomes useful, the
delegated scope and approval requirement must be recorded before launch.

## Implementation Steps

1. Inspect the completed campaign state, queue config, registry entry, and
   Track 2 compact matrix config for feature-contract drift.
2. Trace the checkpoint-loading path used by Track 2 and compare it against the
   training/test-loader path.
3. Build a small condition-level diagnostic table for the already evaluated
   forward curves, separating raw offset, centered shape, torque sign, and
   sequence-window reconstruction behavior.
4. If the evidence indicates a loader or config mismatch, patch the smallest
   responsible repository-owned path and rerun only the pilot forward Track 2
   comparison and shape gate.
5. If no mismatch is found, record the pilot as a true model failure and keep
   the branch blocked from full three-dataset, three-surface training.
6. Run scoped Python and Markdown QA for any touched scripts or reports.
