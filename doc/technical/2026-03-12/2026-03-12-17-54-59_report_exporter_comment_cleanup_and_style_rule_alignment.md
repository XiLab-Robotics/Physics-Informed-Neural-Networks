# Report Exporter Comment Cleanup And Style Rule Alignment

## Overview

This document defines the approved scope for a focused style-alignment pass on `scripts/reports/generate_styled_report_pdf.py` after the user's manual refactoring in commit `0c8b5003ddcce34d672b2822c2afe8e357a1fb26`.

The requested work has two linked goals:

1. shorten the comments that are currently too long, visually heavy, or redundant inside the styled PDF exporter;
2. study the manual coding-style adjustments introduced by the user and propagate the relevant rules into the persistent repository style references.

The intent is not to redesign the exporter behavior again. The intent is to keep the same logic while aligning the code comments and the documented style rules with the latest manually approved direction.

## Technical Approach

The implementation will start from the current version of `scripts/reports/generate_styled_report_pdf.py` and the manual refactoring introduced in commit `0c8b5003ddcce34d672b2822c2afe8e357a1fb26`.

The work will be split into two stages:

1. Comment cleanup inside the exporter:
   - remove or shorten over-explanatory block comments;
   - keep only comments that improve flow scanning or clarify a non-obvious stage;
   - preserve the project convention of title-case comments before logical blocks, but reduce sentence length and repetition.

2. Style-reference alignment:
   - extract the coding-style choices that are clearly intentional in the manual refactor;
   - update the persistent repository rules so those choices are explicit and reusable in future edits;
   - keep the rules precise enough to guide future work without forcing unreadable over-compaction.

The rule update will focus on practical style guidance such as:

- when compact grouped imports are acceptable;
- when a one-line helper signature is preferred;
- when inline conditionals are acceptable;
- how long section comments should be before they become counterproductive;
- how to balance compactness against readability in utility scripts.

## Involved Components

- `scripts/reports/generate_styled_report_pdf.py`
- `AGENTS.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- `README.md`
- `doc/README.md`

## Implementation Steps

1. Inspect the current exporter and the manual refactoring from commit `0c8b5003ddcce34d672b2822c2afe8e357a1fb26`.
2. Identify the comments that are too long, repetitive, or visually noisy.
3. Rewrite only the necessary comments in `scripts/reports/generate_styled_report_pdf.py`, keeping behavior unchanged.
4. Distill the reusable style choices introduced by the manual refactor.
5. Update `AGENTS.md` and `doc/reference_summaries/06_Programming_Style_Guide.md` so those choices become persistent repository rules.
6. Update `README.md` and `doc/README.md` indexes if the new technical document or style references need refreshed descriptions.
7. Verify that the exporter still runs cleanly and that the resulting code is stylistically closer to the manually approved direction.
