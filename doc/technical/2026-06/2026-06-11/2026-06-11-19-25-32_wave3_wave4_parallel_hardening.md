# Wave 3 And Wave 4 Parallel Hardening

## Overview

This technical document plans the next non-campaign hardening step for the
recently committed `Wave 3` and `Wave 4A` embryonic skeletons.

The goal is to continue useful parallel work while the separate `Track 2H`
campaign runs on another workstation. This step must not depend on `Track 2H`
numeric results and must not launch a real `Wave 3` or `Wave 4` campaign.

The work has two coordinated streams:

- make the `Wave 3` harmonic-prior residual skeleton training-smoke-ready;
- turn the `Wave 4A` MMT adapter into a first diagnostic report generator.

Both streams remain exploratory. They are intended to reduce integration risk
before final campaign packaging, not to select winners or promote models.

## Technical Approach

### Wave 3 Training-Smoke-Ready Stream

The current `Wave3HarmonicPriorResidualNetwork` already imports, constructs,
and runs point/sequence forward smoke checks. The next hardening step should
verify that it can pass through the repository training stack without becoming
campaign-ready.

The implementation should:

- add a narrow one-batch validation entry point for the embryonic Wave 3
  template;
- use the existing training setup and datamodule patterns rather than a custom
  standalone training path;
- preserve the `implementation_ready` / `not_campaign_ready` distinction in
  config metadata and launcher messages;
- avoid mutating `doc/running/active_training_campaign.yaml`;
- avoid creating queue YAMLs under active campaign folders;
- avoid running multi-epoch training or Track 2 verification.

The one-batch check should answer only this question: can the Wave 3 model
type be loaded from a repository-style config and execute a minimal training
stack pass without shape, normalization, datamodule, or Lightning-module
integration errors?

The final robust-loss defaults, queue surfaces, and training duration must wait
for `Track 2H` results.

### Wave 4A Diagnostic Stream

The current `Wave4MMTDiagnosticAdapter` can run the repository-owned MMT
equation-chain demonstration and summarize dominant harmonics. The next step
should create a report generator that makes this diagnostic auditable.

The implementation should:

- run the MMT demonstration curve through the adapter;
- compute mean, peak-to-peak amplitude, and dominant harmonic bins;
- compare the dominant bins qualitatively against the repository suspicious
  harmonic groups: `0`, `1`, `156`, `162`, and `240`;
- write a dated Markdown analysis bundle under
  `doc/reports/analysis/wave4/mmt_equation_diagnostic/`;
- write machine-readable companion data under
  `output/validation_checks/wave4_mmt_equation_diagnostic/`;
- keep the conclusion conservative: MMT signals may inform diagnostics,
  features, or soft losses only after dataset-aligned parameter inventory and
  leakage-safe calibration.

This diagnostic should not be treated as a PINN loss yet. It is an
interpretability and readiness check.

## Involved Components

Expected documentation components:

- this technical document;
- `doc/reports/campaign_plans/wave3_wave4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md`;
- `doc/reports/analysis/wave3/Wave 3 Hybrid Structured Models.md`;
- `doc/reports/analysis/wave4/Wave 4 PINN Formulation And First PINN.md`;
- `doc/README.md`;
- `doc/guide/project_usage_guide.md`;
- Sphinx `site/` API or guide entries if new user-facing scripts are added.

Expected Wave 3 implementation components after approval:

- a Wave 3 training-smoke validator under `scripts/campaigns/wave3/`;
- a dry-run PowerShell wrapper under `scripts/campaigns/wave3/`;
- a launcher note under `doc/scripts/campaigns/wave3/`;
- optional template metadata additions under
  `config/training/wave3_embryonic_skeleton/`.

Expected Wave 4A implementation components after approval:

- a report generator under `scripts/reports/analysis/`;
- a script note under `doc/scripts/reports/analysis/` or the existing report
  script index pattern;
- Markdown report output under
  `doc/reports/analysis/wave4/mmt_equation_diagnostic/[2026-06-11]/`;
- validation data under
  `output/validation_checks/wave4_mmt_equation_diagnostic/`.

No subagent is planned for this work. If a subagent becomes useful later, its
scope and approval requirement must be recorded before launch.

## Implementation Steps

1. Create and approve this technical document.
2. Create and approve the paired preliminary hardening plan report.
3. Inspect the current Wave 3 skeleton, training setup validators, and config
   conventions.
4. Use Context7 before changing PyTorch or PyTorch Lightning-facing code.
5. Implement the smallest Wave 3 one-batch validation path that exercises the
   training stack without creating a campaign queue.
6. Add a dry-run Wave 3 PowerShell wrapper and launcher note that clearly state
   that no training campaign is launched.
7. Implement the Wave 4A MMT diagnostic report generator and companion output
   tables.
8. Update Wave 3 and Wave 4 analysis documents with the new readiness state.
9. Update `doc/README.md`, `doc/guide/project_usage_guide.md`, and Sphinx
   entries if new user-facing commands are added.
10. Verify Python compilation, Wave 3 one-batch validation, Wave 4A report
    generation, Markdown QA, Sphinx build if portal scope changes, and
    `git diff --check`.
11. Stop for explicit user approval before any commit.

## Approval Gate

This document and the paired plan authorize only a scoped hardening
implementation after explicit approval. They do not authorize a real `Wave 3`
or `Wave 4` training campaign, active-campaign state mutation, registry update,
or official `Track 2` verification refresh.
