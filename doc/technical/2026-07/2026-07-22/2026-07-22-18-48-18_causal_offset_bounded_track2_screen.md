# Causal Offset Bounded TE Curve Verification Screen

## Overview

This document defines the next step after the completed
`causal_offset_mean_calibration_pilot_2026_07_22` closeout. The pilot selected
`causal_offset_mean_periodic_mlp_harmonic_fw` as the scalar winner, but the
repository promotion policy requires bounded `TE Curve Verification Pipeline`
evidence before changing any accepted forward recommendation.

The requested step is therefore an operator-launched bounded screen, not a new
training campaign and not a full official matrix refresh.

## Technical Approach

The screen will reuse the existing bounded Track 2 pattern used for the
shape-objective and shape-first distillation follow-ups:

- create one compact matrix YAML under
  `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`;
- create one dedicated PowerShell launcher under `scripts/campaigns/track_2/`;
- create the matching launcher note under `doc/scripts/campaigns/track_2/`;
- run local preflight without starting the matrix;
- expose local and `-Remote` execution modes;
- generate matrix output, shape-gated reranker output, and measured-versus-
  predicted TE curve plots under bounded screen-specific output roots.

The screen stays on `polished_dataset`, setpoint inputs, and `Fw` only.
Promotion remains blocked until curve-first evidence is inspected.

## Involved Components

- campaign closeout state:
  `doc/running/active_training_campaign.yaml`
- pilot outputs:
  `output/training_runs/causal_offset_mean_calibration/`
- campaign leaderboard:
  `output/training_campaigns/2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22/campaign_leaderboard.yaml`
- bounded matrix runner:
  `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- shape-gated reranker:
  `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- accepted forward baselines:
  `models/polished_dataset/setpoints/periodic_gru_sequence/forward/reference_inventory.yaml`
  and
  `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/reference_inventory.yaml`

No Codex subagent is planned for this implementation. If a subagent becomes
useful later, its name, boundary, and approval requirement must be recorded
before launch.

## Implementation Steps

1. Create the bounded matrix YAML for:
   `causal_offset_mean_bounded_track2_screen_polished_setpoints_fw`.
2. Include these required candidates:
   `polished_setpoints_periodic_gru_sequence_Fw`,
   `polished_setpoints_periodic_mlp_harmonic_Fw`,
   `causal_offset_mean_periodic_mlp_harmonic_fw`, and
   `causal_offset_mean_gru_sequence_fw`.
3. Include `shape_objective_periodic_mlp_harmonic_Fw` only if the matrix
   support can reference it without widening the screen beyond the intended
   scalar high-water comparison.
4. Create a dedicated PowerShell launcher with `-PreflightOnly`, local run, and
   `-Remote` modes.
5. Create the launcher note with exact local and remote commands.
6. Update `doc/running/active_training_campaign.yaml` to register the prepared
   bounded screen and protect the new screen files while prepared.
7. Run local preflight only.
8. Stop and provide the exact operator command; do not run the heavy bounded
   screen inside Codex unless the user explicitly asks for that execution
   after seeing the prepared package.
