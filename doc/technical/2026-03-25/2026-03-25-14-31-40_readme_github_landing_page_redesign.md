# Overview

This document defines the redesign of the repository `README.md` so it works as
an effective GitHub landing page for a new human user instead of acting as a
large internal documentation index.

The current `README.md` has accumulated technical registry content, historical
document references, and repository-internal implementation notes. That makes it
useful as an internal traceability surface, but weak as a first-contact page for
someone discovering the repository on GitHub.

The user requested a `README.md` that behaves as a presentation-oriented entry
point: clear project description, practical onboarding, documentation pointers,
and usage examples suitable for a new user.

## Technical Approach

## 1. Reposition README As The Public Repository Front Door

The new `README.md` should be written primarily for:

- a new visitor opening the repository on GitHub;
- a collaborator trying to understand what the project does;
- a technically competent user who wants to know how to get started quickly

It should no longer try to enumerate the full internal technical-document tree
or act as a day-by-day change ledger.

## 2. Keep README High-Level And Actionable

The rewritten `README.md` should prioritize:

- what the repository is about;
- why the problem matters;
- what is currently implemented;
- how to install the environment;
- how to run the main workflows;
- where to find the main documentation next

The content should stay concise enough to be readable as a landing page, while
still giving a new user enough information to start productively.

## 3. Move Internal Registry Weight To doc/

The heavy technical-document inventory should remain accessible through:

- `doc/README.md`
- `doc/guide/project_usage_guide.md`

The new `README.md` should link to those canonical deeper references instead of
duplicating their internal indexing role.

## 4. Use A User-Centered README Structure

The rewritten `README.md` should use a structure similar to:

1. project title and concise description;
2. problem context and repository goal;
3. current implemented capabilities;
4. repository layout at a useful high level;
5. quick start / environment setup;
6. short runnable examples;
7. documentation guide for new users;
8. roadmap or current status summary

This structure is appropriate for GitHub because it lets a reader understand the
project before diving into internals.

## 5. Preserve Honest Scope Boundaries

The `README.md` should clearly distinguish:

- implemented workflows;
- planned or future workflows

That is especially important here because the repository title still references
PINN work, while the active implemented surface currently includes multiple
structured ML baselines, training infrastructure, reports, and documentation
tooling in addition to the future full PINN direction.

## 6. Include Realistic Usage Examples

The `README.md` should include a few representative commands for:

- environment setup;
- running a main training workflow;
- opening the main usage documentation;
- optionally running the Markdown validation or other repository-owned tooling

The examples should be short, real, and aligned with the current repository
state so a new user does not start from stale commands.

## 7. Clean Out Presentation-Hurting Artifacts

The redesign should remove or replace presentation-breaking elements from the
current `README.md`, including:

- legacy architecture sketches that no longer match the real repository layout;
- giant historical technical-document enumerations;
- internal process details that belong in `doc/` rather than in the front page;
- formatting artifacts that make the landing page look archival instead of
  intentional

## Involved Components

- `README.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/technical/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Redesign `README.md` as a GitHub-facing landing page for a new user.
3. Replace the current internal-document-heavy structure with a concise
   presentation, onboarding, and usage-oriented structure.
4. Keep strong links to `doc/README.md` and `doc/guide/project_usage_guide.md`
   so deeper internal documentation remains discoverable.
5. Verify that the rewritten `README.md` reflects the current implemented
   repository state and does not promise workflows that are not yet available.
6. Re-run the Markdown checks on the updated documentation files.
