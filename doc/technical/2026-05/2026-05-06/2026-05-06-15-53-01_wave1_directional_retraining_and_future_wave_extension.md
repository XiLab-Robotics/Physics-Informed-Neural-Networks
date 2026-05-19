# 2026-05-06-15-53-01 Wave1 Directional Retraining And Future Wave Extension

## Overview

This document formalizes a new repository-wide training policy that follows
the now-correctly recovered RCIM paper perspective on dataset directionality.

The paper treats `forward` and `backward` as distinct modeling surfaces. A
fair comparison against the repository `Wave 1` families therefore cannot rely
only on the current global models trained with both directions combined.

The next `Wave 1` retraining scope must produce three repository-owned model
surfaces for each implemented family:

1. one `global` model trained on the current combined dataset;
2. one `Fw` model trained on the `forward` split only;
3. one `Bw` model trained on the `backward` split only.

The mandatory `Wave 1` families in scope are:

- `tree`
- `residual_harmonic_mlp`
- `feedforward`
- `periodic_mlp`
- `harmonic_regression`

This policy must then become the default preparation rule for future family
introductions from `Wave 2` onward, so later families are born with
`global` + `Fw` + `Bw` parity instead of needing a retrofit.

## Technical Approach

The implementation will treat the current dataset loader and split logic as
the source of truth for direction-aware training. The repository already has
canonical support for `use_forward_direction` and `use_backward_direction`,
so the new work should extend the existing training and campaign surface
rather than introduce a parallel pipeline.

The target policy is:

- every new family baseline must be defined as a logical family bundle with
  three required training variants: `global`, `Fw`, and `Bw`;
- `global` keeps the current repository behavior with both directions enabled;
- `Fw` enables only `forward`;
- `Bw` enables only `backward`;
- comparisons against paper-faithful directional baselines must use the
  directional variants, not only the global one;
- family registries, campaign winner artifacts, and summary reports must make
  the training scope explicit so `feedforward`, `feedforward_Fw`, and
  `feedforward_Bw` are distinguishable first-class entries.

To keep the implementation inspectable and future-proof, the directional
variant should be encoded explicitly in configuration metadata and run naming,
instead of being inferred later from artifact paths alone.

The implementation should also keep the currently running `Track 1`
paper-faithful campaign untouched. No protected file from
`doc/running/active_training_campaign.yaml` should be edited as part of this
work unless a later explicit approval says otherwise.

## Involved Components

- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `config/datasets/transmission_error_dataset.yaml`
- `scripts/datasets/transmission_error_dataset.py`
- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/train_tree_regressor.py`
- `scripts/training/tree_regression_support.py`
- `scripts/training/run_training_campaign.py`
- `config/training/`
- `scripts/campaigns/`
- `doc/reports/campaign_plans/`
- `output/registries/families/`
- `output/registries/program/`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/Training Results Master Summary.md`

No subagent is planned for this scope. If subagent help becomes useful later,
the proposed agent, delegated boundary, and approval requirement must be
declared before any launch.

## Implementation Steps

1. Create the dedicated campaign planning report for the `Wave 1`
   directional retraining package, including the exact candidate matrix and
   the launcher surface, but do not execute training yet.
2. Introduce a repository-owned directional training variant contract that
   records whether a run is `global`, `Fw`, or `Bw` in config metadata,
   run identity, and artifact/report outputs.
3. Extend the config-generation and campaign-preparation workflow so each
   selected family can materialize the required `global`, `Fw`, and `Bw`
   configs without duplicating training logic.
4. Prepare the `Wave 1` retraining package for the five implemented families,
   producing `15` training configs in total: `5` global, `5` `Fw`, and `5`
   `Bw`.
5. Generate the matching campaign YAML files, PowerShell launcher, launcher
   note, and campaign planning report for the approved retraining batch.
6. Ensure the registry and reporting surfaces can present directional winners
   clearly, without collapsing them into the existing global-only family best
   entries.
7. Update the canonical `Wave 1` and master-summary analysis documents after
   the retraining campaign is completed and the accepted winners are known.
8. Promote the directional-bundle rule into the future-family preparation
   workflow so new `Wave 2+` families are required to declare and prepare all
   three variants from the start.
