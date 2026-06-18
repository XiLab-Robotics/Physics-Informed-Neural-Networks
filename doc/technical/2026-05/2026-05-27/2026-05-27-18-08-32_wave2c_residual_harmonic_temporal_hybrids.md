# Wave 2C Residual Harmonic Temporal Hybrids

## Overview

Plan the `Wave 2C` follow-up to the completed `Wave 2B` harmonic-temporal
hybrid campaign.

`Wave 2B` verified that sparse `RCIM` harmonic features materially improve the
temporal `GRU` and `LSTM` sequence families. The next hypothesis is narrower:
use a structured harmonic branch as the base TE estimate, then let a temporal
recurrent branch learn the local sequence residual.

This document authorizes planning only. Implementation code, materialized
campaign YAML files, launchers, and training execution must wait until both
this technical document and the matching campaign planning report are
explicitly approved.

No Codex subagent is planned for this work. If subagent use becomes useful
later, the proposed subagent name, task boundary, and approval requirement must
be documented before asking for approval.

## Technical Approach

Add two residual harmonic temporal model types:

- `residual_harmonic_gru_sequence`;
- `residual_harmonic_lstm_sequence`.

Each model should preserve the existing `Wave 2` sequence-window contract and
make the harmonic basis an explicit campaign tier. The proposed forward path is:

1. Extract the center timestep raw and normalized feature vectors from the
   sequence window.
2. Send the center raw and normalized vectors through the existing
   `HarmonicRegression` structured branch.
3. Send the full normalized sequence window through a recurrent residual
   branch built from the same `RecurrentSequenceNetwork` pattern used by
   `gru_sequence`, `lstm_sequence`, `periodic_gru_sequence`, and
   `periodic_lstm_sequence`.
4. Add the structured prediction and residual prediction.
5. Optionally expose structured, residual, and combined tensors through a
   diagnostic method matching the existing residual harmonic pattern.

The first implementation should support three explicit harmonic-basis tiers in
one campaign package:

| Basis Tier | Harmonic Index Policy | Role |
| --- | --- | --- |
| `sparse_rcim` | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` | continuity with Wave 2B |
| `dense_240` | explicit inclusive list `0..240` | first dense harmonic stress test |
| `dense_360` | explicit inclusive list `0..360` | full one-revolution harmonic stress test |

The sparse `RCIM` list is:

```text
[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
```

The first campaign should be one unified `18`-run architectural validation:

| Family | Direction Surfaces | Basis Tiers | Candidate Count |
| --- | --- | --- | ---: |
| `residual_harmonic_gru_sequence` | `global`, `Fw`, `Bw` | `sparse_rcim`, `dense_240`, `dense_360` | 9 |
| `residual_harmonic_lstm_sequence` | `global`, `Fw`, `Bw` | `sparse_rcim`, `dense_240`, `dense_360` | 9 |

This is one campaign, not one training run. Each family, direction surface, and
harmonic-basis tier remains a separate materialized queue item so the
leaderboard can isolate whether the dense basis actually helps.

`periodic_temporal_convolution` should not be extended in this first pass,
because the Wave 2B leaderboard showed the recurrent families as the useful
branch and the convolutional branch as the weaker candidate.

## Involved Components

- `doc/reports/campaign_plans/wave_2/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md`
  Matching preliminary campaign plan.
- `scripts/models/residual_harmonic_network.py`
  Existing static residual harmonic reference pattern.
- `scripts/models/temporal_sequence_network.py`
  Existing recurrent `GRU` and `LSTM` sequence backbone.
- `scripts/models/periodic_temporal_sequence_network.py`
  Existing sequence input-context pattern and Wave 2B harmonic-temporal
  reference implementation.
- `scripts/models/model_factory.py`
  Factory registration point for the new model types.
- `config/training/hydra/wave2/`
  Existing Hydra surface to mirror for model-family and direction profiles.
- `config/training/wave2c_residual_harmonic_temporal_hybrid/`
  Proposed materialized campaign package root after approval.
- `scripts/campaigns/wave_2/`
  Proposed launcher location after approval.
- `doc/scripts/campaigns/wave_2/`
  Proposed launcher-note location after approval.
- `doc/running/active_training_campaign.yaml`
  Campaign state file to update only during approved campaign preparation.
- `output/training_runs/`, `output/training_campaigns/`, and
  `output/registries/`
  Required artifact and registry destinations after approved execution and
  closeout.

## Implementation Steps

1. Wait for explicit approval of this technical document and the matching
   campaign planning report.
2. Implement a narrow residual harmonic temporal network module or extend the
   existing residual harmonic module only if the resulting code remains
   inspectable.
3. Register `residual_harmonic_gru_sequence` and
   `residual_harmonic_lstm_sequence` in the model factory.
4. Add focused smoke coverage for rank-3 sequence inputs, shape validation,
   branch-output diagnostics, and factory construction.
5. Add Hydra model-family profiles for the two new families using explicit
   harmonic-basis tier overrides and the same sequence-window settings as Wave
   2B.
6. Prepare the approved `18`-run campaign package for `global`, `Fw`, and `Bw`
   surfaces across `sparse_rcim`, `dense_240`, and `dense_360` basis tiers.
7. Create the dedicated PowerShell launcher and matching launcher note.
8. Update `doc/running/active_training_campaign.yaml` to the prepared campaign
   state with protected queue/config/launcher files.
9. Run pre-launch validation on the materialized queue configs when runtime
   permits.
10. Provide the exact operator launch command and wait for the user to run the
    campaign.
11. After completion, perform normal campaign closeout before proposing any
    optional `Track 2` refresh.
