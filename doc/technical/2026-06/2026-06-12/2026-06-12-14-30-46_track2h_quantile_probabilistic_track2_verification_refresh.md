# Track 2H Quantile Probabilistic Track 2 Verification Refresh

## Overview

This technical document defines the next repository step after the completed
second `Track 2H` quantile/probabilistic campaign. The campaign closeout is
complete, the active campaign state is `none`, and the closeout report marks
official `Track 2` curve verification as a separate optional
operator-launched workflow.

The purpose is to decide whether the scalar improvements and calibration
signals from the quantile/probabilistic campaign translate into real held-out
transmission-error curve behavior. The decision must not be inferred from
scalar campaign `MAE` alone. The refresh will evaluate raw curve error,
mean-centered shape error, mean offset, amplitude behavior, harmonic behavior,
collage plots, and overlay plots against the current accepted Track 2
baselines, `Track 2H` robust-loss candidates, `Track 2G`, `Track 2F-bis`, and
the Wave 2 temporal branches.

The refresh keeps the required deployment branches parallel:

- `global`;
- `Fw`;
- `Bw`.

No subagent is planned for this step. If a subagent becomes useful later, its
name, scope, and approval requirement must be documented before launch.

## Technical Approach

The work will add the six registry-backed `Track 2H`
quantile/probabilistic candidates to the official direction-aware Track 2
matrix and prepare a PowerShell launcher that the operator can run locally or
with `-Remote`. Codex will not run the heavy matrix during preparation.

The candidate set is the full approved second `Track 2H` package:

| Profile | Surface | Candidate Prefix | Deterministic Curve |
| --- | --- | --- | --- |
| `quantile_p10_p50_p90` | `global` | `track2h_quantile_p10_p50_p90_global` | `p50` |
| `quantile_p10_p50_p90` | `Fw` | `track2h_quantile_p10_p50_p90_Fw` | `p50` |
| `quantile_p10_p50_p90` | `Bw` | `track2h_quantile_p10_p50_p90_Bw` | `p50` |
| `gaussian_nll` | `global` | `track2h_gaussian_nll_global` | `mu` |
| `gaussian_nll` | `Fw` | `track2h_gaussian_nll_Fw` | `mu` |
| `gaussian_nll` | `Bw` | `track2h_gaussian_nll_Bw` | `mu` |

Each candidate will resolve to its corresponding family registry under
`output/registries/families/`:

- `track2h_quantile_probabilistic_quantile_p10_p50_p90_global`;
- `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw`;
- `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw`;
- `track2h_quantile_probabilistic_gaussian_nll_global`;
- `track2h_quantile_probabilistic_gaussian_nll_fw`;
- `track2h_quantile_probabilistic_gaussian_nll_bw`.

Direction semantics must remain stable:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

The probabilistic candidates require one extra compatibility check before
matrix launch. Their model checkpoints emit multi-channel outputs:

- quantile heads emit `p10`, `p50`, and `p90`;
- Gaussian heads emit `mu` and `log_sigma`.

The official Track 2 matrix must compare only the deterministic TE curve:
`p50` for quantile runs and `mu` for Gaussian runs. If the current registry
inference path loads the raw backbone directly without the
`TransmissionErrorRegressionModule` deterministic-output extraction, the
shared support code must be patched so the matrix never compares multi-channel
raw outputs against scalar TE curves.

The expected implementation pattern is:

1. Extend the compact matrix generation section in
   `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`.
2. Inspect
   `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
   and verify deterministic output extraction for probabilistic checkpoints.
3. Patch the support code only if the current inference path does not reuse the
   training module's deterministic `p50` or `mu` selection.
4. Create a dedicated operator launcher:
   `scripts/campaigns/track2/run_track2h_quantile_probabilistic_track2_verification_refresh.ps1`.
5. Create the matching launcher note:
   `doc/scripts/campaigns/track2/run_track2h_quantile_probabilistic_track2_verification_refresh.md`.
6. The launcher will run the official matrix locally by default and expose a
   `-Remote` option using the repository remote-campaign conventions.
7. After the operator reports completion, inspect the generated matrix,
   visual reports, official verification report, PDFs, and status documents in
   a separate closeout step.

The local matrix command wrapped by the launcher will use:

```powershell
conda run -n pinns_env python -B scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml `
  --output-suffix track2h_quantile_probabilistic_track2_refresh_<date_token> `
  --windows
```

## Involved Components

The implementation will involve these repository components:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  for the official candidate matrix.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  if deterministic output selection for probabilistic heads needs support.
- `scripts/campaigns/track2/run_track2h_quantile_probabilistic_track2_verification_refresh.ps1`
  for the operator-facing launcher.
- `doc/scripts/campaigns/track2/run_track2h_quantile_probabilistic_track2_verification_refresh.md`
  for the launcher usage note.
- `output/registries/families/track2h_quantile_probabilistic_*` as the source
  of completed model pointers.
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

1. Confirm the active campaign state is `none` and the quantile/probabilistic
   closeout points to a separate optional official Track 2 refresh.
2. Confirm the six family registries exist and each exposes a
   `latest_family_best.yaml`.
3. Add a candidate-generation block to the full Track 2 matrix template with
   the six candidates and correct allowed-direction lists.
4. Inspect the current Track 2 support code and patch deterministic output
   extraction only if probabilistic checkpoints are not already converted to
   scalar `p50` or `mu` predictions during inference.
5. Create the local and `-Remote` launcher script without running the heavy
   matrix.
6. Create the launcher note with both commands and the expected output suffix.
7. Run lightweight validation only:
   - script syntax checks;
   - candidate inventory and registry checks;
   - Markdown checks for touched documents.
8. Stop and provide the exact operator commands.
9. Wait for the user to run the launcher and report completion.
10. In the later closeout step, inspect matrix outputs, regenerate or validate
    collage and overlay reports, create the official decision report, export
    and visually validate PDFs, update status documents, and then ask for
    commit approval.
