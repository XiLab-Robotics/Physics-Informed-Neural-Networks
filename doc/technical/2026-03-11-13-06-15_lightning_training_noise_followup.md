# Lightning Training Noise Follow-Up

## Overview

The current feedforward training entry point is cleaner than before, but two Lightning-originated messages still reduce terminal readability during normal runs:

- the startup `litlogger` suggestion printed by Lightning when the trainer uses a logger other than `LitLogger`;
- the `Sanity Checking: isinstance(treespec, LeafSpec) is deprecated...` warning emitted during the validation sanity pass.

The user requested a follow-up cleanup focused on these residual messages, while keeping the current training workflow, TensorBoard logging, and validation behavior intact.

Local inspection of the installed `lightning` package in `standard_ml_codex_env` shows:

- the `litlogger` message is emitted through `rank_zero_info(...)` inside `lightning.pytorch.trainer.connectors.logger_connector._LoggerConnector.configure_logger`;
- the `_pytree` message surfaces from `lightning.pytorch.utilities._pytree` and is triggered by the `torch.utils._pytree.LeafSpec` deprecation path, while the current repository filter is configured for `DeprecationWarning`, so it does not match the real warning category.

## Technical Approach

The cleanup should stay narrow and avoid changing the numerical training logic.

The planned implementation is:

1. keep the explicit `TensorBoardLogger` configuration already used by the project;
2. suppress only Lightning's startup informational tip by raising the log threshold of the Lightning rank-zero logger from `INFO` to `WARNING` inside the training entry point;
3. preserve warnings and errors from Lightning, so only low-signal informational tips disappear;
4. replace the current `_pytree` warning filter with a filter that matches the real warning category (`FutureWarning`) and the exact warning source path;
5. keep the sanity validation pass enabled unless verification shows the warning still bypasses the corrected filter.

This approach is preferred over disabling the logger entirely or turning off sanity validation because:

- TensorBoard artifact generation should remain unchanged;
- validation smoke-checking is still useful for catching dataset or metric regressions early;
- the current issue appears to be output hygiene, not a functional training failure.

## Involved Components

- `training/train_feedforward_network.py`
  Main training entry point that currently imports Lightning, installs the warning filter, creates the logger, and constructs the trainer.
- `README.md`
  Main project document that must reference this new technical document.
- `doc/README.md`
  Internal documentation index that should stay aligned with the current technical-document set.

## Implementation Steps

1. Update the warning-filter block in `training/train_feedforward_network.py` so the `_pytree` deprecation message is filtered with the correct warning category and module scope.
2. Add a small Lightning logging helper in the training entry point to suppress only rank-zero `INFO` messages that generate the `litlogger` tip.
3. Keep the existing `TensorBoardLogger`, progress bar, checkpointing, and sanity validation configuration unchanged unless verification proves an additional adjustment is necessary.
4. Re-run a lightweight training command in `standard_ml_codex_env` to confirm:
   - the `litlogger` tip no longer appears;
   - the `_pytree` warning no longer appears during sanity checking;
   - the current terminal summaries, progress bar, checkpoints, and TensorBoard logs still work.
5. Update `doc/guide/project_usage_guide.md` only if the approved implementation changes any visible training behavior beyond warning cleanup.
6. Create the required Git commit immediately after the approved modifications and verification are complete.
