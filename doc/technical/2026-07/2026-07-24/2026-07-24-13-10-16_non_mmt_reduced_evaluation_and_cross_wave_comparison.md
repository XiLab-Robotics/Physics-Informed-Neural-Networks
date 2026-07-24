# Non-MMT Reduced Evaluation And Cross-Wave Comparison

## Overview

This technical document prepares the next non-MMT model-development step after
Wave 5.2 MMT was deferred to an inactive future TODO.

The repository already contains the active setpoint matrices for
`polished_dataset` and `simplified_dataset`, the active polished
`actual_values` matrix, and all six expected polished actual-values sparse RCIM
temporal archives:

- `residual_harmonic_gru_sequence_sparse_rcim`: `global`, `Fw`, and `Bw`;
- `residual_harmonic_lstm_sequence_sparse_rcim`: `global`, `Fw`, and `Bw`.

The next step is a non-training reduced TE Curve Verification Pipeline
evaluation followed by an interim cross-wave comparison. It will consolidate
the surviving active model families, simple anchors, and selected RCIM
references without reopening MMT, Wave 4.3, Wave 4.4, or Wave 5.1 as active
training roads.

This document authorizes planning only. It does not authorize execution of the
heavy matrix, model training, registry promotion, or official baseline changes.
No subagent is planned.

## Technical Approach

### Evaluation Surfaces

Prepare six direction-separated report cells:

| Dataset | Input mode | Surface |
| --- | --- | --- |
| `polished_dataset` | `setpoints` | `Fw` |
| `polished_dataset` | `setpoints` | `Bw` |
| `simplified_dataset` | `setpoints` | `Fw` |
| `simplified_dataset` | `setpoints` | `Bw` |
| `polished_dataset` | `actual_values` | `Fw` |
| `polished_dataset` | `actual_values` | `Bw` |

`global` remains paused for this reduced pass. The six available global RCIM
and model archives remain preserved for a later explicitly approved global or
final cross-wave pass.

### Candidate Policy

Each applicable dataset and input-mode cell will keep:

- `periodic_gru_sequence`;
- `periodic_mlp_harmonic`;
- `wave4_1_mae_robust_loss`;
- `wave4_2_quantile_p10_p50_p90`;
- `feedforward`, `tree`, and `harmonic_regression` anchors.

The polished actual-values cells will additionally expose the archived sparse
RCIM `GRU` and `LSTM` temporal references. Polished paper-bank `ET19` and
`GBM19` anchors may remain visible where their dataset and inference contracts
are valid.

Candidate inclusion must resolve through immutable archive inventories or
dataset-scoped registry entries. Direction, dataset, input mode, and inference
shape must be asserted before execution.

### Selection And Reporting

The evaluation will follow the canonical multi-index curve-first policy:

- raw curve error;
- mean-centered shape fidelity;
- offset and continuity behavior;
- harmonic amplitude and phase fidelity;
- robustness and worst-condition behavior;
- visual evidence;
- deployment readiness.

Scalar `MAE`, matrix percentage error, or registry rank alone cannot promote a
candidate.

The first pass will generate the six reduced matrices and their machine-readable
per-curve evidence. A multi-index reranking and interim cross-wave report will
then compare families without collapsing `Fw` and `Bw` into one destructive
ranking.

Visual collage and overlay generation remains conditional: it becomes required
if the reduced matrix changes a recommendation, produces a material
raw-versus-shape disagreement, or is promoted into an official verification
decision.

### Operator Execution Gate

The existing reduced launcher and note will be revised rather than duplicated:

- `scripts/campaigns/track_2/run_reduced_selected_track2_reports.ps1`;
- `doc/scripts/campaigns/track_2/run_reduced_selected_track2_reports.md`.

The launcher must:

- dry-run without evaluation by default;
- run all six cells locally only with an explicit execution switch;
- support `-Remote`;
- sync required source, configuration, archive inventories, and documentation
  before remote execution;
- sync matrices, per-curve artifacts, logs, reranking outputs, and reports
  after completion;
- accept the repository's current `closed` campaign state;
- preserve resumable per-cell execution and immutable output suffixes.

Codex will prepare and validate the launcher but will not run the heavy matrix.
After preparation, the exact local and `-Remote` commands will be provided and
execution will pause until the user confirms completion.

## Involved Components

Canonical policy and status:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`.

Existing matrix inputs:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/selected_active_track2_polished_setpoints_matrix.yaml`;
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/selected_active_track2_simplified_setpoints_matrix.yaml`;
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/selected_active_track2_polished_actual_values_matrix.yaml`;
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reduced_selected_track2_matrix.yaml`.

Launcher and execution support:

- `scripts/campaigns/track_2/run_reduced_selected_track2_reports.ps1`;
- `doc/scripts/campaigns/track_2/run_reduced_selected_track2_reports.md`;
- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`;
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`.

Expected outputs after later execution:

- six dated reports under
  `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/`;
- matrix and per-curve artifacts under
  `output/validation_checks/track2_reference_comparison/`;
- operator logs under
  `output/validation_checks/track2_operator_launch_logs/`;
- a dated interim cross-wave analysis report;
- multi-index ranking and decision artifacts.

Protected-state check:

- `doc/running/active_training_campaign.yaml` is `closed`;
- `protected_file_list` is empty;
- this workflow is non-training and must not reopen campaign state.

## Implementation Steps

1. Obtain explicit approval of this registered technical document.
2. Audit every proposed archive inventory, direction, input mode, ONNX or
   Python artifact, and inference contract.
3. Replace the stale candidate routing in the reduced launcher with the three
   selected-active matrices and six approved report cells.
4. Add the polished actual-values sparse RCIM temporal references to the
   applicable `Fw` and `Bw` matrix cells.
5. Harden the launcher for the current closed-state gate, deterministic
   per-cell output suffixes, resume behavior, local execution, and `-Remote`.
6. Update the launcher note with dry-run, local, remote, resume, artifact, and
   failure-recovery instructions.
7. Validate YAML, PowerShell syntax and dry-run behavior, source coverage,
   candidate directionality, archive existence, and remote synchronization
   manifests.
8. Run Markdown QA, final-newline checks, and a warning-free Sphinx build.
9. Stop and request explicit approval before committing the prepared launcher
   package.
10. After commit approval, provide the exact local and `-Remote` commands and
    wait for the user to run the heavy evaluation.
11. After the user reports completion, inspect the six matrix outputs and run
    the multi-index curve-first reranking.
12. Generate the interim cross-wave report and conditional visual companions.
13. Synchronize backlog, ledger, master summary, and official decision
    surfaces only if the validated evidence changes current truth.
