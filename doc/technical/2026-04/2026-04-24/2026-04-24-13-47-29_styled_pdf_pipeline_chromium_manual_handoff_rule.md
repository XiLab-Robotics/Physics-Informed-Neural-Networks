# 2026-04-24-13-47-29 Styled Pdf Pipeline Chromium Manual Handoff Rule

## Overview

The current styled PDF workflow must be tightened after the failed interrupted
`SVM` partial-closeout export attempt.

The user requirement is explicit:

- `PyMuPDF` must not be used as a rendering fallback for repository-authored
  styled PDF generation;
- if the repository-owned Chromium path cannot materialize the PDF, the agent
  must stop trying alternative renderers;
- instead, the workflow must formalize a manual local handoff by providing the
  simple repository-owned `generate_styled_report_pdf.py` command for the
  target report.

This task formalizes that policy in the repository-owned PDF pipeline
documentation and removes any ambiguity about acceptable fallback behavior.

## Technical Approach

Keep the styled PDF pipeline Chromium-first and Chromium-only for actual PDF
generation.

The approved behavior after this change should be:

1. `generate_styled_report_pdf.py` may use only the repository-owned Chromium
   path (`Chrome` or `Edge`) for the real styled export.
2. If that path fails, the task is considered blocked on local browser export,
   not eligible for a second renderer fallback.
3. The persistent workflow documentation must instruct the agent to provide the
   exact manual export command for the user's workstation.
4. That manual command should be the simple repository-owned
   `python -B scripts\reports\generate_styled_report_pdf.py ...` invocation for
   the target Markdown and PDF paths, not a raw `Chrome` or `Edge` command.

This rule should be documented at the pipeline-note level and, where needed, in
the script-facing notes that future PDF tasks are expected to consult first.

## Involved Components

- `doc/scripts/reports/run_report_pipeline.md`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/generate_styled_report_pdf.py`
- `doc/technical/2026-04/2026-04-24/2026-04-24-13-47-29_styled_pdf_pipeline_chromium_manual_handoff_rule.md`
- `doc/technical/2026-04/2026-04-24/README.md`
- `doc/README.md`

## Implementation Steps

1. Update the persistent PDF-pipeline documentation to state that `PyMuPDF`
   must never be used as a styled-PDF rendering fallback.
2. Document the mandatory failure behavior: when Chromium export fails, stop
   and hand the user the simple `generate_styled_report_pdf.py` command instead
   of trying a different renderer.
3. If needed, align the script-level wording so the exporter and pipeline notes
   reflect the same Chromium-only policy.
4. Run Markdown QA on the touched documentation scope.
5. Report the formalized rule and provide the manual export command for the
   current interrupted `SVM` partial-closeout PDF.
