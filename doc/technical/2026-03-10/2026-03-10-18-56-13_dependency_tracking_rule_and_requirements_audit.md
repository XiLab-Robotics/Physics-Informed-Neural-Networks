# Dependency Tracking Rule And Requirements Audit

## Overview

The current repository workflow already enforces technical-document approval, usage-guide updates for runnable features, and immediate commits after implementation.

However, it does not yet explicitly require dependency tracking when new libraries are introduced in the codebase.

The user requested two actions:

1. add a workflow rule that any newly used library must be recorded in the project dependencies and related setup references;
2. audit the libraries used so far to ensure they are all tracked in `requirements.txt`.

The initial audit of the current Python codebase shows:

- third-party libraries currently imported by the repository include `torch`, `lightning`, `numpy`, `pandas`, `matplotlib`, `PyYAML`, and `colorama`;
- `requirements.txt` already contains every currently imported third-party package except `torch`;
- the setup documentation still installs `torchvision`, even though the current repository code does not import it.

## Technical Approach

The update will formalize dependency tracking as part of the repository workflow and bring the current dependency declarations in line with the actual codebase.

The planned implementation is:

1. add a workflow rule in `AGENTS.md` and `README.md` stating that every newly introduced third-party library must be added to `requirements.txt` and to any relevant setup or usage documentation before the final commit;
2. update `requirements.txt` so the currently used core dependency `torch` is explicitly tracked;
3. audit and refresh the installation instructions in the project documentation so they remain coherent with the dependency file and with the actual imported libraries;
4. remove or clarify references to unused libraries where they create confusion, specifically the current `torchvision` installation step.

Because PyTorch on this project is CUDA-sensitive, the documentation should still preserve the explicit official-wheel installation guidance for the current Windows GPU workflow, but the dependency file should no longer omit `torch` entirely.

## Involved Components

- `AGENTS.md`
  Workflow rules for future repository changes.
- `README.md`
  Main project workflow and environment-installation guidance.
- `requirements.txt`
  Root Python dependency manifest.
- `doc/guide/project_usage_guide.md`
  User-facing setup and runtime instructions.
- `doc/technical/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md`
  Existing technical document that currently explains why `torch` was excluded from `requirements.txt`.
- `doc/README.md`
  Internal documentation index.
- `doc/technical/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md`
  This technical planning document.

## Implementation Steps

1. Add the new dependency-tracking workflow rule to `AGENTS.md` and `README.md`.
2. Update `requirements.txt` to include `torch` with an explicit version range aligned with the current environment baseline.
3. Refresh the environment-installation sections in `README.md` and `doc/guide/project_usage_guide.md` so dependency installation remains reproducible and consistent.
4. Update the existing environment technical document to reflect the new dependency-tracking policy and the decision to track `torch` explicitly.
5. Remove or clarify the current `torchvision` setup reference if it is not part of the actual codebase requirements.
6. Verify the resulting dependency list against the repository imports once more.
7. Commit the rule update and dependency audit changes immediately after implementation.
