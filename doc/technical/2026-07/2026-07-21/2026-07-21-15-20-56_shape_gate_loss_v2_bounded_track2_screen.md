# Shape-Gate Loss V2 Bounded TE Curve Verification Screen

## Overview

This document defines the implementation plan for preparing a bounded
`TE Curve Verification Pipeline` screen for the completed
`shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` checkpoint.

The work is intentionally separate from the completed training campaign
closeout. The objective is to test whether the v2 checkpoint keeps its scalar
gain when evaluated on curve-first evidence before preparing any full
three-target, three-surface expansion.

## Technical Approach

The screen will add the v2 checkpoint as a registry-backed forward candidate in
a narrow `polished_dataset` setpoint `Fw` matrix. The package will compare the
candidate against the relevant forward baselines and the first shape-gate loss
pilot without modifying the official full matrix or promoting the model from
campaign metrics alone.

The implementation will:

- create a dedicated compact matrix config for `polished_dataset` setpoints
  `Fw`;
- include the v2 checkpoint registry entry and the approved baseline candidates;
- create a dedicated PowerShell launcher with local and `-Remote` modes;
- create the matching launcher note and user-facing command entries;
- run only preflight/package validation inside Codex;
- wait for the operator to launch the real screen and report completion;
- inspect generated matrix and shape-gated reranker artifacts only after the
  operator-run screen completes.

No subagent is planned for this task.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `scripts/campaigns/track_2/`
- `doc/scripts/campaigns/track_2/`
- `doc/running/active_training_campaign.yaml`
- `output/registries/families/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw/latest_family_best.yaml`
- `output/training_runs/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence/2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=008-val_mae=0.00198279.ckpt`

## Implementation Steps

1. Inspect the existing compact shape-gate pilot matrix and reduced Track 2
   launchers.
2. Create a v2-specific compact matrix config for `polished_dataset` setpoints
   `Fw`.
3. Add an operator-facing launcher that supports local execution and `-Remote`
   execution without starting the screen during package preparation.
4. Add a launcher note documenting local, `-Remote`, and preflight commands.
5. Update the active campaign state to a prepared verification-screen state
   with the expected launcher and artifact paths.
6. Run preflight validation and static checks only.
7. Provide the exact operator command and wait for run completion before any
   matrix artifact inspection or official decision update.
