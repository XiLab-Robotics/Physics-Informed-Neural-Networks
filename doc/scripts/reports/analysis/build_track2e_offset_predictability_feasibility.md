# Track 2E Offset Predictability Feasibility Builder

## Overview

`scripts/reports/analysis/build_track2e_offset_predictability_feasibility.py`
builds the `Track 2E` diagnostic report from completed `Track 2D`
mean-offset artifacts.

The script is evaluation-only. It does not train models, does not update
registries, does not alter the dataset, and does not pass future curve samples
to a runtime model.

## Main Role

The builder tests whether the curve-level vertical offset observed by
`Track 2D` is predictable enough from causal operating-condition groupings to
justify the next offset-aware branch.

It keeps `Fw`, `Bw`, and `global` surfaces in parallel and assigns each
candidate a recommended next intervention:

- `sequential_offset_model`;
- `posthoc_offset_baseline`;
- `multi_head_shape_offset`;
- `loss_reweighting`;
- `not_offset_first`.

## Inputs

By default, the script reads the accepted `Track 2D` artifact bundle:

- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_per_curve_metrics.csv`
- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_candidate_summary.csv`

Optional CLI filters can restrict execution to one or more candidate ids.

## Outputs

The script writes machine-readable artifacts under:

- `output/validation_checks/track2e_offset_predictability_feasibility/<run_instance_id>/`

The artifact bundle contains:

- `track2e_candidate_feasibility_summary.csv`
- `track2e_surface_intervention_recommendation.csv`
- `track2e_condition_offset_stability.csv`
- `track2e_offset_predictability_feasibility_summary.yaml`

The dated Markdown report is written under:

- `doc/reports/analysis/track2/offset_predictability_feasibility/[YYYY-MM-DD]/`

## Practical Use

Run the default feasibility diagnostic:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2e_offset_predictability_feasibility.py
```

Refresh a dated report bundle:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2e_offset_predictability_feasibility.py `
  --report-date 2026-06-03
```

Run a filtered diagnostic for one candidate:

```powershell
python -B scripts/reports/analysis/build_track2e_offset_predictability_feasibility.py `
  --candidate-id periodic_gru_sequence_global `
  --report-date 2026-06-03
```

## Notes

- Exact full-condition groups are intentionally excluded from the
  recommendation ranking because they can collapse to one evaluated curve and
  overstate deployable offset predictability.
- Corrected `MAE` values are upper-bound diagnostic approximations, not
  production correction metrics.
- Any learned offset model, loss change, or multi-head architecture still
  requires a future technical document and campaign plan before training.
