# Mediapipe Gesture Recognition Reference

## Role In This Project

`mediapipe_gesture_recognition` is a supporting reference that reinforces the same explicit coding style while adding practical patterns for Hydra configuration, PyTorch Lightning training, and utility-driven project setup.

Representative files inspected for this note:

- `reference/codes/mediapipe_gesture_recognition/scripts/training_node.py`
- `reference/codes/mediapipe_gesture_recognition/scripts/recognition_node.py`
- `reference/codes/mediapipe_gesture_recognition/scripts/stream_node.py`
- `reference/codes/mediapipe_gesture_recognition/scripts/utils/lightning_utilities.py`
- `reference/codes/mediapipe_gesture_recognition/scripts/utils/utils.py`
- `reference/codes/mediapipe_gesture_recognition/README.md`

## Main Style Signals

- The repository keeps the same preference for executable scripts, short docstrings, and title-case section comments.
- Imports are grouped by role, with clear boundaries between standard library, PyTorch, Lightning, utilities, and local configuration.
- Helper functions for environment setup are pulled into utilities early in the script so the main training flow stays linear.

## Configuration And Environment Patterns

- `training_node.py` uses Hydra as the top-level configuration entry point.
- Configuration preparation is made explicit through utility calls such as path normalization and environment-variable setup before the training logic begins.
- This is a useful reference for future StandardML training scripts if the project later adopts Hydra-based experiment configuration.

## PyTorch Lightning Patterns

- The training script keeps the trainer definition readable by grouping settings in commented blocks:
  - devices and accelerator;
  - epoch and logging parameters;
  - callbacks;
  - profiler;
  - logger;
  - developer mode.
- Lifecycle callbacks in `scripts/utils/lightning_utilities.py` follow the same simple pattern already seen in `blind_handover_controller`: minimal logic, explicit names, direct prints.
- The project explicitly controls optional features such as `torch.compile`, profiler enablement, and fast-dev-run flags through configuration rather than hidden defaults.

## Dataset And Model Style

- Dataset classes convert incoming arrays to tensors immediately and expose shape helper methods.
- The `NeuralClassifier` module keeps model construction visible in the constructor instead of burying it behind factories.
- The repository favors readable, manually assembled architectures such as `LSTM` plus explicit `MLP` creation helpers.
- Logging of input shape, output shape, optimizer, and learning rate happens near model construction, which makes experiments easier to inspect.

## Reusable Engineering Rules

- Keep configuration activation explicit and near the top of the script.
- Prefer small training utilities that keep the main file readable without hiding the execution flow.
- If optional acceleration features are added in this repository, gate them with transparent config flags and direct status output.
- Reuse this repository mainly for ML-script organization and config-handling patterns, not as the primary naming baseline.
