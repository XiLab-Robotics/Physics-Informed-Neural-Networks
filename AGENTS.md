# Project Instructions

## Documentation

- Use English as the primary project language for file names, identifiers, instructions, comments, and technical documentation.
- Use the `context7` MCP server before implementing or recommending library-specific code for Next.js, React, PyTorch, PyTorch Lightning, NumPy, SciPy, scikit-learn, or adjacent ML tooling.
- Prefer Context7 documentation over memory when API details, configuration keys, or version-specific behavior may have changed.
- If Context7 is unavailable, state that explicitly and fall back to local code inspection plus primary official documentation.
- Always keep the documents in `reference/` or their summaries in `doc/` in scope before making design or implementation choices.
- Before implementing any feature, create a technical project document inside the month/day folder `doc/technical/YYYY-MM/YYYY-MM-DD/` using the filename format `YYYY-MM-DD-HH-mm-SS-feature_name.md`.
- Before creating a new technical project document, read the real current system date and time from the local machine and use that exact timestamp in the filename. Do not infer or estimate the timestamp from conversation context.
- Each new technical project document must contain the sections `Overview`, `Technical Approach`, `Involved Components`, and `Implementation Steps`.
- Repository-relevant Codex skills may be used automatically whenever the request clearly matches their documented purpose. Do not wait for a separate user instruction when the skill is the correct workflow tool for the task.
- Codex subagents must not be launched silently. When a subagent would be useful, declare the proposed subagent, the reason for using it, and the concrete delegated scope, then wait for explicit user approval before launching it.
- When a technical project document is expected to involve a subagent during implementation, state that explicitly in the technical document, including the planned subagent name, intended task boundary, and the fact that runtime launch still requires explicit user approval.
- Every new technical project document must also be referenced from a canonical documentation entry point under `doc/`, typically `doc/README.md` or a topic-local index inside `doc/`.
- Update `README.md` for a new technical project document only when that document changes the public-facing repository presentation, the main documentation entry points, or another README-level summary that belongs on the GitHub-facing landing page.
- Keep `doc/reports/` grouped first by report domain:
  - `analysis/`
  - `campaign_plans/`
  - `campaign_results/`
- Under `doc/reports/analysis/`, prefer readable title-based filenames for standalone canonical reports instead of timestamp-prefixed filenames when the topic is clearer than the creation timestamp and no larger package is needed.
- When one analysis topic has multiple companion artifacts or repeated releases, create a topic-root folder under `doc/reports/analysis/` and place each concrete bundle inside a dated subfolder such as `[2026-03-27]/`.
- Keep companion assets for a topic-local report bundle inside the same dated topic folder instead of creating a separate parallel `*_assets/` root.
- Keep `doc/reports/campaign_plans/` and `doc/reports/campaign_results/` on the existing timestamp-based filename convention because they represent distinct campaign execution instances.
- Treat bracketed date folders under `doc/reports/` such as `[2026-03-27]` as literal paths in tooling-sensitive contexts; for example, use `-LiteralPath` in PowerShell when needed.
- The repository standard for Git-tracked authored Markdown is zero warnings.
- Whenever a repository-owned Git-tracked Markdown document is created or modified, run Markdown warning checks on the touched Markdown scope before closing the task.
- Scope the mandatory per-task Markdown warning pass to the Markdown files created or modified by the task rather than forcing a full repository-wide cleanup every time.
- Treat the Markdown warning pass as incomplete until every warning in the touched Markdown scope has been analyzed and resolved.
- Do not close a task while a newly created or modified Git-tracked Markdown file still emits Markdown warnings.
- As part of that Markdown final pass, also check the file-ending blank-line state of the touched Markdown files so they do not end with an accidental doubled empty line.
- When the user asks for a repository-wide Markdown audit or asks whether the repository is warning-free, run the checks against the full Git-tracked Markdown set, not only the default documentation globs.
- Treat warning-free status claims as valid only after both the repository-owned structural checker and the broader Markdownlint pass succeed on the intended Git-tracked scope.
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
- When a new learning guide is created under `doc/guide/`, create a PDF companion for that guide in the same guide-local folder.
- For learning guides, do not generate or finalize the PDF companion until the user has explicitly approved the generated guide images or diagrams.
- If the user identifies layout defects in learning-guide images, treat the learning-guide PDF task as still open, correct the figures first, obtain image approval, and only then export and validate the PDF.
- After a learning-guide Markdown document and its approved PDF companion are complete, prepare two guide-local `NotebookLM` source-package tracks when the user explicitly approves the video-guide preparation phase:
  - `concept_video_package/`
  - `project_video_package/`
