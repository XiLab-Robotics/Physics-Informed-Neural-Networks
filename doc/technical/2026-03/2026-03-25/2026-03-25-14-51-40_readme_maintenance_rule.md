# Overview

This document defines a permanent maintenance rule for the repository
`README.md` after its redesign as a GitHub-facing landing page for new human
users.

The repository already requires detailed updates to
`doc/guide/project_usage_guide.md` whenever runnable user-facing functionality
changes. However, that rule alone does not guarantee that the public
`README.md` stays aligned with the actual repository state after future
implementations.

The user requested an explicit rule so the new landing-page `README.md` does not
drift out of date.

## Technical Approach

## 1. Separate README From The Detailed Usage Guide

The repository should preserve a clear distinction between:

- `README.md`
  the public GitHub-facing landing page for a new user;
- `doc/guide/project_usage_guide.md`
  the detailed operational reference for runnable workflows

The new rule should reinforce that distinction rather than collapse both files
into the same role.

## 2. Require README Updates When Public-Facing Project State Changes

The repository should require `README.md` updates before the final commit when
approved work changes any of the following:

- the main project description;
- the current implemented capabilities;
- the visible onboarding path for a new user;
- the quick-start setup instructions;
- the primary example commands shown to a new user;
- the recommended documentation entry points;
- the public-facing project status or roadmap summary

This keeps the landing page honest and useful without forcing it to mirror every
low-level implementation detail.

## 3. Keep README High-Level

The maintenance rule should explicitly preserve the intended style of
`README.md`:

- concise;
- newcomer-oriented;
- presentation-oriented;
- linked to deeper documentation instead of duplicating it

This prevents future updates from turning `README.md` back into a large internal
technical registry.

## 4. Keep project_usage_guide.md As The Detailed Operational Surface

The existing rule for `doc/guide/project_usage_guide.md` should remain in place.

That file should still be the canonical detailed reference whenever approved
work adds or changes:

- runnable scripts;
- model architectures;
- training or validation flows;
- inference or export workflows;
- dataset-processing capabilities;
- usage or configuration workflows

## 5. Encode Both Rules In AGENTS.md

The implementation should update `AGENTS.md` so the repository instructions make
both responsibilities explicit:

- update `README.md` when the public-facing landing-page content changes;
- update `doc/guide/project_usage_guide.md` when runnable operational details
  change

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/guide/project_usage_guide.md`
- `doc/technical/2026-03/2026-03-25/2026-03-25-14-51-40_readme_maintenance_rule.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Update `AGENTS.md` with an explicit `README.md` maintenance rule.
3. Keep the existing `project_usage_guide.md` maintenance rule and clarify the
   difference in purpose between the two documents.
4. Verify that the updated instruction wording keeps `README.md` high-level and
   newcomer-oriented.
