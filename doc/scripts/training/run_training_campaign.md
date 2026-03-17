# Training Campaign Runner

## Overview

This script executes multiple training YAML files one by one through a persistent filesystem queue.

It is stored in:

- `scripts/training/run_training_campaign.py`

The runner is meant for long unattended campaigns where the user wants to prepare several configurations in advance and collect an indexed execution report afterward.

For the current feedforward workflow, the runner now reuses the same in-process terminal behavior as `scripts/training/train_feedforward_network.py` instead of flattening the child output through a captured subprocess pipe.

## Main Role

The script coordinates the batch-training flow:

1. optionally copy selected YAML files into the pending queue;
2. discover queued YAML files in `config/training/queue/pending/`;
3. move each file into `running/` before execution;
4. dispatch the YAML to the correct training entry point based on `experiment.model_type`;
5. mirror the live terminal output to both the active console and a per-run campaign log file;
6. move the YAML into `completed/` or `failed/`;
7. write a campaign manifest and markdown execution report.

## Main Components Used

### `config/training/feedforward/presets/`

Reusable feedforward training presets that should be copied into the queue when preparing a campaign.

### `config/training/queue/`

Persistent queue folders:

- `pending/`
- `running/`
- `completed/`
- `failed/`

### `scripts/training/train_feedforward_network.py`

Current single-run feedforward training entry point reused directly by the batch runner for the supported feedforward workflow.

### `output/training_campaigns/`

Campaign-level artifact root that stores:

- `campaign_manifest.yaml`
- `campaign_execution_report.md`
- `campaign_leaderboard.yaml`
- `campaign_best_run.yaml`
- `campaign_best_run.md`
- `logs/*.log`

## Outputs

For each batch execution, the runner generates:

- a queue-state transition for every YAML file;
- the same terminal logging and Lightning progress-bar behavior used by the direct single-run training script for supported model types;
- a compact campaign-progress summary before and after each run, including `current/total` status;
- a campaign manifest with machine-readable run metadata;
- a campaign markdown report summarizing all runs;
- an explicit campaign-local leaderboard and best-run record;
- one terminal log per queued YAML file;
- references to the per-run training artifacts already produced by the underlying trainer.

The runner now resolves canonical per-run snapshots from:

- `training_config.yaml`
- `metrics_summary.yaml`

## Practical Use

Queue existing presets without executing them yet:

```powershell
python scripts/training/run_training_campaign.py `
  config/training/feedforward/presets/baseline.yaml `
  config/training/feedforward/presets/high_epoch.yaml `
  --enqueue-only
```

Process everything currently waiting in the pending queue:

```powershell
python scripts/training/run_training_campaign.py
```

Queue selected presets and execute them immediately in the same command:

```powershell
python scripts/training/run_training_campaign.py `
  config/training/feedforward/presets/baseline.yaml `
  config/training/feedforward/presets/high_density.yaml `
  --campaign-name feedforward_density_check
```

The generated campaign report is intended to be the technical source index for the mandatory final report in `doc/reports/campaign_results/`.

During execution, the campaign runner now keeps the direct single-run training output visible in the terminal, so the user can observe startup messages, Lightning progress bars, validation/test phases, and final artifact summaries without waiting for the campaign to finish.

The underlying run artifacts are now expected under `output/training_runs/<model_family>/<run_instance_id>/`, while campaign summaries remain under `output/training_campaigns/<campaign_id>/`.
