# Commit Workflow Rule Update

## Overview

This document defines an update to the repository operating rules so that every user-requested modification follows a strict three-step workflow:

1. Create a technical document first.
2. Execute the requested modifications only after explicit user approval.
3. Create a Git commit after the approved modifications are completed.

The goal is to make the repository workflow explicit, reproducible, and aligned with the user's preferred review and traceability process.

## Technical Approach

The rule update will be implemented by editing the repository instruction files that already define project workflow expectations.

The updated rule set should state that:

- the technical document is always the first implementation step;
- no implementation changes are allowed before explicit approval of that document;
- once the approved work is complete, a Git commit must always be created;
- the commit message must include a title aligned with the repository's existing commit style;
- the commit body must provide an accurate summary of all relevant modifications.

The change is procedural and documentation-focused. It does not alter runtime code or dataset logic.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/README.md`
- `doc/technical/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md`

## Implementation Steps

1. Add this technical document to `doc/technical/`.
2. Reference the document from the main project documentation index in `README.md`.
3. After user approval, update `AGENTS.md` to formalize the mandatory three-step workflow.
4. After user approval, update `README.md` so the critical project rules reflect the same workflow.
5. Verify that the new rule text is consistent across the repository documentation.
6. Create a Git commit summarizing the approved rule changes.
