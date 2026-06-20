# Wave 4.4 Latent-State Hysteresis TE Curve Verification Pipeline Analysis Preparation

## Overview

This document prepares the separate official `TE Curve Verification Pipeline` analysis workflow for
the latest `Wave 4.4` latent-state / hysteresis-aware models after:

- commit `9c59be2e9ccf742eb125ac72ef3444d1c4f5d1ef`, which adopted the
  multi-index curve-first `TE Curve Verification Pipeline` selection policy; and
- commit `a47173860c93595540cfcd24d24da9d88ce2af5a`, which closed the
  completed `Wave 4.4` campaign.

The preparation must follow the reorganized artifact layout from the campaign
naming cleanup, so campaign closeout reports live under
`doc/reports/campaign_results/track_2/campaign_closeouts/` and official
`TE Curve Verification Pipeline` verification plots live under
`doc/reports/campaign_results/track_2/verification_plots/`.

The approved implementation will prepare an operator-launched verification
refresh. It will not execute the heavy `TE Curve Verification Pipeline` matrix inside Codex.

## Technical Approach

The analysis package will extend the existing full `TE Curve Verification Pipeline` matrix workflow
with one new registry-backed candidate group named
`track2h_latent_state_hysteresis_registry_models`. The group will expose the
six completed `Wave 4.4` registry families:

| Candidate prefix | Surface families |
| --- | --- |
| `track2h_l_gru_offset_residual` | `track2h_latent_state_hysteresis_gru_offset_residual_global`, `track2h_latent_state_hysteresis_gru_offset_residual_fw`, `track2h_latent_state_hysteresis_gru_offset_residual_bw` |
| `track2h_l_causal_tcn_offset_residual` | `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global`, `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw`, `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw` |

The generated candidates will use the source label
`track2h_latent_state_hysteresis_registry` so the official report, collage
report, overlay report, and source-group summaries can keep the new models
separate from robust-loss, probabilistic, mixture-density, and `Wave 5.1`
candidates.

The verification interpretation must follow the canonical multi-index policy:
raw error, mean-centered shape fidelity, offset / continuity behavior,
harmonic / phase fidelity, robustness, visual evidence, and deployment
readiness must remain visible per `global`, `Fw`, and `Bw` surface.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  will receive the new `Wave 4.4` registry-backed candidate group.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  will be checked and, if needed, extended so the new source label is included
  in generated candidate handling and report grouping.
- `scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1`
  will be created as the operator entry point for local and `-Remote`
  verification refresh execution.
- `doc/scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_track2_verification_refresh.md`
  will document the local and remote commands and the expected output bundle.
- The produced verification artifacts will target dated `TE Curve Verification Pipeline` analysis
  bundles under `doc/reports/analysis/track2/` and plot assets under
  `doc/reports/campaign_results/track_2/verification_plots/`.
- No Codex subagent is planned for this work.

## Implementation Steps

1. Add the six `Wave 4.4` family triplets to the full `TE Curve Verification Pipeline` matrix
   template with source label `track2h_latent_state_hysteresis_registry`.
2. Inspect the registry prediction path for `latent_state_hysteresis_probe`
   compatibility and patch the support module only where the new model type or
   source label requires explicit handling.
3. Create the repository-owned PowerShell launcher with both local execution
   and `-Remote` support, reusing the established `TE Curve Verification Pipeline` refresh pattern and
   synchronizing the six registry families plus their training-run roots.
4. Create the matching launcher note with the exact commands:
   `.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1`
   and
   `.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1 -Remote`.
5. Run focused syntax and Markdown QA on the touched implementation and
   documentation files.
6. Stop after preparation and report the operator commands. After the operator
   completes the launcher, inspect the real artifacts before accepting any
   official `Wave 4.4` decision or updating the program ledgers.
