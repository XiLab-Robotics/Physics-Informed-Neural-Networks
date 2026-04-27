# Project Instructions

## Core Rules

- Use English as the primary project language for file names, identifiers,
  instructions, comments, and technical documentation.
- Keep the documents in `reference/` or their summaries in `doc/` in scope
  before making design or implementation choices.
- Use the `context7` MCP server before implementing or recommending
  library-specific code for Next.js, React, PyTorch, PyTorch Lightning, NumPy,
  SciPy, scikit-learn, or adjacent ML tooling.
- Prefer Context7 documentation over memory when API details, configuration
  keys, or version-specific behavior may have changed.
- If Context7 is unavailable, state that explicitly and fall back to local code
  inspection plus primary official documentation.
- Repository-relevant Codex skills may be used automatically whenever the
  request clearly matches their documented purpose.
- Codex subagents must not be launched silently. When a subagent would be
  useful, declare the proposed subagent, the reason for using it, and the
  concrete delegated scope, then wait for explicit user approval before
  launching it.

## Mandatory Workflow

### Technical Document First

- Before implementing any repository change, create a technical project
  document inside `doc/technical/YYYY-MM/YYYY-MM-DD/` with filename format
  `YYYY-MM-DD-HH-mm-SS-feature_name.md`.
- Read the real current local system date and time before naming a new
  technical document. Do not infer the timestamp from conversation context.
- Each new technical project document must contain the sections `Overview`,
  `Technical Approach`, `Involved Components`, and `Implementation Steps`.
- If subagent use is expected during implementation, record the planned
  subagent name, task boundary, and approval requirement in the technical
  document before asking for approval.
- Register every new technical project document from a canonical `doc/`
  entry point, typically `doc/README.md` or a narrower topic-local index.
- Do not write or modify implementation code until the user has explicitly
  approved the technical document for that feature.

### Training Gate

- Before executing any training campaign or training-related experiment, create
  the preliminary planning report in `doc/reports/campaign_plans/`.
- Do not execute training until both the technical document and the planning
  report have been created and explicitly approved.
- For every approved training campaign preparation, also generate the campaign
  YAML files, create the dedicated PowerShell launcher under
  `scripts/campaigns/`, create the matching launcher note under
  `doc/scripts/campaigns/`, store the campaign state, and provide the exact
  launch command.

### Final Approval Gate

- Do not create a Git commit immediately after finishing the work. Stop, report
  completion, and wait for explicit user approval before committing.
- Before any GitHub-bound commit, check for individual files above `100 MB`
  and for aggregate staged size large enough to risk remote pack rejection.
- Every required Git commit must use a title aligned with the repository's
  existing commit style and a body that accurately summarizes the changes.

## Documentation And Indices

- Keep `doc/reports/` grouped first by report domain:
  - `analysis/`
  - `campaign_plans/`
  - `campaign_results/`
- Under `doc/reports/analysis/`, prefer readable title-based filenames for
  standalone canonical reports when the topic is clearer than the timestamp.
- When one analysis topic has multiple companion artifacts or repeated
  releases, create a topic-root folder and place each concrete bundle inside a
  dated subfolder such as `[2026-03-27]/`.
- Keep companion assets for a topic-local report bundle inside the same dated
  topic folder.
- Keep `doc/reports/campaign_plans/` and `doc/reports/campaign_results/` on
  the timestamp-based filename convention.
- Treat bracketed date folders under `doc/reports/` as literal paths in
  tooling-sensitive contexts.
- Update `README.md` only when approved work changes the public-facing
  repository presentation, implemented-capability summary, quick-start flow,
  primary example commands, or main documentation entry points.
- Keep detailed technical registries and operational notes in `doc/`, using
  indexes such as `doc/README.md` and `doc/scripts/tooling/README.md` instead
  of growing `README.md` into an internal registry.

## Markdown QA

- The repository standard for Git-tracked authored Markdown is zero warnings.
- Whenever a repository-owned Git-tracked Markdown file is created or modified,
  run Markdown warning checks on the touched Markdown scope before closing the
  task.
- Treat the Markdown pass as incomplete until every warning in the touched
  scope has been analyzed and resolved.
- Also confirm that touched Markdown files end with a normal single final
  newline and not a doubled trailing blank line.
- For repository-wide warning-free claims, run the checks on the full intended
  Git-tracked Markdown scope, not only the default globs.
- Use the repository-owned entry points:
  - `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
  - `python -B scripts/tooling/markdown/run_markdownlint.py`
- Prefer the `markdown-report-qa` skill and the notes under
  `doc/scripts/tooling/markdown/` when the task is primarily documentation QA.

## Report And PDF QA

- Every final campaign-results report must be delivered both as Markdown and as
  a PDF export, and the real exported PDF must be validated before the task is
  considered complete.
- Treat
  `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  as the visual golden standard for future styled analytical PDFs.
- Do not treat a styled PDF export as complete until the exported PDF has been
  checked against the real deliverable, not only the HTML source.
- Prefer the repository-owned entry points:
  - `python -B scripts/reports/pdf/run_report_pipeline.py`
  - `python -B scripts/reports/pdf/generate_styled_report_pdf.py`
  - `python -B scripts/reports/pdf/validate_report_pdf.py`
- Prefer persistent repository-owned scripts over ad hoc inline Python snippets
  for export or validation work, except when debugging a broken tool.
