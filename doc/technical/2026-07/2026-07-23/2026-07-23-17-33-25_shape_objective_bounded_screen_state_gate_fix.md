# Shape-Objective Bounded Screen State Gate Fix

## Overview

The `shape_objective_bounded_track2_screen` launcher failed before execution
because its preflight required `doc/running/active_training_campaign.yaml` to
contain the exact prepared screen name
`shape_objective_bounded_track2_screen_2026_07_22`.

That state contract is too strict for bounded `TE Curve Verification Pipeline`
screens that are already packaged as standalone repository launchers. The
current active campaign state is correctly closed after the causal-offset
bounded screen, so the shape-objective screen should be allowed to run when its
own matrix configuration, registered model artifacts, launcher note, and output
contract are present.

## Technical Approach

Keep the launcher explicit, but change the local/remote preflight from an exact
active-state campaign-name match to a standalone bounded-screen readiness
check. The revised preflight should still require the active state file to
exist, but it should not reject a closed or different `next_prepared_screen`
when the launcher-specific inputs are valid.

The remote path will sync the corrected launcher and then run the same local
preflight on the remote host. After the fix, the remote execution should use the
same readable output and measured-versus-predicted plot generation contract
introduced for the bounded Track 2 launchers.

## Involved Components

- `scripts/campaigns/track_2/run_shape_objective_bounded_track2_screen.ps1`
- `doc/scripts/campaigns/track_2/run_shape_objective_bounded_track2_screen.md`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_objective_bounded_track2_screen_polished_setpoints_fw_matrix.yaml`
- `output/registries/families/shape_objective_periodic_mlp_harmonic_fw/latest_family_best.yaml`
- `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/reference_inventory.yaml`
- `models/polished_dataset/setpoints/periodic_gru_sequence/forward/reference_inventory.yaml`

No subagent is planned for this fix.

## Implementation Steps

1. Replace the strict active-state screen-name assertion with an explanatory
   status log that reports the current active campaign state when available.
2. Preserve hard failures for missing launcher-specific config, runner scripts,
   registry entries, model inventories, and documentation.
3. Update the launcher note to document that the screen is standalone and may
   run after the previously prepared active campaign state has been closed.
4. Validate the PowerShell syntax and run local `-PreflightOnly`.
5. Run the remote screen and inspect synchronized matrix, reranker, plot, and
   operator-log artifacts.
6. Run Markdown QA for touched Markdown and report the result before any commit
   request.
