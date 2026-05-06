# Wave 1 Directional Retraining Campaign Plan Report

## Overview

Now that the RCIM paper perspective has been recovered correctly, the current
repository `Wave 1` family comparison is no longer fully fair against
direction-split paper-style reasoning.

The paper distinguishes `forward` and `backward` as separate modeling
surfaces. The current `Wave 1` baselines, instead, were selected primarily
from runs trained on the combined bidirectional dataset.

This campaign therefore prepares a directional retraining pass that keeps the
current best configuration of each implemented `Wave 1` family, but retrains
that configuration under three explicit data scopes:

1. `global`
2. `Fw`
3. `Bw`

The goal is to produce a fairer family-level comparison surface without
changing the core modeling logic of the selected baselines.

## Objective

Prepare one repository-owned campaign package that:

- retrains the current best `Wave 1` baseline of each implemented family;
- materializes one `global`, one `Fw`, and one `Bw` model per family;
- keeps the directional identity explicit in config metadata, run naming, and
  registry-facing family keys;
- establishes a reusable preparation pattern that future `Wave 2+` family
  launches can reuse from day one.

## Safety Constraints

| Setting | Value |
| --- | --- |
| Active Campaign State | `running`, untouched |
| Protected Files | `doc/running/active_training_campaign.yaml` and its listed protected files remain untouched |
| Training Execution In This Turn | not performed |
| Directional Split Source | repository canonical dataset config cloned into campaign-local `global` / `Fw` / `Bw` variants |
| Registry Isolation Policy | directional variants use distinct registry-facing family keys such as `feedforward_fw` and `feedforward_bw` |

## Technical Context

The repository already has canonical support for direction-aware data loading:

- dataset direction flags live in `config/datasets/transmission_error_dataset.yaml`;
- the dataset layer already supports `use_forward_direction` and
  `use_backward_direction`;
- the split logic already preserves directional semantics.

Because of that, the retraining campaign does not need a new trainer. It needs
only:

- campaign-local dataset configs for `global`, `Fw`, and `Bw`;
- directional metadata written into the training configs;
- registry-safe family-key separation so `Fw` and `Bw` winners do not collapse
  into the old global-only family registries.

## Candidate Matrix

The campaign will retrain `5` base families across `3` variants each, for a
total of `15` runs.

| Index | Base Family | Source Best Run | Variant | Registry Family Key | Planned Run Name Pattern |
| --- | --- | --- | --- | --- | --- |
| 1 | `tree` | `te_hist_gbr_tabular` | `global` | `tree` | `te_hist_gbr_tabular_global` |
| 2 | `tree` | `te_hist_gbr_tabular` | `Fw` | `tree_fw` | `te_hist_gbr_tabular_Fw` |
| 3 | `tree` | `te_hist_gbr_tabular` | `Bw` | `tree_bw` | `te_hist_gbr_tabular_Bw` |
| 4 | `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `global` | `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1_global` |
| 5 | `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `Fw` | `residual_harmonic_mlp_fw` | `te_residual_h12_deep_joint_wave1_Fw` |
| 6 | `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | `Bw` | `residual_harmonic_mlp_bw` | `te_residual_h12_deep_joint_wave1_Bw` |
| 7 | `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | `global` | `feedforward` | `te_feedforward_stride1_high_compute_long_remote_global` |
| 8 | `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | `Fw` | `feedforward_fw` | `te_feedforward_stride1_high_compute_long_remote_Fw` |
| 9 | `feedforward` | `te_feedforward_stride1_high_compute_long_remote` | `Bw` | `feedforward_bw` | `te_feedforward_stride1_high_compute_long_remote_Bw` |
| 10 | `periodic_mlp` | `te_periodic_mlp_h04_standard` | `global` | `periodic_mlp` | `te_periodic_mlp_h04_standard_global` |
| 11 | `periodic_mlp` | `te_periodic_mlp_h04_standard` | `Fw` | `periodic_mlp_fw` | `te_periodic_mlp_h04_standard_Fw` |
| 12 | `periodic_mlp` | `te_periodic_mlp_h04_standard` | `Bw` | `periodic_mlp_bw` | `te_periodic_mlp_h04_standard_Bw` |
| 13 | `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | `global` | `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery_global` |
| 14 | `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | `Fw` | `harmonic_regression_fw` | `te_harmonic_order12_linear_conditioned_recovery_Fw` |
| 15 | `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | `Bw` | `harmonic_regression_bw` | `te_harmonic_order12_linear_conditioned_recovery_Bw` |

## Source Config Policy

The baseline config for each base family is taken from the current
registry-backed family best:

- `tree` -> `te_hist_gbr_tabular`
- `residual_harmonic_mlp` -> `te_residual_h12_deep_joint_wave1`
- `feedforward` -> `te_feedforward_stride1_high_compute_long_remote`
- `periodic_mlp` -> `te_periodic_mlp_h04_standard`
- `harmonic_regression` -> `te_harmonic_order12_linear_conditioned_recovery`

Each source config is reused structurally, with only these controlled changes:

- dataset config path redirected to a campaign-local variant;
- run name extended with `_global`, `_Fw`, or `_Bw`;
- registry-facing `model_family` changed to `<family>`, `<family>_fw`, or
  `<family>_bw`;
- metadata extended with `base_model_family`, `training_variant`, explicit
  direction flags, and directional notes;
- old completed-run artifact metadata removed so the next run gets a fresh
  `run_instance_id`.

## Campaign Assets

The approved preparation package must materialize:

- planning report:
  `doc/reports/campaign_plans/wave1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md`
- campaign preparer:
  `scripts/campaigns/wave1/prepare_wave1_directional_retraining_campaign.py`
- reusable directional helper:
  `scripts/campaigns/infrastructure/directional_training_variant_support.py`
- queue configs:
  `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/`
- dataset variants:
  `config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/dataset_variants/`
- launcher:
  `scripts/campaigns/wave1/run_wave1_directional_retraining_campaign.ps1`
- launcher note:
  `doc/scripts/campaigns/run_wave1_directional_retraining_campaign.md`

## Evaluation Rules

The retraining package is considered technically correct when:

- all `15` configs are generated with the intended directional metadata;
- `global` configs keep both directions enabled;
- `Fw` configs enable only `forward`;
- `Bw` configs enable only `backward`;
- output roots and family registries are separated cleanly for directional
  variants;
- no protected `Track 1` campaign file is modified.

The future training comparison should then judge:

- global vs directional accuracy shifts within each base family;
- whether some families benefit disproportionately from directional training;
- whether the directional winners change the practical ranking of candidate
  model families for later waves.

## Execution Gate

Before this campaign is launched:

1. the campaign package must be prepared on disk;
2. the launcher and launcher note must exist;
3. the user must explicitly approve this campaign plan;
4. no update to `doc/running/active_training_campaign.yaml` should be made as
   part of this Wave 1 campaign while the unrelated Track 1 campaign remains
   marked `running`.

## Future-Wave Extension Rule

From `Wave 2` onward, a newly introduced family should be treated as
incomplete until its preparation workflow defines:

- one `global` config;
- one `Fw` config;
- one `Bw` config;
- explicit directional metadata in the generated configs;
- distinct registry-facing family keys for directional variants when those
  runs should not collapse into one family-best snapshot.

## Next Step

If this campaign plan is approved, the next step is to run the prepared
launcher:

```powershell
.\scripts\campaigns\wave1\run_wave1_directional_retraining_campaign.ps1
```
