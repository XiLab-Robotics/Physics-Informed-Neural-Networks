# Track 1 Paper Tables 3 4 5 6 Canonical Comparison

## Overview

This technical document defines the next `Track 1` step requested by the user:
build a canonical repository-owned comparison table that mirrors the paper
tables `3`, `4`, `5`, and `6`, shows the paper targets, shows the current
repository results, and makes the remaining gaps explicit.

The scope is the strict paper-faithful exact-model-bank branch that uses:

- the paper and repository references under `reference/`;
- the recovered paper-era code and exported assets;
- the exact input schema `rpm`, `deg`, `tor`;
- the exact harmonic targets `ampl_k` and `phase_k` for harmonics
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`.

The immediate deliverable is not a new training campaign. The immediate
deliverable is a canonical `paper vs repository` table package that allows the
team to inspect, per harmonic target, whether the repository currently matches
the paper family choice and the paper tabulated metric value.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The repository already has most of the exact-paper replication machinery:

- the recovered-paper feature and target schema;
- the recovered family bank;
- the exact validation workflow;
- the current repository target-winner registry;
- a first `paper vs repository` comparison based on expected family direction.

What is still missing is the canonical comparison surface that the user asked
for: a table shaped like the paper tables `3-6`, with the paper-side target
values and the repository-side measured values serialized side by side.

This work should therefore:

1. extract the paper tabulated targets for the harmonics covered by tables
   `3-6`;
2. represent those targets in a canonical repository-owned data structure;
3. align the existing repository exact-paper validation outputs to that paper
   table structure;
4. generate a Markdown report table that includes:
   - the harmonic target;
   - the paper-selected family or family set;
   - the paper tabulated metric value to reach;
   - the current repository winning family;
   - the current repository metric value;
   - the gap or delta;
   - an explicit status such as `matched`, `not_matched`, or
     `partially_matched`;
5. add a harmonic-level summary that collapses amplitude and phase status into
   an inspectable closure snapshot.

Reference boundary:

- facts directly visible in `reference/RCIM_ML-compensation.pdf`,
  `reference/Report Machine Learning.pdf`, and the recovered paper-era code
  should be treated as source-backed;
- any mapping needed to align the repository target names with the paper table
  layout should be labeled as a repository inference if the source does not
  state it explicitly.

Because this task modifies repository-owned Markdown deliverables, the touched
Markdown scope must be re-checked before closure.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `reference/Report Machine Learning.pdf`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/validation_checks/2026-04-12-15-39-15_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_per_harmonic_replication_exact_paper_model_bank_report.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
- `doc/README.md`

## Implementation Steps

1. Inspect the paper tables `3-6` and the recovered paper-era material to
   extract the target harmonics, selected family directions, and tabulated
   numeric values that the repository must reach.
2. Add a canonical repository-owned representation of those table targets so
   the exact-paper workflow no longer depends on ad hoc manual reading of the
   PDF.
3. Extend the exact-paper support layer so the validation summary can align
   repository winners and metrics against the paper table rows directly.
4. Generate a canonical Markdown comparison table shaped around the paper
   tables `3-6`, including paper target values, repository values, and the
   explicit remaining gap.
5. Add a compact harmonic-level summary so `Track 1` status can be read
   quickly without losing the lower-level per-target evidence.
6. Update the relevant exact-paper analysis report so the new canonical table
   becomes part of the normal repository reading path.
7. Run the exact-paper validation workflow again if the new comparison logic
   requires regenerated evidence.
8. Run Markdown warning checks on the touched Markdown files and confirm clean
   trailing newline state before closing the task.

Implementation must not begin until the user explicitly approves this
technical document, per repository policy.
