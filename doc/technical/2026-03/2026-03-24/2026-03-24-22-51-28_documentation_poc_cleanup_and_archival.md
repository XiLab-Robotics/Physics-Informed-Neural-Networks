# Overview

This document defines a cleanup batch for the remaining isolated documentation proof-of-concept artifacts that had still been living at the repository root even though the canonical documentation direction is now the `docs/` Sphinx portal.

The goal is to reduce root-level clutter without losing historical provenance or breaking the technical decision trail that still references the proof-of-concept material.

## Technical Approach

The cleanup should be conservative.

The proof-of-concept artifacts should not be deleted outright in the first pass because:

- they still document the earlier platform comparison process;
- multiple technical notes and the isolated handoff refer to them explicitly;
- they remain useful as historical evidence for why the repository selected the current canonical direction.

Instead, the cleanup should relocate the remaining proof-of-concept assets into a dedicated archival subtree so that:

- the repository root reflects only active canonical entry points;
- the historical documentation-platform experiments remain inspectable;
- references can be updated cleanly without losing provenance.

Recommended archival target:

- `reference/documentation_poc/`

Recommended relocation scope:

- `reference/documentation_poc/mkdocs.poc.yml`
- `reference/documentation_poc/doc_site_poc/`
- `reference/documentation_poc/poc_sources/`
- `reference/documentation_poc/sphinx_poc/`

After relocation, repository-authored references should be updated to the new archival location wherever those references are meant to remain operational rather than purely historical.

## Involved Components

- `mkdocs.poc.yml`
- `doc_site_poc/`
- `poc_sources/`
- `sphinx_poc/`
- `reference/documentation_poc/`
- `readme.temp.md`
- `README.md`
- `doc/README.md`
- `doc/technical/2026-03/2026-03-22/2026-03-22-11-05-00_mkdocs_proof_of_concept.md`
- `doc/technical/2026-03/2026-03-22/2026-03-22-12-05-00_documentation_direction_docstring_standard_and_dual_poc.md`
- `doc/technical/2026-03/2026-03-22/2026-03-22-12-40-00_sphinx_documentation_architecture_backlog_and_github_pages_plan.md`

## Implementation Steps

1. Create a dedicated archival root for historical documentation-platform proof-of-concept assets.
2. Move the remaining root-level POC files and directories into that archival root without modifying their internal contents.
3. Update repository-authored references that should still resolve after the move.
4. Leave purely historical narrative references untouched when they intentionally describe the original isolated state.
5. Re-run targeted searches to confirm that no active repository guidance still points to obsolete root-level POC paths unless intentionally historical.
6. Report the exact archival destination and the updated reference set.

## Implementation Result

The cleanup was executed conservatively.

The former root-level proof-of-concept artifacts were relocated to:

- `reference/documentation_poc/mkdocs.poc.yml`
- `reference/documentation_poc/doc_site_poc/`
- `reference/documentation_poc/poc_sources/`
- `reference/documentation_poc/sphinx_poc/`

The archival root now also includes:

- `reference/documentation_poc/README.md`

Repository-authored technical references that still needed to resolve after the move were updated to the archival location.

Purely historical handoff content in `readme.temp.md` was intentionally left unchanged so it continues to describe the original isolated state accurately.
