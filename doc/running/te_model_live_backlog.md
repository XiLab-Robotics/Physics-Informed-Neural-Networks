# TE Model Live Backlog

## Program Overview

This file is the canonical operational backlog for the TE model implementation program.

Use this document as the day-to-day source of truth for:

- current execution status;
- completed waves;
- next implementation targets;
- deferred and low-priority branches;
- promotion and comparison decisions.

Historical rationale and approval history remain in:

- `doc/technical/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- `doc/technical/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
- later TE-related technical notes under `doc/technical/2026-03-17/`

## Current Status

- Program State: active
- Current Completed Wave: `Wave 0`
- Current Focus: prepare `Wave 1` structured-baseline planning
- Current Best Implemented Family: `feedforward`
- Current Best Implemented Run Registry: `output/registries/program/current_best_solution.yaml`
- Current Reference Feedforward Baseline Run:
  - `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/metrics_summary.yaml`
  - `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/training_test_report.md`
  - `output/registries/families/feedforward/latest_family_best.yaml`
- Wave 0 Verification Artifacts:
  - `output/training_runs/feedforward/2026-03-17-19-49-41__te_feedforward_trial/metrics_summary.yaml`
  - `output/validation_checks/feedforward/2026-03-17-19-49-04__te_feedforward_trial_registry_validation/validation_summary.yaml`
  - `output/smoke_tests/feedforward/2026-03-17-19-49-04__te_feedforward_trial_registry_smoke_test/smoke_test_summary.yaml`

## Completed

### Planning Foundation

- TE family roadmap approved.
- TE analytical family comparison report approved.
- TE implementation backlog approved.
- low-priority `Lightweight Transformer` and `Neural ODE` branches made explicit.
- additional family candidates added explicitly:
  - `State-Space Sequence Model`
  - `Mixture-of-Experts / Regime-Conditioned Model`
  - optional `Kernel Ridge / Gaussian Process` benchmark

### Wave 0

Status:

- completed

Delivered:

- shared training infrastructure in `scripts/training/shared_training_infrastructure.py`
- explicit `experiment.model_family` in feedforward presets
- common artifact names:
  - `training_config.yaml`
  - `metrics_summary.yaml`
- category-specific output roots:
  - `output/training_runs/`
  - `output/validation_checks/`
  - `output/smoke_tests/`
  - `output/registries/`
- reusable one-batch validation entry point:
  - `scripts/training/validate_training_setup.py`
- reusable Lightning smoke-test entry point:
  - `scripts/training/run_training_smoke_test.py`
- feedforward training path updated to consume the shared infrastructure
- documentation updated for the new runnable workflows

Verification:

- one-batch validation completed successfully
- smoke test with checkpoint save/reload completed successfully
- feedforward `trial` run completed successfully with the common metrics schema
- Wave 0 `trial` artifacts are verification-only and are not the canonical program baseline

## In Progress

- no active implementation wave at the moment

## Next Up

### Wave 1. Structured Baseline Planning

Immediate next step:

- create the campaign plan report for the structured baseline wave
- use the registry-selected feedforward best run as the comparison baseline for future Wave 1 results

Included families:

- harmonic regression baseline
- periodic-feature feedforward MLP
- residual MLP over harmonic or analytical baseline
- tree-based benchmark

Expected outputs:

- campaign plan report in `doc/reports/campaign_plans/`
- generated campaign YAML files after approval
- campaign state registration in `doc/running/active_training_campaign.yaml`

### Wave 1. Structured Baseline Implementation

After campaign-plan approval:

- implement the four structured baseline families
- add smoke-test support for each family
- add one-batch validation support for each family
- run the approved structured-baseline campaign
- write the structured-baseline results report with validated PDF export

## Deferred / Low Priority

### Explicit Low-Priority Exploratory Families

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- optional `Kernel Ridge / Gaussian Process` benchmark

Entry rule:

- these families should not displace the main roadmap unless later evidence justifies them or the user explicitly promotes them.

## Wave Checklist

### Wave 0. Shared Infrastructure

- completed

### Wave 1. Structured Static Baselines

- planning report: pending
- implementation: pending
- smoke-tests: pending
- validation checks: pending
- campaign execution: pending
- results report: pending

### Wave 2. Temporal Models

- pending

### Wave 3. Hybrid Structured Models

- pending

### Wave 4. PINN Formulation And First PINN

- pending

### Wave 5. Cross-Wave Comparison And Best Solution

- pending

## Decision Notes

- the live backlog is now the privileged operational view of the TE program
- technical documents remain the historical planning baseline and design rationale
- output artifacts now follow the privileged category-specific structure rather than the old flat family-root convention
- the canonical feedforward reference baseline is the registry-selected best historical run, not the Wave 0 `trial` verification run
- best-result visibility should be read from:
  - campaign-level `campaign_best_run.yaml`
  - family-level `latest_family_best.yaml`
  - program-level `current_best_solution.yaml`
- future updates to program status should land here whenever:
  - a wave starts or finishes
  - a model family is promoted or deferred
  - a campaign is approved, started, completed, or cancelled
  - the current best candidate changes
