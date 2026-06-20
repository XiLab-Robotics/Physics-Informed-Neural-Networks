# Wave 3.1 Sequential Residual-Offset Probe

## Overview

This document gates the first learned implementation step after the prepared
`Wave 3.1` offset-aware probe package.

The current `Wave 3.1` package contains nine descriptors, but only the
post-hoc `direction_torque` offset baseline is runnable as a validation entry.
The learned `sequential_residual_offset_probe` and
`multi_head_shape_offset_probe` entries are intentionally blocked because the
training runner does not yet support those model types.

This step implements the first learned branch:
`sequential_residual_offset_probe`.

The goal is not to change the runtime input contract. The model must still
consume current point-level operating state, supported short causal history, or
causal derived features only. Full curves remain validation and selection
units, not inference inputs.

## Technical Approach

The first implementation should be narrow and inspectable:

1. keep an existing TE base-prediction branch compatible with the current
   neural training stack;
2. add a second learned residual-offset branch that predicts a low-frequency
   or condition-level correction from causal inputs;
3. sum base prediction and residual-offset prediction into the final TE output;
4. expose structured branch outputs for diagnostics where the local model API
   already supports that pattern;
5. keep the first training loss compatible with the existing
   `TransmissionErrorRegressionModule`, then defer curve-level custom loss to
   a later dedicated gate unless the existing training flow already exposes
   the needed batch grouping safely.

The implementation should prefer reuse over a broad rewrite:

- reuse the existing Lightning training entrypoint
  `scripts/training/train_feedforward_network.py`;
- register the new model type in `scripts/models/model_factory.py` and
  `scripts/training/run_training_campaign.py`;
- use the existing data module and sequence-window support where causal
  history is needed;
- materialize initial Wave 3.1 queue YAML files from the prepared descriptors
  after the model type exists;
- leave `multi_head_shape_offset_probe` blocked until its own technical gate.

The first model can be implemented as a causal sequential residual branch
around a compact base predictor. The exact base predictor may be selected from
existing local components during implementation, but the output contract must
stay:

```text
final_te_prediction = base_te_prediction + residual_offset_prediction
```

The branch must not subtract the true full-curve mean at inference time. Any
offset signal used by the residual branch must be learned from runtime-safe
features such as direction, torque, speed, oil temperature, and supported
short causal history.

## Involved Components

Expected implementation targets:

- `scripts/models/model_factory.py`;
- a new or reused model module under `scripts/models/`;
- `scripts/training/train_feedforward_network.py`;
- `scripts/training/run_training_campaign.py`;
- `scripts/training/validate_training_setup.py`;
- `scripts/training/run_training_smoke_test.py`;
- `config/training/hydra/wave2/model_family/`;
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/`;
- `scripts/campaigns/track_2/prepare_track2f_offset_aware_probe_campaign.py`;
- `scripts/campaigns/track_2/run_track2f_offset_aware_probe_campaign.ps1`;
- `scripts/campaigns/track_2/validate_track2f_offset_aware_probe_package.py`;
- `doc/scripts/campaigns/track_2/run_track2f_offset_aware_probe_campaign.md`;
- `doc/running/active_training_campaign.yaml`.

Reference inputs:

- `doc/reports/campaign_plans/track_2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md`;
- `doc/technical/2026-06/2026-06-03/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign.md`;
- `doc/reports/analysis/track2/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`;
- `output/validation_checks/track2f_offset_aware_probe/2026-06-03_track2f_offset_aware_probe_prelaunch/track2f_probe_entry_status.csv`;
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`.

## Implementation Steps

1. Inspect the current model factory, Lightning module, data module, and
   campaign runner to confirm the smallest safe integration surface.
2. Use current PyTorch / Lightning documentation before implementing
   library-specific code paths.
3. Implement and register `sequential_residual_offset_probe` without changing
   existing model behavior.
4. Add or update focused smoke validation so the model can run one minimal
   train/validation/test pass through the shared training stack.
5. Convert the three Wave 3.1 sequential descriptors (`global`, `Fw`, `Bw`)
   into runnable campaign YAML entries while leaving the three multi-head
   descriptors blocked.
6. Update the Wave 3.1 launcher and launcher note so local execution can run
   the sequential probe entries and `-Remote` can use the canonical remote
   training campaign wrapper for the runnable queue only.
7. Update `doc/running/active_training_campaign.yaml` to protect the new
   runnable queue files and record the exact local and remote commands.
8. Run Python compile checks, model smoke checks, launcher preflight, and
   Markdown QA on touched documentation.
9. Stop before actual long training execution and provide the operator launch
   command.

## Protected Campaign Warning

`doc/running/active_training_campaign.yaml` currently marks the prepared
Wave 3.1 package as protected. After this technical document is approved, the
implementation will intentionally modify Wave 3.1 protected files so the
approved placeholders can become runnable sequential probe entries.

This is a controlled continuation of the prepared Wave 3.1 campaign, not an
unrelated edit to a running campaign.
