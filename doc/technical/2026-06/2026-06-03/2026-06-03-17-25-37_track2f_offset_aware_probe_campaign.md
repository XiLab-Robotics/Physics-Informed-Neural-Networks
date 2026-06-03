# Track 2F Offset-Aware Probe Campaign

## Overview

This document plans the next gated step after `Track 2D` and `Track 2E`.

`Track 2D` showed that many direction-valid candidates have a meaningful
curve-level vertical offset component. `Track 2E` then tested whether that
offset is partly predictable from causal operating-condition groupings and
found `direction_torque` to be the strongest conservative aggregate signal
after excluding exact full-condition memorization.

The goal of `Track 2F` is to prepare a small direction-parallel offset-aware
probe campaign. The campaign should compare simple post-hoc causal offset
calibration, sequential residual-offset modeling, and multi-head
shape/offset training without changing the runtime input contract.

This document does not approve training execution. The matching campaign plan
must be approved first, then implementation can prepare YAML files, launcher
scripts, launcher notes, and active campaign state. Actual campaign launch
remains an operator action after the prepared package is approved.

## Technical Approach

The probe campaign should keep `Fw`, `Bw`, and `global` branches in parallel
and avoid collapsing them into one single winner.

The planned intervention families are:

- `posthoc_direction_torque_offset_baseline`: a non-learned causal aggregate
  offset baseline derived from the completed Track 2E finding;
- `sequential_residual_offset_probe`: a causal second-stage offset/residual
  predictor added after a selected base model prediction;
- `multi_head_shape_offset_probe`: one causal model with a shared trunk and
  separate centered-shape and offset / low-frequency heads summed into final
  TE.

The campaign must preserve these constraints:

- model inputs remain current point-level operating state, supported short
  causal history, or causal derived features;
- future TE samples and full-curve means are never supplied as runtime inputs;
- full curves are validation and selection units only;
- scalar `MAE` / `RMSE` remain sanity metrics, while `Track 2` curve-level
  raw, centered-shape, offset, amplitude, and phase diagnostics drive the
  final interpretation;
- `Fw`, `Bw`, and `global` each need their own branch verdict.

The implementation should start from a narrow probe rather than a full model
family expansion. A successful probe is one that shows stable curve-level
improvement and clarifies whether the next full campaign should be sequential,
multi-head, loss-reweighted, or non-offset-first.

## Involved Components

Expected planning and future implementation surfaces:

- campaign plan:
  `doc/reports/campaign_plans/track2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md`;
- future campaign configuration root:
  `config/training/track2f_offset_aware_probe/`;
- future dedicated launcher:
  `scripts/campaigns/track2/run_track2f_offset_aware_probe_campaign.ps1`;
- future launcher note:
  `doc/scripts/campaigns/track2/run_track2f_offset_aware_probe_campaign.md`;
- active campaign state:
  `doc/running/active_training_campaign.yaml`;
- future campaign output root:
  `output/training_campaigns/<run_instance_id>_track2f_offset_aware_probe_campaign`;
- post-campaign result report root:
  `doc/reports/campaign_results/track2/`.

Reference inputs:

- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`;
- `doc/reports/analysis/track2/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`;
- `output/validation_checks/track2e_offset_predictability_feasibility/2026-06-03-13-28-54__track2e_offset_predictability_feasibility/track2e_surface_intervention_recommendation.csv`;
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/Training Results Master Summary.md`.

## Implementation Steps

1. Create the preliminary `Track 2F` campaign plan report under
   `doc/reports/campaign_plans/track2/`.
2. Register the technical document and campaign plan from `doc/README.md`.
3. Wait for explicit user approval before preparing any campaign YAML files,
   launchers, launcher notes, active campaign state, or model/training code.
4. After approval, inspect existing Wave 2B / Wave 2C campaign configuration
   patterns and the current training infrastructure to choose the minimal
   implementable queue shape.
5. Prepare the campaign package with local and `-Remote` launcher commands,
   but do not start training from Codex.
6. Validate the prepared package with Python compile checks, scoped
   configuration inspection, and Markdown QA.
7. Stop again for launch approval and provide the exact local and remote
   operator commands.
