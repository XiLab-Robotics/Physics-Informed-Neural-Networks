# Report Exporter Style Alignment And Rule Update

## Overview

The user reported that:

- `scripts/reports/generate_styled_report_pdf.py`

does not respect the coding-style rules that the repository has established and used elsewhere.

This is a valid observation. The script was expanded quickly across multiple PDF-layout iterations and remained functionally effective, but it drifted from the expected repository style in several ways:

- too little sectioned structure relative to the project standard;
- style blocks and rendering logic accumulated in a utility-oriented form rather than in the staged, commented style used elsewhere in the repository;
- naming and code organization are more generic than the domain-explicit and visually structured style required by the project rules;
- the current rules talk a lot about implementation and training workflows, but they do not yet make it explicit enough that the same code-style discipline applies to report-generation utilities as well.

The goal of this task is therefore twofold:

1. refactor the styled PDF exporter so it conforms much more closely to the repository coding style;
2. update the permanent rules so future utility/report scripts are also expected to follow the same style discipline.

## Technical Approach

This should be handled as a style-alignment refactor with no intended behavioral regression in the produced report artifacts.

### Exporter Refactor Scope

The main target is:

- `scripts/reports/generate_styled_report_pdf.py`

The refactor should improve:

- import grouping and section comments;
- clearer staged function organization;
- more explicit helper naming where needed;
- readability of the main execution flow;
- consistency of docstrings and internal comments with the project style;
- better separation between:
  - Markdown parsing helpers;
  - HTML rendering helpers;
  - style/template construction;
  - PDF export execution.

The goal is not to redesign the exporter behavior again, but to preserve the approved PDF output while making the code match the repository standards more convincingly.

### Rule Update Scope

The persistent style rules should be clarified in:

- `AGENTS.md`

and, if useful, echoed in:

- `README.md`
- `doc/README.md`

The rule update should make explicit that:

- repository coding style applies not only to training or model code;
- it also applies to support utilities such as dataset scripts, tooling helpers, and report exporters;
- rapid one-off utility growth is not a valid reason to bypass the established style rules.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
  Main styled PDF exporter to refactor.
- `AGENTS.md`
  Persistent repository instructions that should explicitly extend the style requirement to report/tooling scripts.
- `README.md`
  Main project index that must reference this technical document and may reflect the clarified style expectation.
- `doc/README.md`
  Documentation index that must reference this technical document.
- `doc/guide/project_usage_guide.md`
  May need a brief note if the refactor changes the visible usage guidance or script structure worth documenting.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, refactor `scripts/reports/generate_styled_report_pdf.py` for style alignment without intentionally changing the generated report output.
3. Improve section structure, helper organization, comments, and naming to better match the repository coding rules.
4. Update `AGENTS.md` so the coding-style discipline explicitly covers utility scripts and report exporters too.
5. Update any related documentation only if needed to reflect the clarified permanent rule.
6. Re-run the styled PDF export once after the refactor to ensure no behavioral regression in the output generation path.
7. Commit the approved refactor and rule update with a repository-aligned commit message.
