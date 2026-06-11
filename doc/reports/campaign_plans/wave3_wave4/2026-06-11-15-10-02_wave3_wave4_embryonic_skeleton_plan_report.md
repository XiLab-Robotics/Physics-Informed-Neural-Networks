# Wave 3 And Wave 4 Embryonic Skeleton Plan

## Purpose

This preliminary plan defines how to prepare embryonic `Wave 3` and `Wave 4`
implementation skeletons without making either wave campaign-ready. The goal
is to do the reusable engineering work now while preserving the decision gates
that depend on `Track 2H`, `Wave 3` smoke evidence, and `Wave 4A` MMT
diagnostics.

## Status Labels

| Label | Meaning |
| --- | --- |
| `implementation-ready` | Code, validators, documentation, and dry-run launch scaffolds can exist and pass local checks. |
| `not campaign-ready` | No real training queue, no active-campaign state, no training launch, and no result registry update. |
| `blocked_on_track2h_results` | Loss defaults and robust/dispersion-aware settings must wait for the running Track 2H campaign. |
| `blocked_on_wave3_smoke` | Wave 4C and later training branches must wait until Wave 3 skeleton behavior is validated. |
| `blocked_on_wave4a_diagnostic` | MMT soft-constraint branches must wait until the analytical diagnostic is numerically useful. |

## Planned Skeletons

| Skeleton | Scope | Ready After This Pass | Campaign Blocker |
| --- | --- | --- | --- |
| `wave3_harmonic_prior_residual` | Harmonic coefficient branch, fixed harmonic reconstruction basis, residual curve branch, configurable residual weight. | import, construction, forward smoke, validator | `Track 2H` loss choice and campaign queue approval |
| `wave3_grouped_harmonic_heads` | Interface placeholders for low-order, middle, and high-order harmonic groups. | config/interface validation | first Wave 3 candidate smoke result |
| `wave4a_mmt_equation_diagnostic` | Batch adapter around MMT reproduction, parameter inventory, diagnostic-output schema. | smoke diagnostic on synthetic or dataset-aligned angle grid | parameter inventory and diagnostic usefulness |
| `wave4b_mmt_feature_generator` | Feature schema and placeholder generator for MMT subsystem terms. | interface validation | Wave 4A diagnostic outcome |
| `wave4c_mmt_soft_constraint_pinn` | Loss-hook placeholder for weak MMT residual penalties. | disabled integration point | Wave 4A/4B evidence plus Wave 3 evidence |

## Files To Create After Approval

| Area | Candidate Files |
| --- | --- |
| Models | `scripts/models/wave3_harmonic_prior_residual_network.py`, `scripts/models/wave4_mmt_diagnostic_adapter.py` |
| Factory | minimal `model_factory.py` registrations for import and construction only |
| Validators | `scripts/campaigns/wave3/validate_wave3_embryonic_skeleton_package.py`, `scripts/campaigns/wave4/validate_wave4_embryonic_skeleton_package.py` |
| Dry-run launchers | `scripts/campaigns/wave3/run_wave3_embryonic_skeleton_checks.ps1`, `scripts/campaigns/wave4/run_wave4_embryonic_skeleton_checks.ps1` |
| Launcher notes | `doc/scripts/campaigns/wave3/wave3_embryonic_skeleton_checks.md`, `doc/scripts/campaigns/wave4/wave4_embryonic_skeleton_checks.md` |
| Config templates | `config/training/wave3_embryonic_skeleton/`, `config/training/wave4_embryonic_skeleton/` |

## Materialized Skeleton Package

| Area | Materialized File | Status |
| --- | --- | --- |
| Wave 3 model | `scripts/models/wave3_harmonic_prior_residual_network.py` | implementation-ready, not campaign-ready |
| Wave 3 factory registration | `scripts/models/model_factory.py` | construction path registered for `wave3_harmonic_prior_residual` |
| Wave 3 template | `config/training/wave3_embryonic_skeleton/wave3_harmonic_prior_residual_template.yaml` | dry-run template only |
| Wave 3 validator | `scripts/campaigns/wave3/validate_wave3_embryonic_skeleton_package.py` | compile, metadata, factory, and forward smoke checks |
| Wave 3 launcher | `scripts/campaigns/wave3/run_wave3_embryonic_skeleton_checks.ps1` | dry-run checks only |
| Wave 4A adapter | `scripts/models/wave4_mmt_diagnostic_adapter.py` | implementation-ready, not campaign-ready |
| Wave 4A template | `config/training/wave4_embryonic_skeleton/wave4a_mmt_equation_diagnostic_template.yaml` | dry-run template only |
| Wave 4A validator | `scripts/campaigns/wave4/validate_wave4_embryonic_skeleton_package.py` | compile, metadata, and MMT demo-summary checks |
| Wave 4A launcher | `scripts/campaigns/wave4/run_wave4_embryonic_skeleton_checks.ps1` | dry-run checks only |

## Files Not To Touch In This Pass

- `doc/running/active_training_campaign.yaml`;
- final queue YAMLs for real training;
- registry files under `output/registries/`;
- campaign result reports;
- heavy official `Track 2` verification scripts or outputs;
- any `Track 2H` campaign files managed on the other workstation.

## Verification Plan

The embryonic skeleton pass is complete only after:

- `py_compile` passes on new Python modules and validators;
- import smoke checks pass;
- model forward smoke passes for Wave 3 with synthetic tensors;
- MMT adapter smoke passes for Wave 4A;
- validators report `implementation-ready` and `not campaign-ready`;
- dry-run launchers refuse to start training and only run checks;
- Markdown QA passes on touched documentation.

## Decision Gates Before Real Campaigns

`Wave 3` can become campaign-ready only after:

- `Track 2H` identifies the preferred robust loss policy or confirms that the
  default should remain conservative;
- the Wave 3 forward and one-batch smoke checks pass;
- a real campaign plan approves queue size, surfaces, losses, and launch mode.

`Wave 4` can become campaign-ready only after:

- `Wave 4A` shows whether the MMT analytical terms are diagnostic, feature,
  loss, calibrated-baseline, or diagnostic-only material;
- at least the first Wave 3 skeleton is validated;
- `Track 2H` informs the loss policy;
- a real campaign plan approves the specific sub-branch, loss weights, and
  leakage checks.

## Launch Policy

The launchers created by this skeleton pass must be dry-run check launchers.
They may run validators, compile checks, and smoke checks. They must not call
`run_training_campaign.py`, mutate active campaign state, or submit remote
training.
