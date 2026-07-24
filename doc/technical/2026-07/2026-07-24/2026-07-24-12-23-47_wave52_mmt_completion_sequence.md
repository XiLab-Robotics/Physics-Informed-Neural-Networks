# Wave 5.2 MMT Completion Sequence

## Overview

This technical document defines the evidence-gated implementation sequence for
continuing the `Wave 5.2` MMT branch after the completed residual-explanatory
provenance audit.

The existing diagnostic closed as
`blocked_by_missing_training_residuals`. The four accepted frozen baselines
resolved successfully, but the configured residual source contained held-out
test rows only. The immediate implementation requirement is therefore a
non-training residual replay over the exact training and validation manifests,
followed by a leakage-safe rerun of the MMT explanatory comparison.

The sequence preserves three evidence classes:

- reference-backed MMT relationships from `MMT_TEModeling.pdf`;
- repository-implemented equation-chain and baseline-inference behavior;
- open hypotheses about whether MMT signatures explain residual offset,
  centered shape, harmonic amplitude, phase, peak-to-peak behavior, or
  derivative error.

No new model training is authorized by this document. A passing explanatory
gate may justify a later MMT feature, auxiliary-output, residual-model, or weak
soft-constraint proposal, but that proposal will require its own technical
document, campaign plan when training is involved, and explicit approval.

No subagent is planned. If subagent review becomes useful, its name, reason,
and exact task boundary will be documented and presented for explicit approval
before launch.

## Technical Approach

### Step 1: Frozen-Baseline Residual Replay

Implement a repository-owned, non-training replay path for these accepted
`polished_dataset` setpoint baselines:

| Surface | Architecture | Candidate |
| --- | --- | --- |
| `Fw` | windowed | `polished_setpoints_periodic_gru_sequence_Fw` |
| `Fw` | non-windowed | `polished_setpoints_periodic_mlp_harmonic_Fw` |
| `Bw` | windowed | `polished_setpoints_periodic_gru_sequence_Bw` |
| `Bw` | non-windowed | `polished_setpoints_periodic_mlp_harmonic_Bw` |

The replay will:

- resolve archived baseline provenance without changing checkpoints;
- reconstruct the original training, validation, and test manifests;
- run inference only on the exact requested split rows;
- preserve direction, operating condition, angle order, dataset input mode,
  encoder-zeroing context, and `DataValid` filtering;
- emit the same per-curve residual schema required by the existing MMT
  residual-explanatory diagnostic;
- refuse random split substitution, target-derived inference inputs, or
  calibration on validation and test targets;
- record row-count, split-coverage, candidate-coverage, and manifest-alignment
  audits.

This step will produce a dated analytical report and machine-readable
artifacts. It will not update model registries or active campaign state.

### Step 2: Leakage-Safe MMT Explanatory Rerun

After Step 1 passes validation, rerun the existing MMT explanatory workflow
with training, validation, and held-out residual coverage.

The comparison will keep `Fw` and `Bw`, windowed and non-windowed baselines,
and the following evidence arms separate:

1. operating metadata only;
2. geometry-locked MMT signatures;
3. train-only calibrated equivalent-error signatures;
4. metadata plus allowed MMT signatures;
5. shuffled-signature controls.

Fitting is allowed on training residuals only. Validation may guide bounded
selection, and the test split remains final held-out evidence. The result must
report raw error, offset, centered shape, harmonic amplitude, harmonic phase,
peak-to-peak behavior, and derivative-related residual targets separately.

The decision gate requires held-out explanatory value beyond metadata-only and
shuffled controls, stable sign or direction where applicable, causal runtime
availability, and evidence across more than one residual view. A single scalar
improvement is insufficient.

### Step 3: Conditional Wave 5.2 Decision

The Step 2 report will record exactly one outcome:

- `diagnostic_only`: MMT does not add stable held-out value;
- `feature_or_auxiliary_pilot_justified`: a compact causal MMT path is
  supported;
- `blocked_by_parameter_availability`: residual coverage is valid but required
  contact geometry or equivalent-error inputs remain unavailable.

If the result is `feature_or_auxiliary_pilot_justified`, implementation stops
at a new proposal. Before any training:

