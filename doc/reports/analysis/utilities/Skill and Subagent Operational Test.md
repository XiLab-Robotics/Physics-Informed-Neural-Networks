# Skill And Subagent Operational Test Wave Two

## Overview

This report records the second operational-test wave for the remaining
repository-owned Codex skills and subagents:

- `campaign-architect`
- `powershell-campaign-tooling`
- `scientific-reference-synthesizer`
- `repo-ml-reviewer`
- `repo-test-strategist`
- `twincat-deployment-analyst`

The goal was to exercise each artifact on a real repository-local task and
judge whether it added useful discipline, deeper review, or better decision
support.

## Tested Repository Scope

### Campaign-Review Scope

- Planning report:
  `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- Launcher:
  `scripts/campaigns/wave1/run_wave1_residual_harmonic_family_campaign.ps1`
- Launcher note:
  `doc/scripts/campaigns/run_wave1_residual_harmonic_family_campaign.md`
- Active campaign state:
  `doc/running/active_training_campaign.yaml`
- Campaign outputs:
  `output/training_campaigns/wave1/2026-03-26-15-01-20_wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00/`
- Family and program registries:
  `output/registries/families/residual_harmonic_mlp/latest_family_best.yaml`
  and `output/registries/program/current_best_solution.yaml`

### Reference-Synthesis Scope

- `reference/RCIM_ML-compensation.pdf`
- `reference/Report Machine Learning.pdf`
- `reference/SpiegazioneSerieDati.pdf`
- matching repository summaries under `doc/reference_summaries/`
- current structured-model framing in
  `doc/guide/Residual Harmonic Network/Residual Harmonic Network.md`

## Skill Results

### `campaign-architect`

What it changed in practice:

- forced the active campaign-state check before touching campaign-local files;
- kept the review centered on planning report, launcher, launcher note, winner
  artifacts, and registries rather than drifting into generic ML analysis;
- made the run-name versus run-instance-id distinction explicit during review.

Operational result:

- the selected completed residual-harmonic campaign package is internally
  aligned;
- the planning report, launcher, launcher note, active-campaign record, and
  campaign output directory all point to the same `Wave 1` campaign identity;
- the campaign output exposes the required winner artifacts:
  `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- the family-level and program-level registries reflect the expected outcome:
  residual-harmonic family best updated, global program best still owned by the
  tree model.

Current judgment:

- useful and non-redundant;
- especially strong as a guardrail against campaign drift and naming mistakes.

### `powershell-campaign-tooling`

What it changed in practice:

- narrowed the review onto the launcher wrapper itself instead of the broader
  training stack;
- forced a script-to-note consistency check;
- kept the launcher evaluation focused on explicitness, path correctness, and
  user-facing command clarity.

Operational result:

- the launcher uses explicit YAML ordering and a visible `campaign_name`;
- the launcher note points to the correct script and preserves the canonical
  launch command;
- no script/note drift was found in the reviewed residual-harmonic launcher.

Current judgment:

- useful, but intentionally narrow;
- best used when the task truly involves campaign wrappers or launcher notes.

### `scientific-reference-synthesizer`

What it changed in practice:

- forced a separation between source-backed claims, repository consequences,
  and open deployment questions;
- kept the synthesis tied to TE-domain constraints such as operating variables,
  `DataValid`, and TwinCAT practicality;
- prevented the deployment discussion from collapsing into generic ML-export
  optimism.

Operational result:

- produced a clearer deployment-facing interpretation of the repository's
  current structured and residual-harmonic direction;
- clarified that the current repository is aligned with several reference
  constraints, but still lacks a concrete export path from trained models to an
  inspectable TwinCAT-friendly runtime bundle.

Current judgment:

- clearly useful;
- likely most valuable when deciding whether a model family is worth extending
  or when preparing deployment-facing documentation.

## Evidence Table

<!-- markdownlint-disable MD013 -->
| Artifact | Tested Task | Primary Inputs | Output Used In This Wave | Net Value |
| --- | --- | --- | --- | --- |
| `campaign-architect` | Review one finished campaign package | planning report, finished campaign state, campaign outputs, registries | this operational-test report | kept campaign-safe scope and naming/bookkeeping review explicit |
| `powershell-campaign-tooling` | Review the campaign launcher wrapper | launcher script, launcher note, active campaign state | this operational-test report | exposed launcher behavior as a distinct workflow surface |
| `scientific-reference-synthesizer` | Produce deployment-facing TE note | `reference/` PDFs, reference summaries, residual-harmonic guide | `Twincat-Friendly Structured TE Modeling.md` | separated facts, repository consequences, and open deployment gaps |
| `repo-ml-reviewer` | Secondary campaign package review | campaign package, launcher, active state | this operational-test report | found concrete workflow/bookkeeping issues missed by the first local pass |
| `repo-test-strategist` | Define minimum evidence set | approved technical document and reviewed artifact set | this operational-test report | prevented unnecessary reruns and sharpened closure criteria |
| `twincat-deployment-analyst` | TwinCAT/PLC feasibility check | reference summaries, residual-harmonic direction, registries | synthesis note plus this report | clarified what is plausible versus still speculative |
<!-- markdownlint-enable MD013 -->

