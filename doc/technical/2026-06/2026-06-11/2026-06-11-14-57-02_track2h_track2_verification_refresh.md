# Wave 4 series TE Curve Verification Pipeline Verification Refresh

## Overview

This technical document defines the next repository step after the completed
`Wave 4.1` robust-loss dispersion-aware campaign. The campaign closeout is
complete, the active campaign state is `none`, and the latest closeout report
marks official `TE Curve Verification Pipeline` verification as a separate optional
operator-approved workflow.

The purpose is to decide whether the robust-loss scalar improvements translate
into real held-out transmission-error curve behavior. The decision must not be
inferred from scalar training `MAE` alone. The refresh will evaluate raw curve
error, mean-centered shape error, mean offset, amplitude behavior, harmonic
behavior, collage plots, and overlay plots against the current accepted TE Curve Verification Pipeline
baselines, `Wave 2.2`, `Wave 3.1`, `Wave 3.2`, and `Wave 3.3`.

The refresh keeps the required deployment branches parallel:

- `global`;
- `Fw`;
- `Bw`.

No subagent is planned for this step. If a subagent becomes useful later, its
name, scope, and approval requirement must be documented before launch.

## Technical Approach

The work will add the nine registry-backed `Wave 4 series` candidates to the
official direction-aware curve-verification matrix and prepare a PowerShell launcher that
the operator can run locally or with `-Remote`. Codex will not run the heavy
matrix during preparation.

The candidate set is the full cross-product of the three approved robust-loss
profiles and the three required surfaces:

| Loss Profile | Surface | Candidate Prefix |
| --- | --- | --- |
| `mae` | `global` | `track2h_mae_robust_global` |
| `mae` | `Fw` | `track2h_mae_robust_Fw` |
| `mae` | `Bw` | `track2h_mae_robust_Bw` |
| `smooth_l1` | `global` | `track2h_smooth_l1_robust_global` |
| `smooth_l1` | `Fw` | `track2h_smooth_l1_robust_Fw` |
| `smooth_l1` | `Bw` | `track2h_smooth_l1_robust_Bw` |
| `log_cosh` | `global` | `track2h_log_cosh_robust_global` |
| `log_cosh` | `Fw` | `track2h_log_cosh_robust_Fw` |
| `log_cosh` | `Bw` | `track2h_log_cosh_robust_Bw` |

Each candidate will resolve to its corresponding family registry under
`output/registries/families/`:

- `track2h_dispersion_aware_mae_robust_global`;
- `track2h_dispersion_aware_mae_robust_fw`;
- `track2h_dispersion_aware_mae_robust_bw`;
- `track2h_dispersion_aware_smooth_l1_robust_global`;
- `track2h_dispersion_aware_smooth_l1_robust_fw`;
- `track2h_dispersion_aware_smooth_l1_robust_bw`;
- `track2h_dispersion_aware_log_cosh_robust_global`;
- `track2h_dispersion_aware_log_cosh_robust_fw`;
- `track2h_dispersion_aware_log_cosh_robust_bw`.

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
   `curve_aware_harmonic_residual_offset_probe` for the completed Wave 4 series
   artifacts without changing the runtime input contract. The model must
   receive the same point or causal short-history data shape supported by the
   current TE Curve Verification Pipeline inference path.
3. Create a dedicated operator launcher:
   `scripts/campaigns/track_2/run_track2h_track2_verification_refresh.ps1`.
4. Create the matching launcher note:
   `doc/scripts/campaigns/track_2/run_track2h_track2_verification_refresh.md`.
5. The launcher will run the official matrix locally by default and expose a
   `-Remote` option using the repository remote-campaign conventions.
6. After the operator reports completion, inspect the generated matrix,
   visual reports, official verification report, PDFs, and status documents in
   a separate closeout step.

The local matrix command wrapped by the launcher will use:

```powershell
conda run -n pinns_env python -B scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml `
  --output-suffix track2h_robust_loss_track2_refresh_<date_token> `
  --windows
```

## Involved Components

The implementation will involve these repository components:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  for the official candidate matrix.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  only if model-loading or inference-shape support needs a small compatibility
  patch.
- `scripts/campaigns/track_2/run_track2h_track2_verification_refresh.ps1` for
  the operator-facing launcher.
- `doc/scripts/campaigns/track_2/run_track2h_track2_verification_refresh.md` for
  the launcher usage note.
- `output/registries/families/track2h_dispersion_aware_*` as the source of the
  completed model pointers.
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

1. Confirm the active campaign state is `none` and `Wave 4 series` closeout points
   to `pending_optional_official_verification_refresh`.
2. Confirm the nine `Wave 4 series` family registries exist and each exposes a
   `latest_family_best.yaml`.
3. Add a `Wave 4 series` candidate-generation block to the full curve-verification matrix
   template with the nine candidates and correct allowed-direction lists.
4. Inspect the current TE Curve Verification Pipeline support code and patch only if the
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
