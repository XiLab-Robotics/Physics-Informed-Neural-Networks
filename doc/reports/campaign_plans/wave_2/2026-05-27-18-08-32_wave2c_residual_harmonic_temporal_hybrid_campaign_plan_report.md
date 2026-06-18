# Wave 2C Residual Harmonic Temporal Hybrid Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the proposed `Wave 2C`
residual-harmonic temporal hybrid comparison without launching training.

`Wave 2B` showed that sparse `RCIM` harmonic features make the recurrent
temporal families competitive and produced the current scalar training-registry
winner, `periodic_gru_sequence_bw`. `Wave 2C` tests the stronger residual
variant: a structured harmonic base branch predicts the primary TE shape, while
a recurrent temporal branch learns the local sequence residual.

The planned campaign contains `18` candidate runs in one unified campaign
batch:

- `residual_harmonic_gru_sequence` across `global`, `Fw`, and `Bw`;
- `residual_harmonic_lstm_sequence` across `global`, `Fw`, and `Bw`.

Each family-direction pair is repeated for three harmonic-basis tiers:

- `sparse_rcim`;
- `dense_240`;
- `dense_360`.

Training must not start until this planning report and the matching technical
document are explicitly approved.

## Baseline And Verification Rule

`Track 2` remains the official offline verification surface. Wave 2C candidates
must not be accepted from training metrics alone. Any promoted result must
later refresh:

- the direction-aware `Track 2` matrix;
- the best-model collage report and PDF;
- the multi-model curve comparison report and PDF;
- the official `Track 2` update ledger;
- the family and program registries;
- `Training Results Master Summary.md`.

The campaign keeps the repository direction rule:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

## Candidate Matrix

| Family | Direction Surfaces | Harmonic Basis Tiers | Candidate Count | Initial Role |
| --- | --- | --- | ---: | --- |
| `residual_harmonic_gru_sequence` | `global`, `Fw`, `Bw` | `sparse_rcim`, `dense_240`, `dense_360` | 9 | compact recurrent residual over a structured harmonic base |
| `residual_harmonic_lstm_sequence` | `global`, `Fw`, `Bw` | `sparse_rcim`, `dense_240`, `dense_360` | 9 | recurrent cell-state residual over a structured harmonic base |

The sparse tier uses the existing `RCIM` harmonic list:

```text
[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
```

The dense tiers must be materialized as explicit inclusive harmonic-index
lists:

| Basis Tier | Harmonic Index Policy |
| --- | --- |
| `sparse_rcim` | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` |
| `dense_240` | explicit inclusive list `0..240` |
| `dense_360` | explicit inclusive list `0..360` |

This keeps all basis choices inside one comparable campaign while preserving
per-candidate isolation in the leaderboard.

## Prepared Configuration Surface

The implementation should mirror the existing Wave 2 and Wave 2B sequence
configuration pattern.

Prepared model-family selections:

- `model_family=residual_harmonic_gru_sequence`
- `model_family=residual_harmonic_lstm_sequence`

Prepared direction selections:

- `direction=global`
- `direction=fw`
- `direction=bw`

Prepared campaign profile:

- `campaign_profile=wave2c_residual_harmonic_temporal_hybrid`

Prepared harmonic-basis selections:

- `harmonic_basis=sparse_rcim`
- `harmonic_basis=dense_240`
- `harmonic_basis=dense_360`

Prepared dataset profile:

- `dataset_profile=transmission_error_sequence`

The dataset profile keeps the existing sequence contract:

- `collate_mode: sequence`
- `sequence_length: 33`
- `sequence_stride: 4`
- `sequence_target_position: center`
- `maximum_sequences_per_curve: 192`

## Execution Gate

Before launch, the approved campaign package must contain:

- materialized queue YAML files for all `18` candidates;
- direction-specific dataset variant YAML files;
- a dedicated PowerShell launcher under `scripts/campaigns/wave_2/`;
- a launcher note under `doc/scripts/campaigns/wave_2/`;
- an updated `doc/running/active_training_campaign.yaml`;
- the exact launch command.

The expected launch command after approved preparation is:

```powershell
.\scripts\campaigns\wave_2\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1
```

No training execution is approved by this report alone.

## Verification Plan

Before campaign execution:

- confirm the campaign state is `prepared`;
- validate all `18` materialized queue YAML files with the one-batch training
  setup checker when runtime permits;
- run focused model/factory smoke tests for the new model types;
- run Markdown QA on touched authored documentation.

After campaign execution:

- inspect `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- update family-level and program-level best-result registries;
- refresh `Training Results Master Summary.md`;
- close out the campaign with Markdown and validated PDF deliverables;
- propose the optional `Track 2` refresh as a separate operator-launched step.

## Decision Criteria

Wave 2C is worth carrying forward only if the residual recurrent design shows
one of the following:

- it beats the matching Wave 2B recurrent candidate on scalar training metrics;
- it provides a stronger global candidate than the existing Wave 2B global
  recurrent models;
- a dense harmonic tier clearly beats the sparse tier without unstable
  validation behavior;
- it gives visibly better TE-curve shape tracking in a later `Track 2` review.

If the residual branch does not improve over Wave 2B, the current Wave 2B
periodic recurrent candidates remain the stronger temporal branch.
