# Polished Stage 1 Checkpoint Reload Fix

## Overview

The `polished_dataset_stage1_smoke_2026_06_21` campaign was launched locally
on June 22, 2026 and stopped on the first Stage 1 run,
`te_feedforward_trial`. The feedforward training loop completed all configured
epochs and the final validation loop completed, but the run failed during best
checkpoint reload with:

```text
ValueError: invalid literal for int() with base 10: 'auto'
```

The failure is not a polished-dataset loading failure. The run summary showed
`Input Feature Dim = 4`, which is the expected polished schema:

```text
inputs = [theta, theta_dot, tau_load, T]
target = theta_TE
```

The failure occurs after training because the best-checkpoint evaluation path
calls `create_model(...)` with the original model configuration where
`model.input_size` is still the string value `auto`. The initial model creation
path resolves `auto` to the datamodule feature dimension, but the checkpoint
reload path in `scripts/training/train_feedforward_network.py` does not reuse
that resolved configuration.

The current campaign state file still reports `status: prepared`, while the
filesystem already contains the failed run queue state and campaign output:

- `config/training/queue/polished_dataset_stage1_smoke/failed/2026-06-22-11-55-01_001_trial.yaml`
- `output/training_campaigns/2026-06-22-11-55-01_polished_dataset_stage1_smoke_2026_06_21/`
- `output/training_runs/feedforward/2026-06-22-11-55-01__te_feedforward_trial/`

`doc/running/active_training_campaign.yaml` is a protected campaign file, so
the repair must update it only after explicit approval.

## Technical Approach

The repair should make dynamic input-size resolution a shared training
infrastructure behavior rather than a one-off feedforward fix.

The intended implementation is:

1. Add or expose a helper in `scripts/training/shared_training_infrastructure.py`
   that returns a model configuration copy with `input_size: auto` replaced by
   the effective datamodule input feature dimension.
2. Reuse that helper anywhere the training script creates a model from a
   training configuration after the datamodule has resolved the dataset schema.
3. Update `scripts/training/train_feedforward_network.py` so the best
   checkpoint reload path passes the resolved model configuration instead of
   the raw YAML model block.
4. Review other training entry points and model reload paths for the same
   pattern. If equivalent reload logic exists outside feedforward, apply the
   same helper rather than duplicating conversion logic.
5. Extend the Stage 1 package validation so a lightweight preflight catches
   `input_size: auto` reload failures before a real campaign spends a full
   training run on the first queue item.
6. Reconcile the Stage 1 persistent state after approval:
   - record that the June 22, 2026 local launch failed during best-checkpoint
     reload;
   - keep the failed output directories as diagnostic artifacts;
   - preserve the protected source queue and launcher files unless the actual
     fix requires changing validation behavior.

This does not change the polished dataset schema, the campaign queue contents,
or the model architecture definitions. It only ensures that the resolved
four-feature input dimension is used consistently during model creation and
checkpoint reload.

## Involved Components

- `scripts/training/shared_training_infrastructure.py`
  - owns dataset-schema-aware model creation and should own the reusable
    `input_size: auto` resolution helper.
- `scripts/training/train_feedforward_network.py`
  - currently reloads the best checkpoint with the raw model config and is the
    observed failure path.
- `scripts/models/model_factory.py`
  - expects concrete integer `input_size` values and should continue receiving
    resolved configurations from training infrastructure.
- `scripts/campaigns/cross_wave/validate_polished_dataset_stage1_smoke_package.py`
  - should be extended or supplemented so the Stage 1 preflight covers the
    checkpoint-reload contract.
- `doc/running/active_training_campaign.yaml`
  - protected campaign state; needs an approved update because the prepared
    campaign has now been launched and failed.
- `config/training/queue/polished_dataset_stage1_smoke/`
  - contains the failed queue item and the remaining pending Stage 1 queue
    items from the local launch.
- `output/training_campaigns/2026-06-22-11-55-01_polished_dataset_stage1_smoke_2026_06_21/`
  - contains the execution report and terminal log proving the reload failure.
- `output/training_runs/feedforward/2026-06-22-11-55-01__te_feedforward_trial/`
  - contains the partial run artifacts and checkpoints from the failed first
    Stage 1 run.

## Implementation Steps

1. Inspect the current dirty tree and preserve the failed-run artifacts without
   deleting or overwriting them.
2. Implement a shared resolved-model-configuration helper in
   `shared_training_infrastructure.py`.
3. Update the feedforward best-checkpoint reload path to use the resolved
   configuration.
4. Search for equivalent `create_model(...)` reload calls that pass raw
   `training_config["model"]` and apply the same helper if needed.
5. Update the Stage 1 validator or validation routine to include an explicit
   reload construction check for `input_size: auto`.
6. Run focused verification:
   - Python compile checks for touched Python files;
   - a minimal model-construction check for polished `input_feature_dim = 4`;
   - the Stage 1 preflight command;
   - the Stage 1 one-batch validation command if the validation runtime remains
     acceptable.
7. Update `doc/running/active_training_campaign.yaml` only after approval, so
   the persistent campaign state reflects the June 22 failed launch and the
   repair/rerun path.
8. Report the exact safe rerun command. The previous failed campaign output
   should remain as evidence and the rerun should produce a new timestamped
   campaign output directory.
