# Project Instructions

## Documentation

- Use the `context7` MCP server before implementing or recommending library-specific code for Next.js, React, PyTorch, PyTorch Lightning, NumPy, SciPy, scikit-learn, or adjacent ML tooling.
- Prefer Context7 documentation over memory when API details, configuration keys, or version-specific behavior may have changed.
- If Context7 is unavailable, state that explicitly and fall back to local code inspection plus primary official documentation.

## Domain Notes

- Treat rotational transmission error as the main accuracy indicator of the RV reducer and keep the separation clear between analytical modeling and ML-based compensation.
- Preserve the test-rig operating variables used throughout the reference material: input speed, applied torque, oil temperature, encoder zeroing, and `DataValid` windows for TE extraction.
- When implementing compensation logic, assume the practical deployment target is TwinCAT/PLC-friendly execution with explicit, inspectable intermediate quantities.

## Coding Style

- Mirror the style used in `blind_handover_controller`, with the same conventions also reinforced by `mediapipe_gesture_recognition` and `multimodal_fusion`.
- Prefer verbose, domain-explicit names such as `train_dataloader`, `trajectory_execution_received`, `human_radius`, `admittance_weight`, and `joint_states`.
- Keep module-level constants and configuration flags in full uppercase, for example `PACKAGE_PATH`, `DEVICE`, `MODEL_TYPE`, `GRIPPER_OPEN`.
- Use `PascalCase` for most classes, but preserve the existing mixed robotics naming when it improves domain clarity, such as `Handover_Controller`, `UR_RTDE_Move`, `UR_Toolbox`, and callback suffixes like `jointStatesCallback`.
- Prefer `snake_case` for utility functions and general methods, and keep ROS-style callback names in the existing mixed form when they match the surrounding code.
- Group imports in blocks with sparse spacing and short heading comments such as `# Import ROS Messages` or `# Import PyTorch Lightning Utilities`.
- Use short docstrings in title case, usually one line, for classes and methods.
- Add frequent section comments before logical blocks. The preferred pattern is imperative or descriptive title case, for example `# Initialize Admittance Controller`, `# Compute Cartesian Velocity`, `# Save Model`.
- Keep comments capitalized and high-signal. It is acceptable to use arrows or quick clarifiers like `->`, parentheses, or acronym-heavy labels when that improves readability.
- Prefer explicit staged code over compact abstraction. Compute intermediate variables step by step and label each stage with comments.
- Keep small conditionals inline when they are obvious in context, for example `if not self.use_admittance: self.ft_sensor_data = Wrench()`.
- Use informative assertions and explicit runtime checks with descriptive messages.
- Use type hints where they are already natural in the surrounding file, especially for tensors, arrays, ROS messages, loaders, and return values.
- Favor aligned or visually structured assignments when several related values are initialized together.
- Preserve the existing print/debug style when needed: explicit status messages, sometimes colorized, with direct wording rather than generic logging prose.
