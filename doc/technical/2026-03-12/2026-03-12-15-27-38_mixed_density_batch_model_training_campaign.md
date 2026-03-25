# Mixed Density Batch Model Training Campaign

## Overview

The user requested a new comparative training campaign that goes beyond the previously tested one-factor-at-a-time variants.

The specific intent is to explore mixed configurations that combine:

- longer optimization schedules, because `high_epoch` was the strongest result so far;
- denser point sampling, including:
  - `point_stride = 10`
  - `point_stride = 5`
  - `point_stride = 1`
- larger effective batch sizes;
- larger feedforward model capacity.

This is a more ambitious campaign than the previous baseline-vs-variant comparison and should therefore be planned explicitly before execution.

## Technical Approach

The previous campaign showed that:

- longer training helped clearly;
- denser point sampling alone did not automatically improve held-out test performance;
- the heaviest all-at-once configuration did not become the best default.

The next step should therefore be a structured mixed campaign, not a random escalation of all parameters at once.

The campaign should be organized in three phases over the same three density levels:

### Phase 1 - Density Plus Long Schedule

Purpose:

- isolate the interaction between denser point sampling and the strongest optimization schedule found so far.

Planned variants:

1. `stride10_long`
   - `point_stride = 10`
   - long epoch schedule aligned with `high_epoch`
   - standard feedforward architecture
   - conservative batch size
2. `stride5_long`
   - `point_stride = 5`
   - long epoch schedule aligned with `high_epoch`
   - standard feedforward architecture
   - conservative batch size
3. `stride1_long`
   - `point_stride = 1`
   - long epoch schedule aligned with `high_epoch`
   - standard feedforward architecture
   - conservative batch size adjusted to remain realistic for full-density data

### Phase 2 - Density Plus Long Schedule Plus Larger Batch

Purpose:

- test whether the denser variants benefit from smoother gradients and better GPU utilization.

Planned variants:

4. `stride10_long_large_batch`
5. `stride5_long_large_batch`
6. `stride1_long_large_batch`

Important note:

- "larger batch" should mean larger than the conservative phase-1 version for the same density;
- it should not force the exact same batch size for all three densities if that would be unrealistic for memory.

### Phase 3 - Density Plus Long Schedule Plus Larger Batch Plus Larger Model

Purpose:

- test whether extra model capacity becomes useful only after the data density and batch regime have already been strengthened.

Planned variants:

7. `stride10_long_large_batch_big_model`
8. `stride5_long_large_batch_big_model`
9. `stride1_long_large_batch_big_model`

This produces a final grid of `9` new runs, which is large but still interpretable and technically motivated.

## Proposed Parameter Logic

The campaign should use the `high_epoch` schedule as the default optimization backbone because it was the best performer in the previous comparison.

The long-schedule backbone should therefore remain close to:

- `min_epochs: 20`
- `max_epochs: 250`
- `patience: 35`

The standard-capacity model should remain:

- hidden layers `128-128-64`

The larger-capacity model should remain close to the previously tested heavier network:

- hidden layers `256-256-128-64`

The batch logic should stay density-aware:

- `stride = 10`
  can support the largest curve batch among the three density levels;
- `stride = 5`
  should use a medium-large curve batch;
- `stride = 1`
  should use the most conservative curve batch because it is the most memory-expensive case.

This means the campaign should not force one identical `curve_batch_size` across all densities. Doing so would be less scientific because it would mix the intended study with avoidable out-of-memory risk.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index for the technical-document set.
- `doc/reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md`
  Current comparison report showing that `high_epoch` is the strongest reference so far.
- `doc/technical/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md`
  This technical planning document.
- `config/feedforward_network_training_high_epoch.yaml`
  Best current schedule reference.
- `config/feedforward_network_training_high_density.yaml`
  Existing denser-sampling reference.
- `config/feedforward_network_training_high_compute.yaml`
  Existing larger-model reference.
- `training/train_feedforward_network.py`
  Single training entry point to reuse for the campaign.
- `output/training_runs/feedforward/`
  Artifact root where the new experiment folders would be generated after approval.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, create the `9` YAML configurations required for the three-phase campaign.
3. Keep the long optimization schedule aligned with the current `high_epoch` winner so the campaign focuses on mixed effects rather than restarting from a weaker schedule.
4. Execute the runs in phase order:
   - Phase 1 first;
   - Phase 2 second;
   - Phase 3 third.
5. For each run, collect:
   - best checkpoint;
   - validation metrics;
   - held-out test metrics;
   - terminal log;
   - output report artifact.
6. Produce a new comparison report that includes:
   - the previous `trial`, `baseline`, `high_density`, `high_epoch`, and `high_compute` runs as context;
   - the `9` new mixed configurations as the main result set.
7. Identify which combination is the best current workstation-scale feedforward configuration.
8. Create the required Git commit immediately after the approved campaign summary documentation is completed.
