# Project Instructions

## Documentation

- Use English as the primary project language for file names, identifiers, instructions, comments, and technical documentation.
- Use the `context7` MCP server before implementing or recommending library-specific code for Next.js, React, PyTorch, PyTorch Lightning, NumPy, SciPy, scikit-learn, or adjacent ML tooling.
- Prefer Context7 documentation over memory when API details, configuration keys, or version-specific behavior may have changed.
- If Context7 is unavailable, state that explicitly and fall back to local code inspection plus primary official documentation.
- Always keep the documents in `reference/` or their summaries in `doc/` in scope before making design or implementation choices.
- Before implementing any feature, create a technical project document inside the day-based folder `doc/technical/YYYY-MM-DD/` using the filename format `YYYY-MM-DD-HH-mm-SS-feature_name.md`.
- Before creating a new technical project document, read the real current system date and time from the local machine and use that exact timestamp in the filename. Do not infer or estimate the timestamp from conversation context.
- Each new technical project document must contain the sections `Overview`, `Technical Approach`, `Involved Components`, and `Implementation Steps`.
- Every new technical project document must also be referenced from the main project document in `README.md`.
- Whenever a new model family, model variant, or materially new model-specific training workflow is introduced, create a dedicated explanatory report that helps the reader understand the model before reading the code.
- The explanatory report for a new model must include:
  - an accurate model description;
  - the operating principle;
  - a conceptual map or schematic explanation of the network or algorithm structure;
  - the main advantages and disadvantages in the project context;
  - a technical section explaining the implemented Python files, classes, and functions for the model.
- When the user requests conceptual maps, schematic explanations, or architecture framing for a model, the explanatory report must also include generated visual material such as diagrams or schematic images rather than remaining text-only.
- These visual assets must be integrated into both the Markdown report and the final PDF deliverable, and they should be stored in a consistent, discoverable report-local location.
- When model-report diagrams are generated, they must be checked after generation to ensure labels stay inside their boxes, spacing remains balanced, and the real visual output does not contain obvious overflow or crowding defects.
- When a new learning guide is created under `doc/reports/analysis/learning_guides/`, create a PDF companion for that guide in the same report-local folder.
- For learning guides, do not generate or finalize the PDF companion until the user has explicitly approved the generated guide images or diagrams.
- If the user identifies layout defects in learning-guide images, treat the learning-guide PDF task as still open, correct the figures first, obtain image approval, and only then export and validate the PDF.
- After a learning-guide Markdown document and its approved PDF companion are complete, prepare a report-local `video_guide_package/` for that guide when the user explicitly approves the video-guide preparation phase.
- Each approved `video_guide_package/` for a learning guide must contain at least:
  - `video_guide_source_brief.md`;
  - `video_guide_terminology_sheet.md`;
  - `video_guide_narration_outline.md`;
  - `video_guide_figure_reference.md`;
  - `video_guide_fact_boundary_notes.md` when the guide contains roadmap, implementation-status, or planned-model content.
- Build `video_guide_package/` documents as repository-owned `NotebookLM` sources rather than generic prompts. They must preserve terminology, chapter order, scope boundaries, and the distinction between implemented versus planned repository capabilities.
- Do not generate or finalize a `NotebookLM` video guide immediately after the package is prepared. Stop after the source package is ready, report completion, and wait for the user's explicit approval before creating or finalizing the actual video-guide generation step.
- For explanatory model reports, prefer providing both:
  - a conceptual diagram that explains the model logic;
  - an architecture-style diagram that explains the concrete network or computational structure.
- If the new model also requires a new training file or a materially new training workflow, the same explanatory report must additionally include:
  - a high-level explanation of how the training workflow operates;
  - a detailed explanation of the implemented Python training functions and code structure.
