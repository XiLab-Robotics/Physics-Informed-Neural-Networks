# Sphinx Isolated Integration Checklist

## Completed Recovery Steps

- [x] Checked `git status` on `standard-ml-codex`
- [x] Verified that no uncommitted local changes required a checkpoint commit
- [x] Fetched `origin/isolated`
- [x] Verified the current `standard-ml-codex` base non-destructively
- [x] Created `integration/sphinx-docs`
- [x] Determined that the isolated commit series was missing from the base
- [x] Cherry-picked the isolated commit series in chronological order
- [x] Verified that cherry-picking completed without conflicts
- [x] Rebuilt the isolated work context from `readme.temp.md`
- [x] Read the requested NotebookLM, MkDocs, Sphinx, docstring, GitHub Pages, and backlog documents
- [x] Produced the integration analysis document

## Shared-File Risk Review

- [x] Marked `README.md` as shared and conflict-sensitive
- [x] Marked `doc/README.md` as shared and conflict-sensitive
- [x] Marked `doc/guide/project_usage_guide.md` as shared and conflict-sensitive
- [x] Marked `scripts/training/train_feedforward_network.py` as changed since isolated divergence
- [x] Marked `scripts/reports/generate_styled_report_pdf.py` as the isolated branch's only shared-code modification requiring explicit review
- [x] Confirmed that the isolated documented mirrors are not safe to promote blindly

## NotebookLM Archive Classification

- [x] Confirmed `doc/imports/notebooklm_exports/` is recovered on the integration branch
- [x] Confirmed the imported bundles remain archive material, not yet canonical guide content
- [x] Confirmed the archive now covers:
  - [x] `neural_network_foundations`
  - [x] `te_model_curriculum`
  - [x] `multilayer_perceptrons`
  - [x] `feedforward_network`
  - [x] `harmonic_regression`
  - [x] `training_validation_and_testing`
  - [x] `periodic_feature_network`
  - [x] `residual_harmonic_network`
- [x] Confirmed that future canonical migration of these archives must happen only after explicit approval

## Canonical Direction Locks

- [x] Confirmed final target platform remains `Sphinx + RTD`
- [x] Confirmed official docstring standard remains `Google-style`
- [x] Confirmed publication target remains `GitHub Pages`
- [x] Confirmed `readme.temp.md` remains the main isolated-mode source of truth

## Batch 0 Canonical Start

- [x] Defined Batch 0 as `Sphinx` portal foundation only
- [x] Excluded guide migration from Batch 0
- [x] Excluded NotebookLM media migration from Batch 0
- [x] Excluded `README.md` documentation-link work from Batch 0
- [x] Excluded `GitHub Pages` publication workflow from Batch 0
- [x] Excluded broad canonical docstring rewrites from Batch 0

## Pending Canonical Integration Work

- [ ] Review whether the isolated patch to `scripts/reports/generate_styled_report_pdf.py` should be promoted canonically
- [ ] Create the canonical `docs/` Sphinx root
- [ ] Add canonical `conf.py`, `index.rst`, and first section shells
- [ ] Validate one local canonical Sphinx HTML build
- [ ] Decide whether `MyST` is needed in Batch 0 or can remain deferred
- [ ] Re-evaluate guide migration from `doc/reports/analysis/learning_guides/` to `doc/guide/`
- [ ] Re-evaluate the future canonical role of `Multilayer Perceptrons`
- [ ] Reconcile canonical source rewrites against the current versions of:
  - [ ] `doc/guide/project_usage_guide.md`
  - [ ] `scripts/training/train_feedforward_network.py`
- [ ] Plan the first real API slice after Batch 0
- [ ] Prepare `GitHub Pages` only after the foundation batch is stable

## Stop Condition

- [x] No canonical implementation changes have been applied yet
- [x] Work stops here pending explicit user approval
