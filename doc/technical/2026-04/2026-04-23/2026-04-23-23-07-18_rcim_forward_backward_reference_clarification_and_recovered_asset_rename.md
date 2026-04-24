# RCIM Forward/Backward Reference Clarification And Recovered Asset Rename

## Overview

This document formalizes a corrected repository interpretation of the RCIM ML-compensation paper after direct clarification from the paper authors. The repository currently treats the recovered paper assets as a single exact-paper harmonic-prediction branch, but the paper notation uses a generalized subscript that covers two distinct operating regimes: forward rotation and backward rotation.

The key clarification is that forward and backward transmission-error behavior follow the same physical and mathematical treatment, but they are modeled with distinct datasets and distinct trained models. The recovered paper assets currently available in the repository correspond only to the forward branch. The repository documentation and recovered-asset naming therefore need to be updated to remove the current ambiguity.

## Technical Approach

The implementation will update the paper-facing documentation at the repository level instead of changing the current model-training logic. The documentation refresh will formalize the following points:

- Section `2.2` of `RCIM_ML-compensation.pdf` defines forward and backward TE curves as two distinct phenomena.
- Equation `(2)` uses a generalized direction subscript that can denote either the forward or backward branch.
- The generalized notation later used for amplitudes, phases, datasets, equations, and tables is therefore shorthand for two parallel formulations: one forward-only and one backward-only.
- Section `3.1` implies two derived training datasets from the original measurements: one forward dataset and one backward dataset.
- The algorithm families discussed in the paper are therefore instantiated twice, once per direction, even though the paper presents the notation in collapsed form.
- The repository recovered models under the current RCIM recovered-asset root are forward-only models.
- The canonical repository wording must explicitly state that the current Track 1 exact-paper replication corresponds to the forward tables and forward model bank only.

The work will update the canonical recovered-asset indexes, the paper summary material, and the deeper RCIM analytical notes so that future comparison, replication, and deployment work does not incorrectly treat forward and backward banks as interchangeable.

The work will also rename the recovered asset root from `reference/rcim_ml_compensation_recovered_assets/` to a forward-explicit name so the physical folder structure matches the corrected interpretation. The current planned target name is `reference/rcim_ml_compensation_recovered_assets/`, subject to adjustment if a shorter project-consistent variant is preferable during implementation.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `reference/README.md`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Recovered Asset Deep Analysis.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- Additional repository documents and scripts that currently reference `reference/rcim_ml_compensation_recovered_assets/`

## Implementation Steps

1. Re-read the relevant paper passages and the recovered-code entrypoints to align the documentation changes with the real current repository evidence.
2. Update the canonical paper summary and recovered-asset summaries to formalize the forward-only interpretation of the currently recovered model bank.
3. Update the deeper RCIM analysis reports so that equations, datasets, table references, and Track 1 wording explicitly distinguish generalized paper notation from the repository's forward-only recovered branch.
4. Rename the recovered asset root to a forward-explicit path and update repository references that point to the old folder name.
5. Run Markdown QA on the touched documentation scope and verify that no stale path references remain after the rename.