- Before executing any training campaign or training-related experiment, create a preliminary planning report in `doc/reports/campaign_plans/` that explains the relevant parameters, their meanings and effects, and the candidate configuration table to be tested. Use `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md` as the reference style and depth.
- For every approved training campaign preparation, automatically generate the campaign YAML files and provide the exact terminal command needed to launch the campaign. Do not treat campaign preparation as complete if only the planning report exists.
- Store future training artifacts by artifact type instead of mixing them in one family-flat root:
  - `output/training_runs/<model_family>/<run_instance_id>/`
  - `output/validation_checks/<model_family>/<run_instance_id>/`
  - `output/smoke_tests/<model_family>/<run_instance_id>/`
  - `output/training_campaigns/<campaign_id>/`
  - `output/registries/families/<model_family>/`
  - `output/registries/program/`
- Treat the logical experiment `run_name` and the physical artifact `run_instance_id` as different concepts. New training runs must write into immutable timestamped `run_instance_id` folders rather than reusing `output/<family>/<run_name>/`.
- Do not introduce new training artifacts under legacy flat family roots such as `output/feedforward_network/<run_name>/` except when explicitly maintaining backward-compatible historical references.
- Track the current prepared or active training campaign persistently in `doc/running/active_training_campaign.yaml`.
- Treat the files listed in `doc/running/active_training_campaign.yaml` as protected campaign files while the campaign is prepared or active.
- If a future user request would modify a protected campaign file while the campaign is prepared or active, issue a `CRITICAL WARNING` and wait for explicit user approval before making the edit.
- When the user says that the campaign has started, update `doc/running/active_training_campaign.yaml` accordingly before doing unrelated work that could affect the campaign baseline.
- When the user says that the campaign is finished, inspect the stored campaign state and gather the campaign artifacts needed for the final post-training results report, but still wait for explicit approval before writing that report.
- When the user says that the campaign is cancelled, inspect the stored campaign state and evaluate completed, failed, running, and pending results before making any queue or artifact cleanup decision.
- Every completed training campaign must expose its winner explicitly inside the campaign output folder through:
  - `campaign_leaderboard.yaml`
  - `campaign_best_run.yaml`
  - `campaign_best_run.md`
- Keep family-level and program-level best-result registries updated after training or campaign completion:
  - `output/registries/families/<model_family>/leaderboard.yaml`
  - `output/registries/families/<model_family>/latest_family_best.yaml`
  - `output/registries/program/current_best_solution.yaml`
- Best-result selection must remain explicit and inspectable. Serialize the ranking policy together with the winning entry instead of relying on manual folder inspection.
- Every final campaign-results report must be delivered both as Markdown and as a PDF export, and the real exported PDF must be validated before the task is considered complete.
- Treat `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf` as the visual golden standard for future styled analytical PDFs in this repository.
- Future styled analytical PDFs must preserve the same restrained professional direction: white page background, restrained blue accents, rounded section cards, readable A4-safe margins, and no clipped borders or overcrowded blocks.
- When comparison matrices are split across multiple tables, repeat the key row anchor such as `Config` in each table and prefer centered comparison-friendly alignment unless a different alignment clearly improves readability.
- After regenerating any styled PDF, validate the real exported PDF output and not only the HTML source. Explicitly check for clipped borders, wrapped headers, broken table fit, crushed identifier columns, oversized numeric columns, and right-edge pressure before closing the task.
- If the PDF-validation evidence is inconclusive or does not prove that the real exported tables are well balanced, treat the PDF task as still open and continue until the layout issue is either fixed or clearly escalated to the user.
- When a table header is too long for its current width, keep it inside its own cell by wrapping it cleanly inside that cell. Never allow a header label to visually spill into the neighboring column.
- When identifier-style values such as `Config` names wrap, prefer semantically meaningful breakpoints such as underscore-delimited token groups. Avoid arbitrary one- or two-letter trailing fragments.
- When balancing table columns, start from broadly similar widths, widen only the columns that clearly need more room, and redistribute the reduction across the others without over-compressing them. Do not allow text to sit too close to the borders or escape its own cell.
- Vertically center table-cell content by default. Keep the existing horizontal alignment choices, but do not leave mixed single-line and multi-line cells visually top-aligned.
- During styled PDF validation, explicitly check that no major section starts at the bottom of a page only to continue immediately on the next page. If that happens and the section can reasonably fit on the next page, move the section start to the next page instead.
- Follow this mandatory execution sequence for every user-requested repository change:
  1. Create the technical project document first.
  2. If the request includes training execution, create the preliminary planning report in `doc/reports/campaign_plans/` before asking for approval.
  3. Wait for the user's explicit approval.
  4. If the approved work is a training campaign, generate the campaign YAML files, store the campaign state, and provide the exact launch command.
  5. Execute the approved modifications.
  6. If the approved work includes training execution, create a detailed post-training results report in `doc/reports/campaign_results/` that includes metrics tables, written interpretation, the best-performing configuration, proposed future improvements, and a validated PDF export.
  7. If the approved work adds or changes user-facing functionality, update `doc/guide/project_usage_guide.md` in detail before the final commit.
  8. If the approved work introduces a new third-party library, add it to `requirements.txt` and update every relevant setup or usage reference before the final commit.
  9. Tell the user the work is complete and explicitly ask for approval to create the Git commit.
  10. Create the Git commit only after the user explicitly approves it.
