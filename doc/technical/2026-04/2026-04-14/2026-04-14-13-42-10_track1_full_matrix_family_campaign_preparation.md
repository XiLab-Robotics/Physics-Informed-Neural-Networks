# Track 1 Full Matrix Family Campaign Preparation

## Overview

This technical document defines the next `Track 1` preparation step requested
by the user after clarifying the real first objective of the paper-faithful
branch.

The requested campaign objective is no longer a narrow open-cell family-subset
repair batch. The requested objective is a much broader full-matrix
reproduction program:

- for each paper model family;
- for each harmonic;
- for amplitudes and phases separately;
- with campaign packaging and a PowerShell launcher ready for execution.

Concretely, the user requested the preparation of a campaign structure that
covers:

- `SVM` amplitude reproduction;
- `SVM` phase reproduction;
- and the same pattern for:
  - `MLP`;
  - `RF`;
  - `DT`;
  - `ET`;
  - `ERT`;
  - `GBM`;
  - `HGBM`;
  - `XGBM`;
  - `LGBM`.

This means the first campaign-preparation target is no longer only
best-envelope closure on Tables `3-6`, but campaign-safe preparation for a
full paper-matrix reproduction program.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The current exact-paper runner already provides:

- the exact recovered input schema `rpm`, `deg`, `tor`;
- the exact paper target set for amplitude and phase harmonics;
- family selection through `training.enabled_families`;
- stable output, validation-summary, and ONNX-export surfaces.

However, it does **not** currently expose a clean campaign-facing control for:

- amplitude-only runs;
- phase-only runs;
- per-harmonic target filtering;
- grouped campaign generation across family x metric scopes.

Therefore, the correct preparation path is:

1. introduce a minimal exact-paper target-scope surface in the configuration,
   so campaign YAML files can request:
   - all targets;
   - amplitude-only targets;
   - phase-only targets;
   - optionally a restricted harmonic subset when needed;
2. define one campaign matrix that is understandable and operationally safe;
3. generate YAML files and a single dedicated PowerShell launcher after user
   approval.

Recommended campaign packaging:

- one umbrella `Track 1` full-matrix reproduction campaign;
- two major tracks per family:
  - amplitude track;
  - phase track;
- each track may contain either:
  - one family-level run covering all harmonics in that metric group; or
  - a narrower harmonic-sliced batch when the family needs follow-up retries.

Because the user explicitly asked for per-harmonic coverage and also allowed
multiple trainings when needed, the initial preparation should balance
tractability and faithfulness:

- base layer:
  one run per family per metric group, covering all harmonics of that group;
- optional retry layer:
  targeted harmonic repair runs only for families and harmonics still far from
  the paper values after the base layer.

This keeps the first campaign finite and launchable while still respecting the
requested matrix-reproduction logic.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-13-21-20-53_track1_exact_paper_open_cell_repair_campaign_plan_report.md`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `output/training_campaigns/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `doc/README.md`

## Implementation Steps

1. Add a configuration-facing exact-paper target-scope surface that can select:
   all targets, amplitude-only targets, phase-only targets, and optional
   harmonic subsets.
2. Validate that the exact-paper workflow still serializes stable
   `validation_summary.yaml` outputs under the new target-scope controls.
3. Write a preliminary campaign planning report for the full family x metric
   reproduction program before generating any campaign package.
4. After user approval, generate the campaign YAML set, dedicated launcher,
   matching launcher note, and prepared active-campaign state.
5. Ensure the campaign naming stays explicit across:
   campaign name, YAML names, run names, launcher name, launcher note, and
   active-campaign state.
6. Provide the exact PowerShell launch command only after the approved
   campaign package exists.
7. Run Markdown warning checks on the touched Markdown scope before closing the
   preparation task.

Implementation must not begin until the user explicitly approves this
technical document and the associated planning report, per repository policy.
