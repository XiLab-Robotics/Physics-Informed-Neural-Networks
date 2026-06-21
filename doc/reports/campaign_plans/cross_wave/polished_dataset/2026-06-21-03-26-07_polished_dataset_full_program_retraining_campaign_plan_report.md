# Polished Dataset Full Program Retraining Campaign Plan

## Campaign Status

Preliminary planning only. No queue, launcher, active campaign state, or
training execution is authorized until this plan and its technical document
are explicitly approved.

## Objective

Retrain and reevaluate the repository-owned Transmission Error model program
using `polished_dataset` as the default source of real pointwise operating
measurements.

Each polished point uses:

```text
inputs = [theta, theta_dot, tau_load, T]
target = theta_TE
```

The program must retain `simplified_dataset` as a selectable compatibility
mode, but all new campaign runs in this plan use `polished_dataset`.

## Excluded Training Surfaces

The following remain frozen and are not retrained:

- recovered paper-original workflow;
- `rcim_original` model archives;
- paper-retuned / `rcim_retuned` model archives;
- their best-parameter registries and source artifacts.

These models may remain visible as fixed historical comparison baselines in
Track 2, clearly labeled as non-polished and non-retrained.

## Included Training Surfaces

The intended scope starts with repository-owned Track 1 and includes all later
implemented learned families:

- Track 1 repository reimplementation and harmonic workflows;
- Wave 1 feedforward, tree, harmonic, periodic, residual, directional, and HPO
  surfaces;
- Wave 2.1 temporal convolution, GRU, and LSTM;
- Wave 2.2 periodic temporal convolution, periodic GRU, and periodic LSTM;
- Wave 2.3 residual harmonic GRU and LSTM variants;
- Wave 3.1 sequential residual-offset models;
- Wave 3.2 harmonic residual-offset models;
- Wave 3.3 curve-aware objective models;
- later robust, probabilistic, mixture-density, harmonic-prior, and
  latent-state / hysteresis families currently registered in the program.

The current configuration inventory contains 21 distinct model types. Final
queue generation must derive its family list from canonical registries and
approved completed-campaign manifests rather than from this prose alone.

## Staged Execution Strategy

### Stage 0: Dataset Compatibility Gate

- implement both dataset schemas;
- validate polished file discovery and column contracts;
- validate forward, backward, and global manifests;
- validate file-level split determinism and leakage prevention;
- validate point and sequence batches;
- validate dynamic input dimension `4` for polished and legacy dimension `5`
  for simplified;
- run no real training.

### Stage 1: Minimal Training Smoke Matrix

Run one bounded smoke configuration for each execution class:

- pointwise neural;
- tree;
- harmonic/static;
- temporal sequence;
- residual harmonic sequence;
- curve-aware / probabilistic;
- Track 1 harmonic-target derivation;
- export and reload;
- Track 2 inference adapter.

Stage 1 must pass before generating the full queue.

### Stage 2: Track 1 Retraining

Retrain repository-owned Track 1 surfaces from polished directional curves.
Keep paper-original and paper-retuned code and artifacts frozen.

### Stage 3: Wave 1 Retraining

Retrain static and structured baselines across approved `global`, `Fw`, and
`Bw` surfaces, including the directional and high-order harmonic variants that
remain part of the canonical program.

### Stage 4: Wave 2 Retraining

Retrain temporal, periodic-temporal, and residual-harmonic temporal families.
Sequence construction must preserve polished row order.

### Stage 5: Wave 3 And Later Retraining

Retrain offset-aware, curve-aware, robust, probabilistic, mixture-density,
harmonic-prior, and latent-state families in chronological dependency order.

### Stage 6: Normal Closeout

For every stage:

- generate campaign leaderboard and best-run artifacts;
- update family and program registries without deleting simplified results;
- produce Markdown and validated PDF campaign-results reports;
- synchronize the Training Results Master Summary and TE Program Status And
  Closeout Ledger;
- clear active campaign state before the next stage.

### Stage 7: Separate Track 2 Refresh

After all retraining stages are closed, prepare a separate operator-run Track 2
launcher with local and `-Remote` modes.

Track 2 must:

- evaluate polished-trained candidates with the four-feature schema;
- preserve separate global, Fw, and Bw surfaces;
- use the multi-index curve-first selection policy;
- retain paper-original and paper-retuned models only as frozen historical
  references;
- never feed filename setpoints into polished-trained candidates.

## Artifact Policy

New artifacts use immutable run-instance directories and include dataset
metadata:

```text
dataset_id: polished_dataset
dataset_schema: polished_point_v1
input_feature_names:
  - theta
  - theta_dot
  - tau_load
  - T
target_feature_names:
  - theta_TE
input_feature_dim: 4
```

Existing simplified results remain immutable. New polished family registry
entries must be distinguishable from prior simplified entries.

## Campaign Package Required After Approval

Approval of this preliminary plan authorizes preparation, not execution, of:

- stage-specific campaign YAML files;
- a dedicated PowerShell launcher under `scripts/campaigns/` supporting local
  and `-Remote` execution;
- a matching launcher note under `doc/scripts/campaigns/`;
- `doc/running/active_training_campaign.yaml` state;
- exact local and remote launch commands;
- queue validation and dry-run checks.

The user must run the launcher and report stage completion before results are
inspected or the next stage is activated.

## Acceptance Criteria

- default dataset selection is polished in every active non-paper-original
  workflow;
- simplified selection remains operational;
- no polished input value is taken from a filename;
- all included model execution classes pass smoke validation;
- each retraining stage closes normally before the next starts;
- no excluded paper-original or paper-retuned model is retrained;
- final Track 2 artifacts clearly separate schema, dataset, direction, and
  model provenance.
