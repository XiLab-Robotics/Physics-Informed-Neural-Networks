---
name: twincat-export-preparation
description: Use when planning, reviewing, or preparing TwinCAT-facing TE model export work in StandardML - Codex. This skill is for PLC-friendly export preparation, inspectable inference-path design, and deployment-readiness discipline, not for generic deployment discussion.
---

# TwinCAT Export Preparation

Prepare TwinCAT-facing TE model export work with the repository's deployment
constraints made explicit before any implementation claim is accepted.

## Use This Skill For

- TwinCAT or Beckhoff-facing export planning;
- PLC-friendly model simplification or decomposition planning;
- review of whether a model family is export-plausible;
- preparation of deployment-facing technical notes or backlog items;
- checking whether a workflow preserves inspectable intermediate quantities.

## Do Not Use This Skill For

- generic model-accuracy review with no deployment implications;
- broad DevOps or cloud deployment discussion;
- claiming deployment readiness without repository evidence.

## Required Checks

Before making TwinCAT/export claims:

1. Read `doc/reference_codes/testrig_twincat_ml_reference.md`.
2. Read
   `doc/technical/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`.
3. Read the relevant `doc/reference_summaries/` notes for:
   speed, torque, oil temperature, encoder zeroing, and `DataValid`.
4. Read the current repository model/report note most relevant to the export
   candidate.

## Workflow

1. Identify the candidate model or workflow being evaluated for TwinCAT-facing
   preparation.
2. Separate:
   reference-backed deployment facts, current repository implementation, and
   open inference.
3. Check whether the proposed path preserves:
   explicit operating variables, inspectable intermediate quantities, and
   analytical-versus-ML separation.
4. Prefer harmonic quantities, conditioned coefficients, or other explicit
   decomposition outputs over opaque end-to-end inference stories.
5. State clearly whether the result is:
   deployment-plausible, export-preparable, or actually deployment-ready.

## Repository Priorities

- Treat rotational transmission error as the target signal.
- Keep speed, torque, oil temperature, angle, encoder zeroing, and `DataValid`
  semantics explicit when they matter.
- Prefer structured or hybrid models with inspectable components over opaque
  black-box deployment stories.
- Keep TwinCAT/PLC claims grounded in repository code, reference notes, or
  clearly labeled inference.

## Output Pattern

Prefer this structure:

1. What the reference and current repository actually support.
2. What makes the candidate export-plausible or not.
3. What export/simplification steps are still required.
4. What remains speculative or unimplemented.

## File Targets To Read First

- `doc/reference_codes/testrig_twincat_ml_reference.md`
- `doc/reference_summaries/`
- `doc/technical/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`
- relevant `doc/guide/`
- relevant `scripts/models/`
- relevant `scripts/training/`

## Typical Outputs

- TwinCAT export-preparation note;
- PLC-friendly feasibility review;
- required simplification/export checklist;
- deployment-readiness boundary statement.
