# Private Repo Pages Publication Backlog Note

## Overview

This document records the current repository decision about the Sphinx portal
publication path.

The repository should remain private for now, so GitHub Pages publication is
not enabled at this stage. The future target remains unchanged:

- make the repository public when the project is ready for public exposure;
- then enable GitHub Pages publication for the canonical Sphinx portal through
  the repository-owned GitHub Actions workflow.

The purpose of this note is to ensure that this deferred publication step stays
visible in a canonical backlog location instead of being lost in transient chat
history.

## Technical Approach

Record the deferred GitHub Pages publication decision in the repository-owned
documentation system and, after approval, also mirror it into the live backlog
surface used for operational reminders.

The reminder should explicitly preserve these facts:

- the current blocker is repository privacy, not a missing Sphinx workflow;
- the GitHub Actions publication workflow already exists in the repository;
- the future activation sequence is:
  - change repository visibility to public;
  - configure GitHub Pages to use `GitHub Actions`;
  - confirm the published site URL and expose it in the appropriate
    documentation entry points if needed.

## Involved Components

- `doc/technical/2026-04/2026-04-03/2026-04-03-16-24-46_private_repo_pages_publication_backlog_note.md`
- `doc/README.md`
- `doc/running/te_model_live_backlog.md`

## Implementation Steps

1. Keep this technical note as the canonical approval gate for the backlog
   reminder.
2. Add this note to `doc/README.md` so the deferred decision is indexed.
3. After approval, record a concise deferred reminder in
   `doc/running/te_model_live_backlog.md` so the future public-repo plus
   GitHub Pages activation step remains visible in the live operational view.
4. Run Markdown warning checks on the touched Markdown scope.
5. Stop after the reminder is recorded and wait for explicit approval before
   creating any Git commit.
