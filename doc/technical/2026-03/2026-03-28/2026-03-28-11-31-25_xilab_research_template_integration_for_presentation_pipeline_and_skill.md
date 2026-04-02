# XiLab Research Template Integration For Presentation Pipeline And Skill

## Overview

This task updates the repository-owned presentation workflow so that the
canonical PowerPoint template for the current and future repository
presentations becomes:

- `reference/templates/Template_XiLab_Research.pptx`

The requested scope includes both implementation and workflow guidance:

- update the `.pptx` generation pipeline so generated presentations inherit the
  XiLab Research template instead of relying only on a plain default
  presentation;
- regenerate the current project-status presentation with that template;
- update the presentation-export skill so future presentation tasks
  automatically honor the same template rule.

The change should make the template a repository rule for future presentation
exports rather than a one-off override for the current deck only.

## Technical Approach

The repository already has a working Markdown-to-PPTX pipeline and a dedicated
presentation-export skill. The new requirement changes the canonical
presentation base from an internally built empty deck to an externally
maintained repository template.

The implementation should therefore do four things:

1. Load the canonical template from
   `reference/templates/Template_XiLab_Research.pptx` during PPTX generation.
2. Preserve the existing repository rendering logic for titles, bullets,
   tables, and slide export, but apply it on top of a presentation created
   from the template.
3. Regenerate the current project-status presentation artifacts (`.pptx` and
   slide PDF) through the updated pipeline and revalidate the real exported
   PDF.
4. Update the `presentation-export-workflows` skill so the template becomes an
   explicit required input and future default.

### Template Integration Strategy

The safest first pass is to treat the template as the source presentation shell
used by `python-pptx` during deck generation.

That means the pipeline should:

- open `Template_XiLab_Research.pptx` instead of creating a blank presentation;
- preserve the template theme, slide masters, and layout definitions;
- continue to add generated slides using template layouts where practical;
- avoid mutating the original template file in place.

The output `.pptx` should be a newly generated presentation saved next to the
owning Markdown deck, not a modified copy stored back under `reference/`.

### Validation Scope

This task is not complete when the code points to the template path. The real
deliverables must be rechecked.

Validation should include:

- successful `.pptx` generation from the template-backed workflow;
- successful PDF export through PowerPoint COM;
- slide-count consistency between Markdown and exported PDF;
- real visual inspection of representative slides to ensure the template is
  actually applied and that the repository content still fits cleanly.

### Skill Update Scope

The `presentation-export-workflows` skill should be updated so it explicitly
states:

- the canonical template path;
- that repository presentation tasks should use the XiLab Research template by
  default;
- that template-aware validation remains mandatory.

The skill should stay concise and should not duplicate implementation details
already better expressed in the scripts.

### Planned Subagent Usage

Planned subagent use during implementation:

- none required.

This is a contained pipeline and skill update and does not currently justify
runtime delegation.

## Involved Components

- `README.md`
- `reference/templates/Template_XiLab_Research.pptx`
- `scripts/reports/generate_markdown_presentation.py`
- `scripts/reports/run_presentation_pipeline.py`
- `.codex/skills/presentation-export-workflows/SKILL.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/reports/analysis/2026-03-27-18-13-19_project_status_assets/`
- `doc/technical/2026-03/2026-03-28/2026-03-28-11-31-25_xilab_research_template_integration_for_presentation_pipeline_and_skill.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before implementing the template
   integration.
3. Update the PPTX-generation workflow to load the XiLab Research template as
   the canonical base presentation.
4. Keep the existing repository rendering flow working on top of the template.
5. Regenerate the current project-status `.pptx` and slide PDF artifacts.
6. Revalidate the real exported slide PDF and inspect representative slides.
7. Update the `presentation-export-workflows` skill so the template rule is
   explicit for future tasks.
8. Update any user-facing documentation that now needs to mention the template
   requirement.
9. Run scoped Markdown checks on touched repository-owned Markdown files and
   confirm normal final-newline state before reporting completion.
