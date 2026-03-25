# Overview

This document defines a cleanup proposal for the repository documentation-root
naming after the introduction of the canonical Sphinx portal.

The current repository uses both:

- `doc/`
  canonical human-authored Markdown documents, guides, reports, and technical
  notes;
- `docs/`
  the Sphinx documentation portal source tree and local build root

That distinction is technically valid, but it is semantically weak and too easy
to confuse. The user explicitly identified the problem: `doc` and `docs` are
too similar for long-term repository clarity.

This document also confirms that `docs/_build/` should remain unversioned as a
generated output and not as a tracked source tree.

## Technical Approach

## 1. Keep Generated Sphinx Build Output Unversioned

`docs/_build/` is generated documentation output.

It should remain:

- excluded from version control;
- excluded from source-oriented Markdown maintenance checks;
- treated as disposable local build output

The current `.gitignore` entry already reflects the correct policy:

- `docs/_build/`

No future cleanup should promote `_build` into tracked canonical content.

## 2. Acknowledge The Naming Collision Clearly

The current naming has this real usability problem:

- `doc/`
  sounds like "documentation";
- `docs/`
  also sounds like "documentation"

That forces contributors to remember an artificial distinction rather than a
self-evident one.

The repository should prefer names that communicate different roles
immediately.

## 3. Preserve doc/ As The Canonical Documentation Source Root

The repository has already standardized many rules, references, and workflows
around `doc/`, including:

- technical documents under `doc/technical/`;
- guides under `doc/guide/`;
- reports under `doc/reports/`;
- script documentation under `doc/scripts/`

Because `doc/` is now the dominant canonical human-authored documentation root,
it should remain unchanged.

## 4. Rename docs/ To A Semantically Distinct Portal Root

The better cleanup direction is to rename the Sphinx portal root from `docs/`
to a name that describes its role instead of colliding with `doc/`.

Candidate names include:

- `site/`
- `documentation_site/`
- `portal/`

The strongest practical candidate is:

- `site/`

because it is short, clear, conventional enough, and immediately distinct from
`doc/`.

Under that scheme:

- `doc/`
  canonical documentation source content;
- `site/`
  Sphinx portal source and local site build workflow

## 5. Treat site/_build/ As Generated Output

If the root is renamed to `site/`, the same generated-output rule should become:

- `site/_build/`

That path should remain ignored in Git and excluded from source-oriented lint
workflows exactly like the current `docs/_build/`.

## 6. Update References Systematically

If approved, the rename must update:

- `.gitignore`
- Sphinx local build commands in `doc/guide/project_usage_guide.md`
- root and internal references that currently mention `docs/`
- Markdown lint configuration or local overrides that currently refer to
  `docs/`
- any technical-document references that need to distinguish historical
  `docs/` wording from the new canonical portal root

Historical technical notes may still mention `docs/` when describing the past.
Those should only be rewritten when the reference is meant to describe the
current canonical structure rather than archival history.

## 7. Keep The Rename Scoped

This should be treated as a naming and clarity cleanup, not as a new
documentation-platform redesign.

The implementation should therefore avoid unrelated changes such as:

- changing the documentation stack away from Sphinx;
- redesigning the portal information architecture from scratch;
- rewriting large amounts of content that do not depend on the root rename

## Involved Components

- `.gitignore`
- `README.md`
- `AGENTS.md` if any persistent wording needs clarification
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `docs/` current Sphinx portal root
- future renamed portal root such as `site/`
- Markdown lint configuration files that currently reference `docs/`
- `doc/technical/2026-03-25/2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md`

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Keep `_build` unversioned and confirm that generated-output policy remains
   unchanged.
3. Rename the canonical Sphinx portal root from `docs/` to the approved
   replacement name, preferably `site/`.
4. Update `.gitignore`, local build commands, lint scope/exclusions, and
   active documentation references.
5. Verify that the renamed portal still has a clear separation from `doc/`.
6. Re-run the relevant Markdown and documentation checks after the rename.
