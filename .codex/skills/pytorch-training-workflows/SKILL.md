---
name: pytorch-training-workflows
description: Use when implementing, refactoring, or reviewing repository Python, PyTorch, PyTorch Lightning, NumPy, SciPy, or scikit-learn training workflows in StandardML - Codex.
---

# PyTorch Training Workflows

Handle model and training changes with repository-specific ML constraints kept
visible.

## Use This Skill For

- model-family implementation in `scripts/models/`;
- training and datamodule work in `scripts/training/`;
- metric-flow and loss-flow changes;
- training-related configuration reasoning;
- refactors that affect data movement, model outputs, checkpoints, or
  validation behavior.

## Do Not Use This Skill For

- generic ML brainstorming with no repository impact;
- campaign orchestration tasks that belong under `campaign-architect`;
- deployment-only analysis that belongs under `twincat-deployment-analyst`;
- changing protected campaign files without explicit approval.

## Required Checks

1. Read the relevant documents in `reference/` or `doc/reference_summaries/`
   before making design choices.
2. Use Context7 before implementing or recommending library-specific code for
   PyTorch, PyTorch Lightning, NumPy, SciPy, scikit-learn, or adjacent ML
   tooling.
3. Read `doc/running/active_training_campaign.yaml` when the task touches
   training, configs, launchers, or user-facing workflow docs.
4. Check whether smoke tests, validation checks, or campaign behavior would be
   affected by the change.

## Repository ML Priorities

- Keep rotational transmission error as the target quantity.
- Preserve the distinction between analytical structure and ML-based
  compensation.
- Keep operating variables explicit:
  input speed, applied torque, oil temperature, encoder zeroing, and
  `DataValid` windows when relevant.
- Keep artifact layout, `run_name`, and `run_instance_id` semantics correct.
- Favor inspectable intermediate stages over opaque shortcuts.

## Implementation Pattern

Prefer this sequence:

1. Read references and local implementation.
2. Identify behavioral constraints and affected workflows.
3. Check library API details with Context7 when version-sensitive.
4. Implement the narrowest safe change.
5. Verify training, smoke-test, validation, and documentation implications.

## File Targets To Read First

- `reference/`
- `doc/reference_summaries/`
- `doc/running/active_training_campaign.yaml`
- `scripts/models/`
- `scripts/training/`
- `config/training/`
- `output/registries/`
