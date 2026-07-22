# Shape-Objective Bounded TE Curve Verification Screen Plan

## Overview

This plan defines the next verification step after the completed
`parallel_shape_objective_followup_2026_07_21` campaign. The scalar campaign
leader is `shape_objective_periodic_mlp_harmonic_fw`, a non-windowed periodic
MLP harmonic model trained on `polished_dataset` setpoint forward curves.

The campaign result is not sufficient for promotion because the repository
selection policy requires curve-first evidence. This screen therefore tests the
winner against the current forward polished setpoint references inside a
bounded `TE Curve Verification Pipeline` run.

## Scope

- Dataset: `polished_dataset`
- Input mode: setpoints
- Surface: `Fw`
- Primary candidate: `shape_objective_periodic_mlp_harmonic_fw`
- Required windowed baseline: `polished_setpoints_periodic_gru_sequence_Fw`
- Required non-windowed baseline: `polished_setpoints_periodic_mlp_harmonic_Fw`

The screen will not update the accepted program best model by itself. Promotion
requires post-run inspection of raw error, centered shape fidelity, offset and
continuity behavior, harmonic and phase evidence, robustness, and visual curve
evidence.

## Planned Artifacts

- Compact matrix config under
  `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- Operator launcher under `scripts/campaigns/track_2/`
- Launcher note under `doc/scripts/campaigns/track_2/`
- Prepared-state update in `doc/running/active_training_campaign.yaml`
- Matrix outputs under `output/validation_checks/track2_reference_comparison/`
- Shape-gated reranker outputs under
  `output/validation_checks/shape_gated_te_curve_reranker/`
- Bounded verification plots under
  `doc/reports/campaign_results/track_2/verification_plots/`

## Commands To Prepare

The package will expose these operator commands after implementation:

```powershell
.\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
    -PreflightOnly
```

```powershell
.\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
    -Remote
```

The matrix itself will not be launched during preparation unless the user
explicitly asks to run the local screen from this workstation.

## Acceptance Criteria

- Local preflight validates the config, launcher, active state, candidate
  registry, and required baseline inventories.
- The launcher supports local execution and `-Remote`.
- The launcher note documents exact commands and expected outputs.
- The bounded screen remains separate from official full-matrix promotion.
- Markdown QA passes on touched Markdown files.
- Python/PowerShell syntax checks pass on touched script files where practical.
