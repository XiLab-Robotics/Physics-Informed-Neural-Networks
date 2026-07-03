# Wave 2.3 TE Curve Verification Pipeline Verification Refresh

## Overview

This technical document plans the optional `TE Curve Verification Pipeline` verification refresh for
the completed `Wave 2.3` residual harmonic temporal hybrid campaign. The normal
campaign closeout is already complete, the active campaign state is cleared,
and the campaign record marks `TE Curve Verification Pipeline` as an operator-launched follow-up.

The refresh will add the completed `Wave 2.3` candidate surfaces to the official
directional offline comparison matrix, prepare a dedicated launcher that can be
run locally or with `-Remote`, and keep the heavy verification execution under
operator control. The workflow must not promote any `Wave 2.3` model from
campaign leaderboard metrics alone; the decision must come from the refreshed
direction-aware `TE Curve Verification Pipeline` matrix and validated visual companion reports.

No subagent use is planned for this implementation. If subagent review becomes
useful later, the task boundary and approval requirement will be declared
before launching it.

## Technical Approach

The implementation will follow the existing `TE Curve Verification Pipeline` refresh pattern and the
post-closeout campaign workflow. It will inspect the completed `Wave 2.3`
registry surface, add the approved candidate entries to the compact matrix
configuration, and prepare an operator-facing PowerShell launcher. The launcher
will run locally by default and expose `-Remote` by reusing the repository LAN
remote-training infrastructure where applicable.

The candidate set will preserve the established direction semantics:

- `global` candidates are trained on both directions and evaluated separately
  on forward and backward curves;
- `Fw` candidates are trained and evaluated on forward curves only;
- `Bw` candidates are trained and evaluated on backward curves only.

After the operator runs the launcher and reports completion, a separate
inspection step will verify the matrix output, regenerate the best-model
collage and multi-model curve comparison reports, create or update the dated
official verification report, export and validate the PDFs, and synchronize the
training status documents.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_results/wave_2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md`
- `doc/reports/campaign_plans/wave_2/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md`
- `output/registries/families/residual_harmonic_gru_sequence_*`
- `output/registries/families/residual_harmonic_lstm_sequence_*`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/`
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`

## Implementation Steps

1. Reconfirm that `doc/running/active_training_campaign.yaml` is cleared and
   that the completed `Wave 2.3` campaign exposes the expected registry files.
2. Inspect the current `TE Curve Verification Pipeline` matrix template and inference support code to
   determine whether the residual harmonic temporal sequence families can use
   existing loading paths or need a small support extension.
3. Add the approved `Wave 2.3` `global`, `Fw`, and `Bw` candidate entries to the
   compact matrix configuration with stable direction semantics.
4. Create a dedicated `Wave 2.3` `TE Curve Verification Pipeline` PowerShell launcher that supports
   local execution and `-Remote`, writes distinguishable output/log suffixes,
   and does not start the heavy matrix during preparation.
5. Add the matching launcher note and document the exact local and `-Remote`
   commands.
6. Stop for operator execution of the launcher.
7. After operator completion, inspect the refreshed matrix artifacts and
   regenerate the matrix report, collage report, overlay report, and official
   verification report.
8. Export and validate the real PDFs for the refreshed visual and official
   reports.
9. Synchronize the live backlog, training master summary, and any `TE Curve Verification Pipeline`
   report pointers with the final decision.
10. Run Python, Markdown, Sphinx, PDF, and Git preflight checks before any
    final commit request.
