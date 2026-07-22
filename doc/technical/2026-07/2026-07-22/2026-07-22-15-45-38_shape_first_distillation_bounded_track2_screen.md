# Shape-First Distillation Bounded TE Curve Verification Screen

## Overview

This document defines the bounded `TE Curve Verification Pipeline` screen for
the completed `shape_first_training_rule_distillation_pilot_2026_07_22`
campaign. The pilot produced one time-windowed GRU candidate and one
non-windowed harmonic MLP candidate on `polished_dataset`, setpoint inputs, and
the forward (`Fw`) surface.

The scalar pilot winner was the non-windowed harmonic MLP, but the closeout
kept promotion blocked until curve-first evidence compares both new candidates
against the accepted polished-setpoint forward baselines.

## Technical Approach

Create a narrow operator-launchable screen rather than a full official matrix
refresh. The screen will evaluate only `polished_dataset`, setpoint inputs, and
forward curves. It will use the repository's existing
`reference_family_vs_feedforward` matrix runner and the shape-gated reranker.

The candidate set is:

- `polished_setpoints_periodic_gru_sequence_Fw`;
- `polished_setpoints_periodic_mlp_harmonic_Fw`;
- `shape_first_distilled_periodic_gru_sequence_fw`;
- `shape_first_distilled_periodic_mlp_harmonic_fw`.

The two new candidates will be loaded from their family registries under
`output/registries/families/`. The two comparison baselines will continue to
use the existing polished setpoint model archives under `models/`.

The launcher must support:

- local preflight only;
- local execution;
- remote preflight only;
- remote execution through the LAN workstation.

The launcher preparation must not execute the heavy matrix. It will provide the
exact local and `-Remote` operator commands, and the run will be inspected only
after the user reports completion.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `scripts/campaigns/track_2/`
- `doc/scripts/campaigns/track_2/`
- `doc/reports/campaign_plans/cross_wave/shape_first_training_rule_distillation/`
- `doc/running/active_training_campaign.yaml`
- `output/registries/families/shape_first_distilled_periodic_gru_sequence_fw/`
- `output/registries/families/shape_first_distilled_periodic_mlp_harmonic_fw/`
- `models/polished_dataset/setpoints/periodic_gru_sequence/forward/`
- `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/`

## Implementation Steps

1. Create a bounded matrix YAML for the four-candidate `polished_dataset`
   setpoint `Fw` screen.
2. Create a dedicated PowerShell launcher under `scripts/campaigns/track_2/`
   with local and `-Remote` modes.
3. Create the matching launcher note under `doc/scripts/campaigns/track_2/`.
4. Create a planning report under `doc/reports/campaign_plans/`.
5. Update `doc/running/active_training_campaign.yaml` with the prepared screen
   state, expected outputs, protected files, and launch commands.
6. Register the technical document, plan, launcher note, and matrix config from
   `doc/README.md`.
7. Run preflight only and static validation for the prepared package without
   launching the matrix.
8. Provide the exact local and remote launch commands for the operator.
