# Feedforward PDF Section Page Breaks

## Overview

This document proposes a targeted layout correction for the canonical guide PDF:

- `doc/guide/FeedForward Network/FeedForward Network.pdf`

The user requested that two specific sections begin on a new page in the real exported PDF:

- `Operating Principle`
- `Advantages`

The goal of this pass is to adjust the styled PDF export behavior so the section starts become cleaner and more deliberate in the final `FeedForward Network` PDF layout.

## Technical Approach

### 1. Treat The Request As A Real PDF Layout Requirement

This is not only a Markdown-content adjustment.

The requirement is about the actual exported PDF page flow, so the implementation must be validated against the real generated PDF rather than inferred only from the Markdown structure.

### 2. Force New-Page Starts For The Two Named Sections

The styled export flow should be adjusted so the `FeedForward Network` guide starts these sections on a new page:

- `Operating Principle`
- `Advantages`

The preferred implementation is to use the report exporter's page-break control rather than inserting crude manual spacing into the Markdown.

### 3. Keep The Change Narrow To The Current Guide Request

This pass should only target the current `FeedForward Network` PDF unless a more general reusable section-break mechanism can be applied safely without changing unrelated guide layouts.

The current user request is specific to one guide and two named sections, so the implementation should remain focused on that scope.

### 4. Regenerate And Validate The Real PDF

After the page-break rule is implemented, the canonical PDF must be regenerated and the real PDF must be validated to confirm that:

- `Operating Principle` starts on a new page;
- `Advantages` starts on a new page;
- no new clipping or layout regressions are introduced.

## Involved Components

- `doc/guide/FeedForward Network/FeedForward Network.md`
- `doc/guide/FeedForward Network/FeedForward Network.pdf`
- `scripts/reports/generate_styled_report_pdf.py`
- any related report-pipeline helper used for PDF regeneration and validation

## Implementation Steps

1. Add this technical document and reference it from `README.md`.
2. Identify the cleanest way to force page breaks for the two requested section headings in the styled exporter flow.
3. Implement the page-break behavior for `Operating Principle` and `Advantages` in the `FeedForward Network` guide export path.
4. Regenerate `doc/guide/FeedForward Network/FeedForward Network.pdf`.
5. Validate the real exported PDF to confirm the requested page starts and check for layout regressions.
6. Report completion and wait for explicit approval before any Git commit.