- create and register a new technical document;
- create a preliminary campaign plan under `doc/reports/campaign_plans/`;
- prepare the required campaign configuration and local/remote launcher only
  after explicit approval;
- preserve both windowed and non-windowed comparisons unless the Step 2
  evidence explicitly closes one branch.

Full PINN and `Wave 6` work remain deferred until a compact MMT feature or
auxiliary-output path proves useful.

### Reporting And Commit Boundaries

Each completed implementation step will include:

- a technical or analytical Markdown report;
- machine-readable result and validation artifacts;
- required backlog, ledger, master-summary, usage-guide, or Sphinx updates
  when the result changes those canonical surfaces;
- repository QA appropriate to the touched files;
- two concise user-facing status lines stating the completed outcome and the
  next gate;
- one narrow Git commit after validation, as explicitly requested by the user.

The technical-document approval remains the first gate. No implementation code
will be changed before explicit approval of this document.

## Involved Components

Primary reference and design inputs:

- `reference/MMT_TEModeling.pdf`;
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`;
- `doc/technical/2026-07/2026-07-23/2026-07-23-21-44-26_wave52_mmt_residual_explanatory_diagnostic.md`;
- `doc/reports/analysis/model_development_waves/wave_5_2/mmt_residual_explanatory_diagnostic/[2026-07-24]/wave52_mmt_residual_explanatory_diagnostic.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`.

Expected Step 1 implementation surfaces after approval:

- a residual-replay builder under `scripts/reports/analysis/`;
- a non-training configuration under `config/analysis/`;
- machine-readable artifacts under
  `output/validation_checks/wave52_frozen_baseline_residual_replay/`;
- a dated report under
  `doc/reports/analysis/model_development_waves/wave_5_2/`;
- documentation registration and status synchronization as required by the
  validated result.

Expected Step 2 implementation surfaces after approval:

- the existing
  `scripts/reports/analysis/build_wave52_mmt_residual_explanatory_diagnostic.py`;
- the existing
  `config/analysis/wave52_mmt_residual_explanatory_diagnostic.yaml`;
- new dated artifacts under
  `output/validation_checks/wave52_mmt_residual_explanatory_diagnostic/`;
- a new dated analytical report and synchronized canonical decision surfaces.

Protected-state check:

- `doc/running/active_training_campaign.yaml` currently reports `closed`;
- `protected_file_list` is empty;
- Step 1 and Step 2 are non-training workflows and will not reopen or replace
  that closed campaign state.

## Implementation Steps

1. Obtain explicit approval of this registered technical document.
2. Inspect the four baseline inventories, training snapshots, loaders,
   prediction utilities, and existing residual schema.
3. Use Context7 before making version-sensitive PyTorch, PyTorch Lightning,
   NumPy, SciPy, or scikit-learn implementation choices.
4. Implement the frozen-baseline residual replay with explicit split,
   provenance, direction, and input-mode assertions.
5. Add a bounded self-test or fixture that proves split isolation and residual
   schema compatibility.
6. Run the replay for the exact training and validation manifests.
7. Generate and inspect machine-readable coverage, provenance, residual, and
   validation artifacts.
8. Generate the Step 1 analytical report and synchronize canonical status
   files only where the replay result changes current truth.
9. Validate Python syntax, relevant self-tests, YAML and CSV parsing, touched
   Markdown, final newlines, and Sphinx when portal scope changes.
10. Run commit preflight, check files over `100 MB` and staged aggregate size,
    then create the narrow Step 1 commit requested by the user.
11. Emit two concise status lines covering the Step 1 outcome and Step 2 gate.
12. Configure and rerun the MMT residual-explanatory diagnostic using the
    validated replay artifacts.
13. Fit explanatory comparisons on training residuals only and evaluate
    validation and held-out test evidence against metadata-only and shuffled
    controls.
14. Generate the Step 2 report, decision summary, machine-readable artifacts,
    and required canonical status synchronization.
15. Repeat the required code, artifact, Markdown, PDF if applicable, Sphinx,
    and commit preflight checks, then create the narrow Step 2 commit.
16. Emit two concise status lines covering the MMT gate outcome and the
    authorized next branch.
17. If a training pilot is justified, stop and create the next technical
    document and campaign plan for explicit approval before implementation or
    launch.
