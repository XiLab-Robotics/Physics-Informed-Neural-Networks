# Post-Retraining Model Archive Promotion

## Overview

This technical document defines the first curated promotion into `models/`
after commit `bebb1d3613adac7c52fe1fabb384344a9e181d2e`. It also preserves the
selection analysis as the canonical restart point for future model-archive
refreshes.

The current `models/` tree is unchanged between that commit and `HEAD`. Its
contract is to retain the best model-development export for each meaningful
family and surface, with source-run provenance stored in leaf-local inventory
files. It is not a mirror of every training checkpoint.

The post-retraining history contains many completed pilots, PINN formulations,
controls, ablations, negative-result campaigns, synthetic oracles, and repeated
seeds. The approved selection boundary is therefore limited to candidates that
have a distinct reusable role, strong curve-first evidence, and sufficient
artifact provenance to justify canonical preservation.

No subagent is planned or authorized. The active campaign state is completed
and its protected-file list is empty. This document and its index registration
must receive explicit user approval before any model artifact, exporter,
inventory, report, guide, or portal file is modified.

## Technical Approach

### Canonical Promotion Set

The proposed promotion contains five dataset, input-mode, family, and surface
leaves.

| Family | Surface | Selected artifact | Archive role |
| --- | --- | --- | --- |
| `temporal_analytical_residual_k01` | `forward` | K01 seed `271828` | Cross-surface temporal offline leader |
| `temporal_analytical_residual_k01` | `backward` | K01 seed `271828` | Cross-surface temporal offline leader with peak-to-peak caveat |
| `temporal_analytical_residual_k01` | `global` | K01 seed `271828` | Direction-aware cross-surface temporal offline leader |
| `complex_harmonic_coefficient_h08` | `forward` | H08 seed `161803` | Preserved non-temporal forward offline specialist |
| `complex_harmonic_coefficient_h04` | `forward` | Stage 15 H04 artifact | Compact interpretable grey-box specialist |

The target layout is:

```text
models/polished_dataset/setpoints/
  temporal_analytical_residual_k01/
    forward/
    backward/
    global/
  complex_harmonic_coefficient_h08/
    forward/
  complex_harmonic_coefficient_h04/
    forward/
```

Only the selected checkpoint for each leaf will be archived. Alternate seeds
remain immutable robustness evidence in `output/training_runs/` and will be
referenced from provenance metadata rather than duplicated into `models/`.

### Promotion Rationale

K01 seed `271828` is the only new candidate accepted by the official
cross-surface multi-index curve-first decision on all three surfaces. It beats
the matched periodic GRU on raw error, offset, centered shape, derivative,
harmonic amplitude, harmonic phase, and closure for the selected surfaces.
The backward peak-to-peak regression remains a mandatory recorded limitation.
Its deployment status is export-prepared and host-qualified; TwinCAT runtime
qualification remains pending.

H08 seed `161803` is retained only on the forward surface. It is compact,
inspectable, deterministic, ONNX-exportable, and useful for harmonic and shape
behavior. Its backward and global variants are excluded because their raw,
offset, and envelope regressions prevent a balanced cross-surface claim.

H04 is retained only on the officially verified forward surface. It is the
strongest compact grey-box result of Wave 5.2R, leads centered-shape,
derivative, and mean harmonic-phase metrics in Stage 15, and already has
Python/ONNX and float32 PLC-reference parity evidence. It remains exploratory
because it does not beat the accepted periodic GRU on raw error, offset, P95,
or peak-to-peak behavior. TwinCAT compilation and runtime replay remain open.

### Deferred Research Components

The following artifacts remain valuable future integration ingredients but
will stay under `output/` unless a later technical decision introduces an
explicit exploratory-component archive class:

| Candidate | Retained value | Current blocker |
| --- | --- | --- |
| Phase 3 `C1-Fw` | Most useful quasi-static compliance PINN and repeated-seed evidence | Behind accepted references; physical parameter not independently validated |
| Stage 10 `R00` | Extended condition library improves raw and mean error | Dense representation; not an interpretable physical law |
| Stage 10 `S01` | Concrete sparse correction candidate | Insufficient sparsity and sign stability |
| Stage 12 `F01` | Centered-shape and tail-error specialist | Offset, correction-bound, and state-consistency regressions |
| Stage 12 `S01` | Useful shape and tail tradeoff | Does not beat K01 or resolve chunk/state limitations |