- Prefer the `styled-report-pdf-qa` skill when the task is primarily PDF or
  report export work.

## Training And Campaign Governance

- Store future training artifacts under:
  - `output/training_runs/<model_family>/<run_instance_id>/`
  - `output/validation_checks/<model_family>/<run_instance_id>/`
  - `output/smoke_tests/<model_family>/<run_instance_id>/`
  - `output/training_campaigns/<campaign_id>/`
  - `output/registries/families/<model_family>/`
  - `output/registries/program/`
- Treat logical `run_name` and physical `run_instance_id` as different
  concepts. New runs must write into immutable timestamped `run_instance_id`
  folders.
- Track the current prepared or active training campaign in
  `doc/running/active_training_campaign.yaml`.
- Treat the files listed in `doc/running/active_training_campaign.yaml` as
  protected while the campaign is prepared or active.
- If a request would modify a protected campaign file, issue a `CRITICAL
  WARNING` and wait for explicit user approval before editing it.
- When the user says the campaign has started, finished, or been cancelled,
  update or inspect the persistent campaign state before doing unrelated work
  that could change the baseline.
- Every completed training campaign must expose its winner explicitly through
  `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`.
- Keep family-level and program-level best-result registries updated after
  training or campaign completion.
- Keep `doc/reports/analysis/Training Results Master Summary.md` synchronized
  after completed campaigns and after tasks that materially change registries,
  active family status, or roadmap status.
- Keep `doc/reports/analysis/RCIM Paper Reference Benchmark.md` synchronized
  when repository-owned online compensation results become available.

## Model Reports And Guides

- Whenever a new model family, model variant, or materially new model-specific
  training workflow is introduced, create a dedicated explanatory report before
  the reader is expected to rely on the code.
- The explanatory report must cover the model description, operating principle,
  conceptual structure, project-context advantages and disadvantages, and the
  implemented Python files, classes, and functions.
- When the user requests conceptual maps, schematic explanations, or
  architecture framing, include generated visual material and verify the real
  diagram output after generation.
- When a new learning guide is created under `doc/guide/`, create a PDF
  companion in the same guide-local folder, but do not finalize the PDF until
  the user has explicitly approved the generated guide images or diagrams.
- Treat the detailed `NotebookLM` source-package workflow, export naming, and
  guide-bundle policy as an on-demand domain workflow. Apply it when the task
  enters `doc/guide/` or explicitly targets guide/video-package generation,
  using the existing guide-local structure and related technical documents as
  the canonical reference.

## Documentation Portal And Dependencies

- Update `doc/guide/project_usage_guide.md` whenever approved work adds or
  changes runnable user-facing functionality.
- Update the canonical Sphinx source tree under `site/` when approved work
  changes scripts, features, documentation entry points, or other user-facing
  repository behavior within the portal scope.
- Whenever approved work affects the canonical Sphinx portal scope, regenerate
  the portal with `python -m sphinx -W -b html site site/_build/html` and treat
  a warning-free build as part of task completion.
- Treat GitHub Pages publication through the repository-owned GitHub Actions
  workflow as the canonical hosting path for the Sphinx portal.
- Whenever approved work introduces a new third-party dependency, update
  `requirements.txt` and all relevant setup or usage documentation before the
  final commit.

## Isolated Mode

- When the user explicitly activates isolated mode, treat every repository file
  that already exists at activation time as locked and read-only until the user
  explicitly exits isolated mode or explicitly requests integration.
- During isolated mode, `README.md` and `AGENTS.md` are also locked.
- During isolated mode, create work only under
  `isolated/active/<session_id>/`, and only modify files created inside that
  session root.
- During isolated mode, maintain `session_context.md`, `work_log.md`,
  `locked_repository_snapshot.txt`, `integration_manifest.yaml`, and
  `integration_checklist.md`.
- When the user later requests integration of isolated work, first revalidate
  the current repository state against the isolated session snapshot, then
  process each manifest item one by one with a double verification pass before
  cleaning up the isolated staging residue.

## Domain Notes

- Treat rotational transmission error as the main accuracy indicator of the RV
  reducer and keep the separation clear between analytical modeling and
  ML-based compensation.
- Preserve the test-rig operating variables used throughout the reference
  material: input speed, applied torque, oil temperature, encoder zeroing, and
  `DataValid` windows for TE extraction.
- When implementing compensation logic, assume the practical deployment target
  is TwinCAT/PLC-friendly execution with explicit, inspectable intermediate
  quantities.

## Coding Style

- Mirror the style used in `blind_handover_controller`, with the same
  conventions also reinforced by `mediapipe_gesture_recognition` and
  `multimodal_fusion`.
- Treat the `blind_handover_controller` style as the strict default for
  repository-owned code, utilities, tooling helpers, dataset-processing
  scripts, and report exporters.
- Prefer verbose domain-explicit names, full-uppercase module constants,
  `PascalCase` classes, `snake_case` utility functions, and existing ROS-style
  callback naming when it improves local consistency.
- Use Google-style docstrings for new or materially refactored repository-owned
  Python scripts where that level of API clarity is warranted.
- Add frequent short section comments before non-trivial logical blocks so the
  control flow remains visually scannable.
- Prefer explicit staged code over compact abstraction, with descriptive
  assertions and runtime checks.
- Preserve the existing direct print/debug style when needed.
- Treat `doc/reference_summaries/06_Programming_Style_Guide.md` as the
  canonical style reference for new code in this repository.
