# Future Guide Generation And NotebookLM Prompt Rule

## Overview

This document formalizes the requested future workflow for newly introduced
guide topics and newly introduced model families.

The user clarified that future model additions should not stop at code plus one
technical explanation. Instead, when a new model or guide topic is approved and
implemented, the repository should automatically prepare the same documentation
surface already established for the current guide tree, including:

- guide-local assets;
- canonical guide Markdown;
- guide-local PDF companion;
- `concept_video_package/`;
- `project_video_package/`;
- one ready-to-paste `NotebookLM` command for the neutral concept video;
- one ready-to-paste `NotebookLM` command for the repository-specific project
  video.

The purpose is to make future guide creation reproducible and to ensure that the
user can immediately generate both video families with separate `NotebookLM`
instances, then bring the generated exports back into the repository for later
cleanup and organization.

## Technical Approach

### 1. Treat New Model Introduction As A Full Documentation Bundle

Whenever a new model family, model variant, or guide-worthy workflow topic is
introduced and approved, the repository should treat the deliverable as a full
documentation bundle rather than as a single Markdown file.

The expected default bundle should include:

- guide-local assets or diagrams;
- canonical guide Markdown;
- guide-local PDF;
- `concept_video_package/`;
- `project_video_package/`;
- `notebooklm_concept_video_prompt.md`;
- `notebooklm_project_video_prompt.md`.

This bundle should be the default expectation unless the user explicitly scopes
out one of these outputs.

### 2. Preserve The Existing Approval Gates

The existing approval structure should remain intact:

1. create the technical document first;
2. implement the guide Markdown and any guide-local figures;
3. wait for explicit image approval before finalizing the PDF;
4. after the guide and PDF are complete, prepare the two `NotebookLM`
   source-package tracks;
5. generate the two repository-owned `NotebookLM` commands;
6. stop and wait for the user's explicit approval before any actual
   `NotebookLM` generation or post-generation cleanup step.

The new rule therefore extends the current guide workflow, but it does not
remove any existing approval gate.

### 3. Store The Ready-To-Paste NotebookLM Commands Inside Each Package

To make the workflow deterministic and discoverable, each guide should store two
final prompt files next to the package content:

- `concept_video_package/notebooklm_concept_video_prompt.md`
- `project_video_package/notebooklm_project_video_prompt.md`

These files should:

- already reflect the style requested by the user;
- be ready to paste directly into `NotebookLM`;
- explicitly reference the package source brief, narration outline, terminology
  sheet, figure reference, and fact-boundary notes;
- request the final video in Italian unless the user explicitly requests a
  different language.

### 4. Capture The Prompt Style As A Persistent Repository Standard

The prompt style already demonstrated by the user should become the tracked
repository standard for future `NotebookLM` prompt generation.

The prompt should remain:

- didactic;
- beginner-friendly but technically precise;
- explicit about the goal;
- explicit about the required chapter order;
- explicit about what must be explained and what must not be overstated;
- explicit about terminology and fact-boundary compliance;
- explicit about desired duration, tone, and visual usage.

This means future `NotebookLM` commands should not be vague one-paragraph notes.
They should instead be structured operational prompt documents that reliably
drive the expected video style.

### 5. Distinguish The Two Prompt Intents Clearly

The future prompt files should follow a stable intent split:

#### `notebooklm_concept_video_prompt.md`

This prompt should ask for:

- a neutral, general explanation of what the model, method, or workflow is;
- operating principle;
- generic training, validation, and testing logic when relevant;
- common strengths, limitations, and use cases;
- minimal repository coupling.

#### `notebooklm_project_video_prompt.md`

This prompt should ask for:

- the repository-specific role of the topic;
- the TE-project rationale for including it;
- project-local strengths and weaknesses;
- implementation mapping when relevant;
- strict status and fact-boundary compliance.

### 6. Apply The Rule To Future Guides By Default

This should become the default future behavior for:

- new model-family guides;
- new model-variant guides when materially distinct;
- new core workflow guides under `doc/guide/`;
- future guide normalization work when an older topic root is upgraded to the
  canonical structure.

The user should not need to restate the desire for:

- guide assets;
- Markdown guide;
- PDF guide;
- concept video package;
- project video package;
- two final `NotebookLM` commands.

These should now be treated as the default documentation expectation for new
approved guide-worthy topics.

## Involved Components

- `AGENTS.md`
  Persistent workflow rules that should be updated after approval so future new
  guides automatically include the full bundle and both final `NotebookLM`
  prompt files.
- `README.md`
  Main project document that must reference this technical planning note.
- `doc/guide/project_usage_guide.md`
  Operational guide that should describe the future dual-prompt expectation for
  guide-local `NotebookLM` preparation.
- Existing guide roots under `doc/guide/`
  Current examples that establish the target structure for future guide bundles.
- Future guide-local targets after approval:
  - `doc/guide/<Guide Name>/concept_video_package/notebooklm_concept_video_prompt.md`
  - `doc/guide/<Guide Name>/project_video_package/notebooklm_project_video_prompt.md`

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before changing permanent workflow rules.
3. Update `AGENTS.md` so future approved guide-worthy topics automatically
   include the full documentation bundle and the two final `NotebookLM` prompt
   files.
4. Update `doc/guide/project_usage_guide.md` to describe the new default guide
   bundle and prompt-file expectation.
5. Ensure future guide-generation work treats both prompt files as standard
   outputs, not optional extras, unless the user explicitly narrows the scope.
