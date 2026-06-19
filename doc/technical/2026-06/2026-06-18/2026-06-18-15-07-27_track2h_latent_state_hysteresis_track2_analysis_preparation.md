# Track 2H-L Latent-State Hysteresis Track 2 Analysis Preparation

## Overview

This document prepares the separate official `Track 2` analysis workflow for
the latest `Track 2H-L` latent-state / hysteresis-aware models after:

- commit `9c59be2e9ccf742eb125ac72ef3444d1c4f5d1ef`, which adopted the
  multi-index curve-first `Track 2` selection policy; and
- commit `a47173860c93595540cfcd24d24da9d88ce2af5a`, which closed the
  completed `Track 2H-L` campaign.

The preparation must follow the reorganized artifact layout from the campaign
naming cleanup, so campaign closeout reports live under
`doc/reports/campaign_results/track_2/campaign_closeouts/` and official
`Track 2` verification plots live under
`doc/reports/campaign_results/track_2/verification_plots/`.

The approved implementation will prepare an operator-launched verification
refresh. It will not execute the heavy `Track 2` matrix inside Codex.

## Technical Approach

The analysis package will extend the existing full `Track 2` matrix workflow
with one new registry-backed candidate group named
`track2h_latent_state_hysteresis_registry_models`. The group will expose the
six completed `Track 2H-L` registry families:

| Candidate prefix | Surface families |
| --- | --- |
| `track2h_l_gru_offset_residual` | `track2h_latent_state_hysteresis_gru_offset_residual_global`, `track2h_latent_state_hysteresis_gru_offset_residual_fw`, `track2h_latent_state_hysteresis_gru_offset_residual_bw` |
| `track2h_l_causal_tcn_offset_residual` | `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global`, `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw`, `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw` |

The generated candidates will use the source label
`track2h_latent_state_hysteresis_registry` so the official report, collage
report, overlay report, and source-group summaries can keep the new models
separate from robust-loss, probabilistic, mixture-density, and `Wave 3`
candidates.

The verification interpretation must follow the canonical multi-index policy:
raw error, mean-centered shape fidelity, offset / continuity behavior,
harmonic / phase fidelity, robustness, visual evidence, and deployment
readiness must remain visible per `global`, `Fw`, and `Bw` surface.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  will receive the new `Track 2H-L` registry-backed candidate group.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  will be checked and, if needed, extended so the new source label is included
  in generated candidate handling and report grouping.
- `scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1`
  will be created as the operator entry point for local and `-Remote`
  verification refresh execution.
- `doc/scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_track2_verification_refresh.md`
  will document the local and remote commands and the expected output bundle.
- The produced verification artifacts will target dated `Track 2` analysis
  bundles under `doc/reports/analysis/track2/` and plot assets under
  `doc/reports/campaign_results/track_2/verification_plots/`.
- No Codex subagent is planned for this work.

## Implementation Steps

1. Add the six `Track 2H-L` family triplets to the full `Track 2` matrix
   template with source label `track2h_latent_state_hysteresis_registry`.
2. Inspect the registry prediction path for `latent_state_hysteresis_probe`
   compatibility and patch the support module only where the new model type or
   source label requires explicit handling.
3. Create the repository-owned PowerShell launcher with both local execution
   and `-Remote` support, reusing the established `Track 2` refresh pattern and
   synchronizing the six registry families plus their training-run roots.
4. Create the matching launcher note with the exact commands:
   `.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1`
   and
   `.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1 -Remote`.
5. Run focused syntax and Markdown QA on the touched implementation and
   documentation files.
6. Stop after preparation and report the operator commands. After the operator
   completes the launcher, inspect the real artifacts before accepting any
   official `Track 2H-L` decision or updating the program ledgers.
