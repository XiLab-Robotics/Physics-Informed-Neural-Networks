# Wave 4.4 Latent-State Hysteresis Closeout

## Overview

This technical note defines the normal closeout for the completed
`track2h_latent_state_hysteresis_campaign_2026_06_16` campaign. The campaign
was executed by the operator and committed in
`07a31aa639b9273b73170742584b344b508b74d9`; this closeout promotes the
resulting evidence into the repository documentation and clears the active
campaign state.

## Technical Approach

The closeout is limited to campaign-result acceptance and documentation. It
does not run the heavy official `TE Curve Verification Pipeline` verification matrix. The workflow
will:

- read the completed campaign leaderboard and best-run pointers;
- create a final campaign-results report and styled PDF;
- compare the scalar branch winners against completed `Wave 4.1` robust,
  probabilistic, and mixture-density baselines;
- update the live backlog, master training summary, user guide, and
  documentation index;
- clear `doc/running/active_training_campaign.yaml` while preserving the last
  completed campaign summary;
- leave official `TE Curve Verification Pipeline` curve-first verification as a separate optional
  operator-approved step.

## Involved Components

- `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/`
- `output/registries/families/track2h_latent_state_hysteresis_*/`
- `output/registries/program/current_best_solution.yaml`
- `doc/running/active_training_campaign.yaml`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Create the final `Wave 4.4` campaign-results Markdown report.
2. Export and validate the styled PDF deliverable from the real report.
3. Update active campaign state to no active campaign with a
   `last_completed_campaign` block.
4. Synchronize the backlog and master summary with the scalar findings and
   non-promotion decision.
5. Register the new technical and campaign-result documents from
   `doc/README.md`.
6. Run Markdown QA and final repository checks before handing off for commit
   approval.

No subagent is planned for this closeout.
