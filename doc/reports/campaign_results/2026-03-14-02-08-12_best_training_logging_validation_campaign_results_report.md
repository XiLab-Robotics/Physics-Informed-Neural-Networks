# Best Training Logging Validation Campaign Results Report

## Overview

This report summarizes the completed one-item campaign prepared in:

- `doc/reports/campaign_plans/2026-03-14-00-56-06_best_training_logging_validation_campaign_plan_report.md`

The campaign objective was not to compare multiple model variants. The objective was to validate the revised live terminal behavior of `training/run_training_campaign.py` during a real feedforward training run using the current recommended preset:

- `config/training/feedforward/presets/best_training.yaml`

The campaign completed successfully at the training and queue level:

- completed runs: `1`
- failed runs: `0`
- queue status for the campaign item: moved from `pending` to `completed`

The execution artifact root is:

- `output/training_campaigns/2026-03-14-01-09-30_best_training_logging_validation_campaign_2026_03_14_00_56_06/`

## Campaign Goal

The run was designed to answer four practical questions:

1. Does the campaign runner now show immediate startup output instead of the earlier silent initialization period?
2. Does the terminal now preserve the same readable sectioned training output used by `train_feedforward_network.py`?
3. Does the campaign still produce the expected queue, report, checkpoint, metric, and log artifacts?
4. Are there any residual logging issues still visible after the campaign-runner refactor?

## Executed Configuration

| Config | Source Preset | Run Name | Model Type | Campaign Role |
| --- | --- | --- | --- | --- |
| `best_training_logging_validation` | `config/training/feedforward/presets/best_training.yaml` | `te_feedforward_best_training` | `feedforward` | Validate the updated live campaign logging on the current best practical preset |

## Training Outcome

The executed run reused the unchanged `best_training` hyperparameters and converged cleanly.

| Config | Best Epoch | Wall Time | Val MAE [deg] | Val RMSE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `best_training_logging_validation` | 63 | 15.4 min | 0.003171 | 0.003759 | 0.003579 | 0.004121 |

### Interpretation

The training result is numerically stable and consistent with a valid feedforward run:

- the best checkpoint was selected at epoch `63`;
- early stopping stopped the run after epoch `76`;
- held-out validation remained strong with `val_mae = 0.003171 deg`;
- held-out test performance finished at `test_mae = 0.003579 deg` and `test_rmse = 0.004121 deg`.

This confirms that the campaign runner changes did not break the core training, checkpointing, validation, or held-out test workflow.

## Terminal Logging Validation Outcome

The live terminal behavior improved in the ways the campaign was supposed to validate.

### Confirmed Improvements

- the campaign printed an immediate campaign header with `1/1` progress before training started;
- the full sectioned summary from the single-run training script remained visible:
  - configuration;
  - dataset summary;
  - model summary;
  - normalization statistics;
  - runtime summary;
  - training, validation, checkpoint evaluation, test, and artifact sections;
- epoch-level progress was readable directly in the active terminal during the real run;
- the campaign printed a clear completion footer with total completed and failed counts.

### Campaign Artifact Validation

The queue-based workflow still produced the expected outputs:

| Artifact | Status | Notes |
| --- | --- | --- |
| `campaign_manifest.yaml` | generated | campaign-level machine-readable execution index |
| `campaign_execution_report.md` | generated | campaign-level execution summary |
| mirrored terminal log | generated | one log file stored under the campaign `logs/` folder |
| checkpoints | generated | best checkpoint and last checkpoint available |
| `training_test_metrics.yaml` | generated | final validation and test metrics available |
| `training_test_report.md` | generated | per-run markdown summary available |

## Residual Issues

The campaign also exposed two residual logging defects that should be treated as follow-up work rather than ignored.

### 1. Shutdown Exception After Successful Completion

After the campaign finished successfully, the terminal printed a final exception from `colorama` shutdown handling:

- `ValueError: I/O operation on closed file`

The most likely cause is that the mirrored tee stream in the campaign runner is already closed when `colorama` executes its `atexit` reset callback.

This does **not** invalidate the training results, but it means the campaign runner shutdown path is still not fully clean.

### 2. Mirrored Log File Is Not Yet Clean Enough

The stored mirrored campaign log still contains:

- ANSI escape sequences;
- mangled progress-bar glyphs in some progress sections.

This means the live terminal experience improved substantially, but the serialized per-run log file is still not as clean as the direct terminal view.

## Best-Performing Configuration

Because this campaign intentionally ran only one configuration, the best-performing configuration is trivially:

- `best_training_logging_validation`

That does **not** mean this campaign re-selected the global best feedforward preset from scratch. It confirms that the already selected `best_training` preset still executes correctly through the revised campaign runner.

From a workflow perspective, this is the main practical result of the campaign:

- the recommended preset remains usable inside the campaign queue flow,
- and the remaining issues are now concentrated in logging cleanup rather than in training correctness.

## Main Conclusions

This one-item validation campaign supports four practical conclusions.

### 1. The New Live Campaign Logging Is Functionally Better

The original silence-at-start problem is no longer the dominant user experience. The campaign now shows immediate context and live training progress.

### 2. The Core Queue Workflow Remains Intact

The revised runner still completed the queue transition, training run, metrics export, checkpointing, and campaign reporting correctly.

### 3. The `best_training` Preset Remains Executable As A Campaign Item

The current recommended feedforward preset ran successfully inside the queue-based campaign workflow without breaking the training pipeline.

### 4. One Logging Fix Is Still Needed

The final `colorama` shutdown exception and the noisy mirrored log-file encoding show that the campaign-runner logging work is improved but not fully finished.

## Recommended Next Improvements

The next useful follow-up tasks are:

1. fix the runner shutdown path so `colorama` cannot write to a closed tee stream at process exit;
2. clean the mirrored log serialization so stored logs do not keep ANSI escape sequences or mangled progress glyphs;
3. re-run a short one-item validation campaign after that fix to confirm both live terminal output and stored logs are clean.

## Artifact References

Campaign-level references:

- `output/training_campaigns/2026-03-14-01-09-30_best_training_logging_validation_campaign_2026_03_14_00_56_06/campaign_manifest.yaml`
- `output/training_campaigns/2026-03-14-01-09-30_best_training_logging_validation_campaign_2026_03_14_00_56_06/campaign_execution_report.md`
- `output/training_campaigns/2026-03-14-01-09-30_best_training_logging_validation_campaign_2026_03_14_00_56_06/logs/2026-03-14-01-09-30_001_01_best_training_logging_validation.log`

Run-level references:

- `output/feedforward_network/te_feedforward_best_training/best_checkpoint_path.txt`
- `output/feedforward_network/te_feedforward_best_training/training_test_metrics.yaml`
- `output/feedforward_network/te_feedforward_best_training/training_test_report.md`
- `output/feedforward_network/te_feedforward_best_training/checkpoints/feedforward-epoch=063-val_mae=0.00317104.ckpt`
