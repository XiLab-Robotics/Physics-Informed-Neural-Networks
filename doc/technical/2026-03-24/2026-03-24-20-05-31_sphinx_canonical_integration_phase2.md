# Sphinx Canonical Integration Phase 2

## Overview

This document defines the second canonical integration slice for the recovered
`isolated` documentation work.

The goal of this phase is to expose the already recovered isolated material
inside the canonical `Sphinx + RTD` portal without promoting the old proof of
concept trees themselves into canonical project roots.

This phase specifically targets:

- the isolated technical decision trail for documentation-platform selection;
- the recovered `NotebookLM` archive provenance;
- the archived `ur_rtde` visual reference PDF;
- the shared styled PDF exporter module under `scripts/reports/`.

## Technical Approach

The implementation should stay conservative:

- keep `reference/documentation_poc/mkdocs.poc.yml`, `reference/documentation_poc/doc_site_poc/`, `reference/documentation_poc/poc_sources/`, and `reference/documentation_poc/sphinx_poc/` as
  historical proof-of-concept artifacts rather than canonical source roots;
- expose the underlying decisions and recovered materials through canonical
  wrapper pages under `docs/`;
- add an `archives` section to the portal for imported `NotebookLM` bundles and
  external visual references;
- expose the stable report-generation module as a canonical API page and
  improve only the docstrings needed for readable generated documentation.

The canonical portal should therefore integrate the useful outcomes of the
isolated branch while avoiding a direct promotion of temporary or experimental
structures.

## Involved Components

- `docs/index.rst`
- `docs/api/index.rst`
- `docs/api/reports/`
- `docs/technical/`
- `docs/archives/`
- `scripts/reports/generate_styled_report_pdf.py`
- `doc/technical/2026-03-20/`
- `doc/technical/2026-03-22/`
- `doc/technical/2026-03-23/`
- `reference/isolated_handoff/notebooklm_exports_provenance_manifest.md`
- `reference/documentation_visual_references/ur_rtde_api_reference_example.pdf`

## Implementation Steps

1. Add a new portal section for recovered archives and external references.
2. Create canonical wrapper pages for the relevant isolated technical documents.
3. Add a canonical archive inventory page for the recovered `NotebookLM`
   bundles and their current non-canonical status.
4. Add a canonical page for the archived `ur_rtde` visual reference.
5. Integrate the styled PDF exporter into the API section and improve its
   public docstrings.
6. Rebuild the Sphinx site with warnings treated as errors and fix any
   integration issues before closing the batch.
