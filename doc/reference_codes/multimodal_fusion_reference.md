# Multimodal Fusion Reference

## Role In This Project

`multimodal_fusion` is a supporting reference for compact ROS application structure, explicit command encoding, straightforward dataset generation, and simple PyTorch Lightning classification baselines.

Representative files inspected for this note:

- `reference/codes/multimodal_fusion/script/fusion.py`
- `reference/codes/multimodal_fusion/script/network/neural_classifier_training.py`
- `reference/codes/multimodal_fusion/script/network/dataset_creation.py`
- `reference/codes/multimodal_fusion/script/utils/utils.py`
- `reference/codes/multimodal_fusion/README.md`

## Main Style Signals

- The code stays procedural and explicit, especially in small-to-medium scripts.
- Domain mappings are often written directly into the file as large labeled comment blocks instead of being hidden behind external metadata.
- Class and function boundaries remain simple: one script often owns one main responsibility and the control flow is easy to follow top to bottom.

## Dataset And Labeling Patterns

- `dataset_creation.py` is a good reference for deterministic synthetic-dataset creation logic.
- Scenario labels, gesture identifiers, and voice identifiers are documented directly inside the script before the implementation logic.
- The implementation favors explicit `if/elif` mappings instead of compressed lookup tables when readability for the operator is more important than compactness.

## PyTorch Lightning Patterns

- `neural_classifier_training.py` shows a minimal Lightning baseline:
  - top-level hyperparameters near the file header;
  - dataset class in the same file for simple projects;
  - explicit `prepareDataloaders(...)` helper;
  - compact `LightningModule` with `forward`, `configure_optimizers`, `training_step`, `validation_step`, and `test_step`;
  - direct save of the trained weights at the end of the script.
- This is useful as a lower-complexity counterpart to the more structured training flow found in `blind_handover_controller`.

## ROS And Runtime Patterns

- `fusion.py` keeps the entire multimodal decision flow readable through class-level flags, explicit callback methods, and direct state resets.
- The repository uses direct assertions to guard semantic assumptions such as valid gestures or voice commands.
- The logging tone remains short and concrete, with ROS loggers used for state transitions such as command reception and recognition start.

## Reusable Engineering Rules

- For small support scripts in this repository, prefer directness over premature abstraction.
- Keep domain enumerations close to the logic that consumes them when they are central to operator understanding.
- Use this repository as a reference for simple ML utilities, synthetic-dataset scripts, and readable event-driven control code.
- When a design choice conflicts with `blind_handover_controller`, prefer the `blind_handover_controller` pattern.
