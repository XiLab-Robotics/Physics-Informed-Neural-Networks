# Large Tree Model Exportability Constraint

## Overview

This task records an explicit repository constraint after the remote LAN
training campaign produced a `tree_model.pkl` artifact of roughly `91 GB`. That
model size makes the corresponding tree configuration unsuitable for the future
TwinCAT / PLC deployment branch and unsuitable as a candidate export target,
even if its offline training run completes successfully on a stronger
workstation.

## Technical Approach

The change is documentation and backlog hardening, not a training-code change.
The repository should explicitly treat this oversized tree variant as excluded
from practical deployment/export candidate sets because:

1. it is far beyond realistic PLC memory budgets;
2. it is too heavy to treat as a normal deployable artifact;
3. future export tooling should avoid spending effort on an artifact class that
   is already known to violate deployment constraints.

The implementation will:

1. record the exclusion in the live backlog so the deployment/export branch
   does not re-promote this model later by accident;
2. add an explicit note in the tree-training workflow documentation so the
   constraint remains visible near the artifact type that generated it;
3. keep the statement narrow: this does not ban all tree models, only the
   oversized deployment-incompatible variant class represented by the
   ~`91 GB` artifact.

No subagent is planned for this implementation. The work is local, explicit,
and documentation-focused.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/scripts/training/train_tree_regressor.md`
- `doc/README.md`

## Implementation Steps

1. Add a backlog note excluding the oversized tree-model variant from future
   deployment/export candidate sets.
2. Add a workflow-local note in the tree-training documentation so the
   exportability constraint is visible where `tree_model.pkl` is described.
3. Update the documentation index with this technical note.
4. Run the required Markdown checks on the touched Markdown scope.
5. Report completion and wait for explicit approval before creating the commit.
