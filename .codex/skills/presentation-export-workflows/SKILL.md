---
name: presentation-export-workflows
description: Use when generating, exporting, validating, or maintaining repository-owned presentation decks in StandardML - Codex. This skill is for Markdown-to-PPTX generation, slide PDF export, and real presentation-deliverable QA, not for generic PowerPoint editing.
---

# Presentation Export Workflows

Run the repository-owned presentation workflow from canonical Markdown slide
decks to real `.pptx` and slide-PDF deliverables.

## Use This Skill For

- generating a repository-owned `.pptx` deck from Markdown slides;
- exporting a generated `.pptx` deck to slide PDF;
- validating the real exported slide PDF;
- repairing presentation-pipeline issues under `scripts/reports/`;
- keeping presentation artifact naming and placement aligned with the report
  bundle that owns the deck;
- updating repository documentation indexes when new presentation artifacts are
  added or changed.

## Do Not Use This Skill For

- generic PowerPoint editing with arbitrary external files;
- notebook-style analytical report PDF layout work;
- generic office-document conversion unrelated to repository decks;
- closing a presentation-export task without checking the real exported PDF.

## Required Checks

1. Treat the repository-owned Markdown slide deck as the canonical source.
2. Use `reference/templates/Template_XiLab_Research.pptx` as the default
   canonical template unless the task explicitly approves a different template.
3. Generate the `.pptx` artifact before discussing the export as complete.
4. Export the `.pptx` to PDF through the tracked Windows PowerPoint COM path.
5. Validate the real exported PDF, not only the Markdown deck or the `.pptx`.
6. Check that the Markdown slide count matches the exported PDF page count.
7. If repository-owned Markdown documentation was touched, run scoped Markdown
   checks and confirm normal final-newline state.

## Repository Presentation Rules

- Keep generated presentation artifacts next to the owning Markdown deck unless
  the task explicitly defines a different output root.
- Prefer repository-owned pipeline scripts over ad hoc manual export steps.
- Prefer the XiLab Research template as the standard base presentation for
  future repository decks.
- Keep artifact names explicit and discoverable.
- Surface the current environment assumption when relevant:
  Windows plus Microsoft PowerPoint COM for PDF export.
- If the exported PDF has visible clipping, broken bullets, table overflow, or
  obviously broken slide flow, keep the task open and repair the pipeline.

## Commands And Tools To Prefer

```powershell
python -B scripts/reports/presentation/generate_markdown_presentation.py
python -B scripts/reports/presentation/run_presentation_pipeline.py
python -B scripts/reports/pdf/validate_report_pdf.py
```

## Validation Output Pattern

Prefer this structure:

1. Generated `.pptx` artifact.
2. Exported slide PDF.
3. Slide-count check result.
4. Real-PDF validation result.
5. Any remaining environment or layout risks.

## File Targets To Read First

- `scripts/reports/presentation/generate_markdown_presentation.py`
- `scripts/reports/presentation/run_presentation_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `reference/templates/Template_XiLab_Research.pptx`
- the owning Markdown slide deck under `doc/reports/` or `doc/guide/`
- `doc/README.md`
- `doc/guide/project_usage_guide.md` when the workflow surface changed
