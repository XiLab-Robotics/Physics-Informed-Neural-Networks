# Overview

This technical document defines the next implementation pass for the strict
RCIM exact-paper `Track 1` branch after the first real baseline execution
attempt failed during ONNX export and exposed that the current runner is still
too thin compared with the repository's normal training workflows.

Two problems must be solved together:

1. the exact-paper validation runner currently fails during per-target ONNX
   export, with the observed crash occurring inside `skl2onnx` while exporting
   the recovered `SVR` branch;
2. the workflow still behaves like a single ad-hoc validation script, while it
   should behave like the repository's campaign-oriented training workflows:
   multiple prepared runs, PowerShell launcher entry points, logging, stable
   campaign bookkeeping, and clearer operator-facing execution.

The goal of this pass is therefore:

- make the exact-paper validation path robust enough to execute end-to-end on
  the recovered family bank;
- convert it into a repository-owned batch-run workflow with logging and a
  PowerShell launcher;
- preserve paper-faithful behavior while adopting the repository's normal
  campaign discipline.

## Technical Approach

The failure must be addressed at the export surface, not only by suppressing
one family. The terminal trace shows that `skl2onnx` fails while exporting an
`SVMRegressor` node with empty support-vector structures. The recovered paper
code exported estimators per target, but the modern dependency combination in
this repository appears stricter than the original environment.

The fix strategy is:

1. reproduce and isolate the failing family/target export behavior inside the
   repository-owned exact-paper support layer;
2. add robust export handling in the exact-paper support module:
   - family-aware conversion branches;
   - explicit capture of per-target export failures;
   - non-destructive export summaries that record failures instead of crashing
     the full run immediately when configured;
   - optional strict mode so the workflow can still be used both for diagnosis
     and for final faithful validation;
3. compare the repository export behavior against the recovered paper export
   surface and document any unavoidable modern-environment mismatches.

The campaignization strategy is:

1. create a dedicated exact-paper campaign config package;
2. introduce a PowerShell launcher under `scripts/campaigns/`;
3. add operator-facing launcher documentation under `doc/scripts/campaigns/`;
4. add logging and per-run status printing so batch execution remains visible;
5. update `doc/running/active_training_campaign.yaml` when this branch is later
   prepared as a real campaign.

The batch campaign should remain paper-faithful in content while being
repository-faithful in operations. That means:

- multiple exact-paper family-bank runs can be orchestrated together;
- the launcher should support staged configurations such as:
  - full exact bank with strict export;
  - full exact bank with diagnostic non-strict export;
  - optional family-subset diagnostic runs when needed for isolation;
- reporting should remain per-run and campaign-aware.

No subagent use is planned for this implementation.

## Involved Components

Current exact-paper implementation surface to modify:

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`

Reference material that should stay in scope:

- [RCIM Recovered Asset Deep Analysis.md](../../../reports/analysis/RCIM%20Recovered%20Asset%20Deep%20Analysis.md)
- [RCIM Exact Paper Model Bank Workflow.md](../../../reports/analysis/RCIM%20Exact%20Paper%20Model%20Bank%20Workflow.md)
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-predictorML_v7.py`
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`

New repository workflow components likely to be added:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/...`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_model_bank_campaign.ps1`
- `doc/scripts/campaigns/run_exact_paper_model_bank_campaign.md`
- `doc/reports/campaign_plans/...` for the exact-paper campaign preparation

Canonical documentation likely to be updated:

- `doc/guide/project_usage_guide.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/te_model_live_backlog.md`
- `site/`

## Implementation Steps

1. Reproduce the current ONNX export failure inside the exact-paper support
   layer and isolate the failing family/target combinations.
2. Refactor exact-paper ONNX export into a safer per-target export routine with
   explicit failure capture and family-specific diagnostics.
3. Add configuration controls for:
   - strict export failure behavior;
   - diagnostic skip/continue behavior;
   - optional family-subset runs for debugging.
4. Update the exact-paper validation summary and report so export failures,
   skipped targets, and successful target counts are all serialized clearly.
5. Prepare a dedicated exact-paper campaign plan under
   `doc/reports/campaign_plans/` describing the candidate batch runs and their
   purpose.
6. Create the exact-paper campaign config package and dedicated PowerShell
   launcher with repository-style logging and operator usage notes.
7. Update the canonical reports and usage guide so the new batch-run path is
   visible as the correct execution surface for this branch.
8. Validate the new Python scripts, touched Markdown scope, and canonical
   Sphinx portal integration before closing the task.
