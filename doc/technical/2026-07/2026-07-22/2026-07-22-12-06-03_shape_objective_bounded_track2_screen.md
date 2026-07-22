# Shape-Objective Bounded TE Curve Verification Screen

## Overview

This technical document covers the bounded `TE Curve Verification Pipeline`
screen for the completed
`parallel_shape_objective_followup_2026_07_21` campaign. The screen evaluates
the scalar pilot winner,
`shape_objective_periodic_mlp_harmonic_fw`, against the forward polished
setpoint reference baselines before any promotion decision.

The screen is deliberately narrower than the official full matrix. It targets
`polished_dataset`, setpoint inputs, and the forward (`Fw`) surface only. The
accepted program baseline is not changed by this preparation step.

No subagent use is planned for this implementation.

## Technical Approach

The implementation will reuse the established bounded-screen pattern from the
shape-gate loss v2 verification launcher. It will create a dedicated compact
matrix config for the shape-objective winner and its comparison baselines, then
create an operator-facing PowerShell launcher with local and `-Remote` modes.

The launcher will run only preflight when requested and will not launch the
heavy matrix during package preparation. The normal execution path will run the
reference-family comparison matrix and the shape-gated reranker for the bounded
candidate set, then synchronize local or remote artifacts into the repository.

The candidate set will include:

- `shape_objective_periodic_mlp_harmonic_fw`
- `polished_setpoints_periodic_gru_sequence_Fw`
- `polished_setpoints_periodic_mlp_harmonic_Fw`

Additional active forward references may be retained only if they help interpret
the decision without turning the bounded screen into a full matrix.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/registries/families/shape_objective_periodic_mlp_harmonic_fw/latest_family_best.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/campaigns/track_2/`
- `doc/scripts/campaigns/track_2/`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `doc/reports/analysis/te_curve_verification_pipeline/`
- `output/validation_checks/track2_reference_comparison/`
- `output/validation_checks/shape_gated_te_curve_reranker/`

## Implementation Steps

1. Create a compact matrix YAML for the bounded shape-objective forward screen.
2. Create a dedicated PowerShell launcher with local, `-Remote`, and
   `-PreflightOnly` modes.
3. Create the matching launcher note with exact local and remote commands.
4. Update active campaign state only to record the prepared operator-run
   verification screen and its launch commands.
5. Run local preflight without launching the matrix.
6. Run Markdown and Python syntax checks on the touched scope.
7. Stop and report the exact operator command for the user to launch the
   bounded screen.
