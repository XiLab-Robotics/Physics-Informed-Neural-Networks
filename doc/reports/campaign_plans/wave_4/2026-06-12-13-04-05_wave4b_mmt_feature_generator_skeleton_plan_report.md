# Wave 4B MMT Feature Generator Skeleton Plan

## Purpose

This preliminary plan defines a non-campaign `Wave 4B` skeleton pass while the
separate `Track 2H` quantile / probabilistic campaign runs on another
workstation.

The output is a dry-run MMT feature-generation package. It must be useful for
future `Wave 3`, `Wave 4B`, or `Wave 4C` work, but it must not become a real
training campaign in this pass.

## Scope

| Stream | Planned Output | Campaign Readiness |
| --- | --- | --- |
| `Wave 4B` | MMT feature schema and generator skeleton. | not campaign-ready |
| `Wave 4B` | Leakage-aware feature metadata and dry-run sample output. | not campaign-ready |
| `Wave 4B` | Validator, dry-run launcher, and launcher note. | not campaign-ready |
| Documentation | Technical note, plan report, and index registrations. | implementation gate only |

## Boundaries

This pass may:

- compile and import new feature-generation scripts;
- generate a small local validation payload under
  `output/validation_checks/wave4b_mmt_feature_generator/`;
- add dry-run validation commands and documentation;
- update relevant documentation indexes.

This pass must not:

- launch a training campaign;
- create active queue YAMLs;
- edit `doc/running/active_training_campaign.yaml`;
- update model registries or campaign winner artifacts;
- use `Track 2H` quantile / probabilistic results before closeout;
- treat MMT feature generation as a validated physical loss.

## Planned Files

| Area | Candidate Files |
| --- | --- |
| Feature generator | `scripts/features/wave4b_mmt_feature_generator.py` |
| Template config | `config/training/wave4_embryonic_skeleton/wave4b_mmt_feature_generator_template.yaml` |
| Validator | `scripts/campaigns/wave_4/validate_wave4b_mmt_feature_generator_package.py` |
| Dry-run launcher | `scripts/campaigns/wave_4/run_wave4b_mmt_feature_generator_checks.ps1` |
| Launcher note | `doc/scripts/campaigns/wave_4/wave4b_mmt_feature_generator_checks.md` |
| Validation output | `output/validation_checks/wave4b_mmt_feature_generator/` |

## Verification Plan

The pass is complete only after:

- Python compilation passes for new and touched scripts;
- the `Wave 4B` validator passes and writes finite sample outputs;
- the dry-run launcher passes and does not launch training;
- leakage labels are validated so only inference-safe fields are exposed for
  inference use;
- Markdown QA passes for touched authored Markdown;
- Sphinx builds with `-W` if `site/` scope changes;
- `git diff --check` passes.

## Decision Gates

After this skeleton pass:

- `Wave 4B` can only become a real feature-augmented training campaign after
  the in-flight `Track 2H` campaign is closed out and a new approved campaign
  plan selects queue size, surfaces, losses, and feature consumers;
- `Wave 4C` can only consume MMT features as weak-loss inputs after `Wave 4B`
  feature leakage checks and dataset-aligned parameter availability are
  accepted;
- no campaign launch is approved by this plan.
