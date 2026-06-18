# Wave 2B Harmonic Temporal Hybrid Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the first `Wave 2B`
harmonic-temporal hybrid comparison without launching training.

`Wave 2` verified temporal convolution, `GRU`, and `LSTM` sequence models in
the official `Track 2` workflow, but none of those temporal candidates was
promoted over the current repository-owned `tree` baseline. `Wave 2B` tests the
follow-up hypothesis that the temporal backbones need an explicit TE harmonic
prior rather than only short sequence context.

The planned campaign contains `9` candidate runs:

- `periodic_temporal_convolution` across `global`, `Fw`, and `Bw`;
- `periodic_gru_sequence` across `global`, `Fw`, and `Bw`;
- `periodic_lstm_sequence` across `global`, `Fw`, and `Bw`.

Training must not start until this campaign package is explicitly approved.

## Baseline And Verification Rule

`Track 2` remains the official offline verification surface. Wave 2B candidates
are not accepted from training metrics alone. Any promoted result must refresh:

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

| Family | Direction Surfaces | Harmonic Basis | Initial Role |
| --- | --- | --- | --- |
| `periodic_temporal_convolution` | `global`, `Fw`, `Bw` | RCIM sparse list | local temporal context plus explicit periodic features |
| `periodic_gru_sequence` | `global`, `Fw`, `Bw` | RCIM sparse list | compact recurrent memory plus explicit periodic features |
| `periodic_lstm_sequence` | `global`, `Fw`, `Bw` | RCIM sparse list | recurrent cell-state baseline plus explicit periodic features |

The first campaign uses the RCIM sparse harmonic list:

```text
[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
```

Dense `0..240` or `0..360` harmonic sweeps remain later branches. They are not
part of this first Wave 2B campaign.

## Prepared Configuration Surface

The campaign uses the Hydra root:

`config/training/hydra/wave2/config.yaml`

Prepared model-family selections:

- `model_family=periodic_temporal_convolution`
- `model_family=periodic_gru_sequence`
- `model_family=periodic_lstm_sequence`

Prepared direction selections:

- `direction=global`
- `direction=fw`
- `direction=bw`

Prepared campaign profile:

- `campaign_profile=wave2b_harmonic_temporal_hybrid`

Prepared dataset profile:

- `dataset_profile=transmission_error_sequence`

The dataset profile keeps the existing Wave 2 sequence contract:

- `collate_mode: sequence`
- `sequence_length: 33`
- `sequence_stride: 4`
- `sequence_target_position: center`
- `maximum_sequences_per_curve: 192`

## Execution Gate

Before launch, the prepared campaign package must contain:

- materialized queue YAML files for all `9` candidates;
- direction-specific dataset variant YAML files;
- a dedicated PowerShell launcher under `scripts/campaigns/wave_2/`;
- a launcher note under `doc/scripts/campaigns/wave_2/`;
- an updated `doc/running/active_training_campaign.yaml`;
- the exact launch command.

The launch command is expected to be:

```powershell
.\scripts\campaigns\wave_2\run_wave2b_harmonic_temporal_hybrid_campaign.ps1
```

No training execution is approved by this report alone.

## Verification Plan

Before campaign execution:

- confirm the campaign state is `prepared`;
- validate all `9` materialized queue YAML files with the one-batch training
  setup checker when runtime permits;
- run Markdown QA on the touched authored documentation.

After campaign execution:

- inspect `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- update family-level and program-level best-result registries;
- refresh `Training Results Master Summary.md`;
- refresh the official `Track 2` matrix and visual reports for the Wave 2B
  candidates;
- append the Wave 2B verdict to the official `Track 2` report ledger.

## Decision Criteria

Wave 2B candidates are promoted only if both conditions hold:

- scalar `Track 2` metrics are competitive with the current repository-owned
  `tree` baseline on the matching direction surface;
- visual curve evidence shows useful TE tracking behavior rather than only a
  local training-metric improvement.

If either condition fails, the Wave 2B campaign remains a completed exploratory
training experiment and the accepted offline baseline remains unchanged.
