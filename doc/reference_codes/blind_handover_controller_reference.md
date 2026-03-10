# Blind Handover Controller Reference

## Role In This Project

`blind_handover_controller` is the primary programming-style baseline for this repository. It is the strongest reference for naming, section comments, runtime checks, ROS-node organization, utility structure, and PyTorch Lightning training flow.

Representative files inspected for this note:

- `reference/codes/blind_handover_controller/scripts/handover_controller.py`
- `reference/codes/blind_handover_controller/scripts/admittance.py`
- `reference/codes/blind_handover_controller/scripts/ft_load_network/train_network.py`
- `reference/codes/blind_handover_controller/scripts/ft_load_network/process_dataset.py`
- `reference/codes/blind_handover_controller/scripts/ft_load_network/pl_utils.py`
- `reference/codes/blind_handover_controller/scripts/utils/move_robot.py`
- `reference/codes/blind_handover_controller/scripts/utils/robot_toolbox.py`

## Structural Patterns

- Scripts are usually executable entry points with imports first, then helper functions, then the main class, then an `if __name__ == '__main__':` block.
- ROS-facing modules keep the main control logic inside one explicit node/controller class instead of splitting simple flows into many abstractions.
- Initialization blocks are long but readable because they are segmented by title-case comments.
- Class-level state is often declared near the class header to make controller status immediately visible.

## Naming Conventions

- Variable names are domain-explicit and rarely abbreviated without context.
- Examples worth mirroring:
  - `trajectory_execution_received`
  - `train_dataloader`
  - `ft_sensor_data`
  - `human_radius`
  - `admittance_weight`
  - `joint_states`
- Module-level constants use full uppercase and usually remain close to the top of the file.
- Class names are mostly `PascalCase`, but robotics-specific mixed naming is preserved when it improves clarity:
  - `Handover_Controller`
  - `UR_RTDE_Move`
  - `UR_Toolbox`
- Callback names preserve ROS-style mixed naming:
  - `jointStatesCallback`
  - `FTSensorCallback`
  - `cartesianGoalCallback`

## Comment And Docstring Style

- Comments are frequent, short, and operational.
- The dominant pattern is title case before each logical block:
  - `# Declare Parameters`
  - `# Initialize Admittance Controller`
  - `# Get Joint Goal from Cartesian Goal`
  - `# Save Hyperparameters in Config File`
- Comments are used as flow markers, not as general prose.
- Docstrings are short, usually one line, and also written in title case:
  - `""" Handover Controller Class """`
  - `""" Train LSTM Network """`
  - `""" Apply Oversampling to the Dataset """`

## Import Organization

- Imports are grouped in blocks with sparse spacing.
- Important groups are introduced by short headers such as:
  - `# Import ROS2 Libraries`
  - `# Import ROS Messages, Services, Actions`
  - `# Import PyTorch Lightning Functions`
  - `# Import Processed Dataset and DataLoader`
- This pattern should be retained in the future neural-network implementation because it keeps large robotics and ML files readable.

## Runtime And Validation Style

- The code prefers explicit assertions and direct runtime checks over silent assumptions.
- Representative patterns:
  - validating sequence length and stride before dataset creation;
  - validating balance strategies against an allowed list;
  - raising `ValueError` on invalid model types.
- Debug and status output uses direct `print(...)` messages, often colorized with `termcolor`.
- The messaging style is concrete and engineering-oriented, for example model settings, parameter dumps, and lifecycle start/end notifications.

## PyTorch And PyTorch Lightning Patterns

- The training flow is explicit and staged:
  - process dataset;
  - build dataloaders;
  - compute derived hyperparameters;
  - instantiate model;
  - configure trainer;
  - fit, test, validate;
  - save model and hyperparameters.
- Utility helpers in `pl_utils.py` centralize repeated training-side operations such as naming, serialization, and start/end callbacks.
- Model, config, and dataset names are generated from meaningful hyperparameters, which is useful for experiment traceability.
- Dataset processing is engineered as a first-class component, not as an inline helper inside the training script.

## Reusable Engineering Rules

- Prefer progressive code with visible intermediate variables over compact chained logic.
- Keep configuration names semantically transparent and derived from the actual experiment setup.
- Place comments before blocks that change state, perform conversions, or call external systems.
- Make assumptions inspectable through assertions, explicit branches, and printed configuration summaries.
- When designing the RV-reducer neural-network stack, this repository should remain the default reference for file structure, naming tone, and training orchestration.
