# RCIM Exact-Paper Workflow README Expansion

## Overview

This task adds a repository-owned README expansion for
`scripts/paper_reimplementation/rcim_ml_compensation/` so the exact-paper
reimplementation surface exposes a practical operator guide comparable to
`recovered_original_workflow/README.md`.

The current root README for `rcim_ml_compensation/` is only a short subtree
index. The requested change is to turn that surface into a workflow-oriented
document that:

- describes the exact-paper and original-dataset exact-paper branches;
- explains how the shared pipeline is organized;
- lists the canonical Python and PowerShell entrypoints;
- documents the new stage-aware operator surface and best-parameter flow;
- gives ready-to-run commands for the most important usage paths.

## Technical Approach

The implementation will expand the existing
`scripts/paper_reimplementation/rcim_ml_compensation/README.md` instead of
creating a disconnected duplicate README elsewhere.

The expanded README will stay focused on the repository-owned reimplementation
surface and will be organized as an operator-facing guide with:

- subtree structure and branch purpose;
- workflow mapping across `exact_paper_model_bank/`,
  `original_dataset_exact_model_bank/`, and the recovered-original branch;
- canonical execution order for the exact-paper reimplementation;
- stage semantics for `Search`, `Eval`, `Export`, and `LoadBest`;
- command examples for the Python runners;
- command examples for the main Track 1 paper-faithful launcher;
- artifact and registry outputs that operators should expect.

The recovered-original README will be used as the structural reference, but
the new document will remain specific to the reimplementation rather than
copying historical content verbatim.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`

## Implementation Steps

1. Re-read the current root README and the recovered-original README to mirror
   the right documentation depth and command style.
2. Expand the root `rcim_ml_compensation/README.md` into an operational guide
   for the exact-paper reimplementation surface.
3. Add command examples for the two Python runners and the canonical Track 1
   paper-faithful launcher, including the new stage-control options.
4. Document the best-parameter summary plus registry flow and the main output
   locations used by the reimplementation.
5. Run repository Markdown QA on the touched Markdown scope and fix any
   warnings before closing the task.