- Each approved `concept_video_package/` or `project_video_package/` must contain at least:
  - `video_source_brief.md`;
  - `video_terminology_sheet.md`;
  - `video_narration_outline.md`;
  - `video_figure_reference.md`;
  - `video_fact_boundary_notes.md` when the package contains roadmap, implementation-status, or planned-model boundaries that the narration must preserve.
- Each approved `concept_video_package/` must also contain `concept_video_scope_notes.md`.
- Each approved `project_video_package/` must also contain `project_video_scope_notes.md`.
- Build `concept_video_package/` and `project_video_package/` documents as repository-owned `NotebookLM` sources rather than generic prompts. They must preserve terminology, chapter order, scope boundaries, and the distinction between neutral topic explanation versus repository-specific explanation.
- The `concept_video_package/` track must stay neutral and explain what the model, method, or workflow is, how it works, how training and testing operate, and where it is used in general, without collapsing into repository-specific framing.
- The `project_video_package/` track must explain why the topic exists in this repository, what role it plays in the TE workflow, how it is implemented or positioned here, and what its project-local advantages and disadvantages are.
- For future approved guide-worthy topics, treat the default deliverable as a full bundle rather than only one guide file. Unless the user explicitly narrows the scope, prepare:
  - guide-local assets;
  - canonical guide Markdown;
  - guide-local PDF companion;
  - `concept_video_package/`;
  - `project_video_package/`;
  - `concept_video_package/notebooklm_concept_video_prompt.md`;
  - `project_video_package/notebooklm_project_video_prompt.md`.
- The two final `NotebookLM` prompt files must be repository-owned, ready to paste, and written in the structured style already established in this repository: explicit goal, explicit requirements, explicit terminology/fact-boundary compliance, and explicit output style.
- `notebooklm_concept_video_prompt.md` must request the neutral educational video for the topic.
- `notebooklm_project_video_prompt.md` must request the repository-specific educational video for the topic.
- Future imported `NotebookLM` exports must use filenames that explicitly declare guide name, track, and artifact type, for example `FeedForward Network - Concept Mind Map.png` or `FeedForward Network - Project Video Overview.mp4`, instead of generic names such as `Mind Map.png` or `Video Overview.mp4`.
- If a topic root already exists under `doc/guide/` but does not yet have the full canonical guide Markdown/PDF pair, a `NotebookLM` source package may still be prepared only when the user explicitly approves that exception. In that case, the package scope notes must record the missing canonical-guide status explicitly rather than hiding it.
- Do not generate or finalize a `NotebookLM` video guide immediately after the package is prepared. Stop after the source package is ready, report completion, and wait for the user's explicit approval before creating or finalizing the actual video-guide generation step.
- For explanatory model reports, prefer providing both:
  - a conceptual diagram that explains the model logic;
  - an architecture-style diagram that explains the concrete network or computational structure.
- If the new model also requires a new training file or a materially new training workflow, the same explanatory report must additionally include:
  - a high-level explanation of how the training workflow operates;
  - a detailed explanation of the implemented Python training functions and code structure.