A future archive extension for these candidates must add explicit metadata such
as `acceptance_status`, `intended_role`, and `known_limitations` so research
components cannot be confused with accepted or qualified model exports.

### Excluded Candidate Groups

The following groups will not be promoted by this refresh:

- shape-gate, shape-objective, shape-first distillation, and causal-offset
  pilots that were not promoted through the curve-first gate;
- Phase 2 harmonic/kinematic candidates and Phase 3 compliance candidates
  other than the deferred C1 research component;
- the negative Stage 4 capacity ladder;
- Stage 5 controls, ablations, and dominated variants other than H04 and H08;
- Stage 6 spectral/Sobolev, Stage 7 multi-head, and Stage 8 compliance-prior
  candidates, none of which produced a promoted component;
- Stage 9 controls, replays, and dominated temporal formulations other than
  K01;
- Stage 10 formulations other than the deferred R00 and S01 components;
- Stage 11 trust calibrators, which produced no qualified trust component;
- Stage 12 optimizers other than the deferred diagnostic F01 and S01 results;
- Stage 13 synthetic-oracle experiments, which certify implementation paths
  but are not real-data deployment candidates;
- non-selected stability seeds and internal analytical anchors.

### Artifact And Export Contract

Each promoted leaf must contain or reference:

- the selected immutable Python checkpoint;
- a deterministic ONNX export with fixed runtime tensor contracts;
- the source training configuration or promotion metadata;
- the selected metrics and official decision references;
- checkpoint and ONNX SHA-256 hashes;
- a `reference_inventory.yaml` file recording dataset, input mode, surface,
  candidate ID, seed, run instance, split signature, role, acceptance status,
  known limitations, and deployment status;
- parity evidence appropriate to the model family.

K01 requires an explicit stateful contract covering input history, hidden-state
input/output, reset behavior, chunk equivalence, causal-prefix behavior, and
the runtime fallback boundary. H08 and H04 require inspectable analytical
anchor, coefficient-correction, coefficient-output, and curve-reconstruction
metadata.

The existing generic archive exporter primarily resolves Lightning `.ckpt`
and tree-model artifacts. These candidates use custom `best_model.pt`
checkpoints and dedicated ONNX preparation paths. The implementation must
extend or add repository-owned export handling without weakening the existing
archive behavior.

### Verification And Deployment Boundary

Archive promotion means that a candidate is canonically preserved for its
documented role. It does not automatically mean that the candidate is the
program-best model or TwinCAT deployment-ready.

Required closure checks include:

- exact source-run and selected-seed resolution;
- checkpoint hash and provenance verification;
- Python replay against saved predictions;
- ONNX structural validation and numerical parity;
- K01 hidden-state and chunk-contract validation;
- H04 and H08 coefficient and reconstructed-curve parity;
- inventory schema validation and aggregate inventory regeneration;
- confirmation that only the five approved leaves are added;
- no mutation or removal of the accepted periodic GRU and periodic harmonic
  MLP archives;
- clear status labels separating offline leader, forward specialist, and
  exploratory grey-box roles.

H04 static Structured Text parity and the K01/H08 host latency proxies are
supporting evidence only. TwinCAT compilation, target download, TF3820 or
TF38x0 runtime execution, task-cycle timing, invalid-input handling, online
`DataValid` replay, and compensation-loop commissioning remain separate gates.

### Future Restart Rule

Future model implementations should restart archive selection from this
document and compare new candidates against the five-leaf promotion set plus
the retained periodic GRU and periodic harmonic MLP references.

A future model should enter `models/` only when it satisfies at least one
non-redundant role:

1. accepted or qualified cross-surface leader;
2. officially supported surface specialist;
3. compact and interpretable deployment-research specialist with verified
   parity;
4. explicitly classified exploratory component required by an approved future
   integration roadmap.

Repeated seeds, controls, ablations, negative results, synthetic-only oracles,
and diagnostic calibrators remain in `output/` unless a later approved archive
policy explicitly changes their classification.

## Implementation Outcome

The approved implementation completed on 2026-07-31. A dedicated exporter now
rebuilds all five leaves in
`output/validation_checks/post_retraining_model_archive_promotion/`, validates
them, and promotes them only with the explicit `--promote` option. It refuses
to overwrite an existing destination family root.

The promoted artifact hashes are:

| Family | Surface | Checkpoint SHA-256 prefix | ONNX SHA-256 prefix |
| --- | --- | --- | --- |
| K01 | `forward` | `970c667aa734` | `250b62f9132d` |
| K01 | `backward` | `0b35b4ef37bc` | `fdbe29c35b8e` |
| K01 | `global` | `9ebf48190775` | `8858976d0533` |
| H08 | `forward` | `5167df19b729` | `d8c8fa5d86b7` |
| H04 | `forward` | `61732ac19b69` | `fadc9e5c0dde` |

Checkpoint replay, full held-out-surface ONNX parity, and inventory hash checks
passed. H04 additionally retains its passed static float32 PLC-reference
package. The final polished-setpoint inventory contains 113 leaves: 39
forward, 37 backward, and 37 global. The five new bundles occupy approximately
5.25 MB in total.

The promotion deliberately left the deferred components and all rejected
groups under `output/`. It did not modify the accepted periodic GRU or periodic
harmonic MLP leaves, accepted registries, or deployment-leader decisions.

## Involved Components

- `models/polished_dataset/setpoints/`
  Destination for the five new canonical model leaves.
- `models/README.md`
  Archive contract and family-role documentation if clarification is required.
- `models/polished_dataset/setpoints/model_development_export_inventory.yaml`
  Aggregate inventory to regenerate after successful leaf creation.
- `scripts/models/export_dataset_model_archives.py`
  Existing generic archive exporter whose checkpoint assumptions must be
  preserved or extended safely.
- `scripts/models/causal_temporal_analytical_residual_network.py`
  K01 model and stateful inference contract.
- `scripts/models/complex_harmonic_coefficient_residual_network.py`
  H04 and H08 structured coefficient model contract.
- `output/training_runs/temporal_analytical_residual_models/`
  Source checkpoints and metadata for selected K01 surfaces.
- `output/training_runs/complex_harmonic_coefficient_residuals/`
  Source checkpoints and metadata for selected H04 and H08 artifacts.
- `output/validation_checks/wave52r_offline_leader_promotion/`
  K01 and H08 ONNX, causality, state, parity, latency, and fallback evidence.
- `output/validation_checks/wave52r_stage15_deployment_parity/`
  H04 ONNX and PLC-reference parity package.
- `output/analysis/wave_5_2r/offline_leader_cross_surface_track2/`
  Official cross-surface multi-index decision and curve diagnostics.
- `doc/reports/analysis/model_development_waves/wave_5_2/`
  Canonical scientific, official-verification, and deployment-preparation
  evidence.
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
  Status surface to review because the canonical archive inventory changes.
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
  Status surface to review for archive-role and deployment-boundary alignment.
- `doc/guide/project_usage_guide.md` and `site/`
  User-facing and portal documentation to update only if archive discovery or
  export commands change.

## Implementation Steps

1. Register this technical document in `doc/README.md` and wait for explicit
   user approval.
2. Revalidate the completed campaign state, clean worktree, selected official
   decision, source checkpoint paths, seeds, surfaces, and SHA-256 hashes.
3. Define the exact custom `.pt` archive-export contract for K01, H08, and H04
   without changing existing Lightning and tree-model behavior.
4. Stage the five approved archive leaves outside `models/`, including Python
   artifacts, ONNX exports, provenance snapshots, metrics, decision pointers,
   hashes, role labels, limitations, and parity evidence.
5. Validate Python replay, ONNX inference and parity, K01 stateful behavior,
   and H04/H08 coefficient and curve reconstruction from the staged bundle.
6. Promote only the validated staged leaves into the approved canonical paths.
7. Generate leaf `reference_inventory.yaml` files and regenerate the polished
   setpoint aggregate inventory from leaf provenance.
8. Confirm that no non-selected seed, control, ablation, diagnostic, synthetic
   oracle, backward/global H08, or backward/global H04 artifact entered the
   archive.
9. Update `models/README.md`, the master summary, the closeout ledger, the
   project usage guide, and the Sphinx portal only where the implemented
   archive or runnable commands materially require synchronization.
10. Run Python syntax or targeted exporter tests, artifact hash and inventory
    validation, ONNX/parity checks, Markdown style and Markdownlint checks,
    the warning-free Sphinx build when portal sources change, final-newline
    checks, and `git diff --check`.
11. Report the exact promoted leaves, artifact sizes, hashes, parity results,
    known limitations, and any files deliberately left in `output/`; then stop
    for user review before any Git commit.
