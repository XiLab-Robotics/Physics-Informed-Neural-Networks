# Wave 2 Temporal Model Entry Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the first `Wave 2` temporal-model
comparison without launching training.

The campaign is scoped to three lightweight sequence families:

- `temporal_convolution`
- `gru_sequence`
- `lstm_sequence`

Each family must expose the same three verification surfaces used by the
closed `Wave 1` and official `Track 2` workflow:

- `global`
- `Fw`
- `Bw`

The planned campaign therefore contains `9` primary candidate runs. Training
must not start until this campaign plan and the launcher package are explicitly
approved.

## Baseline And Verification Rule

`Track 2` is the official offline verification report for new model families.
The Wave 2 candidates are not accepted by training metrics alone. Promoted
results must refresh:

- the official direction-aware `Track 2` matrix;
- the best-model collage report;
- the multi-model curve comparison report;
- the official `Track 2` update ledger;
- the family and program registries.

The campaign inherits the direction rule:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

## Candidate Matrix

| Family | Direction Surfaces | Input Contract | Initial Role |
| --- | --- | --- | --- |
| `temporal_convolution` | `global`, `Fw`, `Bw` | centered sequence windows | short-context convolution baseline |
| `gru_sequence` | `global`, `Fw`, `Bw` | centered sequence windows | compact recurrent-memory baseline |
| `lstm_sequence` | `global`, `Fw`, `Bw` | centered sequence windows | recurrent cell-state baseline |

## Prepared Configuration Surface

The campaign uses the Hydra root:

`config/training/hydra/wave2/config.yaml`

Prepared model-family selections:

- `model_family=temporal_convolution`
- `model_family=gru_sequence`
- `model_family=lstm_sequence`

Prepared direction selections:

- `direction=global`
- `direction=fw`
- `direction=bw`

Prepared dataset profile:

- `dataset_profile=transmission_error_sequence`

The dataset profile enables sequence collation with:

- `collate_mode: sequence`
- `sequence_length: 33`
- `sequence_stride: 4`
- `sequence_target_position: center`
- `maximum_sequences_per_curve: 192`

## Execution Gate

Before launch, the next approved preparation step must generate:

- materialized training YAML files for all `9` candidates;
- a dedicated PowerShell launcher under `scripts/campaigns/`;
- a launcher note under `doc/scripts/campaigns/`;
- an updated `doc/running/active_training_campaign.yaml`;
- the exact launch command.

No training execution is approved by this report alone.

## Verification Plan

Before full campaign execution:

- compile the modified Python modules;
- instantiate all three model families through `create_model`;
- validate random rank-3 forward passes for output shape compatibility;
- run Markdown QA for the touched documentation scope.

After campaign execution:

- run the repository training setup validation on all materialized configs;
- run the campaign through the approved launcher;
- update `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- update family and program registries;
- refresh `Training Results Master Summary.md`;
- refresh the official `Track 2` report and visual companion reports for
  promoted candidates.

## Decision Criteria

Wave 2 candidates are promoted only if they provide a clear benefit over the
closed `Wave 1` and official `Track 2` baselines on direction-aware held-out
TE reconstruction, while remaining simple enough to inspect and later assess
for PLC/TwinCAT deployment.