## Local Review Findings

### Campaign Package Findings

The first local pass found the reviewed residual-harmonic campaign package
mostly aligned, but the subagent review surfaced four non-trivial issues that
should be treated as real findings.

Observed strengths:

- planning/reporting/launcher naming stayed aligned;
- campaign output bookkeeping is inspectable and winner-aware;
- the reviewed package respects the immutable `run_instance_id` artifact
  layout;
- the family-level best result did not incorrectly overwrite the program-level
  best result.

Integrated findings:

1. The launcher is not a passive wrapper. It force-deletes matching queue items
   from `pending` and `running` before launch, which creates campaign-workflow
   risk for reruns or overlapping preparation.
2. The active campaign state records both a PowerShell launcher path and a raw
   Python replay command, but those two paths are not behaviorally equivalent
   because the raw Python command does not perform the same queue cleanup.
3. The active campaign `started_at` timestamp does not align with the campaign
   output timestamp or first queued run timestamp, which weakens auditability.
4. One terminal log filename is truncated relative to the run name, which is a
   smaller but real traceability drift.

Residual risks:

- the launcher note is intentionally concise, so it remains a usage note rather
  than a full operational warning document;
- deployment-facing implications of the residual-harmonic winner are not yet
  encoded in campaign artifacts, only in separate technical reasoning;
- there is still no automated consistency check that proves launcher behavior,
  launch-command recording, and campaign-manifest replay semantics stay
  synchronized.

### Reference-Synthesis Findings

The reference material supports the following repository consequences:

- TE modeling must stay tied to real rig variables:
  speed, torque, temperature, and angular context;
- valid TE computation depends on the `DataValid` acquisition window and on the
  distinction between raw, zeroed, and cumulative angular quantities;
- TwinCAT deployment favors lightweight and inspectable model structures rather
  than opaque black-box pipelines;
- separating structured periodic content from learned correction remains a
  defensible direction for this repository.

## Subagent Results

The approved subagent outputs were used as secondary checks on the same wave.
Their integrated conclusions are summarized here after local review.

### `repo-ml-reviewer`

Contribution:

- added the strongest concrete findings of the whole wave;
- found real workflow and bookkeeping issues, not style nits;
- changed the conclusion from â€œpackage is fully alignedâ€ to â€œpackage is mostly
  aligned, but replay and audit semantics are weaker than they look.â€

Net value:

- high;
- non-redundant with the local review.

### `repo-test-strategist`

Contribution:

- confirmed that this wave should close on review-grade evidence, not on fresh
  training execution;
- identified the minimum required evidence set and recommended an evidence
  table, which is now included in this report.

Net value:

- high;
- especially useful for preventing over-testing and scope drift.

### `twincat-deployment-analyst`

Contribution:

- sharpened the deployment conclusion into a clearer split:
  harmonic-informed direction is plausible, but deployment readiness is still
  unimplemented;
- highlighted that the strongest evidence-backed PLC path is harmonic
  reconstruction with explicit intermediate quantities, not blind export of the
  current best offline model.

Net value:

- medium to high;
- most useful when the task asks for deployment implications rather than pure
  training accuracy.

## Overall Assessment

This wave suggests the remaining skills and subagents are directionally
correct.

Most useful artifacts in practice:

1. `campaign-architect`
2. `scientific-reference-synthesizer`
3. `repo-ml-reviewer` and `repo-test-strategist`, if they return focused and
   non-overlapping output

More situational artifacts:

1. `powershell-campaign-tooling`
2. `twincat-deployment-analyst`

These two remain valuable, but mainly when the task actually touches launchers
or deployment-facing model choices.

## Follow-Up Recommendations

1. Add a future campaign-tooling fix so launcher notes explicitly disclose any
   queue cleanup side effects.
2. Tighten campaign-state bookkeeping so `started_at` reflects the real first
   launch timestamp or explicitly records the distinction.
3. Consider a small consistency checker that compares:
   launcher behavior, active-campaign replay command, and campaign-manifest
   semantics.
4. Treat TwinCAT deployment as a separate implementation track focused on
   explicit harmonic quantities or another inspectable runtime decomposition,
   not as a direct export of the current offline winners.
