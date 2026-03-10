# Project Programming Style Guide

## Reference Sources

- `reference/codes/blind_handover_controller-master.zip`
- `reference/codes/mediapipe_gesture_recognition-master.zip`
- `reference/codes/multimodal_fusion-master.zip`

The main style baseline is `blind_handover_controller`, while the other two repositories reinforce the same naming, comment, structure, and implementation patterns.

## Naming

### Variables

- Prefer explicit, domain-oriented names.
- Representative examples:
  - `trajectory_execution_received`
  - `train_dataloader`
  - `human_radius`
  - `admittance_weight`
  - `joint_states`
  - `process_dataset`

### Constants

- Use full uppercase for module-level constants and flags.
- Examples:
  - `PACKAGE_PATH`
  - `DEVICE`
  - `MODEL_TYPE`
  - `GRIPPER_OPEN`
  - `DYNAMIC_PLANNER`

### Classes

- Use `PascalCase` in most cases.
- Preserve mixed robotics naming when it improves semantic clarity.
- Examples:
  - `TrainingNetwork`
  - `AdmittanceController`
  - `UR_RTDE_Move`
  - `UR_Toolbox`
  - `Handover_Controller`

### Functions And Methods

- Use `snake_case` for general utilities and helper functions.
- For ROS callbacks or node-facing methods, preserve the mixed naming convention already present in the reference repositories.
- Examples:
  - `train_network`
  - `get_model_name`
  - `save_hyperparameters`
  - `jointStatesCallback`
  - `FTSensorCallback`

## Comments

### Comment Style

- Frequent, short, and operational.
- Written in title case.
- Used to structure the flow more than to explain obvious syntax.

### Preferred Patterns

- `# Import ROS Messages`
- `# Initialize Admittance Controller`
- `# Compute Cartesian Velocity`
- `# Save Model`
- `# Move to Home | Error -> Return`

### Practical Rules

- Capitalize the main words.
- Place comments before distinct logical blocks.
- It is acceptable to use `->`, parentheses, or technical acronyms when they improve readability.

## Docstrings

- Keep them short, one line, in title case.
- They usually describe the class or function directly, without extra prose.

Correct examples:

- `""" Handover Controller Class """`
- `""" Compute Loss """`
- `""" Cartesian Goal Callback """`

## Code Structure

- Prefer explicit and progressive code.
- Break the reasoning into well-named intermediate blocks.
- Avoid overly compact abstractions when they reduce readability.
- Separate logical groups with comments.

## Imports

- Organize imports in grouped blocks.
- Add short heading comments above important import groups.

Typical pattern:

```python
from termcolor import colored

# Import PyTorch Lightning Functions
from pytorch_lightning.callbacks import EarlyStopping

# Import Processed Dataset and DataLoader
from process_dataset import ProcessDataset
```

## Checks And Validation

- Use explicit assertions with detailed messages.
- Make assumptions about data type and shape visible.

Correct tone example:

```python
assert len(joint_positions) == 6, f"Joint Positions Length must be 6 | {len(joint_positions)} given"
```

## Type Hints

- Use type hints when they clarify tensors, arrays, ROS messages, return tuples, and dataloaders.
- They do not need to be forced everywhere, but they are part of the technical tone of the reference code.

## Logging And Debug

- Use direct, concrete messages, often through `print` or ROS loggers.
- If useful, use colorized output for training, debugging, or controller state.
- Avoid generic or overly narrative logging text.

## Rules To Apply In This Repository

- Every new file should use explicit and readable naming.
- Every non-trivial function should be split into blocks with title-case comments.
- Configurations and constants should remain semantically transparent.
- ML code should remain understandable from an engineering perspective and compatible with future export or deployment.
- When in doubt, follow the pattern used in `blind_handover_controller`.
