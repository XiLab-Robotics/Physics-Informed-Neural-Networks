# Wave 5.1 And Wave 5.2 Embryonic Skeleton Plan

## Purpose

This preliminary plan defines how to prepare embryonic `Wave 5.1` and `Wave 5.2`
implementation skeletons without making either wave campaign-ready. The goal
is to do the reusable engineering work now while preserving the decision gates
that depend on `Wave 4 series`, `Wave 5.1` smoke evidence, and `Wave 5.2A` MMT
diagnostics.

## Status Labels

| Label | Meaning |
| --- | --- |
| `implementation-ready` | Code, validators, documentation, and dry-run launch scaffolds can exist and pass local checks. |
| `not campaign-ready` | No real training queue, no active-campaign state, no training launch, and no result registry update. |
| `blocked_on_track2h_results` | Loss defaults and robust/dispersion-aware settings must wait for the running Wave 4 series campaign. |
| `blocked_on_wave3_smoke` | Wave 5.2C and later training branches must wait until Wave 5.1 skeleton behavior is validated. |
| `blocked_on_wave4a_diagnostic` | MMT soft-constraint branches must wait until the analytical diagnostic is numerically useful. |

## Planned Skeletons

| Skeleton | Scope | Ready After This Pass | Campaign Blocker |
| --- | --- | --- | --- |
| `wave3_harmonic_prior_residual` | Harmonic coefficient branch, fixed harmonic reconstruction basis, residual curve branch, configurable residual weight. | import, construction, forward smoke, validator | `Wave 4 series` loss choice and campaign queue approval |
| `wave3_grouped_harmonic_heads` | Interface placeholders for low-order, middle, and high-order harmonic groups. | config/interface validation | first Wave 5.1 candidate smoke result |
| `wave4a_mmt_equation_diagnostic` | Batch adapter around MMT reproduction, parameter inventory, diagnostic-output schema. | smoke diagnostic on synthetic or dataset-aligned angle grid | parameter inventory and diagnostic usefulness |
| `wave4b_mmt_feature_generator` | Feature schema and placeholder generator for MMT subsystem terms. | interface validation | Wave 5.2A diagnostic outcome |
| `wave4c_mmt_soft_constraint_pinn` | Loss-hook placeholder for weak MMT residual penalties. | disabled integration point | Wave 5.2A/4B evidence plus Wave 5.1 evidence |

## Files To Create After Approval

| Area | Candidate Files |
| --- | --- |
| Models | `scripts/models/wave3_harmonic_prior_residual_network.py`, `scripts/models/wave4_mmt_diagnostic_adapter.py` |
| Factory | minimal `model_factory.py` registrations for import and construction only |
| Validators | `scripts/campaigns/wave_3/validate_wave3_embryonic_skeleton_package.py`, `scripts/campaigns/wave_4/validate_wave4_embryonic_skeleton_package.py` |
| Dry-run launchers | `scripts/campaigns/wave_3/run_wave3_embryonic_skeleton_checks.ps1`, `scripts/campaigns/wave_4/run_wave4_embryonic_skeleton_checks.ps1` |
| Launcher notes | `doc/scripts/campaigns/wave_3/wave3_embryonic_skeleton_checks.md`, `doc/scripts/campaigns/wave_4/wave4_embryonic_skeleton_checks.md` |
| Config templates | `config/training/wave3_embryonic_skeleton/`, `config/training/wave4_embryonic_skeleton/` |

## Materialized Skeleton Package

| Area | Materialized File | Status |
| --- | --- | --- |
| Wave 5.1 model | `scripts/models/wave3_harmonic_prior_residual_network.py` | implementation-ready, not campaign-ready |
| Wave 5.1 factory registration | `scripts/models/model_factory.py` | construction path registered for `wave3_harmonic_prior_residual` |
| Wave 5.1 template | `config/training/wave3_embryonic_skeleton/wave3_harmonic_prior_residual_template.yaml` | dry-run template only |
| Wave 5.1 validator | `scripts/campaigns/wave_3/validate_wave3_embryonic_skeleton_package.py` | compile, metadata, factory, and forward smoke checks |
| Wave 5.1 launcher | `scripts/campaigns/wave_3/run_wave3_embryonic_skeleton_checks.ps1` | dry-run checks only |
| Wave 5.2A adapter | `scripts/models/wave4_mmt_diagnostic_adapter.py` | implementation-ready, not campaign-ready |
| Wave 5.2A template | `config/training/wave4_embryonic_skeleton/wave4a_mmt_equation_diagnostic_template.yaml` | dry-run template only |
| Wave 5.2A validator | `scripts/campaigns/wave_4/validate_wave4_embryonic_skeleton_package.py` | compile, metadata, and MMT demo-summary checks |
| Wave 5.2A launcher | `scripts/campaigns/wave_4/run_wave4_embryonic_skeleton_checks.ps1` | dry-run checks only |

## Files Not To Touch In This Pass

- `doc/running/active_training_campaign.yaml`;
- final queue YAMLs for real training;
- registry files under `output/registries/`;
- campaign result reports;
- heavy official `TE Curve Verification Pipeline` verification scripts or outputs;
- any `Wave 4 series` campaign files managed on the other workstation.

## Verification Plan

The embryonic skeleton pass is complete only after:

- `py_compile` passes on new Python modules and validators;
- import smoke checks pass;
- model forward smoke passes for Wave 5.1 with synthetic tensors;
- MMT adapter smoke passes for Wave 5.2A;
- validators report `implementation-ready` and `not campaign-ready`;
- dry-run launchers refuse to start training and only run checks;
- Markdown QA passes on touched documentation.

## Decision Gates Before Real Campaigns

`Wave 5.1` can become campaign-ready only after:

- `Wave 4 series` identifies the preferred robust loss policy or confirms that the
  default should remain conservative;
- the Wave 5.1 forward and one-batch smoke checks pass;
- a real campaign plan approves queue size, surfaces, losses, and launch mode.

`Wave 5.2` can become campaign-ready only after:

- `Wave 5.2A` shows whether the MMT analytical terms are diagnostic, feature,
  loss, calibrated-baseline, or diagnostic-only material;
- at least the first Wave 5.1 skeleton is validated;
- `Wave 4 series` informs the loss policy;
- a real campaign plan approves the specific sub-branch, loss weights, and
  leakage checks.

## Launch Policy

The launchers created by this skeleton pass must be dry-run check launchers.
They may run validators, compile checks, and smoke checks. They must not call
`run_training_campaign.py`, mutate active campaign state, or submit remote
training.
