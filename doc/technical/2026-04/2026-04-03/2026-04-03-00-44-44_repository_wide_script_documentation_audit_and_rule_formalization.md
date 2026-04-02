# Repository-Wide Script Documentation Audit And Rule Formalization

## Overview

This document defines a repository-wide follow-up after the targeted
video-guide script retrofit.

The new request extends the scope from three recently touched scripts to the
full `scripts/` Python surface. The task now has two linked goals:

1. audit the repository-owned Python scripts for alignment with the expected
   comment and docstring format;
2. formalize a single canonical repository rule so every new script must follow
   that same format by default.

The current repository state contains a rule mismatch that should be resolved
explicitly rather than layered over:

- `doc/reference_summaries/06_Programming_Style_Guide.md` still says docstrings
  should usually stay short, one line, and in title case;
- the Sphinx portal under `site/conf.py` enables `sphinx.ext.napoleon` with
  `napoleon_google_docstring = True`;
- the approved documentation direction already established Google-style
  docstrings for generated API documentation;
- recent script work showed that placeholder one-line docstrings are no longer
  sufficient for the repository-owned tooling surface.

This follow-up should therefore both audit the existing scripts and update the
repository rules so future scripts do not regress back to the older minimal
docstring pattern.

## Technical Approach

The implementation should proceed in two coordinated layers.

### 1. Repository-Wide Script Audit

Audit every repository-owned Python file under `scripts/` and classify each
file according to documentation quality:

- aligned;
- partially aligned;
- materially underdocumented.

The audit should inspect at least:

- module-level clarity;
- dataclass and class docstrings;
- public helper and workflow-function docstrings;
- internal section-comment coverage in non-trivial functions;
- consistency with the approved Sphinx plus Napoleon documentation direction.

The audit result should be persisted in a repository-owned analysis or
technical note rather than remaining only in terminal output.

### 2. Rule Formalization

Update the canonical repository rules so the expected format becomes explicit
and conflict-free.

The formalized rule should state that:

- every new non-trivial repository-owned Python script must use Google-style
  docstrings for public modules, classes, dataclasses, and non-trivial public
  functions;
- short title-case internal section comments remain mandatory inside non-trivial
  functions;
- compact utility helpers may still use brief docstrings when the API is truly
  trivial, but the default for new script-level workflow code is no longer the
  older placeholder one-line style;
- new scripts must be written so the repository Sphinx plus Napoleon pipeline
  can render them cleanly without a later documentation retrofit pass.

The rule should be recorded in all canonical rule surfaces that govern future
implementation choices, especially:

- `AGENTS.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md`

If the audit reveals materially underdocumented scripts outside the recent
video-guide scope, the implementation may also patch the highest-priority
outliers in the same approved pass, but the rule update should happen even if
the user later chooses to defer broader retrofit work.

No subagent is planned for this task. The work is primarily local repository
inspection plus documentation and rule updates, and it does not require
delegated execution.

### Audit Baseline

The current repository-wide audit over `scripts/` shows that most files are
already strong on public function and class docstring coverage. The main gaps
are narrower and more concrete than a full repository rewrite:

- the recent `scripts/tooling/lan_ai/` modules still rely too heavily on
  placeholder docstrings and underuse internal section comments compared with
  the stronger report, training, and video-guide tooling files;
- several older but otherwise healthy scripts still miss a module docstring,
  even though their function-level documentation is already present;
- the main repository rule documents still describe the older one-line
  docstring norm too strongly, which conflicts with the approved Sphinx plus
  Napoleon direction.

The implementation should therefore focus on:

1. formalizing a single forward-looking rule for all future scripts;
2. retrofitting the highest-priority current outliers;
3. avoiding a broad noisy rewrite of already acceptable files.

## Involved Components

- `AGENTS.md`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- `doc/README.md`
- `site/conf.py`
- Python files under `scripts/`

## Implementation Steps

1. Audit the full `scripts/` Python tree and identify which files are already
   aligned versus which remain materially underdocumented.
2. Summarize the audit results in a repository-owned document so the current
   status is inspectable later.
3. Update `doc/reference_summaries/06_Programming_Style_Guide.md` to formalize
   the repository docstring and comment expectations in a way that is
   consistent with Sphinx `napoleon`.
4. Update `AGENTS.md` so future repository changes must follow the same
   comment-and-docstring format for every new script by default.
5. Apply targeted documentation retrofits to the highest-priority existing
   script outliers found by the audit, keeping behavior unchanged.
6. Run focused syntax validation on any touched Python files.
7. Run Markdown warning checks on the touched Markdown scope, including this
   technical document, `doc/README.md`, and any updated rule documents.
8. Stop after the implementation and verification pass, report the results, and
   wait for explicit approval before creating any Git commit.
