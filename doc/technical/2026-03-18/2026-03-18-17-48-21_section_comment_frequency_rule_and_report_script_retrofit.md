# Section Comment Frequency Rule And Report Script Retrofit

## Overview

This document defines a coding-style correction for the recently added report scripts:

- `scripts/reports/generate_model_report_diagrams.py`
- `scripts/reports/run_report_pipeline.py`

The current issue is not missing docstrings, but missing frequent section comments inside the function bodies.

In this repository, utility scripts are expected to use short `# ...` section comments regularly to make the execution stages visually obvious while scanning the file. The two new report scripts currently rely too heavily on raw staged code without enough internal section markers, so they do not match the established local style closely enough.

This work should both:

1. add the missing section comments to the two report scripts;
2. make the expectation explicit and persistent in the project rules.

## Technical Approach

The correction should be stylistic and structural, not behavioral.

### 1. Reinforce The Rule In The Persistent Instructions

The coding-style rules should explicitly state that:

- section comments are expected frequently inside non-trivial functions, not only occasionally;
- utility scripts and tooling helpers must follow the same pattern;
- recently added code should not rely on docstrings alone when the body contains multiple logical stages.

This should sharpen the existing guidance rather than replace it.

### 2. Retrofit The Two Report Scripts

The two report scripts should be updated so their internal stages are clearly segmented with short, high-signal comments such as:

- `# Resolve Report Paths`
- `# Validate Tool Env`
- `# Export Styled PDF`
- `# Build Card Geometry`
- `# Draw Layer Connections`

The goal is not to comment every line, but to make the control flow visually readable in the same way as the surrounding repository scripts.

### 3. Preserve The Existing Compactness

The retrofit should stay disciplined:

- comments should remain short;
- comments should mark real logical blocks;
- comments should not turn into sentence-length narration;
- obvious one-line helpers should remain compact when they are already clear.

## Involved Components

The work will affect:

- `AGENTS.md`
  to make the rule persistent.
- `scripts/reports/generate_model_report_diagrams.py`
  to add frequent section comments inside the staged drawing and generation helpers.
- `scripts/reports/run_report_pipeline.py`
  to add frequent section comments inside the pipeline orchestration logic.

No behavioral changes are intended.

## Implementation Steps

1. Update `AGENTS.md` to state the expected frequency and role of section comments more explicitly.
2. Add short section comments throughout `scripts/reports/generate_model_report_diagrams.py`.
3. Add short section comments throughout `scripts/reports/run_report_pipeline.py`.
4. Verify syntax after the style-only refactor.
