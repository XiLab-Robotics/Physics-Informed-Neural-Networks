# Wave 3 Grouped Harmonic Heads Skeleton Plan

## Purpose

This preliminary plan defines a non-campaign skeleton pass for
`wave3_grouped_harmonic_heads` while the separate `Track 2H` quantile /
probabilistic campaign runs on another workstation.

The output is a dry-run model-interface package. It must help future `Wave 3`
campaign preparation, but it must not become a training campaign in this pass.

## Scope

| Stream | Planned Output | Campaign Readiness |
| --- | --- | --- |
| `Wave 3` | Grouped harmonic-head model skeleton. | not campaign-ready |
| `Wave 3` | Config template and factory construction path. | not campaign-ready |
| `Wave 3` | Point/sequence forward validator and dry-run launcher. | not campaign-ready |
| Documentation | Technical note, plan report, launcher note, and index updates. | implementation gate only |

## Boundaries

This pass may:

- compile and import new PyTorch model code;
- run synthetic point and sequence forward checks;
- generate small validation artifacts under
  `output/validation_checks/wave3_grouped_harmonic_heads/`;
- update documentation and Sphinx entries for the dry-run command.

This pass must not:

- launch a training campaign;
- create active queue YAMLs;
- edit `doc/running/active_training_campaign.yaml`;
- update model registries or campaign winner artifacts;
- use `Track 2H` quantile / probabilistic results before closeout;
- select final branch weights, regularizers, or robust-loss defaults.

## Planned Files

| Area | Candidate Files |
| --- | --- |
| Model | `scripts/models/wave3_grouped_harmonic_heads_network.py` |
| Factory | `scripts/models/model_factory.py` |
| Template config | `config/training/wave3_embryonic_skeleton/wave3_grouped_harmonic_heads_template.yaml` |
| Validator | `scripts/campaigns/wave3/validate_wave3_grouped_harmonic_heads_package.py` |
| Dry-run launcher | `scripts/campaigns/wave3/run_wave3_grouped_harmonic_heads_checks.ps1` |
| Launcher note | `doc/scripts/campaigns/wave3/wave3_grouped_harmonic_heads_checks.md` |
| Validation output | `output/validation_checks/wave3_grouped_harmonic_heads/` |

## Verification Plan

The pass is complete only after:

- Context7 is consulted before PyTorch-facing implementation;
- Python compilation passes for new and touched scripts;
- the grouped-head validator passes point and sequence forward smoke checks;
- auxiliary output keys expose low, middle, high, residual, and combined
  tensors;
- the dry-run launcher passes and does not launch training;
- Markdown QA passes for touched authored Markdown;
- Sphinx builds with `-W` if `site/` scope changes;
- `git diff --check` passes.

## Decision Gates

After this skeleton pass:

- `Wave 3` can only become a real campaign package after the in-flight
  `Track 2H` campaign is closed out and a new approved campaign plan selects
  queue size, surfaces, losses, branch weights, and launch mode;
- `wave3_grouped_harmonic_heads` remains a second candidate behind the
  already training-smoke-ready `wave3_harmonic_prior_residual` until evidence
  justifies promoting it;
- no campaign launch is approved by this plan.
