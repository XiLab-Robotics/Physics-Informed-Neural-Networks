# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `feedforward`;
- model type: `feedforward`;
- logical run name: `te_feedforward_trial`;
- output run name: `te_feedforward_trial_skill_operational_test`;
- run instance id: `2026-03-30-10-46-31__te_feedforward_trial_skill_operational_test`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/feedforward/presets/trial.yaml` |
| Output Directory | `output/validation_checks/feedforward/2026-03-30-10-46-31__te_feedforward_trial_skill_operational_test` |
| Model Family | `feedforward` |
| Model Type | `feedforward` |
| Run Name | `te_feedforward_trial` |
| Output Run Name | `te_feedforward_trial_skill_operational_test` |
| Run Instance ID | `2026-03-30-10-46-31__te_feedforward_trial_skill_operational_test` |

## Batch Structure

| Field | Value |
| --- | ---: |
| Point Batch Size | 830 |
| Input Feature Dim | 5 |
| Target Feature Dim | 1 |
| Curve Count | 8 |

## Finite Checks

| Check | Status |
| --- | --- |
| Finite Loss | Pass |
| Finite MAE | Pass |
| Finite RMSE | Pass |
| Finite Prediction Tensor | Pass |

## Metrics

| Metric | Value |
| --- | ---: |
| Loss | 0.61044693 |
| MAE | 0.03091770 |
| RMSE | 0.03562582 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
