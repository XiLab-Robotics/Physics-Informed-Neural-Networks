# Sphinx Isolated Integration Analysis

## Overview

This document records the synchronized integration analysis for the isolated documentation work recovered from `origin/isolated` into the dedicated branch:

- `integration/sphinx-docs`

The integration preparation was requested under these constraints:

- preserve the current local work on `standard-ml-codex` without destructive actions;
- recover the isolated branch work conservatively and in order;
- rebuild the handoff context from `readme.temp.md` and the related technical documents;
- stop after producing an integration analysis document and an explicit checklist;
- do not promote canonical repository changes yet.

The recovery work has already been completed safely:

- current source branch checked: `standard-ml-codex`
- uncommitted local changes found: none
- non-destructive checkpoint commit needed: no
- dedicated branch created: `integration/sphinx-docs`
- isolated commit series cherry-picked in chronological order:
  - `4df4dcc41b248dc24649f6739bb01ecebc0cc44d`
  - `6d9fb985ffd4f0e857aa3abbd9f11274e8b8b321`
  - `9fa6dfcb0296f7ebe41991a913d584e40b116d4f`
  - `e07e0f44e8d64da2a3c6b29473020d7c09d62793`
  - `6fa27b82e5246b9e589e6088c062c27ca66f8a2a`
- cherry-pick conflicts encountered: none

## Technical Approach

### What The Isolated Branch Already Completed

The isolated branch does not contain one single feature. It contains four distinct work families:

1. `NotebookLM` archive ingestion and handoff preparation
2. documentation-platform evaluation and comparison reporting
3. `MkDocs` proof-of-concept work
4. `Sphinx + RTD` proof-of-concept work and backlog planning

Recovered artifacts already present on `integration/sphinx-docs` include:

- standalone handoff root:
  - `readme.temp.md`
- imported NotebookLM archive root:
  - `doc/imports/notebooklm_exports/`
- documentation comparison report:
  - `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.md`
  - `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.pdf`
- MkDocs POC:
  - `mkdocs.poc.yml`
  - `doc_site_poc/`
  - `poc_sources/`
- Sphinx POC:
  - `sphinx_poc/`
- external visual benchmark:
  - `reference/documentation_visual_references/ur_rtde_api_reference_example.pdf`

### Current Confirmed Direction

After reading the recovered handoff and the related technical notes, the direction is already decided and should be treated as valid unless the user explicitly changes it:

- documentation platform target:
  - `Sphinx + RTD`
- docstring standard:
  - `Google-style`
- publication target:
  - `GitHub Pages`

This means the earlier `MkDocs` work remains useful as comparative evidence, but it is no longer the canonical target architecture.

### Shared Files And Conflict-Risk Analysis

The isolated cherry-pick set mainly adds new files. It does not directly rewrite the most conflict-prone canonical files such as:

