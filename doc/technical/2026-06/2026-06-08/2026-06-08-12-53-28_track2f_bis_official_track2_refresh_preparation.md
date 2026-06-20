# Wave 3.2 Official TE Curve Verification Pipeline Refresh Preparation

## Overview

This technical document plans the operator-launched official `TE Curve Verification Pipeline`
verification refresh for the completed `Wave 3.2` harmonic-offset probe.

The normal campaign closeout is already complete in commit `2f34437a0`. The
campaign state is cleared in `doc/running/active_training_campaign.yaml`, and
the closeout report records six completed candidates with zero unresolved
failed runs.

The refresh must preserve the project direction policy. It must evaluate clean
and harmonic candidates in parallel for each deployment surface, not collapse
the campaign into the scalar-first `Fw` row.

| Surface | Clean Candidate | Harmonic Candidate |
| --- | --- | --- |
| `global` | `track2f_bis_clean_sequential_residual_offset_global` | `track2f_bis_harmonic_residual_offset_global` |
| `Fw` | `track2f_bis_clean_sequential_residual_offset_fw` | `track2f_bis_harmonic_residual_offset_fw` |
| `Bw` | `track2f_bis_clean_sequential_residual_offset_bw` | `track2f_bis_harmonic_residual_offset_bw` |

The refresh is a curve-first acceptance check. Scalar campaign `MAE` and
`RMSE` remain useful diagnostics, but the promotion decision must come from the
official TE Curve Verification Pipeline direction-aware matrix, visual overlays, and companion PDF
reports.

No subagent use is planned for this work.

## Technical Approach

Prepare a dedicated operator-facing Wave 3.2 verification launcher without
running the heavy matrix inside Codex. The launcher will update or wrap the
official curve-verification matrix workflow so the six registry-backed candidates above
are included with correct direction scopes:

- `global`: evaluate against forward and backward TE Curve Verification Pipeline curves;
- `Fw`: evaluate only forward curves;
- `Bw`: evaluate only backward curves.

The local command will run the official reference-family-versus-feedforward
comparison with a Wave 3.2-specific output suffix. The launcher must also
support `-Remote` through the repository-owned remote campaign infrastructure
when available, so the user can execute the heavy matrix on the stronger
workstation.

After the user runs the launcher and reports completion, the resulting
artifacts will be inspected and accepted through the standard TE Curve Verification refresh
workflow:

- confirm the candidate inventory and matrix count include the six new
  Wave 3.2 candidates;
- regenerate or refresh the directional comparison report;
- regenerate the best-model collage and multi-model curve comparison reports;
- create a new dated official model-verification report bundle;
- export and visually validate the real PDFs;
- update the backlog and training-results master summary with the final
  decision.

The expected decision language must distinguish at least three outcomes:

- whether the harmonic branch improves curve following over the clean branch
  for `global`;
- whether the harmonic branch improves curve following over the clean branch
  for `Fw`;
- whether the harmonic branch improves curve following over the clean branch
  for `Bw`.

The refresh must also state whether any accepted `tree`, paper-derived, Wave
2B, or prior Wave 3.1 baseline changes. The closeout metrics alone do not
justify promotion.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report.md`
- `output/registries/families/track2f_bis_clean_sequential_residual_offset_global/latest_family_best.yaml`
- `output/registries/families/track2f_bis_clean_sequential_residual_offset_fw/latest_family_best.yaml`
- `output/registries/families/track2f_bis_clean_sequential_residual_offset_bw/latest_family_best.yaml`
- `output/registries/families/track2f_bis_harmonic_residual_offset_global/latest_family_best.yaml`
- `output/registries/families/track2f_bis_harmonic_residual_offset_fw/latest_family_best.yaml`
- `output/registries/families/track2f_bis_harmonic_residual_offset_bw/latest_family_best.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- future launcher under `scripts/campaigns/track_2/`
- future launcher note under `doc/scripts/campaigns/track_2/`
- future official report bundle under
  `doc/reports/analysis/track2/official_model_verification_report/[2026-06-08]/`

## Implementation Steps

1. Inspect the current curve-verification matrix template and support code to confirm
   whether `sequential_residual_offset_probe` and
   `harmonic_residual_offset_probe` can be loaded from the family registries
   without new inference support.
2. Add the six Wave 3.2 candidate entries to the compact curve-verification matrix
   configuration with correct `global`, `Fw`, and `Bw` direction scopes.
3. Create a dedicated PowerShell launcher for the Wave 3.2 verification
   refresh. The launcher must support local execution and `-Remote`, and it
   must not start the matrix during preparation.
4. Create the matching launcher note with exact local and `-Remote` commands.
5. Run lightweight validation only: syntax checks, matrix/config sanity checks,
   Markdown QA, and launcher preflight if available. Do not run the heavy Track
   2 matrix from Codex.
6. Provide the exact command to the user and wait for the user to report that
   the launcher completed.
7. After completion, inspect the generated matrix artifacts and confirm the
   six Wave 3.2 candidates are present in the directional report.
8. Regenerate the best-model collage and multi-model curve comparison reports
   for the dated refresh bundle.
9. Create the dated official TE curve verification report that records
   clean-vs-harmonic results for `global`, `Fw`, and `Bw`, the strongest
   candidate per surface, and the promotion or rejection decision.
10. Export and raster-validate the real PDFs for the official report and visual
    companion reports, repairing table/page layout issues before closeout.
11. Update `doc/running/te_model_live_backlog.md` and
    `doc/reports/analysis/Training Results Master Summary.md` with the final
    Wave 3.2 decision.
12. Stop before committing until the user explicitly requests the commit.
