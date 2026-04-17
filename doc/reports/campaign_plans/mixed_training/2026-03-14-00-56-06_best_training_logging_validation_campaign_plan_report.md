# Best Training Logging Validation Campaign Plan Report

## Overview

This report defines a focused follow-up campaign for **Saturday, March 14, 2026**.

The campaign has one purpose:

- validate the updated terminal and logging behavior of `training/run_training_campaign.py` during a real campaign execution,

while keeping the training configuration fixed to the current recommended preset:

- `config/training/feedforward/presets/best_training.yaml`

This is intentionally a **single-configuration campaign**. It is a workflow-validation run on top of an already selected practical feedforward preset, not a new hyperparameter comparison study.

## Why This Plan Makes Sense

The repository now has two relevant facts:

1. the mixed campaign already identified `best_training.yaml` as the current best practical feedforward preset;
2. the campaign runner was recently updated so its terminal behavior should now match direct single-run training output.

That means the next useful step is not another grid search. The next useful step is to validate the new campaign-execution experience under a meaningful real workload.

Using `best_training.yaml` is the right choice because:

- it is already the recommended preset in the usage guide;
- it represents a non-trivial long schedule rather than a toy smoke test;
- it exercises the revised runner under realistic checkpointing, validation, test, and report-generation conditions.

## Main Variables To Control

This campaign is intentionally designed to keep almost everything fixed.

### 1. Training Preset

Fixed to:

- `config/training/feedforward/presets/best_training.yaml`

Reason:

- the objective is workflow validation, not parameter exploration.

### 2. Campaign Size

Fixed to:

- `1` run

Reason:

- this is enough to validate live terminal behavior, per-run logging, queue transitions, and campaign artifacts without burning unnecessary compute.

### 3. Logging Surface

The run should specifically validate that the campaign terminal now shows:

- the campaign progress header;
- the same sectioned training summary used by direct single-run execution;
- live Lightning progress bars;
- final validation, best-checkpoint evaluation, test, and artifact summaries.

### 4. Artifact Traceability

The campaign should still produce the normal batch artifacts:

- campaign manifest;
- campaign execution report;
- one mirrored terminal log;
- per-run checkpoints;
- per-run metrics snapshot;
- per-run markdown report.

## Parameter Meaning And Expected Effects

The selected preset keeps the following practical behavior:

| Parameter Group | Value | Meaning | Expected Effect |
| --- | --- | --- | --- |
| `dataset.curve_batch_size` | `4` | Number of directional curves loaded per batch | Moderately strong throughput without the more aggressive large-batch variants |
| `dataset.point_stride` | `5` | Point subsampling step along each TE curve | Denser than baseline and aligned with the current best practical result |
| `dataset.maximum_points_per_curve` | `null` | No explicit point cap per curve | Lets the stride setting control density directly |
| `dataset.num_workers` | `8` | DataLoader worker count | Higher input-pipeline throughput on the target workstation |
| `dataset.pin_memory` | `true` | Pinned host memory for GPU transfer | Better CUDA input-transfer behavior |
| `model.hidden_size` | `128-128-64` | Standard recommended MLP depth/width | Keeps the strongest practical architecture without the heavier big-model variant |
| `training.learning_rate` | `0.0010` | AdamW learning rate | Matches the current recommended feedforward training regime |
| `training.min_epochs` | `20` | Minimum training length | Prevents too-early stopping before the long schedule has a chance to settle |
| `training.max_epochs` | `250` | Maximum epoch budget | Preserves the stronger optimization depth discovered in the mixed campaign |
| `training.patience` | `35` | Early-stopping patience on `val_mae` | Allows slow improvements without running forever |

## What Should Stay Fixed

To keep this campaign interpretable, the following should remain fixed:

- dataset split logic;
- feature set and target definition;
- optimizer family;
- output/checkpoint/report workflow;
- direct reuse of the `best_training` hyperparameters;
- queue-based campaign execution through `training/run_training_campaign.py`.

## Candidate Configuration Table

The campaign should contain exactly one candidate configuration.

| Config | Source Preset | Planned Run Name | Model Type | Point Stride | Curve Batch Size | Hidden Layers | Epoch Range | Patience | Campaign Role |
| --- | --- | --- | --- | ---: | ---: | --- | --- | ---: | --- |
| `best_training_logging_validation` | `config/training/feedforward/presets/best_training.yaml` | `te_feedforward_best_training` | `feedforward` | 5 | 4 | 128-128-64 | 20-250 | 35 | Validate the updated live campaign logging on the current best practical preset |

## Recommended Execution Order

The execution order is trivial:

1. prepare one dedicated campaign YAML derived from `best_training.yaml`;
2. launch the one-item campaign;
3. observe the terminal directly during startup, training, validation, and test;
4. inspect the generated campaign log and execution report afterward.

## What We Expect To Learn

This campaign should answer these specific questions:

1. Does the terminal show immediate startup output instead of the previous silent initialization period?
2. Do the Lightning progress bars remain readable during campaign execution?
3. Does the mirrored campaign log preserve the same readable output structure?
4. Does the one-item queue workflow still generate the expected campaign-level artifacts cleanly?

## Practical Recommendation Before Execution

This campaign is technically low-risk and high-value because it validates the updated runner behavior without introducing any new modeling variables.

My recommendation is:

- approve the preparation of the one-item campaign,
- generate the dedicated campaign YAML and active-campaign state,
- then launch it exactly once as the first real validation of the revised campaign terminal workflow.