- Before executing any training campaign or training-related experiment, create a preliminary planning report in `doc/reports/campaign_plans/` that explains the relevant parameters, their meanings and effects, and the candidate configuration table to be tested. Use `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md` as the reference style and depth.
- For every approved training campaign preparation, automatically generate the campaign YAML files, create a dedicated PowerShell launcher under `scripts/campaigns/`, create the matching launcher note under `doc/scripts/campaigns/`, and provide the exact terminal command needed to launch the campaign. Do not treat campaign preparation as complete if only the planning report exists.
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
  2. If subagent use is expected for the approved implementation, record that planned subagent usage explicitly in the technical project document before asking for approval.
  3. If the request includes training execution, create the preliminary planning report in `doc/reports/campaign_plans/` before asking for approval.
  4. Ask for explicit user approval of the technical document and, when applicable, explicit user approval of the proposed subagent usage before continuing.
  5. Wait for the user's explicit approval.
  6. If the approved work is a training campaign, generate the campaign YAML files, create the dedicated campaign launcher plus its documentation note, store the campaign state, and provide the exact launch command.
  7. Execute the approved modifications.
  8. If the approved work includes training execution, create a detailed post-training results report in `doc/reports/campaign_results/` that includes metrics tables, written interpretation, the best-performing configuration, proposed future improvements, and a validated PDF export.
  9. If the approved work changes the public-facing repository presentation, implemented-capability summary, quick-start flow, primary example commands, or main documentation entry points, update `README.md` before the final commit while keeping it concise and GitHub-facing.
  10. If the approved work adds or changes user-facing functionality, update `doc/guide/project_usage_guide.md` in detail before the final commit.
  11. If the approved work introduces a new third-party library, add it to `requirements.txt` and update every relevant setup or usage reference before the final commit.
  12. Before creating a GitHub-bound commit, check the files involved in the commit and stop immediately if any file exceeds `100 MB`, then explicitly warn the user because those files cannot be pushed to GitHub as regular repository objects.
  13. Tell the user the work is complete and explicitly ask for approval to create the Git commit.
  14. Create the Git commit only after the user explicitly approves it.
- Do not write or modify implementation code until the user has explicitly approved the technical document for that feature.
- Do not execute any training campaign until both the technical document and the preliminary training-planning report in `doc/reports/campaign_plans/` have been created and explicitly approved by the user.
- Do not treat a styled PDF export as complete until the exported PDF has been checked against the project golden standard for layout discipline and readability.
- Do not create a Git commit immediately after finishing the work. Always stop, report completion, and wait for explicit user approval before committing.
- Before creating a GitHub-bound commit, always check the commit's files for GitHub size-limit violations and stop with an explicit warning if any file exceeds `100 MB`.
- Before the final commit, update `README.md` whenever the approved work changes the public-facing repository description, implemented-capability summary, quick start, primary examples, or main documentation entry points. Keep `README.md` as a concise GitHub-facing landing page for a new human user rather than turning it into an internal technical registry or a chronological log of technical documents.
- Keep detailed technical-document registries, topic-local provenance notes, and operational indexes in `doc/` rather than re-growing `README.md`. Use `doc/README.md` and narrower domain indexes such as `doc/scripts/tooling/README.md` for that purpose.
- Before the final commit, update `doc/guide/project_usage_guide.md` whenever the approved work adds or changes runnable functionality such as training scripts, model architectures, inference/export flows, dataset-processing capabilities, or usage/configuration workflows.
- Before the final commit, whenever the approved work introduces a new third-party dependency, update `requirements.txt` and any relevant installation or usage documentation so the environment remains reproducible.
- Before the final commit, if the task created or modified repository-owned Markdown files, run the Markdown warning checks on the touched Markdown scope and resolve warning regressions in those files.
- Before the final commit, if the task created or modified repository-owned Markdown files, confirm that the touched Markdown files end with a normal single final newline and not a doubled trailing blank line.
- Every required Git commit must use a title aligned with the repository's existing commit style and a body that accurately summarizes all relevant modifications.
- When the user explicitly activates isolated mode, treat every repository file that already exists at activation time as locked and read-only until the user explicitly exits isolated mode or explicitly requests integration.
- During isolated mode, `README.md` and `AGENTS.md` are also locked and cannot be modified.
- During isolated mode, create work only under a session root inside `isolated/active/<session_id>/`, and only modify files created inside that session root.
- During isolated mode, maintain the session files `session_context.md`, `work_log.md`, `locked_repository_snapshot.txt`, `integration_manifest.yaml`, and `integration_checklist.md` instead of using a root-level temporary README handoff.
- When the user later requests integration of isolated work, first revalidate the current repository state against the isolated session snapshot, then process each manifest item one by one with a double verification pass before cleaning up the isolated staging residue.

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
