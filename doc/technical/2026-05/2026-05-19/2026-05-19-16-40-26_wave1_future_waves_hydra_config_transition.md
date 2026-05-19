# Wave 1 And Future Waves Hydra Configuration Transition

## Overview

This document formalizes the planned transition toward `Hydra`-based
configuration composition for `Wave 1` follow-up work and all future wave
training workflows.

The transition is intentionally not a repository-wide rewrite. `Hydra` should
be introduced as the standard configuration composition and validation layer
for evolving TE-model workflows, while the repository-owned campaign pipeline
remains the operational source of truth for queue materialization, launcher
execution, artifact taxonomy, active campaign state, closeout reports,
registries, and model export bookkeeping.

`Track 1` exact-paper workflows are excluded from retroactive migration because
they are closed, paper-faithful reproduction workflows. Future non-faithful
Track 1 derivatives or `Track 1.5` style benchmark branches may opt into the
Hydra configuration layer, but the closed exact-paper protocol should remain
stable.

## Technical Approach

Use `Hydra` for configuration composition where it removes real duplication and
improves validation:

- config groups for `dataset`, `direction`, `model_family`, `model_variant`,
  `trainer`, `export`, `evaluation`, and `campaign_profile`;
- command-line overrides for narrow smoke runs and operator-controlled
  experiments;
- structured configs for runtime validation of required keys and type-sensitive
  settings;
- explicit materialization of the resolved configuration into the run or queue
  artifact folder before execution.

Do not use `Hydra` as the first-generation replacement for the repository
campaign system. In particular:

- disable or explicitly control `hydra.job.chdir` so repository-relative paths
  keep their current semantics;
- set or bypass `hydra.run.dir` and `hydra.sweep.dir` so output roots remain
  under the repository taxonomy;
- avoid direct `Hydra` multiruns as a substitute for campaign queue execution
  until campaign reporting, registry refresh, and closeout hooks are integrated;
- keep generated queue YAML files inspectable and commit-scopable.

The first implementation should be a bounded pilot that composes a `Wave 1`
training configuration and writes the resolved YAML without changing the
existing campaign execution contract.

No subagent use is planned for this technical document or the first transition
design. If subagent use becomes useful for later implementation, its task
boundary and explicit approval requirement must be added before launch.

## Involved Components

- `config/training/`
- `config/training/wave1_*`
- future `config/training/wave*/` roots
- `scripts/training/`
- `scripts/campaigns/wave1/`
- `scripts/campaigns/infrastructure/`
- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`
- `doc/running/active_training_campaign.yaml`
- `output/training_runs/`
- `output/training_campaigns/wave1/`
- `output/registries/`
- `requirements.txt`
- `doc/guide/project_usage_guide.md`
- `site/`

## Implementation Steps

1. Add `Hydra` and `OmegaConf` as explicit dependencies only after approval of
   the implementation phase.
2. Create a `Wave 1` pilot config tree with config groups for dataset scope,
   direction, model family, trainer policy, export policy, and campaign profile.
3. Add a small repository-owned config composition entry point that resolves a
   selected `Hydra` configuration and writes the materialized YAML to a
   deterministic repository path.
4. Add structured config schemas for the pilot surface so missing required keys
   and invalid field types fail before training starts.
5. Keep the existing campaign preparation pipeline as the execution boundary:
   campaign queue YAMLs must remain inspectable artifacts, not implicit
   `Hydra` multirun state.
6. Add guardrails for `hydra.job.chdir`, `hydra.run.dir`, and
   `hydra.sweep.dir` so `Hydra` cannot silently write outside the repository
   taxonomy.
7. Update the `Wave 1` launcher or preparer only after the pilot has proven
   that resolved configs match the existing training contract.
8. Document that closed `Track 1` exact-paper workflows remain legacy
   paper-faithful workflows and are not migrated retroactively.
9. Permit future `Track 1` derivatives, `Track 1.5`, and future waves to opt
   into the `Hydra` layer when they are not strict reproductions of the closed
   exact-paper protocol.
10. Update user-facing documentation and Sphinx portal pages when runnable
    commands or setup requirements change.