- Do not write or modify implementation code until the user has explicitly approved the technical document for that feature.
- Do not execute any training campaign until both the technical document and the preliminary training-planning report in `doc/reports/campaign_plans/` have been created and explicitly approved by the user.
- Do not treat a styled PDF export as complete until the exported PDF has been checked against the project golden standard for layout discipline and readability.
- Do not create a Git commit immediately after finishing the work. Always stop, report completion, and wait for explicit user approval before committing.
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
- Apply the same coding-style discipline to utility scripts, tooling helpers, dataset-processing scripts, and report exporters, not only to training or model code.
- Prefer verbose, domain-explicit names such as `train_dataloader`, `trajectory_execution_received`, `human_radius`, `admittance_weight`, and `joint_states`.
- Keep module-level constants and configuration flags in full uppercase, for example `PACKAGE_PATH`, `DEVICE`, `MODEL_TYPE`, `GRIPPER_OPEN`.
- Use `PascalCase` for most classes, but preserve the existing mixed robotics naming when it improves domain clarity, such as `Handover_Controller`, `UR_RTDE_Move`, `UR_Toolbox`, and callback suffixes like `jointStatesCallback`.
- Prefer `snake_case` for utility functions and general methods, and keep ROS-style callback names in the existing mixed form when they match the surrounding code.
- Group imports in blocks with sparse spacing and short heading comments such as `# Import ROS Messages` or `# Import PyTorch Lightning Utilities`.
- Use short docstrings in title case, usually one line, for classes and methods.
- Add frequent section comments before logical blocks. The preferred pattern is imperative or descriptive title case, for example `# Initialize Admittance Controller`, `# Compute Cartesian Velocity`, `# Save Model`.
- Do not rely on docstrings alone inside non-trivial functions. Use section comments frequently enough that the control flow stays visually scannable while reading the function body.
- Keep comments capitalized and high-signal. It is acceptable to use arrows or quick clarifiers like `->`, parentheses, or acronym-heavy labels when that improves readability.
- Keep section comments short. Prefer compact labels such as `# Resolve Browser Path` or `# Flush Pending Paragraph` over sentence-length explanations that restate the code line by line.
- Prefer explicit staged code over compact abstraction. Compute intermediate variables step by step and label each stage with comments.
- Keep small conditionals inline when they are obvious in context, for example `if not self.use_admittance: self.ft_sensor_data = Wrench()`.
- Compact grouped imports, one-line helper signatures, and short inline validations are preferred when they remain easy to scan.
- When a user performs a manual refactor that sharpens the local style of a file, treat that version as the immediate reference for future edits to similar files.
- Use informative assertions and explicit runtime checks with descriptive messages.
- Use type hints where they are already natural in the surrounding file, especially for tensors, arrays, ROS messages, loaders, and return values.
- Favor aligned or visually structured assignments when several related values are initialized together.
- Preserve the existing print/debug style when needed: explicit status messages, sometimes colorized, with direct wording rather than generic logging prose.
