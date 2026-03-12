# Project Instructions

## Documentation

- Use English as the primary project language for file names, identifiers, instructions, comments, and technical documentation.
- Use the `context7` MCP server before implementing or recommending library-specific code for Next.js, React, PyTorch, PyTorch Lightning, NumPy, SciPy, scikit-learn, or adjacent ML tooling.
- Prefer Context7 documentation over memory when API details, configuration keys, or version-specific behavior may have changed.
- If Context7 is unavailable, state that explicitly and fall back to local code inspection plus primary official documentation.
- Always keep the documents in `reference/` or their summaries in `doc/` in scope before making design or implementation choices.
- Before implementing any feature, create a technical project document in `doc/technical/` using the filename format `YYYY-MM-DD-HH-mm-SS-feature_name.md`.
- Each new technical project document must contain the sections `Overview`, `Technical Approach`, `Involved Components`, and `Implementation Steps`.
- Every new technical project document must also be referenced from the main project document in `README.md`.
- Before executing any training campaign or training-related experiment, create a preliminary planning report in `doc/reports/` that explains the relevant parameters, their meanings and effects, and the candidate configuration table to be tested. Use `doc/reports/2026-03-12-training_configuration_analysis_report.md` as the reference style and depth.
- Follow this mandatory execution sequence for every user-requested repository change:
  1. Create the technical project document first.
  2. If the request includes training execution, create the preliminary planning report in `doc/reports/` before asking for approval.
  3. Wait for the user's explicit approval.
  4. Execute the approved modifications.
  5. If the approved work includes training execution, create a detailed post-training results report in `doc/reports/` that includes metrics tables, written interpretation, the best-performing configuration, and proposed future improvements.
  6. If the approved work adds or changes user-facing functionality, update `doc/guide/project_usage_guide.md` in detail before the final commit.
  7. If the approved work introduces a new third-party library, add it to `requirements.txt` and update every relevant setup or usage reference before the final commit.
  8. Create a Git commit immediately after the modifications are completed.
- Do not write or modify implementation code until the user has explicitly approved the technical document for that feature.
- Do not execute any training campaign until both the technical document and the preliminary training-planning report have been created and explicitly approved by the user.
- Before the final commit, update `doc/guide/project_usage_guide.md` whenever the approved work adds or changes runnable functionality such as training scripts, model architectures, inference/export flows, dataset-processing capabilities, or usage/configuration workflows.
- Before the final commit, whenever the approved work introduces a new third-party dependency, update `requirements.txt` and any relevant installation or usage documentation so the environment remains reproducible.
- Every required Git commit must use a title aligned with the repository's existing commit style and a body that accurately summarizes all relevant modifications.

## Domain Notes

- Treat rotational transmission error as the main accuracy indicator of the RV reducer and keep the separation clear between analytical modeling and ML-based compensation.
- Preserve the test-rig operating variables used throughout the reference material: input speed, applied torque, oil temperature, encoder zeroing, and `DataValid` windows for TE extraction.
- When implementing compensation logic, assume the practical deployment target is TwinCAT/PLC-friendly execution with explicit, inspectable intermediate quantities.

## Coding Style

- Mirror the style used in `blind_handover_controller`, with the same conventions also reinforced by `mediapipe_gesture_recognition` and `multimodal_fusion`.
- Treat the `blind_handover_controller` style as a strict default, not a loose inspiration.
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
