# Batch Training Queue And Config Reorganization

## Overview

The user requested a training workflow that can execute multiple YAML configurations without requiring an interactive session for every run.

Two orchestration strategies were proposed:

1. a filesystem queue with a folder for pending configurations and another folder for completed ones;
2. a command-line batch script invoked with explicit YAML file names, for example:
   `python batch_training.py config1.yaml config2.yaml`

The request also includes a broader reorganization of the `config/` folder so the repository can grow beyond the current feedforward-only setup, plus an automatic technical execution report that records what was tested and where the relevant artifacts can be found for the mandatory post-training results report.

## Technical Approach

The recommended primary workflow is the filesystem queue.

Reasoning:

- long campaigns need persistent state even if the terminal session is closed;
- queued files are visible at a glance and can be prepared incrementally over time;
- completed and failed jobs remain auditable without reconstructing the original command line;
- the workflow naturally supports resume-after-interruption behavior;
- this scales better once multiple model families exist.

The command-line argument mode is still useful, but only as a convenience layer on top of the queue, not as the main workflow. A robust design is therefore:

- **primary mode**: execute every queued YAML in a dedicated `pending` folder;
- **secondary mode**: accept YAML paths as CLI arguments and internally enqueue them into the same workflow.

This avoids maintaining two independent execution paths.

### Proposed Config Reorganization

The current flat `config/` folder should be reorganized so configuration intent is explicit and future model families remain isolated.

Proposed structure:

```text
config/
  datasets/
    transmission_error_dataset.yaml
  visualization/
    transmission_error_visualization.yaml
  training/
    feedforward/
      presets/
        baseline.yaml
        trial.yaml
        high_epoch.yaml
        high_density.yaml
        high_compute.yaml
    queue/
      pending/
      running/
      completed/
      failed/
```

Design notes:

- `presets/` stores canonical reusable training configurations;
- `queue/` stores execution copies, not the canonical presets;
- `running/` makes interrupted campaigns easier to diagnose;
- `failed/` prevents silent loss of configurations that need inspection.

This separation is preferable to moving the main reusable YAML files themselves between folders, because the project should keep a stable library of named configurations while still supporting queue-based execution.

### Proposed Batch Runner Behavior

The batch runner should be added as a dedicated training orchestration entry point, for example:

- `training/run_training_campaign.py`

Core behavior:

1. discover queued YAML files from `config/training/queue/pending/` sorted by filename;
2. move the current file into `running/` before execution;
3. read the YAML and resolve the target trainer from `experiment.model_type`;
4. execute the corresponding training entry point;
5. capture terminal output into a per-run log file;
6. move the YAML into `completed/` on success or `failed/` on error;
7. append the run result to a campaign-level manifest and markdown report.

For the current repository state, only `feedforward` would be supported. The runner should fail fast with a clear message when an unsupported `model_type` is encountered.

### Metadata For Campaign Reporting

To support later creation of the mandatory post-training report, each queued YAML should remain compatible with the current training schema but may optionally add a small metadata section such as:

```yaml
metadata:
  campaign_name: mixed_density_followup
  planning_report_path: doc/reports/campaign_plans/...
  notes: test longer schedule with denser sampling
```

This metadata is not required for the trainer itself, but it is valuable for campaign traceability.

### Automatic Execution Report

The batch runner should generate a machine-readable manifest plus a human-readable execution report under a campaign artifact root such as:

```text
output/training_campaigns/<timestamp>_<campaign_name>/
  campaign_manifest.yaml
  campaign_execution_report.md
  logs/
    <job_name>.log
```

Each run entry should record at least:

- queue YAML path;
- final queue status (`completed` or `failed`);
- `experiment.run_name`;
- `experiment.model_type`;
- training output directory;
- `best_checkpoint_path.txt`;
- `training_test_metrics.yaml`;
- `training_test_report.md`;
- terminal log path;
- start time, end time, and duration;
- exception message if the run fails;
- linked planning-report path when available.

This execution report is not a substitute for the required final campaign-results report in `doc/reports/campaign_results/`, but it gives all references needed to create that report efficiently after long unattended training sessions.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index that should also reference this technical document.
- `doc/guide/project_usage_guide.md`
  Will need an update after approval because the repository will gain a new runnable training workflow.
- `config/`
  Current flat configuration folder that should be reorganized into clearer dataset, visualization, and training subtrees.
- `config/feedforward_network_training.yaml`
  Current baseline training-configuration example to migrate into the new structure.
- `training/train_feedforward_network.py`
  Existing single-run feedforward trainer that the batch runner should reuse.
- `models/model_factory.py`
  Current model-type dispatch point that should inform batch-runner routing.
- `doc/reports/campaign_plans/`
  Existing location for mandatory pre-training planning reports.
- `doc/reports/campaign_results/`
  Existing location for mandatory post-training results reports.
- `output/feedforward_network/`
  Existing per-run artifact root that the campaign manifest must reference.
- `output/training_campaigns/`
  Proposed new campaign-level artifact root for batch execution metadata and log indexing.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, reorganize `config/` into separate dataset, visualization, and training subtrees without losing the existing reusable feedforward presets.
3. Add the new batch-training orchestration entry point that uses the queue as the primary workflow and supports CLI file arguments as an optional enqueue shortcut.
4. Route each YAML to the correct trainer based on `experiment.model_type`, initially supporting the current `feedforward` trainer.
5. Capture per-run logs and create a campaign-level manifest plus markdown execution report under `output/training_campaigns/`.
6. Update `doc/guide/project_usage_guide.md` so the new queue workflow, naming conventions, and report artifacts are documented before any final commit.
7. Keep the mandatory training workflow intact:
   - create the planning report in `doc/reports/campaign_plans/` before executing a real campaign;
   - use the generated campaign execution report as the source index for the final report in `doc/reports/campaign_results/`.
