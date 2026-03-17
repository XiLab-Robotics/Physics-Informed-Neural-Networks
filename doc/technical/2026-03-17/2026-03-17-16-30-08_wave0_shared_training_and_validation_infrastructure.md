# Wave 0 Shared Training And Validation Infrastructure

## Overview

This document defines the first implementation wave requested by the user after the TE model-family planning phase.

The purpose of `Wave 0` is not to add a new model family yet. It is to prepare the repository so that all future model families can be implemented, validated, smoke-tested, trained, and compared through the same infrastructure.

The current repository already has a working feedforward path, but it is still oriented around a single family. Before adding harmonic, temporal, hybrid, or PINN models, the shared training stack should be generalized in a controlled way.

The Wave 0 scope is therefore:

- formalize a model-family-agnostic training config path;
- formalize a common metrics artifact schema;
- add reusable smoke-test and one-batch validation utilities;
- make model registration and run naming architecture-aware;
- define the shared comparison-report data structure that later campaign reports can reuse.

This wave should stay intentionally narrow. It should not yet implement the new TE model families themselves.

## Technical Approach

### Why This Wave Should Happen First

The approved backlog already identified a common risk: if each future architecture family is added on top of the current feedforward-specific workflow without first unifying the infrastructure, the repository will accumulate:

- inconsistent config shapes;
- inconsistent artifact naming;
- inconsistent metric files;
- inconsistent smoke-test behavior;
- expensive report normalization work later.

That would make cross-family comparison weaker precisely when the project needs it most.

Wave 0 is therefore an enabling step. It does not seek model accuracy gains directly. It seeks experiment quality, comparability, and implementation speed for all later waves.

### Wave 0 Deliverables

#### 1. Model-Family-Agnostic Training Config Structure

The training stack should stop assuming only one concrete family.

The config path should support:

- model family selection;
- family-specific parameter blocks;
- shared optimization and trainer blocks;
- shared dataset and runtime blocks;
- later reuse by campaign YAML generation.

The immediate requirement is not to redesign the whole repository config system. The requirement is to reach a clean enough abstraction so a new family can plug into the same training entry path without ad hoc branching everywhere.

#### 2. Common Metrics Schema

The repository should define one common result artifact structure across model families.

The schema should cover at least:

- model family and model type identifiers;
- train, validation, and test metrics;
- checkpoint path information;
- main configuration summary;
- selected runtime or complexity indicators if already available.

This is necessary so later campaign reports can compare different families without custom parsers per architecture.

#### 3. Shared Smoke-Test Entry Point

The repository should add one reusable smoke-test path that can be run for any registered model family.

The smoke-test should verify:

- config loading;
- model instantiation;
- datamodule batch retrieval;
- one forward pass;
- one loss computation;
- one optimizer step or equivalent mini-train path;
- checkpoint save and reload behavior when relevant.

The smoke-test should stay lightweight enough to run quickly during model-family implementation.

#### 4. Shared Validation Path

The repository should add one reusable validation utility or script for one-batch verification before launching longer campaigns.

The validation path should check:

- tensor shapes;
- feature ordering;
- finite outputs and losses;
- deterministic behavior for fixed weights and input;
- compatibility with the current TE valid-window data path.

This is separate from the smoke-test because a model can technically run while still being wired incorrectly.

#### 5. Family-Aware Artifact Naming

The repository should ensure that run folders, metric files, and report references carry enough family identity to remain legible when multiple architectures coexist.

This is especially important because later waves will add:

- harmonic models;
- temporal models;
- hybrid structured models;
- exploratory low-priority branches;
- PINN variants.

#### 6. Shared Comparison Data Structure

Wave 0 should define the comparison payload structure that later campaign reports will reuse.

This does not require producing the final big comparison report yet. It requires standardizing the fields that later reports should collect, such as:

- best validation and test metrics;
- harmonic-quality indicators;
- model size or parameter count;
- runtime notes;
- interpretability and deployment notes.

### Scope Boundaries

Wave 0 should include:

- infrastructure changes that generalize the training stack;
- small validation or smoke-test runs needed to prove the infrastructure works;
- documentation updates required by the new shared workflow.

Wave 0 should not include:

- implementation of harmonic regression;
- implementation of temporal models;
- implementation of hybrid or PINN families;
- multi-run campaign execution for new families.

That separation matters because Wave 0 is a prerequisite for the next campaign-planning wave, not the campaign wave itself.

### Expected Verification

The minimum acceptable verification for Wave 0 is:

1. the existing feedforward model still trains or at least passes the new smoke-test path;
2. the common metrics artifact is produced successfully;
3. the one-batch validation utility confirms correct shapes and finite outputs;
4. the family-aware naming appears correctly in the generated artifacts.

This verification is sufficient for Wave 0 because the main goal is infrastructure readiness, not a new model result.

## Involved Components

- `README.md`
  Main project document that must reference this Wave 0 technical note.
- `doc/README.md`
  Internal documentation index that should also list this note.
- `doc/technical/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md`
  This Wave 0 technical document.
- `doc/technical/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  Approved backlog document whose Wave 0 infrastructure goals this note operationalizes.
- `scripts/training/train_feedforward_network.py`
  Current training entry point that will likely need generalization or extraction of shared logic.
- `scripts/training/transmission_error_datamodule.py`
  Current data path that the new validation and smoke-test utilities must exercise.
- `scripts/training/transmission_error_regression_module.py`
  Current loss and metric path that should align with the common metrics schema.
- `scripts/training/run_training_campaign.py`
  Existing campaign runner that must remain compatible with the generalized training structure.
- `scripts/models/model_factory.py`
  Current model-registration path that should become the stable hook for future family additions.
- `scripts/models/feedforward_network.py`
  Current baseline model used to verify that the generalized infrastructure still works.
- `config/training/`
  Current training config tree that should evolve toward a cleaner family-aware structure.
- `doc/scripts/training/train_feedforward_network.md`
  Script documentation that may need updates later if the runnable workflow changes.
- `doc/guide/project_usage_guide.md`
  Must be updated later if the approved infrastructure changes the user-facing training workflow.

## Implementation Steps

1. Create this Wave 0 technical document and register it in the documentation indexes.
2. Wait for explicit user approval before modifying implementation code or training configuration files.
3. Review the current training entry path, model factory, datamodule, and metric artifact outputs in detail.
4. Refactor the training config handling so model-family identity is explicit and reusable across future architectures.
5. Define and implement a common metrics artifact schema shared by the current feedforward baseline and future model families.
6. Add a reusable smoke-test entry point that can instantiate a registered model family and run a minimal batch-level training verification.
7. Add a reusable one-batch validation path that checks shapes, finite values, and feature alignment before long runs.
8. Add family-aware artifact naming so future model-family outputs remain unambiguous.
9. Define the shared comparison payload structure that later campaign reports can consume.
10. Verify Wave 0 by running the new smoke-test and validation path on the current feedforward baseline.
11. Update the relevant training documentation if the approved changes alter the runnable workflow.
12. Report completion and wait for explicit user approval before creating any Git commit.
