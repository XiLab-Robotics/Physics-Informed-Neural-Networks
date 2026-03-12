# Configuration Layout

The repository configuration files are grouped by workflow:

- `datasets/`
  Dataset-processing and dataset-root configuration.
- `visualization/`
  Plotting and inspection configuration.
- `training/feedforward/presets/`
  Reusable feedforward training presets.
- `training/queue/`
  Persistent batch-training queue folders.

The `training/queue/` folders use this execution flow:

- `pending/`
  YAML copies waiting to be executed.
- `running/`
  YAML files currently being executed.
- `completed/`
  YAML files that finished successfully.
- `failed/`
  YAML files that ended with an error and require inspection.

Keep canonical reusable presets under `training/feedforward/presets/`.
Do not move those presets between queue folders. Copy them into `pending/`
when preparing a training campaign.
