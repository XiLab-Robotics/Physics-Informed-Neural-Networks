# Parallel Shape-Objective Follow-Up

## Overview

The completed `shape_gate_loss_v2` bounded screen showed a real improvement
over the first shape-gate pilot, but it did not beat the current
`polished_dataset` setpoint forward recommendation. The v2 branch is a
windowed `periodic_gru_sequence` run with `collate_mode: sequence`,
`sequence_length: 33`, `sequence_stride: 8`, and center readout. Its bounded
screen also included non-windowed polished-setpoint baselines:
`feedforward`, `tree`, `harmonic_regression`, and
`periodic_mlp_harmonic`.

This follow-up should test a small number of materially different techniques
in parallel without extending the same weak branch. The first decision gate
will remain a bounded forward screen against both the best windowed reference
and the best non-windowed reference.

Pilot closeout reports should also include a small, fixed graph bundle so the
operator can inspect behavior visually before any promotion decision. The graph
bundle should be generated as repository-owned artifacts and embedded in both
the Markdown report and the styled PDF export.

## Technical Approach

The follow-up campaign should use `polished_dataset` setpoints `Fw` as the
bounded proving surface, then stop unless a candidate clears curve-first
evidence. The planned pilot arms are:

- `shape_objective_v3_periodic_gru_sequence_fw`: keep the causal sequence
  contract but replace the checkpoint-selection emphasis with a stronger
  centered-shape, derivative, and harmonic amplitude/phase objective.
- `shape_objective_periodic_mlp_harmonic_fw`: test the best relevant
  non-windowed neural branch so the result is not judged only against a GRU.
- `shape_objective_curve_aware_residual_fw`: test a curve-aware residual
  backbone related to the robust/quantile families that already beat v2 in the
  bounded screen.

Each arm should remain a pilot, not a full expansion. The acceptance gate is
not scalar test MAE alone. A candidate must beat or materially match:

- the current windowed forward recommendation,
  `polished_setpoints_periodic_gru_sequence_Fw`;
- the best non-windowed forward reference in the previous bounded screen,
  `polished_setpoints_periodic_mlp_harmonic_Fw`;
- the current robust/quantile forward references on curve-first evidence.

Context7 must be consulted before any PyTorch or PyTorch Lightning API-level
implementation changes. No subagent is planned. If a subagent becomes useful,
the proposed subagent name, scope, and approval requirement must be recorded
before launch.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `config/training/`
- `scripts/campaigns/`
- `scripts/training/`
- `scripts/models/`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `output/training_runs/`
- `output/training_campaigns/`
- `output/validation_checks/`
- `output/registries/families/`
- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`
- `doc/reports/analysis/project_status/current/`

## Implementation Steps

1. Prepare the approved campaign package with one queue entry per pilot arm,
   all scoped to `polished_dataset` setpoints `Fw`.
2. Reuse existing model-family implementations where possible before adding
   new code; add only the narrow loss/metric plumbing needed for the new
   objective terms.
3. Generate a dedicated PowerShell launcher with local and `-Remote` paths,
   preflight-only mode, one-batch validation, remote source sync, and canonical
   artifact sync-back.
4. Update `doc/running/active_training_campaign.yaml` with the prepared
   campaign state and exact local/remote launch commands.
5. Run preflight and one-batch validation only after approval.
6. Launch the pilot remotely only after the training gate is approved.
7. Close out the campaign with leaderboard, best-run artifacts, campaign
   results report, pilot graph bundle, and PDF validation.
8. Run a bounded `TE Curve Verification Pipeline` screen only for candidates
   that survive the scalar closeout, and compare against both windowed and
   non-windowed references.

The pilot graph bundle should include representative measured-versus-predicted
curves, residual/error curves, per-condition error bars or heatmaps, and a
compact baseline comparison plot against the current windowed and non-windowed
references.
