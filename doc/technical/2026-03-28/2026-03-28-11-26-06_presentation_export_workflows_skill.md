# Presentation Export Workflows Skill

## Overview

This task adds a new repository-owned Codex skill dedicated to presentation
export workflows in StandardML - Codex.

The skill should cover the end-to-end workflow for repository-authored
presentation decks that start as Markdown and must be delivered as real
presentation artifacts such as:

- `.pptx` files;
- slide PDF exports;
- validated slide-PDF outputs;
- matching documentation-index updates when presentation deliverables are added
  or changed.

The goal is not to create a micro-skill for one script. The goal is to codify
the reusable workflow that now exists across:

- `scripts/reports/generate_markdown_presentation.py`;
- `scripts/reports/run_presentation_pipeline.py`;
- `scripts/reports/validate_report_pdf.py`;
- repository documentation and artifact-index maintenance.

## Technical Approach

The repository now has a working implementation path for generating
presentation artifacts from Markdown slide decks. That workflow includes
multiple non-obvious repository-specific requirements:

- use the repository-owned Markdown deck as the canonical source;
- generate a real `.pptx` artifact;
- export the `.pptx` to PDF through the Windows PowerPoint COM path;
- validate the real exported slide PDF instead of stopping at source
  generation;
- keep artifact naming and placement aligned with the existing report-local
  bundle structure;
- update `doc/README.md` and `doc/guide/project_usage_guide.md` when the
  workflow surface changes.

That is enough repeated structure to justify a dedicated skill.

The new skill should therefore:

- trigger when the user asks for repository presentation export, deck
  generation, slide PDF generation, or presentation-pipeline maintenance;
- direct Codex to read the relevant report scripts first;
- make the real `.pptx` and slide PDF artifacts explicit deliverables;
- require validation of the exported PDF;
- remind Codex to check touched Markdown documentation before closure.

The skill should stay focused on repository presentation workflows. It should
not become a generic PowerPoint skill or a generic office-doc conversion skill.

### Planned Skill Scope

The skill should cover:

- generation of `.pptx` presentations from repository Markdown decks;
- export of slide PDFs through the tracked pipeline;
- validation of exported slide PDFs;
- documentation-index maintenance tied to presentation deliverables;
- practical workflow notes about the current Windows + PowerPoint COM
  assumption.

The skill should not cover:

- arbitrary external `.pptx` editing tasks;
- general-purpose presentation design advice;
- NotebookLM source-package authoring as a whole;
- styled analytical report PDF work that is already covered by
  `styled-report-pdf-qa`.

### Planned Subagent Usage

Planned subagent use during implementation:

- none required.

This is a small repository-skill addition and does not currently justify
runtime delegation.

## Involved Components

- `README.md`
- `.codex/skills/`
- future `.codex/skills/presentation-export-workflows/SKILL.md`
- optional future `.codex/skills/presentation-export-workflows/agents/openai.yaml`
- `scripts/reports/generate_markdown_presentation.py`
- `scripts/reports/run_presentation_pipeline.py`
- `scripts/reports/validate_report_pdf.py`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before implementing the new skill.
3. Create `.codex/skills/presentation-export-workflows/`.
4. Write `SKILL.md` so it describes when to use the skill and how to execute
   the repository presentation workflow.
5. If useful and lightweight, add `agents/openai.yaml` metadata aligned with
   the skill content.
6. Validate the skill structure and wording against the repository style.
7. Run scoped Markdown checks on touched repository-owned Markdown files and
   confirm normal final-newline state before reporting completion.