- `README.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `scripts/models/feedforward_network.py`
- `scripts/training/train_feedforward_network.py`

However, the synchronized repository state shows that several shared files changed on `standard-ml-codex` after the isolated branch diverged. These files are therefore high-risk for future canonical integration work:

#### High-Risk Shared Files

- `README.md`
  Changed on `standard-ml-codex` after divergence. The isolated handoff intentionally avoided touching it.
- `doc/README.md`
  Changed on `standard-ml-codex` after divergence. The isolated handoff intentionally avoided touching it.
- `doc/guide/project_usage_guide.md`
  Changed on `standard-ml-codex` after divergence. The MkDocs POC contains only a mirrored snapshot under `doc_site_poc/guide/project_usage_guide.md`, not a canonical update.
- `scripts/training/train_feedforward_network.py`
  Changed on `standard-ml-codex` after divergence. The isolated documented mirror is therefore only a point-in-time reference and cannot be promoted blindly.
- `scripts/reports/generate_styled_report_pdf.py`
  Modified by the isolated branch to support specific comparison-report table classes. This is the only real shared-code change already present inside the isolated work and must be reviewed carefully before any canonical merge decision.

#### Medium-Risk Shared Structures

- `doc/reports/analysis/learning_guides/`
  The isolated handoff assumes these guides should eventually move under `doc/guide/`, but that migration is not yet canonical and touches multiple shared references.
- future canonical `docs/` tree
  It does not exist yet in the current repository. Creating it is low-conflict by itself, but wiring it into shared navigation, CI, and README links will be conflict-sensitive.
- `requirements.txt`
  Not changed by the isolated branch, but future canonical Sphinx promotion will require dependency decisions and therefore a synchronized review.

### Assumptions From Isolated Work That Still Hold

The following isolated assumptions are still valid in the synchronized state:

- `NotebookLM` imported bundles should remain treated as archived external material until an explicit canonical migration pass is approved.
- `Sphinx + RTD` remains the selected documentation platform target.
- `Google-style docstrings` remain the selected documentation standard.
- `GitHub Pages` remains the selected hosting target.
- the archived `ur_rtde` PDF remains a valid visual benchmark for API density and structure.
- `readme.temp.md` remains the authoritative handoff source for what was done in isolated mode.

### Assumptions From Isolated Work That Need Revalidation

The following isolated assumptions are not safe to promote blindly:

- moving the full learning-guide family from `doc/reports/analysis/learning_guides/` to `doc/guide/`
  This still looks directionally reasonable, but it touches shared indexes and shared guide references and therefore must be revalidated during canonical implementation.
- using the mirrored `MkDocs` and `Sphinx` POC module copies as direct canonical content
  They are comparative artifacts, not final canonical source.
- promoting the isolated mirrored `project_usage_guide` page directly
  The canonical `doc/guide/project_usage_guide.md` has changed since divergence, so the mirrored copy is only a POC input, not an up-to-date source of truth.
- promoting the isolated documented mirror of `train_feedforward_network.py` directly
  The canonical file changed after divergence, so any future docstring rewrite must start from the current canonical file, not from the isolated mirror.

### Canonical Versus Archive Boundary

The recovered isolated work splits cleanly into two groups.

#### Archive / Handoff / Comparative Material

These should remain archival or comparative until a later explicit canonical integration batch:

- `readme.temp.md`
- `doc/imports/notebooklm_exports/`
- `mkdocs.poc.yml`
- `doc_site_poc/`
- `poc_sources/`
- `sphinx_poc/`
- isolated documented mirror modules
- imported NotebookLM slide decks, videos, mind maps, and supporting PDFs

#### Material Likely To Influence Canonical Repository Work

These should be treated as integration inputs for future canonical decisions:

- `doc/technical/2026-03-22/2026-03-22-10-05-00_code_documentation_platform_evaluation.md`
- `doc/technical/2026-03-22/2026-03-22-10-20-00_code_documentation_comparison_report_and_pdf.md`
- `doc/technical/2026-03-22/2026-03-22-11-28-00_docstring_standard_and_rich_api_poc.md`
- `doc/technical/2026-03-22/2026-03-22-12-05-00_documentation_direction_docstring_standard_and_dual_poc.md`
- `doc/technical/2026-03-22/2026-03-22-12-40-00_sphinx_documentation_architecture_backlog_and_github_pages_plan.md`
- `reference/documentation_visual_references/ur_rtde_api_reference_example.pdf`
- the renderer support patch in `scripts/reports/generate_styled_report_pdf.py`

### Batch 0 Canonical Recommendation

The correct canonical starting point for `Sphinx` is not guide migration, NotebookLM migration, or docstring rewrite.

The correct Batch 0 is a minimal portal foundation only.

#### Batch 0 Scope

- create the canonical `docs/` root
- create `docs/conf.py`
- create `docs/index.rst`
- create section-shell pages for:
  - `Getting Started`
  - `Project Guide`
  - `API Reference`
- enable:
  - `sphinx.ext.autodoc`
  - `sphinx.ext.napoleon`
  - `sphinx.ext.viewcode`
  - `sphinx_rtd_theme`
- add local build instructions
- validate one clean local HTML build

#### Batch 0 Explicit Non-Goals

- no guide migration to `doc/guide/`
- no NotebookLM media migration into canonical guide folders
- no `README.md` documentation link yet
- no `GitHub Pages` workflow yet
- no broad canonical docstring rewrite yet
- no direct promotion of `MkDocs` POC files
- no blind import of isolated mirrored Python modules

This keeps the first canonical step small, low-risk, and compatible with the current synchronized repository state.

## Involved Components

- `readme.temp.md`
  Main authoritative handoff for isolated-mode work.
- `doc/imports/notebooklm_exports/`
  Recovered archive tree for imported NotebookLM guide materials.
- `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`
- `doc/technical/2026-03-22/2026-03-22-09-50-07_additional_notebooklm_guide_archives.md`
- `doc/technical/2026-03-22/2026-03-22-10-05-00_code_documentation_platform_evaluation.md`
- `doc/technical/2026-03-22/2026-03-22-10-20-00_code_documentation_comparison_report_and_pdf.md`
- `doc/technical/2026-03-22/2026-03-22-11-05-00_mkdocs_proof_of_concept.md`
- `doc/technical/2026-03-22/2026-03-22-11-28-00_docstring_standard_and_rich_api_poc.md`
- `doc/technical/2026-03-22/2026-03-22-12-05-00_documentation_direction_docstring_standard_and_dual_poc.md`
- `doc/technical/2026-03-22/2026-03-22-12-40-00_sphinx_documentation_architecture_backlog_and_github_pages_plan.md`
- `doc/technical/2026-03-22/2026-03-22-13-00-00_ur_rtde_visual_reference_archival.md`
- `doc/technical/2026-03-23/2026-03-23-11-02-32_periodic_and_residual_notebooklm_guide_archives.md`
- `scripts/reports/generate_styled_report_pdf.py`
  Shared script modified by the isolated branch and therefore requiring special review.
- `README.md`
- `doc/README.md`
- `doc/guide/project_usage_guide.md`
- `scripts/training/train_feedforward_network.py`
  Shared files whose current synchronized state must be respected in any later canonical integration batch.

## Implementation Steps

1. Preserve the current local branch state non-destructively and verify whether a checkpoint commit is needed.
2. Fetch `origin/isolated`, create `integration/sphinx-docs`, and cherry-pick the missing isolated commits in chronological order.
3. Reconstruct the isolated-mode context by reading `readme.temp.md` and the related documentation-architecture technical notes.
4. Compare the synchronized repository state against the isolated assumptions and identify shared files at conflict risk.
5. Classify the recovered isolated files into:
   - archive / handoff / comparative material
   - future canonical integration inputs
6. Define the correct canonical Batch 0 for `Sphinx`.
7. Produce this integration analysis document and the explicit integration checklist.
8. Stop before any canonical implementation changes and wait for user approval.
