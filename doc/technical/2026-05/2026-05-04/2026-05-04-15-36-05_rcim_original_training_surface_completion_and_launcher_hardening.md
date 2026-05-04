# RCIM Original Training Surface Completion And Launcher Hardening

## Overview

This document plans the next repository-owned hardening pass for the recovered
original RCIM workflow and its dedicated paper-reference launchers.

The requested scope is to make the `rcim_original` training surface complete
enough for real operator use:

- restore the missing model families in `retune`;
- align `paper_eval` and `retune` to the intended family coverage;
- capture terminal output into persistent log files;
- improve launcher robustness and visible progress reporting;
- move raw run artifacts under `output/training_campaigns/rcim_original/`;
- reserve `models/paper_reference/rcim_original/` for curated closeout-time
  archives instead of live runtime dumps;
- fix the current mismatch where `paper_eval` produces only CSV artifacts
  rather than ONNX and Python model bundles.

## Technical Approach

The implementation will modify the repository-owned workflow under:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

and the repository-owned launchers under:

- `scripts/campaigns/paper_reference/rcim_original/`

The main design changes are:

1. Expand the family coverage logic in `training_models.py`.
   - `retune` should include `SVR` and `ELM`.
   - `paper_eval` should continue to include the full recovered set.
   - the emitted run summary should record the final resolved family list so
     the count is explicit in the artifacts.

2. Introduce persistent logging for launcher-run stdout/stderr.
   - each launcher should create a dedicated log file adjacent to the run
     artifact root;
   - operator terminal output should remain readable while the full stream is
     also persisted to disk for postmortem diagnosis.

3. Harden launcher shutdown behavior.
   - the launcher should tolerate heavy warning surfaces without depending on
     the VS Code integrated terminal to preserve the only copy of stdout;
   - the launcher should report the final Python exit code explicitly;
   - the launcher should print family/stage/run-root progress before and after
     each stage.

4. Split raw run artifacts from curated model archives.
   - launcher output roots should move from
     `models/paper_reference/rcim_original/.../source_runs/`
     to
     `output/training_campaigns/rcim_original/...`;
   - `models/paper_reference/rcim_original/forward` and
     `models/paper_reference/rcim_original/backward` should be treated as the
     future closeout-time destination for curated ONNX/Python model archives,
     not as live runtime roots.

5. Add an explicit export surface for paper-reference runs.
   - the current `paper_eval` branch only writes prediction CSVs;
   - if the user expects ONNX and Python artifacts from the same operator
     command, the workflow needs either:
     - a new combined mode that evaluates and exports, or
     - an orchestrated launcher sequence that runs both the `paper_eval`
       semantics and the export path in one controlled wrapper.

The least risky path is to keep the model logic in `predictorML.py` intact and
improve orchestration in the repository-owned wrapper plus launcher layer.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `models/paper_reference/rcim_original/`
- `output/training_campaigns/rcim_original/`

Protected campaign state acknowledged and intentionally left untouched:

- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Update `training_models.py` family-resolution rules so `retune` includes
   the missing `SVR` and `ELM` families and the emitted run metadata makes the
   final coverage obvious.
2. Add repository-owned progress prints around family execution so the active
   family index and family code are always visible in the terminal and in the
   persisted logs.
3. Add launcher-side logging that captures the full Python stdout/stderr into
   per-run log files placed beside the raw runtime artifact root.
4. Move launcher output roots to `output/training_campaigns/rcim_original/`
   while preserving a stable run-identifier naming policy.
5. Add a repository-owned training/export orchestration path so the final
   operator-visible commands can also generate ONNX and Python model artifacts
   instead of only prediction CSV files.
6. Update the workflow README and adjacent usage documentation to reflect the
   new run-root policy and the archive-versus-runtime split.
