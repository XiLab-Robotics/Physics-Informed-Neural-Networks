# Track 2G Track 2 Verification Refresh

## Overview

This technical document defines the next repository step after the completed
`Track 2G` curve-aware training campaign. The campaign closeout is already
complete and the active campaign state is cleared, so this work prepares a
separate operator-launched official `Track 2` refresh for the twelve completed
`Track 2G` candidates.

The purpose is to decide whether the curve-aware loss profiles improve real
held-out transmission-error curve behavior. The decision must not be inferred
from scalar training `MAE` alone. The refresh will evaluate raw curve error,
mean-centered shape error, mean offset, amplitude behavior, harmonic behavior,
collage plots, and overlay plots against the current accepted Track 2
baselines, `Wave 2B`, `Track 2F`, and `Track 2F-bis`.

The refresh keeps the required deployment branches parallel:

- `global`;
- `Fw`;
- `Bw`.

No subagent is planned for this step. If a subagent becomes useful later, its
name, scope, and approval requirement must be documented before launch.

## Technical Approach

The work will add the twelve registry-backed `Track 2G` candidates to the
official direction-aware Track 2 matrix and prepare a PowerShell launcher that
the operator can run locally or with `-Remote`. Codex will not run the heavy
matrix during preparation.

The candidate set is the full cross-product of the four approved loss profiles
and the three required surfaces:

| Loss Profile | Surface | Candidate Prefix |
| --- | --- | --- |
| `pointwise_control` | `global` | `track2g_curve_aware_pointwise_control_global` |
| `pointwise_control` | `Fw` | `track2g_curve_aware_pointwise_control_Fw` |
| `pointwise_control` | `Bw` | `track2g_curve_aware_pointwise_control_Bw` |
| `raw_centered_shape` | `global` | `track2g_curve_aware_raw_centered_shape_global` |
| `raw_centered_shape` | `Fw` | `track2g_curve_aware_raw_centered_shape_Fw` |
| `raw_centered_shape` | `Bw` | `track2g_curve_aware_raw_centered_shape_Bw` |
| `raw_offset` | `global` | `track2g_curve_aware_raw_offset_global` |
| `raw_offset` | `Fw` | `track2g_curve_aware_raw_offset_Fw` |
| `raw_offset` | `Bw` | `track2g_curve_aware_raw_offset_Bw` |
| `full_curve_composite` | `global` | `track2g_curve_aware_full_curve_composite_global` |
| `full_curve_composite` | `Fw` | `track2g_curve_aware_full_curve_composite_Fw` |
| `full_curve_composite` | `Bw` | `track2g_curve_aware_full_curve_composite_Bw` |

Each candidate will resolve to its corresponding family registry under
`output/registries/families/`:

- `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global`;
- `track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw`;
- `track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw`;
- `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global`;
- `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw`;
- `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw`;
- `track2g_curve_aware_harmonic_residual_offset_raw_offset_global`;
- `track2g_curve_aware_harmonic_residual_offset_raw_offset_fw`;
- `track2g_curve_aware_harmonic_residual_offset_raw_offset_bw`;
- `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global`;
- `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw`;
- `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw`.

Direction semantics must remain stable:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

The expected implementation pattern is:

1. Extend the compact matrix generation section in
   `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`.
2. Verify that the existing registry-model inference path supports
   `curve_aware_harmonic_residual_offset_probe` without changing the runtime
   input contract. The model must receive the same point or causal short-history
   data shape supported by the current Track 2 inference path.
3. Create a dedicated operator launcher:
   `scripts/campaigns/track2/run_track2g_track2_verification_refresh.ps1`.
4. Create the matching launcher note:
   `doc/scripts/campaigns/track2/run_track2g_track2_verification_refresh.md`.
5. The launcher will run the official matrix locally by default and expose a
   `-Remote` option using the repository remote-campaign conventions.
6. After the operator reports completion, inspect the generated matrix,
   visual reports, official verification report, PDFs, and status documents in
   a separate closeout step.

The local matrix command wrapped by the launcher will use:

```powershell
conda run -n pinns_env python -B scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml `
  --output-suffix track2g_curve_aware_track2_refresh_<date_token> `
  --windows
```

## Involved Components

The implementation will involve these repository components:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  for the official candidate matrix.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  only if model-loading or inference-shape support needs a small compatibility
  patch.
- `scripts/campaigns/track2/run_track2g_track2_verification_refresh.ps1` for
  the operator-facing launcher.
- `doc/scripts/campaigns/track2/run_track2g_track2_verification_refresh.md` for
  the launcher usage note.
- `output/registries/families/track2g_curve_aware_harmonic_residual_offset_*`
  as the source of the completed model pointers.
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md` as the
  canonical matrix report that will be refreshed only after the operator run.
- `doc/reports/analysis/track2/best_model_collage_report/[YYYY-MM-DD]/` for
  visual collage evidence after the matrix run.
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[YYYY-MM-DD]/`
  for overlay evidence after the matrix run.
- `doc/reports/analysis/track2/official_model_verification_report/[YYYY-MM-DD]/`
  for the accepted verification decision after the operator run.
- `doc/running/te_model_live_backlog.md` and
  `doc/reports/analysis/Training Results Master Summary.md` for final status
  synchronization after results are inspected.

## Implementation Steps

1. Confirm the active campaign state is `none` and `Track 2G` closeout points
   to `pending_separate_operator_refresh`.
2. Confirm the twelve `Track 2G` family registries exist and each exposes a
   `latest_family_best.yaml`.
3. Add a `Track 2G` candidate-generation block to the full Track 2 matrix
   template with the twelve candidates and correct allowed-direction lists.
4. Inspect the current Track 2 support code and patch only if the
   `curve_aware_harmonic_residual_offset_probe` registry model cannot be
   evaluated by the existing inference path.
5. Create the local and `-Remote` launcher script without running the heavy
   matrix.
6. Create the launcher note with both commands and the expected output suffix.
7. Run lightweight validation only:
   - script syntax checks;
   - package/candidate inventory checks;
   - Markdown checks for touched documents.
8. Stop and provide the exact operator commands.
9. Wait for the user to run the launcher and report completion.
10. In the later closeout step, inspect matrix outputs, regenerate or validate
    collage and overlay reports, create the official decision report, export and
    visually validate PDFs, update status documents, and then ask for commit
    approval.
