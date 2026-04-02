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

- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
- later TE-related technical notes under `doc/technical/2026-03/2026-03-17/`

## Current Status

- Program State: active
- Current Completed Wave: `Wave 1` structured-baseline familywise optimization pass
- Current Focus: `Wave 1` is now fully closed in campaign execution, reporting, and ranking; the next main focus is TwinCAT deployment evaluation preparation plus `Wave 2` planning
- Current Best Implemented Family: `tree` (`hist_gradient_boosting`)
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

- post-`Wave 1` transition toward the TwinCAT deployment-evaluation branch
- planning handoff from completed static structured baselines toward `Wave 2` temporal-model work

## Next Up

### Post-Wave 1 Follow-Up

Current next step:

- schedule a follow-up random forest retry on a higher-memory machine to verify whether the observed `MemoryError` is workstation-specific and whether a larger RAM budget improves the benchmark outcome
- use the consolidated `Wave 1` closeout report as the canonical summary when comparing future families against the current structured-baseline stage

### Post-Campaign TwinCAT Deployment Evaluation

Planned execution order after the now-closed `Wave 1` reporting work:

- formalize a dedicated `TwinCAT deployment evaluation` execution branch in the
  operational workstream
- use [testrig_twincat_ml_reference.md](../reference_codes/testrig_twincat_ml_reference.md)
  as the canonical technical baseline for the imported TestRig PLC path
- keep the legacy Beckhoff path as the main deployment target:
  - `TF38x0`
  - `FB_MllPrediction`
  - `XML/BML`
- open a separate comparison track for the newer Beckhoff server path:
  - `TF3820/TF3830`
  - `FB_MlSvrPrediction`
  - `ONNX + JSON + PlcOpenXml`
- evaluate both branches against repository-authored models instead of relying
  only on historical paper coverage
- compare at least:
  - model acceptance and conversion success
  - artifact workflow complexity
  - runtime behavior and timing suitability
  - maintainability and engineering cost
- use isolated mode for preparatory or parallel experiments whenever campaign-
  sensitive repository areas should remain untouched

Entry conditions:

- `Wave 1` closeout remains synchronized in the running-state documents and registries;
- or the user explicitly approves isolated parallel preparation before full
  integration.

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

- planning report: completed
- implementation: completed
- smoke-tests: completed
- validation checks: completed
- campaign execution: completed
- results report: completed

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
- the currently tracked residual-harmonic family optimization belongs to `Wave 1` and its campaign assets have been realigned to the same naming
- the first cross-family `Wave 1` execution had a mixed operational outcome, but the missing branches were recovered and the wave now has campaign-specific reporting plus a consolidated closeout summary
- best-result visibility should be read from:
  - campaign-level `campaign_best_run.yaml`
  - family-level `latest_family_best.yaml`
  - program-level `current_best_solution.yaml`
- future updates to program status should land here whenever:
  - a wave starts or finishes
  - a model family is promoted or deferred
  - a campaign is approved, started, completed, or cancelled
  - the current best candidate changes
  - a TwinCAT deployment branch is promoted, deferred, or selected as the
    preferred deployment path
