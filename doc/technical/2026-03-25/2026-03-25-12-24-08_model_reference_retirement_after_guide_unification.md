# Model Reference Retirement After Guide Unification

## Overview

This document proposes the final retirement pass for:

- `doc/guide/model_reference/`

The repository now has canonical per-model guides under:

- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`

Those canonical guides now integrate both:

- the learning-oriented explanation layer;
- the technical implementation and training-reference layer.

Because of that completed unification, the older parallel material still stored under `doc/guide/model_reference/` is now duplication residue rather than an active canonical documentation surface.

The goal of this pass is to retire that duplicate subtree cleanly so the repository no longer exposes two parallel long-form homes for the same implemented model families.

## Technical Approach

### 1. Treat `doc/guide/<Model Name>/` As The Only Canonical Surface

The implemented model families should now be considered canonically documented only under:

- `doc/guide/<Model Name>/`

This means the repository indexes, cross-links, assets, and PDF workflow should continue to point only to those guide-local model folders.

### 2. Remove The Parallel `model_reference` Guide Files

The current duplicate residue under:

- `doc/guide/model_reference/FeedForward Network/`
- `doc/guide/model_reference/Harmonic Regression/`
- `doc/guide/model_reference/Periodic Feature Network/`
- `doc/guide/model_reference/Residual Harmonic Network/`

should be removed once it is confirmed that:

- the guide-local assets are canonical;
- the guide-local Markdown files are canonical;
- the guide-local PDFs have been regenerated and validated;
- the active repository links no longer depend on `model_reference`.

### 3. Update Any Remaining Non-Historical References

Before the subtree is deleted, the pass should verify that no active non-historical surface still points to:

- `doc/guide/model_reference/`

Historical technical documents may still mention the old path as provenance, but active navigation and tooling should not.

### 4. Keep The Retirement Focused On The Duplicate Subtree

This pass should not rewrite the canonical guide content again.

The scope is limited to:

- confirming the canonical guide-local paths;
- removing the now-obsolete `model_reference` duplicate tree;
- updating any final active references if needed.

## Involved Components

- `doc/guide/model_reference/`
- `README.md`
- `doc/README.md`
- `doc/guide/TE Model Curriculum/TE Model Curriculum.md`
- `doc/guide/project_usage_guide.md`
- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/generate_model_report_diagrams.py`
- `doc/scripts/reports/generate_model_report_diagrams.md`

## Implementation Steps

1. Confirm that the canonical model guides and their PDF companions now live only under `doc/guide/<Model Name>/`.
2. Verify that no active non-historical repository surface still depends on `doc/guide/model_reference/`.
3. Remove the duplicate `doc/guide/model_reference/` subtree.
4. Recheck the repository indexes and tooling references after the removal.
5. Report completion and wait for explicit approval before any Git commit.
