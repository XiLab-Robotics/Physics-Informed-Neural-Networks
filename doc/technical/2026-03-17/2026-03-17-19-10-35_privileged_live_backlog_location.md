# Privileged Live Backlog Location

## Overview

This document formalizes a repository workflow improvement requested after the first TE planning and Wave 0 implementation work.

The current TE implementation backlog exists mainly inside technical planning documents under `doc/technical/`.

That is useful for historical traceability, but it is not the best operational location for a backlog that should remain:

- easy to find;
- easy to update incrementally;
- clearly identified as the current working plan rather than as a historical planning artifact.

The requested improvement is therefore:

- move the canonical operational backlog into a more privileged repository location;
- keep it updated progressively while implementation waves advance;
- preserve the existing technical documents as historical design references rather than deleting or overwriting their planning rationale.

## Technical Approach

### Problem With The Current Situation

The current backlog is documented well, but it lives in files such as:

- `doc/technical/..._te_model_implementation_backlog.md`

This creates three practical problems:

1. the canonical working backlog is not obvious from repository navigation;
2. the document looks like a historical technical note instead of a live execution tracker;
3. future updates risk mixing immutable planning rationale with mutable execution state.

### Proposed Canonical Location

The operational backlog should move into `doc/running/`, which already hosts persistent project state that must stay visible during ongoing work.

The recommended canonical file is:

- `doc/running/te_model_live_backlog.md`

This file should become the privileged operational backlog for the TE model program.

### Why `doc/running/` Is The Right Place

`doc/running/` already has the right semantics:

- it stores persistent active or prepared project state;
- it is meant to be consulted during ongoing execution, not only after the fact;
- it naturally separates live operational state from historical technical notes and final reports.

That makes it a better home for:

- current wave status;
- completed steps;
- next pending steps;
- current active branch of the model program.

### Role Separation

The repository should separate three document roles clearly.

#### 1. Technical Notes In `doc/technical/`

These remain the design rationale and approval history.

They should answer:

- why a workflow exists;
- why a family was included or deferred;
- what was approved at a planning level.

They should not be treated as the primary day-to-day operational checklist.

#### 2. Live Backlog In `doc/running/`

This becomes the day-to-day operational source of truth.

It should answer:

- what is completed;
- what is currently active;
- what is next;
- what is blocked, deferred, or low-priority.

#### 3. Reports In `doc/reports/`

These remain campaign-specific or analytical deliverables.

They should answer:

- what was tested;
- what results were obtained;
- what conclusions were reached.

### Proposed Live Backlog Structure

The privileged live backlog should be concise and operational.

Recommended sections:

- `Program Overview`
- `Current Status`
- `Completed`
- `In Progress`
- `Next Up`
- `Deferred / Low Priority`
- `Wave Checklist`
- `Decision Notes`

The file should not duplicate every long-form technical explanation already present in `doc/technical/`.

It should instead link back to the relevant technical documents where needed.

### Update Rule

Once introduced, this live backlog should be updated whenever one of these changes happens:

- a wave starts;
- a wave completes;
- a model family is promoted or deferred;
- a campaign plan is approved;
- a campaign finishes and changes the next decision point;
- the current best candidate family changes.

This update rule should be treated as part of the implementation workflow, not as optional documentation cleanup.

### Documentation Visibility

To make the backlog truly privileged, the repository should also expose it prominently in:

- `README.md`
- `doc/README.md`
- `doc/running/README.md`

The wording should make clear that:

- `doc/running/te_model_live_backlog.md` is the canonical operational backlog;
- the technical backlog documents remain the historical planning baseline.

### Optional Companion State File

If later needed, a small machine-readable companion file could also be introduced, for example:

- `doc/running/te_model_live_backlog.yaml`

This is not required immediately.

The first implementation should prefer a readable Markdown backlog as the human-facing source of truth.

## Involved Components

- `README.md`
  Main project document that must later link clearly to the live backlog.
- `doc/README.md`
  Internal documentation index that must later expose the live backlog prominently.
- `doc/running/README.md`
  Running-state documentation that should later explain the role of the live backlog.
- `doc/running/te_model_live_backlog.md`
  Proposed new canonical operational backlog file.
- `doc/technical/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  Existing historical technical backlog document that should remain as the planning baseline.
- `doc/technical/2026-03-17/2026-03-17-19-10-35_privileged_live_backlog_location.md`
  This technical note.

## Implementation Steps

1. Create this technical note and register it in the documentation indexes.
2. Wait for explicit user approval before creating the live backlog file or modifying the running-document structure.
3. Create `doc/running/te_model_live_backlog.md` as the new canonical operational backlog.
4. Seed it from the currently approved TE implementation backlog, but rewrite it into an operational state format instead of copying the full technical note verbatim.
5. Update `README.md`, `doc/README.md`, and `doc/running/README.md` so the live backlog is the clearly privileged entry point.
6. Keep the technical backlog documents unchanged as historical planning references.
7. From that point forward, update the live backlog incrementally whenever the TE implementation program advances.
