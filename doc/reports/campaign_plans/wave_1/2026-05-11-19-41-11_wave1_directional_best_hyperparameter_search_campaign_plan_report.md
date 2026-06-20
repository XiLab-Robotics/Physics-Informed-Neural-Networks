# Wave 1 Directional Best Hyperparameter Search Campaign Plan Report

## Overview

This campaign prepares the next optimization pass for the `15` completed
directional `Wave 1` winner surfaces.

The objective is best-hyperparameter refinement around the current directional
winners, not simple rerunning.

## Objective

Prepare one repository-owned campaign package that:

- refines all `15` directional winner surfaces from the completed `Wave 1`
  retraining pass;
- uses `Optuna` as the canonical neural-family HPO engine;
- keeps bounded non-neural search surfaces inspectable and CPU-throttled;
- preserves the existing directional family separation used by registries,
  reports, and exported-model archives.

## Search Strategy Split

### Neural Surfaces

Families:

- `feedforward`
- `periodic_mlp`
- `residual_harmonic_mlp`

Execution method:

- persisted `Optuna` studies;
- `9` studies total;
- `18` trial budget per study;
- objective metric: `val_mae`;
- one GPU-visible worker process per study execution slot.

### Non-Neural Surfaces

Families:

- `tree`
- `harmonic_regression`

Execution method:

- bounded explicit grid configs materialized as normal campaign YAML files;
- sequential queue execution through the existing repository runner;
- explicit CPU throttling to avoid host oversubscription.

## Candidate Surface Matrix

| Index | Surface Family | Base Family | Variant | Search Engine |
| --- | --- | --- | --- | --- |
| 1 | `tree` | `tree` | `global` | bounded_grid |
| 2 | `tree_fw` | `tree` | `Fw` | bounded_grid |
| 3 | `tree_bw` | `tree` | `Bw` | bounded_grid |
| 4 | `residual_harmonic_mlp` | `residual_harmonic_mlp` | `global` | optuna |
| 5 | `residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | `Fw` | optuna |
| 6 | `residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | `Bw` | optuna |
| 7 | `feedforward` | `feedforward` | `global` | optuna |
| 8 | `feedforward_fw` | `feedforward` | `Fw` | optuna |
| 9 | `feedforward_bw` | `feedforward` | `Bw` | optuna |
| 10 | `periodic_mlp` | `periodic_mlp` | `global` | optuna |
| 11 | `periodic_mlp_fw` | `periodic_mlp` | `Fw` | optuna |
| 12 | `periodic_mlp_bw` | `periodic_mlp` | `Bw` | optuna |
| 13 | `harmonic_regression` | `harmonic_regression` | `global` | bounded_grid |
| 14 | `harmonic_regression_fw` | `harmonic_regression` | `Fw` | bounded_grid |
| 15 | `harmonic_regression_bw` | `harmonic_regression` | `Bw` | bounded_grid |

## Planned Search Volume

| Phase | Surface Count | Budget Per Surface | Total Planned Executions |
| --- | ---: | ---: | ---: |
| `tree` bounded grid | 3 | 18 | 54 |
| `harmonic_regression` bounded grid | 3 | 12 | 36 |
| neural `Optuna` studies | 9 | 18 trials | 162 |
| total | 15 | mixed | 252 |

## Hardware Policy

| Family Group | Runtime Policy | Main Reason |
| --- | --- | --- |
| neural `Optuna` studies | GPU-preferred, `1` GPU-visible worker per study slot | use available GPU capacity and avoid CPU-only long sweeps |
| `tree` bounded grid | CPU only, sequential queue | estimator backend is CPU-bound in practice |
| `harmonic_regression` bounded grid | CPU-throttled queue | keep the launcher predictable and leave GPUs available to the heavier neural studies |

## Campaign Assets

The approved package must materialize:

- planning report:
  `doc/reports/campaign_plans/wave_1/2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md`
- preparer:
  `scripts/campaigns/wave_1/prepare_wave1_directional_best_hyperparameter_search_campaign.py`
- Optuna helpers:
  `scripts/training/optuna_hpo_support.py`
- neural study runner:
  `scripts/training/run_optuna_neural_hpo_study.py`
- launcher:
  `scripts/campaigns/wave_1/run_wave1_directional_best_hyperparameter_search_campaign.ps1`
- launcher note:
  `doc/scripts/campaigns/run_wave1_directional_best_hyperparameter_search_campaign.md`

## Execution Gate

Before this campaign is launched:

1. the package must exist on disk;
2. `Optuna` must be installed from the tracked `requirements.txt`;
3. the launcher note must document the GPU-id contract;
4. the unrelated `RCIM Model-Bank Reproduction` campaign state must remain untouched;
5. the user must explicitly approve the launch.

## Launch Command

```powershell
.\scripts\campaigns\wave_1\run_wave1_directional_best_hyperparameter_search_campaign.ps1 -GpuIdList 0,1
```
